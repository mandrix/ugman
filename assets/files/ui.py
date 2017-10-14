import json #Para leer el archivo JSON guardadon.json
from tkinter import * #Para el GUI
import assets.files.ugman as ugman#El archivo principal de ugman
import random #Para conseguir valores aleatores
import tkinter.messagebox # Para poner cajas de mensajes en el GUI (i.e Habilidades J1)
import logging # Para el logging de juego


jugadores = []
jugador1_escoje = True

#Funciones apartes para escojer la clase
#Un jugador
def ARQ1():
    logging.debug("ARQ1()")
    top.destroy()
    un_jugador_escogio("arq")

def GUE1():
    logging.debug("GUE1()")
    top.destroy()
    un_jugador_escogio("gue")

#Dos jugadores
def ARQ2():
    global jugador1_escoje
    logging.debug("ARQ2()")
    if jugador1_escoje:
        print("1")
        jugador1_escoje = False
        jugadores.append("arq")
    else:
        jugadores.append("gue")
        print(jugadores)
        un_jugador_ini(multijugador=2)

def GUE2():
    global jugador1_escoje
    logging.debug("GUE2()")
    if jugador1_escoje:
        print("2")
        jugador1_escoje = False
        jugadores.append("gue")
    else:
        jugadores.append("gue")
        print(jugadores)
        un_jugador_ini(multijugador=2)


#Dos jugadores
def escojer_personaje_aux():
    Comenzar.destroy()
    nombreJ1_mult.destroy()
    nombreJ2_mult.destroy()
    Nombre1.destroy()
    Nombre2.destroy()
    escojer_personaje(2)



def local_mult_ini():
    Comenzar.destroy()
    Nombre1.destroy()
    nombreJ1.grid_remove()
    Nombre2.destroy()
    nombreJ2.grid_remove()



    nombreJugador1 = nombreJ1.get()
    ugman.J1.nombre = nombreJugador1
    nombreJugador2 = nombreJ2.get()
    ugman.J2.nombre = nombreJugador2


    log = Label(root,text=ugman.info(ugman.n), fg="green", bg="black", font=GrandeFont)
    log.grid(row=4, column=1)





#UN JUGADOR


def accionUJ(event=""):
    logging.debug("accionUJ")
    if event != "" and event.char != " ":
        accion = event.char
    else:
        accion = str(Accion.get()).lower()


    log.destroy()


    if accion not in ugman.ACCIONES and accion != "":
        pass
    else:
        logNuevo = ugman.ini(accion)
        un_jugador_ini("", logNuevo)

    logging.debug("VARIABLES:\naccion: {}\n".format(accion))

def habilidadesJ1Func():
    mensaje = tkinter.messagebox.showinfo("Habilidades J1", ugman.J1.habilidades)
    logging.debug("habilidadesJ1Func")

def habilidadesJ2Func():
    mensaje = tkinter.messagebox.showinfo("Habilidades J2", ugman.J2.habilidades)
    logging.debug("habilidadesJ2Func")


def ShowInfoHabilidad():
    tkinter.messagebox.showinfo("Informacion sobre la habilidad", ugman.LogTurno[2])


