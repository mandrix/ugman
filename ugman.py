from random import randint
import random
import time


#globales
n = 1#los turnos
console = False# bool que dice si está en modo consola
NPC_NOMBRES = ["Abaet","Bildon","Codern","Darmor","Etran","Gibolock","Hydale","Ithric","Lerin","Nuwolf","Orin","Radag'mal","Ethan"]
ACCIONES = ["a","q","w","e","r"]#todas las acciones posibles
primerTurno = True
quienComienza = ""

class personajes:




    def turno(self, other,accion):


        if self.stun != 0:
            print("%s está estuneado por %d más turnos, no pudo atacar" % (self.nombre,self.stun-1))
            self.stun -= 1
            if self.stun < 0:
                self.stun = 0
            return ("%s está estuneado por %d más turnos, no pudo atacar" % (self.nombre,self.stun-1))
        else:
            if accion == "a":
                daño = (self / other)
                if console:
                    print("\n%s atacó a %s con %d" % (self.nombre,other.nombre,daño))
                else:
                    return ("\n%s atacó a %s con %s" % (self.nombre,other.nombre,daño))
            elif accion == "q":
                self.velocidad_cambiar(20)
                return ("%s ahora tiene una velocidad de %d\n" % (
                self.nombre, self.velocidad))
            elif accion == "w":
                self.defensa_cambiar(30)
                self.stun_funcion(1)
                print("%s ahora tiene una defensa de %d\nY estará estuneado por %d turnos" % (self.nombre,self.defensa,self.stun))
                return ("%s ahora tiene una defensa de %d\nY estará estuneado por %d turnos" % (self.nombre,self.defensa,self.stun))
            elif accion == "e":
                self.golpeCritico_cambiar(0)
                self.velocidad_cambiar(0)
                daño = self.GUE_critico(other)
                return ("%s ahora tiene una velocidad y golpe critico de %d\n%s atacó a %s con %s"
                        % (self.nombre, self.velocidad,self.nombre,other.nombre,daño))
            else:
                self.stun_funcion(2)
                daño = self.GUE_ultra(other)
                return ("%s atacó a %s con %s usando la ULTRA\nY estará estuneado por %d turnos"
                    % ( self.nombre, other.nombre, daño, self.stun))

            print("============\n %s: %dHP\n %s: %dHP" % (self.nombre,self.vida,other.nombre,other.vida))



    def __truediv__(self, other):
        ataque = self.ataque
        defensa = other.defensa
        if self.clase == "guerrero":

            if randint(1,100) < self.presicion_critica:
                print("*CRITICO*")
                daño = (ataque * self.daño_critico - (ataque * self.daño_critico * defensa / 100))*2
                other.vida -= daño
                return ("%d *CRITICO*" % (daño))
            else:
                daño = ataque - (ataque * defensa / 100)
                other.vida -= daño
                return ("%.1f"% (daño))
        else:
            if randint(1, 100) < self.presicion_critica:
                return ataque * self.daño_critico - (ataque * self.daño_critico * defensa / 100)
            else:
                return ataque - (ataque * defensa / 100)


    def __init__(self,**kwargs):


        """
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
        """


    def defensa_cambiar(self,opcion):
        self.defensa = opcion
    def stun_funcion(self, opcion):
        self.stun = opcion
    def velocidad_cambiar(self,opcion):
        self.velocidad = opcion
    def golpeCritico_cambiar(self,opcion):
        self.golpe_critico = opcion

