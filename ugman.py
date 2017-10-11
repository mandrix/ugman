from random import randint
import random
import time


#globales
n = 1#los turnos
console = False# bool que dice si está en modo consola
NPC_NOMBRES = ["Abaet","Bildon","Codern","Darmor","Etran","Gibolock","Hydale","Ithric","Lerin","Nuwolf","Orin","Radag'mal","Ethan","Tyrion"]
ACCIONES = ["a","q","w","e","r"]#todas las acciones posibles
primerTurno = True
quienComienza = ""

class personajes:




    def turno(self, other,accion):


        if self.stun > 0:
            self.stun -= 1
            if self.stun == 0:
                return ("el stun de %s se acabado, pero a perdido este turno" % (self.nombre))
            else:
                return ("%s está estuneado por %d más turnos y no podra atacar" % (self.nombre, self.stun))
        else:
            if self.clase == "Guerrero":
                if accion == "a":
                    daño = (self / other)
                    if console:
                        print("\n%s atacó a %s con %d" % (self.nombre, other.nombre, daño))
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
            elif self.nombre == "Arquero":
                if accion == "a":
                    daño = (self / other)


            print("============\n %s: %dHP\n %s: %dHP" % (self.nombre,self.vida,other.nombre,other.vida))



    def __truediv__(self, other):
        if self.clase == "Guerrero":
            if randint(1,100) < self.presicion_critica:
                print("*CRITICO*")
                daño = (self.ataque * self.daño_critico - (self.ataque * self.daño_critico * other.defensa / 100))*2
                other.vida -= daño
                return ("%d *CRITICO*" % (daño))
            else:
                daño = self.ataque - (self.ataque * self.defensa / 100)
                other.vida -= daño
                return ("%.1f"% (daño))
        elif self.clase == "Arquero":
            if randint(1, 100) < self.presicion_critica:
                print ("*CRITICO*")
                daño = self.ataque * self.daño_critico - (self.ataque * self.daño_critico * other.defensa / 100)
                other.vida -= daño
                print ("%d *CRITICO*" % (daño))
           # aqui falta
            else:
                daño = self.ataque  - (self.ataque * self.defensa / 100)
                other.vida -= daño
            if randint(1,100) < self.presicion_critica:
                daño = self.ataque * self.daño_critico - (self.ataque * self.daño_critico * other.defensa / 100)
                other.vida -= (daño / 2)
            else:
                daño = self.ataque * self.daño_critico - (self.ataque * self.daño_critico * other.defensa / 100)
                other.vida -= (daño / 2)




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
        print("*CRITICO*")
        daño = (self.ataque * self.daño_critico - (self.ataque * self.daño_critico * other.defensa / 100))*2
        other.vida -= daño
        return ("%d *CRITICO*" % (daño))



    def __init__(self):
        #habilidades
        self.habilidades = "Pasiva: daño critico x2\n\rQ: Aumenta velocidad a 18\n\rW: Aumenta defensa a 30 pero se estunea por 2 turnos\n\rE: Golpe Critico pero velocidad y golpe critico bajan a 0\n\rR: Haces 150 de daño bruto pero quedas estuneado por 2 turnos"


        self.ultra = False
        self.stun = 0
        self.vida = randint(450,500)#vida del jugador
        self.guardar_vida = self.vida
        self.defensa = randint(12,16)#porcentaje que bloquea del ataque
        self.ataque = randint(55,60)#cantidad de puntos de vida en daño fisico que puede inflijir al enemigo sin buffs o debuffs
        self.magia = 0
        self.resistencia_magica = randint(8,12)
        self.presicion = randint(15,18)#probabilidad de fallar
        self.daño_critico = 1.5# porcentaje de aumento de daño ataque
        self.presicion_critica = randint(34,40)#probabilidad de golpe critico
        self.presicion_debuff = randint(20,24)
        self.resistencia_debuff = randint(8,12)
        self.rapidez = 45#comienza el que tenga mas rapidez
        self.velocidad = randint(10,11)#probabilidad en porcentaje de que sea el turno del jugador
        self.clase = "Guerrero"#dependiendo de la clases, cambia stats, AI y pasivas
        self.nombre = ""#nombre que aparece en el juego


