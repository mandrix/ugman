from tkinter import *
import ugman


def def_nom():
    Comenzar.destroy()
    Nombre1.destroy()
    nombreJ1.grid_remove()
    Nombre2.destroy()
    nombreJ2.grid_remove()

    root.geometry("345x530")


    param1 = nombreJ1.get()
    ugman.J1.nombre = param1
    param2 = nombreJ2.get()
    ugman.J2.nombre = param2

    log = Label(root,text=ugman.info(ugman.n), fg="green", bg="black")
    log.grid(row=5, column=1)



def start_func():
    start.destroy()
    comoJugar.destroy()

    global local
    local = Button(root, text="Local Multijugador", fg="red", bg="black", command=local_func)
    local.grid(row=1, column=1)

def local_func():
    local.destroy()

    global Comenzar, Nombre1, nombreJ1, Nombre2, nombreJ2
    Comenzar = Button(root, text="Comenzar", fg="red", bg="black", command=def_nom)
    Nombre1 = Label(root, text="J1", fg="red")
    nombreJ1 = Entry(root)
    Nombre2 = Label(root, text="J2", fg="red")
    nombreJ2 = Entry(root)

    Comenzar.grid(row=2)
    Nombre1.grid(row=3, column=0)
    Nombre2.grid(row=4, column=0)
    nombreJ1.grid(row=3, column=1)
    nombreJ2.grid(row=4, column=1)



root = Tk()
root.geometry("250x250")
root.resizable(height=False, width=False)
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