class guerrero(personajes):
    """
    pasiva : daño critico x2
    ataque basico : melee
    q : velocidad
    w : aumento de defensa por dos turnos hacia 90 % pierde su siguiente turno
    e : haces critico pero tu velocidad y golpe critico baja a 0
    r : haces 150 daño bruto pero estas estuneado por 2 turnos
    """

    def opcion(self):
        #Inteligencias artificiales dependiendo de la clase
        prob = randint(0,99)
        if self.ultra:
            prob -= 15
        if prob < 40:return "a"#40%
        elif prob < 55 and prob >= 40:return "q"#15%
        elif prob < 70 and prob >= 55:return "w"#15%
        elif prob < 85 and prob >= 70:return "e"#15%
        else:return "r"#15%

    def GUE_ultra(self,other):
        if not self.ultra:

            other.vida -= 150
            self.ultra = True
            return "150"
        return "0"

    def GUE_critico(self,other):
        ataque = self.ataque
        defensa = other.defensa

        print("*CRITICO*")
        daño = (ataque * self.daño_critico - (ataque * self.daño_critico * defensa / 100))*2
        other.vida -= daño
        return ("%d *CRITICO*" % (daño))



    def __init__(self):
        #habilidades
        self.habilidades = "Pasiva: daño critico x2\n\rQ: Aumenta velocidad a 18\n\rW: Aumenta defensa a 30 pero se estunea por 2 turnos\n\rE: Golpe Critico pero velocidad y golpe critico bajan a 0\n\rR: Haces 150 de daño bruto pero quedas estuneado por 2 turnos"


        self.ultra = False
        self.stun = 0
        self.vida = randint(450,500)#vida del jugador
        self.defensa = randint(10,14)#porcentaje que bloquea del ataque
        self.ataque = randint(55,60)#cantidad de puntos de vida en daño fisico que puede inflijir al enemigo sin buffs o debuffs
        self.magia = 0
        self.resistencia_magica = 9
        self.presicion = randint(15,18)#probabilidad de fallar
        self.daño_critico = 1.5# porcentaje de aumento de daño ataque
        self.presicion_critica = randint(34,40)#probabilidad de golpe critico
        self.mana = 0
        self.resistencia_debuff = 25
        self.rapidez = 45#comienza el que tenga mas rapidez
        self.velocidad = randint(10,11)#probabilidad en porcentaje de que sea el turno del jugador
        self.clase = "guerrero"#dependiendo de la clases, cambia stats, AI y pasivas
        self.nombre = ""#nombre que aparece en el juego


class arquero():
    """
    pasiva : cada golpe hara un segundo golpe de la mitad de su ataque a otro objetivo al azar
    ataque basico : alcance
    q : aumenta la probabilidad de fallar en un 70% del enemigo x2 durante 2 turnos(cd 2)
    w : aumenta el ataque de un aliado escogido y el tuyo por dos turnos (cd 3)
    e : encadena una serie de ataques por 3 turnos los cuales aumentaran su ataque (x1.1 x1.3 x1.5) si ninguno es fallado
        (si es fallado se stunea por un turno)
        y el tercer ataque tiene un 20% de stunear al enemigo y su bono de ataque se restablece no como la defensa op
        del guerrero :v(cd 2 (despues de terminar el encadenamiento))
    r : se pone inmune por 3 turnos y gana un turno despues de usarse(cd 6)
    """

    def opcion(self):
        #Inteligencias artificiales dependiendo de la clase
        prob = randint(0,99)
        if self.ultra:
            prob -= 15
        if prob < 40:return "a"#40%
        elif prob < 55 and prob >= 40:return "q"#15%
        elif prob < 70 and prob >= 55:return "w"#15%
        elif prob < 85 and prob >= 70:return "e"#15%
        else:return "r"#15%

    def ARQ_ultra(self):
        #aekgjojiwnfom
        refuerzo = self.defensa
        self.defensa = 100
        # le falta incluir el bono de turno ademas de que la defensa le falta reztablecerla en 3 turnos

    def ARQ_trifecta(self, other, other_2, num):
        if num == 0:
            self.ataque = self.ataque * 1.1
        elif num == 1:
            self.ataque = 1.3 * self.ataque
        else:
            self.ataque = 1.5 * self.ataque

        daño_0 = (self / other)
        daño_1 = (self / other_2)

        return (("%s atacó a %s con %.1f\n%s atacó a %s con %.1f" % (self.nombre, other.nombre, daño_0, self.nombre, other_2.nombre, daño_1)))

    def __init__(self):
        #habilidades
        self.habilidades = "Pasiva: daño critico x2\n\rQ: Aumenta velocidad a 18\n\rW: Aumenta defensa a 30 pero se estunea por 2 turnos\n\rE: Golpe Critico pero velocidad y golpe critico bajan a 0\n\rR: Haces 150 de daño bruto pero quedas estuneado por 2 turnos"

        self.ultra = False
        self.stun = 0
        self.vida = randint(450,500)#vida del jugador
        self.defensa = randint(10,14)#porcentaje que bloquea del ataque
        self.ataque = randint(55,60)#cantidad de puntos de vida en daño fisico que puede inflijir al enemigo sin buffs o debuffs
        self.magia = 0
        self.resistencia_magica = 9
        self.presicion = randint(15,18)#probabilidad de fallar
        self.daño_critico = 1.5# porcentaje de aumento de daño ataque
        self.presicion_critica = randint(34,40)#probabilidad de golpe critico
        self.resistencia_debuff = 25
        self.rapidez = 45#comienza el que tenga mas rapidez
        self.velocidad = randint(10,11)#probabilidad en porcentaje de que sea el turno del jugador
        self.clase = "guerrero"#dependiendo de la clases, cambia stats, AI y pasivas
        self.nombre = ""#nombre que aparece en el juego
        self.inmunidad =

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