class arquero(personajes):
    """
    pasiva : cada golpe hara un segundo golpe de la mitad de su ataque a otro objetivo al azar
    ataque basico : alcance
    q : aumenta la probabilidad de fallar en un 70% del enemigo x2 durante 2 turnos(cd 2)
    w : aumenta el ataque de un aliado escogido y el tuyo por dos turnos (cd 3)
    e : encadena una serie de ataques por 3 turnos los cuales aumentaran su ataque (x1.1 x1.3 x1.5) si ninguno es fallado
        (si es fallado se stunea por un turno)
        y el tercer ataque tiene un 20% de stunear al enemigo(+ % de base) y su bono de ataque se restablece no como la defensa op
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
        refuerzo = self.defensa
        self.defensa = 100
        # le falta incluir el bono de turno despues de usar esta habilidad ademas de que la defensa le falta reztablecerla en 3 turnos

    def ARQ_beneficio(self, others):
        self.ataque *= 2
        others.ataque *= 2
        # le falta que se reztablezcca despues de 3 turnos

    def ARQ_bomba_de_gas(self,other):
        if randint(0,99) < (70 + self.presicion_debuff) -  ((70 + self.presicion_debuff) / other):
            other.presicion *= 2
        #3 le falta que se restablezca despues de 2 turnos

    def ARQ_trifecta(self, other, other_2, num):
        #se stunea por un turno si falla
        #son ataques que se realizan por turnos consecutivamente hasta que llegue el tercero o hasta que falle
        #le falta return prints
        if num == 0:
            daño = self.ataque * 1.1
        elif num == 1:
            daño = self.ataque * 1.3
        else:
            if randint(0,99) < (20 + self.presicion_debuff) -  ((20 + self.presicion_debuff) / other.resistencia_debuff):
                other.stun = 1
            daño = self.ataque * 1.5

        if randint(1, 100) < self.presicion_critica:
            print("*CRITICO*")
            daño = daño * self.daño_critico - (daño * self.daño_critico * other.defensa / 100)
            other.vida -= daño
            print("%d *CRITICO*" % (daño))
            # aqui falta
        else:
            daño = daño - (daño * other.defensa / 100)
            other.vida -= daño

        if randint(1, 100) < self.presicion_critica:
            daño_1 = (daño * self.daño_critico - (daño * self.daño_critico * other_2.defensa / 100)) / 2
            other.vida -= daño_1
        else:
            daño_1 = (daño * self.daño_critico - (daño * self.daño_critico * other_2.defensa / 100)) / 2
            other.vida -= daño
        return (("%s atacó a %s con %.1f\n%s atacó a %s con %.1f" % (self.nombre, other.nombre, daño, self.nombre, other_2.nombre, daño_1)))

    def __init__(self):
        #habilidades
        self.habilidades = "Pasiva: cada ataque genera un ataque extra que sera l mitad de su ataque\n\rQ: aumenta la probabilidad de fallar en un 70% del enemigo x2 durante 2 turnos\n\rW: aumenta el ataque de un aliado escogido y el tuyo por dos turnos\n\rE:hace la trifecta \n\rR:se pone inmune por 3 turnos y gana un turno despues de usarse"
        self.ultra = False
        self.stun = 0
        self.vida = randint(375,425)#vida del jugador
        self.guardar_vida = self.vida
        self.defensa = randint(8,12)#porcentaje que bloquea del ataque
        self.ataque = randint(40,45)#cantidad de puntos de vida en daño fisico que puede infligir al enemigo sin buffs o debuffs
        self.magia = 0
        self.resistencia_magica = randint(12,16)
        self.presicion = randint(20,24)#probabilidad de fallar
        self.daño_critico = 1.5# porcentaje de aumento de daño ataque
        self.presicion_critica = randint(30,35)#probabilidad de golpe critico
        self.presicion_debuff = randint(15, 20)
        self.resistencia_debuff = randint(25, 30)
        self.rapidez = 45#comienza el que tenga mas rapidez
        self.velocidad = randint(10,11)#probabilidad en porcentaje de que sea el turno del jugador
        self.clase = "Arquero"#dependiendo de la clases, cambia stats, AI y pasivas
        self.nombre = ""#nombre que aparece en el juego
        self.inmunidad = 0

class orco(personajes):
    """
    pasiva : cada vez recibes o haces daño te aumenta la defensa por 2% maximo 10 cargas
    ataque basico : ataca al enemigo entre mas defensa mas daño causas
    q : cura tu vida en 10% + 50% de la defensa actual ofende a todos sun enemigos por 50% durante 1 turno (10% + 10% * def / 50 )
    w : ataca con su bate un ataque giratotio a todos sus enemigos de un 40% de su ataque, entre mas vida te falte mas daño hace
    e : se libera de cualquier debuff y a sus aliados cura al aliado con el rango mas bajo de vida por 20%
    r :
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

    def ORC_ultra(self, other):




    def ORC_Qrefuerzo(self, other):
        pass

    def ARQ_Wespiral(self,other):
        pass

    def ARQ_trifecta(self, other, other_2, num):
        #se stunea por un turno si falla
        if num == 0:
            self.ataque = self.ataque * 1.1
        elif num == 1:
            self.ataque = 1.3 * self.ataque
        else:
            if randint(0,99) < (20 + self.presicion_debuff) -  ((20 + self.presicion_debuff) / other):
                other.stun = 1
            self.ataque = 1.5 * self.ataque
        daño_0 = (self / other)
        daño_1 = (self / other_2)# aqui es la mitad

        return (("%s atacó a %s con %.1f\n%s atacó a %s con %.1f" % (self.nombre, other.nombre, daño_0, self.nombre, other_2.nombre, daño_1)))

    def __init__(self):
        #habilidades #listas
        self.habilidades =  "pasiva : cada vez recibe o hace daño el orco aumenta la defensa por 2% maximo 10 cargas\r\n Q: cura tu vida en 10% + 50% de la defensa actual ofende a todos sun enemigos por 50% durante 1 turno \r\n W: ataca con su bate un ataque giratotio a todos sus enemigos de un 40% de su ataque, entre mas vida te falte mas daño hace\r\nE: se libera de cualquier debuff y a sus aliados cura al aliado con el rango mas bajo de vida por 20%\r\nR : ataca a su objetivo infligiendo todo el hp que te falta + porcentuamente la defensa, lo deja stuneado un turno"
        self.ultra = False
        self.stun = 0
        self.vida = randint(500, 550)#vida del jugador
        self.guardar_vida = self.vida
        self.defensa = randint(18,22)#porcentaje que bloquea del ataque
        self.ataque = randint(20,25)#cantidad de puntos de vida en daño fisico que puede infligir al enemigo sin buffs o debuffs
        self.magia = 0
        self.resistencia_magica = randint(20,24)
        self.presicion = randint(15,19)#probabilidad de fallar
        self.daño_critico = 1.5# porcentaje de aumento de daño ataque
        self.presicion_critica = randint(20,25)#probabilidad de golpe critico
        self.presicion_debuff = randint(15, 20)
        self.resistencia_debuff = randint(10, 15)
        self.rapidez = 45#comienza el que tenga mas rapidez
        self.velocidad = randint(10,11)#probabilidad en porcentaje de que sea el turno del jugador
        self.clase = "Orco"#dependiendo de la clases, cambia stats, AI y pasivas
        self.nombre = ""#nombre que aparece en el juego
        self.inmunidad = 0
