from random import randint
from tkinter import *
from tkinter import ttk
"""
root = Tk()
root.geometry("450x450")
root.title("Ugman")

 
frame = Frame(root)
 
labelText = StringVar()
 
label = Label(frame, textvariable=labelText)
button = Button(frame, text="jugar")
 
labelText.set("ugman")
label.pack()
button.pack()
frame.pack()
resultado = Frame(root)
r = StringVar()
f = Label(resultado, textvariable=r)
r.set()
f.pack()
resultado.pack()
root.mainloop()
"""
accion = input("que ataque quieres realizar: ").lower()
class personajes:
    def __truediv__(self, other):#ataque neto
        ataque = self.ataque
        defensa = other.defensa
        if self.clase == "guerrero":

            if randint(1,100) < self.presicion_critica:
                print("si es")
                return (ataque * self.daño_critico - (ataque * self.daño_critico * defensa / 100))*2
            else:
                print("no es ")
                return ataque - (ataque * defensa / 100)
        else:

            if randint(1, 100) < self.presicion_critica:
                return ataque * self.daño_critico - (ataque * self.daño_critico * defensa / 100)
            else:
                return ataque - (ataque * defensa / 100)
    def __init__(self,**kwargs):
        self.vida = kwargs["vida"]# cantidad de vida :v
        self.defensa = kwargs["defensa"]# porcentaje de ataque que se reduce
        self.ataque = kwargs["ataque"]# daño de ataque fijo
        self.magia = kwargs["magia"]# daño magico fijo
        self.resistencia_magica = kwargs["resistencia_magica"]#porcentaje de magia que se reduce
        self.presicion = kwargs["presicion"]# porcentaje de posibilidad de pegar debuff
        self.daño_critico = kwargs["daño_critico"]# porcentaje de aumento de daño ataque
        self.presicion_critica = kwargs["presicion_critica"]#porcentaje de que haya golpe critico
        self.mana = kwargs["mana"]#cantidad para arrojar hechizos
        self.resistencia_debuff = kwargs["resistencia_debuff"]# porcentaje de posibilidad de resistir un debuff
        self.rapidez = kwargs["rapidez"]#el tiempo para que llego cada turno
        self.clase = kwargs["clase"]
        self.velocidad = kwargs["velocidad"]#alcance para moverse en su turno "cantidad de casillas"
    def defensa_cambiar(self,opcion):
        self.defensa = opcion
class guerrero(personajes):
    """
    pasiva : daño critico x2
    ataque basico : melee
    q : velocidad
    w : aumento de defensa por dos turnos hacia 90 % pierde su siguiente turno
    e :
    r :
    """
class arquero():
    pass
    """
    alcance
    rapidez x4 cuando le falte media barra para atacar
    """
class orco():
    pass
    """
    melee
    cuando la vida baja de 30% su defensa y su ataque aumentan por 2 y se cura por 15 %
    countdown 5 turnos
    """
class mago():

    pass
    """
    mago
    cuando su mana sea menor de 30% su habilidades cuestan el 50%
    """
class curandera():
    pass
    """
    mago
    aura curacion 10x10 
    """
class paladin():
    pass
    """
    melee
    revive con 50% de vida al morir despues de una ronda 
    7 turnos de countdown
    """
class tanque():
    pass
    """
    mago
    previene en un 60% los ataques de distancia que van hacia los aliados detras de el
    """
class bomberman():
    pass
    """
    mago
    al morir explotara a cada enemigo una bomba equivalente al 35% de su ataque
    """
class asesino():
    pass
    """
    melee
    ataque x2 cuando la vida  del enemigo tenga menos de 50%
    """
class cazador():
    pass
    """
    alcance
    los ataques de el haran que  aumente la rapidez de los aliados
    """
class vampiro():
    pass
    """
    melee
    roba el 45% de su ataque como vida
    """
class pirata():
    pass
    """
    alcance
    silencia la pasiva del enemigo por 3 turnos
    """
class abejita ():
    pass





ugman2 = guerrero(vida = 500, defensa = 14, ataque = 55, magia = 0, resistencia_magica = 9,
                 presicion = 45, daño_critico = 1.5, presicion_critica = 34, mana = 0,
                 resistencia_debuff = 25, rapidez = 45, clase = "guerrero")

ugman = guerrero(vida = 500, defensa = 14, ataque = 55, magia = 0, resistencia_magica = 9,
                 presicion = 45, daño_critico = 1.5, presicion_critica = 34, mana = 0,
                 resistencia_debuff = 25, rapidez = 45, clase = "guerrero")

def guerrero_habilidades():
    if accion == "q":
        ugman.defensa_cambiar(90)
    if accion == "w":



print(ugman2 / ugman)

guerrero_habilidades()
print("def", ugman2 / ugman)