J1 = guerrero()
J2 = guerrero()



"""
J2 = guerrero(vida = 500, defensa = 14, ataque = 55, magia = 0, resistencia_magica = 9,
                 presicion = 45, daño_critico = 1.5, presicion_critica = 34, mana = 0,
                 resistencia_debuff = 25, rapidez = 45, velocidad = 10, clase = "guerrero", nombre = nom2)

J1 = guerrero(vida = 500, defensa = 14, ataque = 55, magia = 0, resistencia_magica = 9,
                 presicion = 45, daño_critico = 1.5, presicion_critica = 34, mana = 0,
                 resistencia_debuff = 25, rapidez = 45, velocidad = 10 ,clase = "guerrero", nombre = nom1)
"""


def info(turno, Mas = True ,enseñar = False):
    if not enseñar:
        global primerTurno, quienComienza
        if primerTurno:
            quienComienza = ((J1.nombre if J1.rapidez > J2.rapidez else J2.nombre) if J1.rapidez != J2.rapidez else (J1.nombre if random.random() < 0.5 else J2.nombre ))
            primerTurno = False

    if console:
        print("##############TURNO %d##############\n"%(turno),15*"=")
        print("J1\nNombre: %s\nClase: %s\nVida: %d\nDefensa: %d\nAtaque: %d\nMagia: %d\nRM: %d\nPrecision: %d" % (J1.nombre,J1.clase,J1.vida,J1.defensa,J1.ataque,J1.magia,J1.resistencia_magica,J1.presicion))
        print("\n\n")
        print("J2\nNombre: %s\nClase: %s\nVida: %d\nDefensa: %d\nAtaque: %d\nMagia: %d\nRM: %d\nPrecision: %d" % (J2.nombre,J2.clase,J2.vida,J2.defensa,J2.ataque,J2.magia,J2.resistencia_magica,J2.presicion))
        print(15*"=","\n")
    if not enseñar:
        return ("##############TURNO %d##############\n\nJ1\nNombre: %s\nClase: %s\nVida: %d\nDaño_Crítico: %.1f\nDefensa: %d\nPresicion_critica: %d\nAtaque: %d\nMana: %d\nMagia: %d\nResistencia_Debuff: %d\nResistencia Mágica: %d\nVelocidad: %d\nPrecision: %d\n\n\n"
                "J2\nNombre: %s\nClase: %s\nVida: %d\nDaño_Crítico: %.1f\nDefensa: %d\nPresicion_critica: %d\nAtaque: %d\nMana: %d\nMagia: %d\nResistencia Debuff: %d\nResistencia Mágica: %d\nVelocidad: %d\nPrecision: %d\n\nTurno de %s\n"
                % (turno,J1.nombre,J1.clase,J1.vida,J1.daño_critico,J1.defensa,J1.presicion_critica,J1.ataque,J1.mana,J1.magia,J1.resistencia_debuff,J1.resistencia_magica,J1.velocidad,J1.presicion,
                   J2.nombre,J2.clase,J2.vida,J2.daño_critico,J2.defensa,J2.presicion_critica,J2.ataque,J2.mana,J2.magia,J2.resistencia_debuff,J2.resistencia_magica,J2.velocidad,J2.presicion, quienComienza))
    else:
        if not Mas:
            BarraDeVida = ""
            vida1 = J1.vida

            while True:
                porcentaje = vida1 - (500 * (1 / 10))
                if porcentaje >= 0:
                    BarraDeVida+="□"
                    vida1-=(500*(1/10))
                else:
                    break

            BarraDeVida2 = ""
            vida2 = J2.vida

            while True:
                porcentaje = vida2 - (500 * (1 / 10))
                if porcentaje >= 0:
                    BarraDeVida2+="□"
                    vida2-=(500*(1/10))
                else:
                    break
            return ("%s: \n%s\n%s: \n%s\n" % (J1.nombre, BarraDeVida,J2.nombre, BarraDeVida2))
        else:
            return (
            "##############TURNO %d##############\n\nJ1\nNombre: %s\nClase: %s\nVida: %d\nDaño_Crítico: %.1f\nDefensa: %d\nPresicion_critica: %d\nAtaque: %d\nMana: %d\nMagia: %d\nResistencia_Debuff: %d\nResistencia Mágica: %d\nVelocidad: %d\nPrecision: %d\n\n\n"
            "J2\nNombre: %s\nClase: %s\nVida: %d\nDaño_Crítico: %.1f\nDefensa: %d\nPresicion_critica: %d\nAtaque: %d\nMana: %d\nMagia: %d\nResistencia Debuff: %d\nResistencia Mágica: %d\nVelocidad: %d\nPrecision: %d\n\nTurno de %s\n"
            % (
            turno, J1.nombre, J1.clase, J1.vida, J1.daño_critico, J1.defensa, J1.presicion_critica, J1.ataque, J1.mana,
            J1.magia, J1.resistencia_debuff, J1.resistencia_magica, J1.velocidad, J1.presicion,
            J2.nombre, J2.clase, J2.vida, J2.daño_critico, J2.defensa, J2.presicion_critica, J2.ataque, J2.mana,
            J2.magia, J2.resistencia_debuff, J2.resistencia_magica, J2.velocidad, J2.presicion, quienComienza))