def un_jugador_ini(event = "", logParam = "", multijugador=1):
    logging.debug("un_jugador_ini()")
    #global nombreJ1, nombreJ2
    global nombreJugador2, logVida, primerTurno
    global Accion, log, habilidadesJ1, habilidadesJ2, AccionButton, Info
    w = 15

    frameTop = Frame(root, background="#18121E")
    frameTop.grid(row=0,column=0)

    frameRight = Frame(root, background="black", bd=8, relief="ridge")
    frameRight.grid(row=0, column=2, sticky="n")

    if not primerTurno:
        infoDeHabilidad = Button(frameRight, text="Sobre", fg="black", bg="white", command=ShowInfoHabilidad)
        infoDeHabilidad.grid(row=2,column=0)

    if not primerTurno:
        logText = ugman.info(ugman.n, Habilidad=True)
        logHabilidad = Label(frameRight, text=logText, bg="black",fg="green",borderwidth=5 ,width=w,font=GrandeFont)
        logHabilidad.grid(row=1, column=0)

    if primerTurno and multijugador == 1:
        ugman.definir_clase(claseJ1, claseJ2)
        primerTurno = False
        ugman.J1.nombre = nombreJ1.get()

    if primerTurno and multijugador == 2:

        ugman.definir_clase(jugadores[0], jugadores[1])
        primerTurno = False
        print(nombreJ1_mult.get())
        ugman.J1.nombre = nombreJ1_mult.get()
        ugman.J2.nombre = nombreJ2_mult.get()


    Comenzar.destroy()
    Nombre1.destroy()
    recordar.grid_remove()
    modo.destroy()




    try:
        habilidadesJ2.destroy()
        habilidadesJ1.destroy()
        Accion.destroy()
        AccionButton.destroy()
        Info.destroy()
        logVida.destroy()
    except:
        pass

    if recordarVar.get() == 1:
        JSON = json.load(open("./saves/guardado.json"))
        nombreRec = open("./saves/guardado.json","w+")
        content = "{\"Nombre\":\"%s\",\"Victorias\":0,\"Derrotas\":0,\"Partidas Jugadas\":0,\"Logros\":[],\"MODO_HISTORIA\":[]}" % (JSON["Nombre"])
        nombreRec.write(content)
        nombreRec.close()

    root.resizable(height=True, width=True)



    global nombreJugador1
    if ugman.J1.nombre == " " or ugman.J1.nombre == "":
        try:
            nombreRec = json.load(open("./saves/guardado.json"))
            #nombreRec = open("./saves/.guardado","r")
            #nom = nombreRec.read()
            #nombreRec.close()
            nombreJugador1 = nombreRec["Nombre"]

        except:
            if ugman.J1.nombre != "":
                nombreJugador1 = ugman.J1.nombre
    else:
        nombreJugador1 = ugman.J1.nombre
    nombreJ1.destroy()

    ugman.J1.nombre = nombreJugador1



    ugman.J2.nombre = nombreJugador2

    logVida = Label(frameRight, text=ugman.info(ugman.n, False, True), fg="green", bg="black",width=w, font=GrandeFont)
    logVida.grid(row=0, column=0)




    salir = Button(frameTop, text="Salir", fg="black",bg="white" ,width=w ,command=root.destroy,font=mainFont)
    salir.grid(row=1,column=0)


    habilidadesJ1 = Button(frameTop, text="Habilidades J1", fg="white", bg="blue" ,width=w, command=habilidadesJ1Func,font=mainFont)
    habilidadesJ1.grid(row=2, column=0)


    habilidadesJ2 = Button(frameTop, text="Habilidades J2", fg="white", bg="red" ,width=w , command=habilidadesJ2Func,font=mainFont)
    habilidadesJ2.grid(row=3, column=0)



    Info = Button(frameTop, text="Información", fg="black", bg="#d7d700" ,width=w,font=mainFont)
    Info.grid(row=4, column=0)

    Accion = Entry(frameTop)
    Accion.grid(row=5, column=1)

    if logParam == "":
        rondaLog = (ugman.info(ugman.n)).replace("_"," ")
        log = Label(root,text=rondaLog, fg="green", bg="black", height="50", width="60",font=mainFont, bd=8, relief="ridge")
    else:
        try:
            temp ="".join(list(logParam))
        except:
            temp = logParam
            print("a:",logParam)
        log = Label(root, text=(temp), fg="green", bg="black", height="50", width="60",font=mainFont, bd=5, relief="sunken")
    log.grid(row=0, column=1, sticky="n")

    if modoVar.get() == 1:
        AccionButton = Button(frameTop, text="PASAR", fg="white", bg="#94618E", width=w, command=accionUJ,font=mainFont)
        AccionButton.grid(row=5, column=0)
        Accion.grid_remove()
        root.bind("q", accionUJ)
        root.bind("w", accionUJ)
        root.bind("e", accionUJ)
        root.bind("r", accionUJ)
        root.bind("a", accionUJ)
        root.bind("<space>", accionUJ)
    else:
        AccionButton = Button(frameTop, text="ACCIÓN o PASAR", fg="white", bg="#94618E", width=w, command=accionUJ,font=mainFont)
        AccionButton.grid(row=5, column=0)
        root.bind("<Return>", accionUJ)

    logging.debug("\nw: {}\nprimerTurno: {}\nrecordarVar.get(): {}\nugman.J1.nombre: {}\nugman.J2.nombre: {}\nlogParam: {}\nmodoVar.get(): {}".
                  format(w,primerTurno,recordarVar.get(),ugman.J1.nombre,ugman.J2.nombre, logParam, modoVar.get()))


