from random import randint



class personajes:
    def turno(self, other,accion):
        if self.stun != 0:
            print("%s está estuneado por %d más, no pudo atacar" % (self.nombre,self.stun-1))
            self.stun -= 1
        else:
            if accion == "a":
                daño = (self / other)
                print("%s atacó a %s con %d" % (self.nombre,other.nombre,daño))
            elif accion == "q":
                pass
            elif accion == "w":
                self.defensa_cambiar(90)
                self.stun_funcion()
                print("%s ahora tiene una defensa de %d\nY estará estuneado por %d turnos" % (self.nombre,self.defensa,self.stun))

            print("============\n %s: %dHP\n %s: %dHP" % (self.nombre,self.vida,other.nombre,other.vida))


    def __truediv__(self, other):#ataque neto
        ataque = self.ataque
        defensa = other.defensa
        if self.clase == "guerrero":

            if randint(1,100) < self.presicion_critica:
                print("*CRITICO*")
                daño = (ataque * self.daño_critico - (ataque * self.daño_critico * defensa / 100))*2
                other.vida -= daño
                return daño
            else:
                daño = ataque - (ataque * defensa / 100)
                other.vida -= daño
                return daño
        else:

            if randint(1, 100) < self.presicion_critica:
                return ataque * self.daño_critico - (ataque * self.daño_critico * defensa / 100)
            else:
                return ataque - (ataque * defensa / 100)
    def __init__(self,**kwargs):
        self.stun = 0
        self.nombre = kwargs["nombre"]
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
    def stun_funcion(self):
        self.stun = 1

class guerrero(personajes):
    def vidaf(self):return self.vida
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


nom1 = nom2 = ""


J2 = guerrero(vida = 500, defensa = 14, ataque = 55, magia = 0, resistencia_magica = 9,
                 presicion = 45, daño_critico = 1.5, presicion_critica = 34, mana = 0,
                 resistencia_debuff = 25, rapidez = 45, velocidad = 10, clase = "guerrero", nombre = nom2)

J1 = guerrero(vida = 500, defensa = 14, ataque = 55, magia = 0, resistencia_magica = 9,
                 presicion = 45, daño_critico = 1.5, presicion_critica = 34, mana = 0,
                 resistencia_debuff = 25, rapidez = 45, velocidad = 10 ,clase = "guerrero", nombre = nom1)



def info(turno):
    print("##############TURNO %d##############\n"%(turno),15*"=")
    print("J1\nNombre: %s\nClase: %s\nVida: %d\nDefensa: %d\nAtaque: %d\nMagia: %d\nRM: %d\nPrecision: %d" % (J1.nombre,J1.clase,J1.vida,J1.defensa,J1.ataque,J1.magia,J1.resistencia_magica,J1.presicion))
    print("\n\n")
    print("J2\nNombre: %s\nClase: %s\nVida: %d\nDefensa: %d\nAtaque: %d\nMagia: %d\nRM: %d\nPrecision: %d" % (J2.nombre,J2.clase,J2.vida,J2.defensa,J2.ataque,J2.magia,J2.resistencia_magica,J2.presicion))
    print(15*"=","\n")

    return ("##############TURNO %d##############\n"%(turno),15*"=","\nJ1\nNombre: %s\nClase: %s\nVida: %d\nDefensa: %d\nAtaque: %d\nMagia: %d\nRM: %d\nPrecision: %d\n" % (J1.nombre,J1.clase,J1.vida,J1.defensa,J1.ataque,J1.magia,J1.resistencia_magica,J1.presicion),"\n\n","\nJ2\nNombre: %s\nClase: %s\nVida: %d\nDefensa: %d\nAtaque: %d\nMagia: %d\nRM: %d\nPrecision: %d\n" % (J2.nombre,J2.clase,J2.vida,J2.defensa,J2.ataque,J2.magia,J2.resistencia_magica,J2.presicion),15*"=","\n")

n = 1
def ini():
    global n
    while True:
        info(n)
        if J1.vida <= 0: return "Jugador2"
        if J2.vida <= 0: return "Jugador1"
        if J1.rapidez < J2.rapidez:
            pass
        elif J1.rapidez > J2.rapidez:
            pass
        else:
            if randint(0,1):
                print("%s:\n"%(J2.nombre))
                tecla = input("Que ataque quieres realizar: ").lower()
                print("Turno de %s\n"%(J2.nombre),J2.turno(J1,tecla))
            else:
                print("%s:\n"%(J1.nombre))
                tecla = input("Que ataque quieres realizar: ").lower()
                print("Turno de %s\n"%(J1.nombre),J1.turno(J2,tecla))
        n+=1

