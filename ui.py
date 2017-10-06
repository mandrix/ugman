from tkinter import *
import ugman
import random
import tkinter.messagebox

param2 = ugman.NPC_NOMBRES[random.randint(0,12)]
param1 = ugman.NPC_NOMBRES[random.randint(0,12)]
clases = ["gue", "arq"]
claseJ2 = clases[random.randint(0,len(clases))-1]
mas_menos = False
primerTurno = True

def local_mult():
    #funcion al darle el boton local multijugador
    local.destroy()

    global Comenzar, Nombre1, nombreJ1, Nombre2, nombreJ2
    Comenzar = Button(root, text="Comenzar", fg="red", bg="black", command=local_mult_ini)
    Nombre1 = Label(root, text="J1", fg="red")
    nombreJ1 = Entry(root)
    Nombre2 = Label(root, text="J2", fg="red")
    nombreJ2 = Entry(root)

    Comenzar.grid(row=2)
    Nombre1.grid(row=3, column=0)
    Nombre2.grid(row=4, column=0)
    nombreJ1.grid(row=3, column=1)
    nombreJ2.grid(row=4, column=1)





def local_mult_ini():
    Comenzar.destroy()
    Nombre1.destroy()
    nombreJ1.grid_remove()
    Nombre2.destroy()
    nombreJ2.grid_remove()

    root.geometry("335x530")


    param1 = nombreJ1.get()
    ugman.J1.nombre = param1
    param2 = nombreJ2.get()
    ugman.J2.nombre = param2


    log = Label(root,text=ugman.info(ugman.n), fg="green", bg="black")
    log.grid(row=5, column=1)





#UN JUGADOR

def enseñarInfo_func():
    global enseñarInfoMas, mas_menos, enseñarInfoMenos
    log.destroy()
    enseñarInfoMas.destroy()
    enseñarInfoMas.destroy()


    if not mas_menos:
        global logMenos
        try:
            logMenos.destroy()
        except:
            pass

        global logMas
        logMas = Label(root, text=ugman.info(ugman.n, False, True), fg="green", bg="black")
        logMas.grid(row=5, column=1, sticky=W)
        try:
            enseñarInfoMenos.destroy()
        except:
            pass
        enseñarInfoMas = Button(root, text="Mas", fg="red", bg="black", command=enseñarInfo_func)
        enseñarInfoMas.grid(row=5, column=0, sticky=W)
        mas_menos = True
    else:

        try:
            logMas.destroy()
        except:
            pass


        logMenos = Label(root, text=ugman.info(ugman.n, True ,True), fg="green", bg="black")
        logMenos.grid(row=5, column=1, sticky=W)
        try:
            enseñarInfoMas.destroy()
        except:
            pass
        enseñarInfoMenos = Button(root, text="Menos", fg="red", bg="black", command=enseñarInfo_func)
        enseñarInfoMenos.grid(row=5, column=0)
        mas_menos = False

def accionUJ(event=""):

    if event != "" and event.char != " ":
        accion = event.char
    else:
        accion = str(Accion.get()).lower()

    if ugman.quienComienza == ugman.J1.nombre and accion == "":
        tkinter.messagebox.showinfo("Error","Debes poner una accion")
    else:
        log.destroy()


    if accion not in ugman.ACCIONES and accion != "":
        pass
    else:
        logNuevo = ugman.ini(accion)
        un_jugador_ini(logNuevo)

def habilidadesJ1Func():
    mensaje = tkinter.messagebox.showinfo("Habilidades J1", ugman.J1.habilidades)

def habilidadesJ2Func():
    mensaje = tkinter.messagebox.showinfo("Habilidades J2", ugman.J2.habilidades)

def un_jugador_ini(logParam = ""):
    global param2, logMas, primerTurno
    global Accion, log, habilidadesJ1, habilidadesJ2, AccionButton, Info

    if primerTurno:
        ugman.definir_clase(claseJ1, claseJ2)
        primerTurno = False


    Comenzar.destroy()
    Nombre1.destroy()
    nombreJ1.grid_remove()
    recordar.grid_remove()

    try:
        habilidadesJ2.destroy()
        habilidadesJ1.destroy()
        Accion.destroy()
        AccionButton.destroy()
        Info.destroy()
        logMas.destroy()
    except:
        pass

    if recordarVar.get() == 1:
        nombreRec = open(".guardado","w+")
        nombreRec.write(nombreJ1.get())
        nombreRec.close()

    root.resizable(height=True, width=True)

    frameTop = Frame(root)
    frameTop.grid(row=0,column=0)

    global param1
    try:
        nombreRec = open(".guardado","r")
        nom = nombreRec.read()
        nombreRec.close()
        param1 = nom

    except:
        if nombreJ1.get() != "":
            param1 = nombreJ1.get()

    ugman.J1.nombre = param1


    ugman.J2.nombre = param2

    logMas = Label(frameTop, text=ugman.info(ugman.n, False, True), fg="green", bg="black")
    logMas.grid(row=0, column=2, sticky=N)

    salir = Button(frameTop, text="Salir", command=root.destroy)
    salir.grid(row=0,column=0)


    habilidadesJ1 = Button(frameTop, text="Habilidades J1", fg="white", bg="blue", command=habilidadesJ1Func)
    habilidadesJ1.grid(row=1, column=0)

    habilidadesJ2 = Button(frameTop, text="Habilidades J2", fg="white", bg="red", command=habilidadesJ2Func)
    habilidadesJ2.grid(row=2, column=0)

    root.bind("q", accionUJ)
    root.bind("w", accionUJ)
    root.bind("e", accionUJ)
    root.bind("r", accionUJ)
    root.bind("a", accionUJ)
    root.bind("<space>", accionUJ)

    AccionButton = Button(frameTop, text="ACCIÓN o PASAR", fg="red", bg="black", command=accionUJ)
    AccionButton.grid(row=4, column=0)

    Info = Button(frameTop, text="Información", fg="white", bg="yellow")
    Info.grid(row=3, column=0)

    Accion = Entry(frameTop)
    Accion.grid(row=4, column=1)

    if logParam == "":
        log = Label(root,text=ugman.info(ugman.n), fg="green", bg="black")
    else:
        log = Label(root, text=logParam, fg="green", bg="black")
    log.grid(row=0, column=1)