def un_jugador_escogio(clase):
    logging.debug("un_jugador_escogio()")
    global Comenzar, Nombre1, nombreJ1, recordar, recordarVar, claseJ1, modoVar, modo

    claseJ1 = clase

    recordarVar = IntVar()
    recordar = Checkbutton(root, text="Recordar Nombre", variable=recordarVar, selectcolor="black",fg="white",bg="#18121E",font=mainFont)
    recordar.grid(row=4, column=1)
    modoVar = IntVar()
    modo = Checkbutton(root, text="Modo Teclas", variable=modoVar, fg="white",selectcolor="black",bg="#18121E",font=mainFont)
    modo.grid(row=4, column=2)
    modo.select()

    Comenzar = Button(root, text="Comenzar", fg="white",bg="#94618E", command=un_jugador_ini,font=mainFont)
    Nombre1 = Label(root, text="J1", fg="red", bg="#18121E",font=mainFont)

    try:
        nom_r = json.load(open("saves/guardado.json"))
        #nom = open("./saves/.guardado", "r")
        #nom_r = nom.read()
        nombreJ1 = Entry(root)
        nombreJ1.insert(0, nom_r["Nombre"])
        print(nom_r["Nombre"])
    except:
        raise
        nombreJ1 = Entry(root)

    Comenzar.grid(row=3, column=2)
    Nombre1.grid(row=3, column=0)
    nombreJ1.grid(row=3, column=1)

    root.bind("<Return>", un_jugador_ini)

    logging.debug("VARIABLES:\n claseJ1: {}".format(claseJ1))




def escojer_personaje(jugadores = 1):
    logging.debug("escojer_personaje()")

    global top, jugador1_escoje, local, unJug

    jugador1_escoje = True

    #funcion al darle el boton un jugador
    local.destroy()
    unJug.destroy()

    w = 15

    top = Frame(root)
    top.grid(row=1, column=1)

    if jugadores == 1:
        funciones = [GUE1,ARQ1]
    elif jugadores == 2:
        funciones = [GUE2,ARQ2]


    guerreroButt = Button(top, text="Guerrero", bg="grey", width= w, command=funciones[0],font=mainFont)
    guerreroButt.grid(row=0,column=0)

    arqueraButt = Button(top, text="Arquera", bg="green", width= w, command=funciones[1],font=mainFont)
    arqueraButt.grid(row=0,column=1)

    orcoButt = Button(top, text="Orco", bg="#808040", width= w,font=mainFont)
    orcoButt.grid(row=0,column=2)

    magoButt = Button(top, text="Mago", bg="#0000ff", width= w,font=mainFont)
    magoButt.grid(row=0,column=3)

    curanderaButt = Button(top, text="Curandera", bg="#800040", width= w,font=mainFont)
    curanderaButt.grid(row=1,column=0)

    paladinButt = Button(top, text="Paladin", bg="#ffff80", width= w,font=mainFont)
    paladinButt.grid(row=1,column=1)

    berzerkerButt = Button(top, text="Berzerker", bg="#ff0000", width= w,font=mainFont)
    berzerkerButt.grid(row=1,column=2)

    asesinoButt = Button(top, text="Asesino", bg="#800000", width= w,font=mainFont)
    asesinoButt.grid(row=1,column=3)

    cazadorButt = Button(top, text="Cazador", bg="#004000", width= w,font=mainFont)
    cazadorButt.grid(row=2,column=0)

    vampiroButt = Button(top, text="Vampiro", bg="#000000", fg="white", width= w,font=mainFont)
    vampiroButt.grid(row=2,column=1)

    pirataButt = Button(top, text="Pirata", bg="#408080", width= w,font=mainFont)
    pirataButt.grid(row=2,column=2)

    duendeButt = Button(top, text="Duende", bg="#00ff00", width= w,font=mainFont)
    duendeButt.grid(row=2,column=3)

    carroñeroButt = Button(top, text="Carroñero", bg="#ff8000", width= w,font=mainFont)
    carroñeroButt.grid(row=3,column=0)

    brujaButt = Button(top, text="Bruja", bg="#400040", width= w,font=mainFont)
    brujaButt.grid(row=3,column=1)

    ninjaButt = Button(top, text="Ninja", bg="#c0c0c0", width= w,font=mainFont)
    ninjaButt.grid(row=3,column=2)

    zombieButt = Button(top, text="Zombie", bg="#008040", width= w,font=mainFont)
    zombieButt.grid(row=3,column=3)

    logging.debug("VARIABLES:\n w: {}".format(w))


