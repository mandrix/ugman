from tkinter import *
import ugman
import random

param2 = ugman.NPC_NOMBRES[random.randint(0,12)]
mas_menos = False

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
    log.destroy()
    enseñarInfo.destroy()



    global enseñarInfoMas, mas_menos, enseñarInfoMenos
    if not mas_menos:

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
        enseñarInfoMas.grid(row=5, column=0)
        mas_menos = True
    else:

        try:
            logMas.destroy()
        except:
            pass

        global logMenos
        logMenos = Label(root, text=ugman.info(ugman.n, True ,True), fg="green", bg="black")
        logMenos.grid(row=5, column=1, sticky=W)
        try:
            enseñarInfoMas.destroy()
        except:
            pass
        enseñarInfoMenos = Button(root, text="Menos", fg="red", bg="black", command=enseñarInfo_func)
        enseñarInfoMenos.grid(row=5, column=0)
        mas_menos = False

def accionUJ():
    log.destroy()

    accion = str(Accion.get()).lower()
    if accion not in ugman.ACCIONES:
        pass
    else:
        logNuevo = ugman.ini(accion)
        un_jugador_ini(logNuevo)

def un_jugador_ini(logParam = ""):
    Comenzar.destroy()
    Nombre1.destroy()
    nombreJ1.grid_remove()

    root.resizable(height=True, width=True)


    param1 = "Valkoor"#nombreJ1.get()
    ugman.J1.nombre = param1

    global param2
    ugman.J2.nombre = param2

    salir = Button(root, text="Salir", bg="black", fg="red", command=root.destroy)
    salir.grid(row=4,column=0)

    global Accion, log, enseñarInfo
    enseñarInfo = Button(root, text="Mas", fg="red", bg="black", command=enseñarInfo_func)
    enseñarInfo.grid(row=5, column=0)
    AccionButton = Button(root, text="ACCIÓN", fg="red", bg="black", command=accionUJ)
    AccionButton.grid(row=6, column=0)
    Accion = Entry(root)
    Accion.grid(row=6, column=1)
    if logParam == "":
        log = Label(root,text=ugman.info(ugman.n), fg="green", bg="black")
    else:
        log = Label(root, text=logParam, fg="green", bg="black")
    log.grid(row=5, column=1)



def un_jugador():
    #funcion al darle el boton un jugador
    local.destroy()
    unJug.destroy()

    global Comenzar, Nombre1, nombreJ1
    Comenzar = Button(root, text="Comenzar", fg="red", bg="black", command=un_jugador_ini)
    Nombre1 = Label(root, text="J1", fg="red")
    nombreJ1 = Entry(root)


    Comenzar.grid(row=2)
    Nombre1.grid(row=3, column=0)
    nombreJ1.grid(row=3, column=1)



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