def un_jugador_escogio(clase):
    global Comenzar, Nombre1, nombreJ1, recordar, recordarVar, claseJ1

    claseJ1 = clase

    recordarVar = IntVar()
    recordar = Checkbutton(root, text="Recordar nombre", variable=recordarVar)
    recordar.grid(row=4, column=1)
    Comenzar = Button(root, text="Comenzar", fg="red", bg="black", command=un_jugador_ini)
    Nombre1 = Label(root, text="J1", fg="red")

    try:
        nom = open(".guardado", "r")
        nom_r = nom.read()
        nombreJ1 = Entry(root)
        nombreJ1.insert(0, nom_r)
    except:
        nombreJ1 = Entry(root)

    Comenzar.grid(row=2)
    Nombre1.grid(row=3, column=0)
    nombreJ1.grid(row=3, column=1)


def ARQ1():
    top.destroy()
    un_jugador_escogio("arq")

def GUE1():
    top.destroy()
    un_jugador_escogio("gue")

def un_jugador():
    global top#guerreroButt, arqueraButt, orcoButt, magoButt, curanderaButt, paladinButt, berzerkerButt, asesinoButt, cazadorButt, vampiroButt, pirataButt, duendeButt, carroñeroButt, brujaButt, ninjaButt, zombieButt

    #funcion al darle el boton un jugador
    local.destroy()
    unJug.destroy()

    w = 15

    top = Frame(root)
    top.grid(row=1, column=1)

    guerreroButt = Button(top, text="Guerrero", bg="grey", width= w, command=GUE1)
    guerreroButt.grid(row=0,column=0)

    arqueraButt = Button(top, text="Arquera", bg="green", width= w, command=ARQ1)
    arqueraButt.grid(row=0,column=1)

    orcoButt = Button(top, text="Orco", bg="#808040", width= w)
    orcoButt.grid(row=0,column=2)

    magoButt = Button(top, text="Mago", bg="#0000ff", width= w)
    magoButt.grid(row=0,column=3)

    curanderaButt = Button(top, text="Curandera", bg="#800040", width= w)
    curanderaButt.grid(row=1,column=0)

    paladinButt = Button(top, text="Paladin", bg="#ffff80", width= w)
    paladinButt.grid(row=1,column=1)

    berzerkerButt = Button(top, text="Berzerker", bg="#ff0000", width= w)
    berzerkerButt.grid(row=1,column=2)

    asesinoButt = Button(top, text="Asesino", bg="#800000", width= w)
    asesinoButt.grid(row=1,column=3)

    cazadorButt = Button(top, text="Cazador", bg="#004000", width= w)
    cazadorButt.grid(row=2,column=0)

    vampiroButt = Button(top, text="Vampiro", bg="#000000", fg="white", width= w)
    vampiroButt.grid(row=2,column=1)

    pirataButt = Button(top, text="Pirata", bg="#408080", width= w)
    pirataButt.grid(row=2,column=2)

    duendeButt = Button(top, text="Duende", bg="#00ff00", width= w)
    duendeButt.grid(row=2,column=3)

    carroñeroButt = Button(top, text="Carroñero", bg="#ff8000", width= w)
    carroñeroButt.grid(row=3,column=0)

    brujaButt = Button(top, text="Bruja", bg="#400040", width= w)
    brujaButt.grid(row=3,column=1)

    ninjaButt = Button(top, text="Ninja", bg="#c0c0c0", width= w)
    ninjaButt.grid(row=3,column=2)

    zombieButt = Button(top, text="Zombie", bg="#008040", width= w)
    zombieButt.grid(row=3,column=3)

#       bombermanButt = Button(top, text="Bomberman", bg="green")
#        bombermanButt.grid(row=0,column=1)


def start_func():
    #Funcion al darle el boton de jugar
    start.destroy()
    comoJugar.destroy()

    global local, unJug
    local = Button(root, text="Local Multijugador", fg="red", bg="black", command=local_mult)
    local.grid(row=1, column=1)
    unJug = Button(root, text="Un Jugador", fg="red", bg="black", command=un_jugador)
    unJug.grid(row=1, column=2)






root = Tk()
root.title("UGMAN")


icon = PhotoImage(file="ugman.png")
iconL = Label(root, image=icon)
iconL.grid(row=0, column=1)


start = Button(root, text="Jugar", fg="red", bg="black", command=start_func)
comoJugar = Button(root, text="Como Jugar", fg="red", bg="black")

start.grid(row=1, column=0)
comoJugar.grid(row=1,column=1)

#local



root.mainloop()