def start_func():
    global local, unJug
    #Funcion al darle el boton de jugar
    start.destroy()
    comoJugar.destroy()
    Perfil.destroy()

    logging.debug("start_func()")




    local = Button(root, text="Local Multijugador", fg="white", bg="#94618E", command=local_mult,font=mainFont)
    local.grid(row=1, column=1)
    unJug = Button(root, text="Un Jugador", fg="white", bg="#94618E", command=escojer_personaje,font=mainFont)
    unJug.grid(row=1, column=2)



def local_mult():
    #funcion al darle el boton local multijugador
    local.destroy()
    unJug.destroy()

    global Comenzar, Nombre1, nombreJ1_mult, Nombre2, nombreJ2_mult
    Comenzar = Button(root, text="Comenzar", fg="white", bg="#94618E", command=escojer_personaje_aux,font=mainFont)
    Nombre1 = Label(root, text="J1", fg="red",font=mainFont, bg="#18121E")
    nombreJ1_mult = Entry(root)
    Nombre2 = Label(root, text="J2", fg="red",font=mainFont, bg="#18121E")
    nombreJ2_mult = Entry(root)

    Comenzar.grid(row=2)
    Nombre1.grid(row=3, column=0)
    Nombre2.grid(row=4, column=0)
    nombreJ1_mult.grid(row=3, column=1)
    nombreJ2_mult.grid(row=4, column=1)




#Funcion para ver y editar el perfil
def perfil():
    global ListoNombre

    start.destroy()
    comoJugar.destroy()
    Perfil.destroy()
    iconL.destroy()

    logging.debug("perfil()")

    frameTop = Frame(root, background="#18121E", bd=10, relief="ridge")
    frameTop.grid(row=0,column=0)


    def ListoNombre(nombre):

        frameContenido = Frame(root, bg="#18121E")
        frameContenido.grid(row=1,column=0)

        frameLogros = Frame(frameContenido, bg="#18121E")
        frameLogros.grid(row=0,column=0)

        frameProg = Frame(frameContenido, bg="#18121E")
        frameProg.grid(row=0,column=1)

        info = Label(frameTop, text=nombre, font=nombreFont, fg="white" , bg="#18121E")
        info.grid(row=0,column=0)

        info = Label(frameTop, text=("Victorias: %s"%(victorias)), font=perfilFont, fg="white" , bg="#18121E")
        info.grid(row=1,column=1, padx=50)

        info = Label(frameTop, text=("Derrotas: %s" % (derrotas)), font=perfilFont, fg="white", bg="#18121E")
        info.grid(row=1, column=2, padx=50)

        info = Label(frameTop, text=("Partidas Jugadas: %s" % (partidas)), font=perfilFont, fg="white", bg="#18121E")
        info.grid(row=1, column=3, padx=50)

        info = Label(frameLogros, text="Logros", font=perfilFont, fg="white", bg="#18121E")
        info.grid(row=0, column=0)

        info = Label(frameProg, text="Progreso modo historia", font=perfilFont, fg="white", bg="#18121E")
        info.grid(row=0, column=0, padx=50)


    try:

        with open('saves/guardado.json') as infoJSON:
            data = json.load(infoJSON)
            nombre = data["Nombre"]
            victorias = data["Victorias"]
            derrotas = data["Derrotas"]
            partidas = data["Partidas Jugadas"]
            logros = data["Logros"] if len(data["Logros"]) > 0 else ""
            progresoHistoria = data["MODO_HISTORIA"] if len(data["MODO_HISTORIA"]) else ""


            def nuevoNombre():
                def verificar():

                    nombre_aux = inputNombreTexto.get()
                    if nombre_aux == "" or nombre_aux == " ":
                        tkinter.messagebox.showwarning("Error","El nombre debe tener contenido")
                        nuevoNombre()
                    data["Nombre"] = nombre_aux
                    content = "{\"Nombre\":\"%s\",\"Victorias\":0,\"Derrotas\":0,\"Partidas Jugadas\":0,\"Logros\":[],\"MODO_HISTORIA\":[]}"%(data["Nombre"])
                    file = open('saves/guardado.json',"w")
                    file.write(content)
                    inputNombreTexto.destroy()
                    inputNombre.destroy()
                    submit.destroy()
                    ListoNombre(nombre_aux)


                inputNombre = Label(frameTop, text="Nombre",font=mainFont,fg="white",bg="#18121E")
                inputNombre.grid(row=0,column=0)
                inputNombreTexto = Entry(frameTop)
                inputNombreTexto.grid(row=0,column=1)
                submit = Button(frameTop, text="Listo",font=mainFont,command=verificar)
                submit.grid(row=0,column=2)




            if nombre == "":
                nuevoNombre()
            else:
                ListoNombre(nombre)


    except:
        raise
        tkinter.messagebox.showwarning("Alerta","El archivo guardado.json no se encuentra. Esto puede significar que no podrás guardar")
        nombre = "Sin Nombre"