def ini(teclaParam="", multijugador = False):
    n += 1
    global n
    while console:
        info(n)
        if J1.vida <= 0: return ("¡%s a Ganado!"% J2.nombre)
        if J2.vida <= 0: return ("¡%s a Ganado!"% J1.nombre)
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

    else:
        if multijugador:
            while True:
                info(n)
                if J1.vida <= 0: return "¡Jugador2 a Ganado!"
                if J2.vida <= 0: return "¡Jugador1 a Ganado!"

                global quienComienza
                if quienComienza == J1.nombre:
                    quienComienza = J2.nombre
                    return (J2.turno(J1, teclaParam),"\n%s\n" % (info(n)))
                else:
                    quienComienza = J1.nombre
                    return (J1.turno(J2, teclaParam),"\n%s\n" % (info(n)))
        else:
            info(n)
            if J1.vida <= 0: return "¡Jugador2 a Ganado!"
            if J2.vida <= 0: return "¡Jugador1 a Ganado!"

            global quienComienza

            #quien va primero dependiendo de velocidad
            if randint(0,99) < J1.velocidad:
                quienComienza = J2.nombre

                return (J1.turno(J2, teclaParam), "\n*Va %s por su velocidad*\n%s\n" % (J1.nombre,info(n)))
            elif randint(0,99) < J2.velocidad:
                quienComienza = J1.nombre

                return (J2.turno(J1, J2.opcion()), "\n*Va %s por su velocidad*\n%s\n" % (J2.nombre,info(n)))


            #quien va primero dependiendo de quien fue antes
            if quienComienza == J1.nombre:
                quienComienza = J2.nombre

                if J1.presicion > randint(0,99):
                    return ("*La precision de %s lo hizo fallar*\n%s" % (J1.nombre, info(n)))
                return (J1.turno(J2, teclaParam), "\n%s\n" % (info(n)))
            else:
                quienComienza = J1.nombre

                if J2.presicion > randint(0,99):
                    return ("*La precision de %s lo hizo fallar*\n%s" % (J2.nombre, info(n)))
                return (J2.turno(J1, J2.opcion()), "\n%s\n" % (info(n)))


#si inicia este archivo en vez del ui.py entonces se juega en modo consola

if __name__ == "__main__":
    console = True