class mago(personajes):

    pass
    """
    mago
    cuando su mana sea menor de 30% su habilidades cuestan el 50%
    """
class curandera(personajes):
    pass
    """
    mago
    aura curacion 10x10 
    """
class paladin(personajes):
    pass
    """
    melee
    revive con 50% de vida al morir despues de una ronda 
    7 turnos de countdown
    """
class tanque(personajes):
    pass
    """
    mago
    previene en un 60% los ataques de distancia que van hacia los aliados detras de el
    """
class bomberman(personajes):
    pass
    """
    mago
    al morir explotara a cada enemigo una bomba equivalente al 35% de su ataque
    """
class asesino(personajes):
    pass
    """
    melee
    ataque x2 cuando la vida  del enemigo tenga menos de 50%
    """
class cazador(personajes):
    pass
    """
    alcance
    los ataques de el haran que  aumente la rapidez de los aliados
    """
class vampiro(personajes):
    pass
    """
    melee
    roba el 45% de su ataque como vida
    """
class pirata(personajes):
    pass
    """
    alcance
    silencia la pasiva del enemigo por 3 turnos
    """



def definir_clase(claseJ1, claseJ2):
    global J1, J2
    if claseJ1 == "gue":
        J1 = guerrero()
    elif claseJ1 == "arq":
        J1 = arquero()


    if claseJ2 == "gue":
        J2 = guerrero()
    elif claseJ2 == "arq":
        J2 = arquero()




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
        return ("##############TURNO %d##############\n\nJ1\nNombre: %s\nClase: %s\nVida: %d\nDaño_Crítico: %.1f\nDefensa: %d\nPresicion_critica: %d\nAtaque: %d\nMagia: %d\nResistencia_Debuff: %d\nResistencia Mágica: %d\nVelocidad: %d\nPrecision: %d\n\n\n"
                "J2\nNombre: %s\nClase: %s\nVida: %d\nDaño_Crítico: %.1f\nDefensa: %d\nPresicion_critica: %d\nAtaque: %d\nMagia: %d\nResistencia Debuff: %d\nResistencia Mágica: %d\nVelocidad: %d\nPrecision: %d\n\nTurno de %s\n"
                % (turno,J1.nombre,J1.clase,J1.vida,J1.daño_critico,J1.defensa,J1.presicion_critica,J1.ataque,J1.magia,J1.resistencia_debuff,J1.resistencia_magica,J1.velocidad,J1.presicion,
                   J2.nombre,J2.clase,J2.vida,J2.daño_critico,J2.defensa,J2.presicion_critica,J2.ataque,J2.magia,J2.resistencia_debuff,J2.resistencia_magica,J2.velocidad,J2.presicion, quienComienza))
    else:
        if not Mas:
            BarraDeVida = ""
            vida1 = J1.vida

            while True:
                print(J1.guardar_vida)
                print(J1.vida)
                porcentaje = vida1 - (J1.guardar_vida * (1 / 10))
                if porcentaje >= 0:
                    BarraDeVida += "□"
                    vida1-=(J1.guardar_vida * (1 / 10))
                else:
                    break

            BarraDeVida2 = ""
            vida2 = J2.vida

            while True:
                porcentaje = vida2 - (  J2.guardar_vida * (1 / 10))
                if porcentaje >= 0:
                    BarraDeVida2 += "□"
                    vida2-=(J2.guardar_vida * (1 / 10))
                else:
                    break
            return ("%s: \n%s\n%s: \n%s\n" % (J1.nombre, BarraDeVida,J2.nombre, BarraDeVida2))
        else:
            return (
            "##############TURNO %d##############\n\nJ1\nNombre: %s\nClase: %s\nVida: %d\nDaño_Crítico: %.1f\nDefensa: %d\nPresicion_critica: %d\nAtaque: %d\nMagia: %d\nResistencia_Debuff: %d\nResistencia Mágica: %d\nVelocidad: %d\nPrecision: %d\n\n\n"
            "J2\nNombre: %s\nClase: %s\nVida: %d\nDaño_Crítico: %.1f\nDefensa: %d\nPresicion_critica: %d\nAtaque: %d\nMagia: %d\nResistencia Debuff: %d\nResistencia Mágica: %d\nVelocidad: %d\nPrecision: %d\n\nTurno de %s\n"
            % (
            turno, J1.nombre, J1.clase, J1.vida, J1.daño_critico, J1.defensa, J1.presicion_critica, J1.ataque,
            J1.magia, J1.resistencia_debuff, J1.resistencia_magica, J1.velocidad, J1.presicion,
            J2.nombre, J2.clase, J2.vida, J2.daño_critico, J2.defensa, J2.presicion_critica, J2.ataque,
            J2.magia, J2.resistencia_debuff, J2.resistencia_magica, J2.velocidad, J2.presicion, quienComienza))


def ini(teclaParam="", multijugador = False):
    global n
    global quienComienza

    n += 1

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