#Funcion principal
def setup_ui():
    #Creacion de los logs de ui.py
    logging.info("\n************************\nInicio del debugging de ui.py")


    global nombreJugador1, nombreJugador2, claseJ2, clases, mas_menos, primerTurno,start, comoJugar, root, iconL, mainFont, GrandeFont, Perfil, perfilFont, nombreFont


    #Font principales
    mainFont = ("Times", 11, "bold")
    GrandeFont = ("Times", 14, "bold")
    perfilFont = ("Helvetica", 20, "bold italic")
    nombreFont = ("Helvetica", 22, "bold italic underline")

    #Selecionando los nombres aleatoriamente
    nombreJugador2 = ugman.NPC_NOMBRES[random.randint(0, 12)]
    nombreJugador1 = ugman.NPC_NOMBRES[random.randint(0, 12)]

    #Las clases
    clases = ["gue", "arq"]

    #Automaticamente escojer J2
    claseJ2 = clases[random.randint(0, len(clases)) - 1]

    mas_menos = False
    primerTurno = True



    #Creando la ventana de Tkinter
    root = Tk()
    root.title("UGMAN")
    root.configure(background='#18121E')
    root.iconbitmap(r'./assets/img/ugman.ico')

    #Agarrando el ugman.png y colocarlo
    try:
        icon = PhotoImage(file="./assets/img/ugman.png")
    except:
        raise NameError("ugman.png no existe o no está en el directorio correcto")
    iconL = Label(root, image=icon)
    iconL.grid(row=0, column=1)


    #Botones del menú principal
    start = Button(root, text="Jugar", fg="white", bg="#94618E", width=15, command=start_func, font=mainFont)
    comoJugar = Button(root, text="Como Jugar", fg="white", width=15, bg="#94618E", font=mainFont)
    Perfil = Button(root, text="Perfil", fg="white", width=15, bg="#94618E", font=mainFont, command=perfil)

    start.grid(row=1, column=0)
    comoJugar.grid(row=1, column=1)
    Perfil.grid(row=1, column=2)

    #El loop de Tkinter principal para que corra el programa, mainloop()
    #Sin el mainloop el programa se cierra apenas se corre

    #Dando los primeros variables
    logging.debug("VARIABLES: \nnombreJugador1: {}\nnombreJugador2: {}\nclaseJ2: {}\nmas_menos: {}\nprimerTurno: {}".format(nombreJugador1,nombreJugador2,claseJ2,mas_menos,primerTurno))
    root.mainloop()

if __name__ == "__main__":
    logging.warning("Se ejecutó ui.py")
    raise NameError("Archivo incorrecto")