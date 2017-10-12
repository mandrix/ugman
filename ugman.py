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
equipoA = []
equipoB = []

class personajes:


    def turno(self, other, accion, intento = False):


        #Turnos debuffs
        for key, value, in self.efectos.items():
            
            if key == "D_precision":
                if value[0] != 0:
                    self.efectos[key][0] -= 1
                elif self.efectos[key][1]:
                    self.efectos[key][1] = False
                    self.precision = self.guardar_precision

            elif key == "B_ataque":
                if value[0] != 0:
                    self.efectos["B_ataque"][0] -= 1
                elif self.efectos["B_ataque"][1]:
                   self.efectos["B_ataque"][1] = False
                   self.ataque = self.guardar_ataque

            elif key == "B_inmunidad":
                if value[0] != 0:
                    self.efectos["B_inmunidad"][0] -= 1
                elif self.efectos["B_inmunidad"][1]:
                    self.efectos["B_inmunidad"][1] = False
                    self.defensa = self.guardar_defensa

            elif key == "B_defensa":
               if value[0] != 0:
                   self.efectos["B_defensa"][0] -= 1
               elif self.efectos["B_defensa"][1]:
                   self.efectos["B_defensa"][1] = False
                   self.defensa = self.guardar_defensa
                   
            elif key == "Trifecta":
                if intento and self.efectos["Trifecta"][1]:
                    self.efectos["Trifecta"] = [0, False]
                    self.stun = 2


        if self.stun > 0:
            self.stun -= 1
            if self.stun == 0:
                return ("el stun de %s se acabado, pero a perdido este turno" % (self.nombre))
            else:
                return ("%s está estuneado por %d más turnos y no podra atacar" % (self.nombre, self.stun))
        
        if not intento:
            if self.clase == "Guerrero":
                if accion == "a":
                    daño = (self / other)
                    return ("\n%s atacó a %s con %s" % (self.nombre,other.nombre,daño))
                elif accion == "q":
                    self.velocidad_cambiar(20)
                    return ("%s ahora tiene una velocidad de %d\n" % (
                    self.nombre, self.velocidad))
                elif accion == "w":
                    self.defensa_cambiar(30)
                    self.efectos["B_defensa"] = [2, True]
                    self.stun_funcion(1)
                    return ("%s ahora tiene una defensa de %d\nY estará estuneado por %d turnos" % (self.nombre,self.defensa,self.stun))
                elif accion == "e":
                    self.golpeCritico_cambiar(0)
                    self.velocidad_cambiar(0)
                    daño = self.GUE_E_critico(other)
                    return ("%s ahora tiene una velocidad y golpe critico de %d\n%s atacó a %s con %s"
                            % (self.nombre, self.velocidad,self.nombre,other.nombre,daño))
                else:
                    self.stun_funcion(2)
                    daño = self.GUE_R_ultra(other)
                    return ("%s atacó a %s con %s usando la ULTRA\nY estará estuneado por %d turnos"
                        % ( self.nombre, other.nombre, daño, self.stun))

            elif self.clase == "Arquero":
                if self.efectos["Trifecta"][0] != 0:
                    accion = "e"
                if accion == "a":
                    daño = (self / other)
                    return ("\n%s atacó a %s con %s" % (self.nombre,other.nombre,daño))
                elif accion == "q":
                    return (self.ARQ_Q_bomba_de_gas(other))
                elif accion == "w":
                    if self in equipoB:
                        return self.ARQ_W_beneficio(equipoB)
                    else:
                        return self.ARQ_W_beneficio(equipoA)
                elif accion == "e":
                    if self in equipoB:
                        return self.ARQ_E_trifecta(other, equipoA[randint(0,len(equipoA)-1)])
                    else:
                        return self.ARQ_E_trifecta(other, equipoB[randint(0, len(equipoB)-1)])
                else:
                    pass



    #Ataque basico
    def __truediv__(self, other):
        if self.clase == "Guerrero":
            if randint(1,100) < self.precision_critica:
                daño = (self.ataque * self.daño_critico - (self.ataque * self.daño_critico * other.defensa / 100))*2
                other.vida -= (daño) // 1
                return ("%d *CRITICO*" % (daño))
            else:
                daño = self.ataque - (self.ataque * other.defensa / 100)
                other.vida -= (daño) // 1
                return (daño)

        elif self.clase == "Arquero":
            global equipoB
            other2 = equipoB[randint(0,len(equipoB)-1)]
            if randint(1, 100) < self.precision_critica:
                daño1 = self.ataque * self.daño_critico - (self.ataque * self.daño_critico * other.defensa / 100)
                other.vida -= daño1
                critico1 = "*CRITICO*"
            else:
                daño1 = self.ataque - (self.ataque * other.defensa / 100)
                other2.vida -= daño1
                critico1 = ""
            if randint(1, 100) < self.precision_critica:
                daño2 = (self.magia * self.daño_critico - (self.magia * self.daño_critico * other2.resistencia_magica / 100))
                other2.vida -= daño2
                critico2 = "*CRITICO*"
                return ("%d y a %s con %d" % (daño1, other2.nombre, daño2))
            else:
                daño2 = (self.magia - (self.magia * other2.resistencia_magica / 100))
                other2.vida -= daño2
                critico2 = "*CRITICO"
                return ("%d %s y a %s con %d %s " % (daño1, critico1,other2.nombre, daño2, critico2 ))

    def defensa_cambiar(self,opcion):
        self.defensa = opcion
    def stun_funcion(self, opcion):
        self.stun = opcion
    def velocidad_cambiar(self,opcion):
        self.velocidad = opcion
    def golpeCritico_cambiar(self,opcion):
        self.golpe_critico = opcion
    def __init__(self):
        self.efectos = {"D_precision" : [0,False], "B_ataque" : [0,False], "B_inmunidad" : [0, False] , "B_defensa" : [0, False] }

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
        prob = randint(1,100)
        if self.ultra:
            prob -= 15
        if prob < 40:return "a"#40%
        elif prob < 55 and prob >= 40:return "q"#15%
        elif prob < 70 and prob >= 55:return "w"#15%
        elif prob < 90 and prob >= 70:return "e"#20%
        else:return "r"#10%

    def GUE_R_ultra(self,other):
        if not self.ultra:
            other.vida -= 140
            self.ultra = True
            return "140"
        return "0"

    def GUE_E_critico(self,other):
        daño = (self.ataque * self.daño_critico - (self.ataque * self.daño_critico * other.defensa / 100))*2
        other.vida -= daño
        return ("%d *CRITICO*" % (daño))

    def __init__(self):
        personajes.__init__(self)
        #habilidades
        self.habilidades = "Pasiva: daño critico x2\n\rQ: Aumenta velocidad a 18\n\rW: Aumenta defensa a 30 pero se estunea por 2 turnos\n\rE: Golpe Critico pero velocidad y golpe critico bajan a 0\n\rR: Haces 150 de daño bruto pero quedas estuneado por 2 turnos"

        #Variables constantes
        self.efectos = {"D_precision": [0, False], "B_ataque": [0, False], "B_inmunidad": [0, False],
                        "B_defensa": [0, False]}
        self.ultra = False
        self.stun = 0
        self.nombre = ""#nombre que aparece en el juego


        self.vida = randint(45000,50000)#vida del jugador
        self.guardar_vida = self.vida
        self.defensa = randint(10,14)#porcentaje que bloquea del ataque
        self.ataque = randint(50,55)#cantidad de puntos de vida en daño fisico que puede inflijir al enemigo sin buffs o debuffs
        self.guardar_ataque = self.ataque
        self.magia = 0
        self.resistencia_magica = randint(8,13)

        self.precision = randint(11, 15)  # probabilidad de fallar
        self.guardar_precision = self.precision

        self.daño_critico = 1.5# porcentaje de aumento de daño ataque
        self.precision_critica = randint(34,40)#probabilidad de golpe critico
        self.precision_debuff = randint(20,24)
        self.resistencia_debuff = randint(8,12)
        self.rapidez = 44#comienza el que tenga mas rapidez
        self.velocidad = randint(10,11)#probabilidad en porcentaje de que sea el turno del jugador
        self.clase = "Guerrero"#dependiendo de la clases, cambia stats, AI y pasivas

        #Varaibles de guardar
        self.guardar_vida = self.vida
        self.guardar_defensa = self.defensa



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

    def ARQ_R_ultra(self):#R
        if not self.efectos["B_inmunidad"][1]:
            self.defensa = 100
            self.efectos["B_inmunidad"] = [2, True]
        else:
            self.efectos["B_inmunidad"] = [2, True]
        return ("la inmunidad de %s ha sido actualizada a 2" % (self.nombre))
        # le falta incluir el bono de turno despues de usar esta habilidad ademas de que la defensa le falta reztablecerla en 2 turnos

    def ARQ_W_beneficio(self, grupo):#W
        for x in grupo:
            if not x.efectos["B_ataque"][1]:
                x.ataque *= 1.5
                x.efectos["B_ataque"] = [2, True]
            else:
                x.efectos["B_ataque"] = [2, True]
        return ("El ataque de todos los aliados de %s se a aumentado " % (self.nombre))

    def ARQ_Q_bomba_de_gas(self,other):#Q
        if randint(0,99) < (70 + self.precision_debuff) -  ((70 + self.precision_debuff) / other.resistencia_debuff):
            if not other.efectos["D_precision"][1]:
                other.precision *= 2
                other.efectos["D_precision"] = [2, True]
                return ("La precision de %s a sido aumentada por 2 por %d turnos" % (other.nombre, other.efectos["D_precision"][0]))
            else:
                other.efectos["D_precision"] = [2, True]
                return ("los turnos de mala precision de %s a sido establecida a 2" % (other.nombre))
        return ("Bomba de Gas no hizo efecto")

    def ARQ_E_trifecta(self, other, other2):
        #se stunea por un turno si falla (listo)
        #(listo)son ataques que se realizan por turnos consecutivamente hasta que llegue el tercero o hasta que falle (hasta que falle nos falta agregar)

        if self.efectos["Trifecta"][0]  == 0:
            daño = self.ataque * 1.1
            daño_1 = self.magia * 1.1
            self.efectos["Trifecta"][0] += 1
            self.efectos["Trifecta"][1] = True
            valor = ""
        elif self.efectos["Trifecta"][0] == 1:
            daño = self.ataque * 1.3
            daño_1 = self.magia * 1.3
            self.efectos["Trifecta"][0] += 1
            valor = ""
        else:
            if randint(0,99) < (20 + self.precision_debuff) -  ((20 + self.precision_debuff) / other.resistencia_debuff):
                other.stun = 1
            daño = self.ataque * 1.5
            daño_1 = self.magia * 1.5
            self.efectos["Trifecta"][0] = 0
            self.efectos["Trifecta"][1] = False
            valor = ("ya termino la trifecta, has stuneado a %s " % (other.nombre))

        if randint(1, 100) < self.precision_critica:
            daño = daño * self.daño_critico - (daño * self.daño_critico * other.defensa / 100)
            other.vida -= daño

            critico = "*CRITICO"
        else:
            daño = daño - (daño * other.defensa / 100)
            other.vida -= daño
            critico = ""

        if randint(1, 100) < self.precision_critica:
            daño_1 = (daño_1 * self.daño_critico - (daño_1 * self.daño_critico * other2.resistencia_magica / 100))
            other2.vida -= daño_1
            critico2 = "*CRITICO*"
        else:
            daño_1 = (daño_1 * self.daño_critico - (daño_1 * self.daño_critico * other2.resistencia_magica / 100))
            other2.vida -= daño_1
            critico2 = ""
        return (("%s atacó a %s con %.1f %s \n%s atacó a %s con %.1f %s %s" % (self.nombre, other.nombre, daño,critico, self.nombre, other2.nombre, daño_1, critico2,valor )))

    def __init__(self):
        #habilidades
        personajes.__init__(self)
        self.habilidades = "Pasiva: cada ataque genera un ataque extra que sera l mitad de su ataque\n\rQ: aumenta la probabilidad de fallar en un 70% del enemigo x2 durante 2 turnos\n\rW: aumenta el ataque de un aliado escogido y el tuyo por dos turnos\n\rE:hace la trifecta \n\rR:se pone inmune por 3 turnos y gana un turno despues de usarse"
        self.efectos = {"D_precision": [0, False], "B_ataque": [0, False], "B_inmunidad": [0, False],
                        "B_defensa": [0, False], "Trifecta" : [0,False]}
        self.ultra = False
        self.stun = 0
        self.nombre = ""#nombre que aparece en el juego
        self.vida = randint(37500,42500)#vida del jugador
        self.defensa = randint(8,12)#porcentaje que bloquea del ataque
        self.ataque = randint(40,45)#cantidad de puntos de vida en daño fisico que puede inflijir al enemigo sin buffs o debuffs
        self.guardar_ataque = self.ataque
        self.magia = randint(18,23)
        self.resistencia_magica = randint(16,20)
        self.precision = randint(12,17)#probabilidad de fallar
        self.guardar_precision = self.precision
        self.daño_critico = 1.5# porcentaje de aumento de daño ataque
        self.precision_critica = randint(30,35)#probabilidad de golpe critico
        self.precision_debuff = randint(15, 20)
        self.resistencia_debuff = randint(25, 30)
        self.rapidez = 50#comienza el que tenga mas rapidez
        self.velocidad = randint(10,11)#probabilidad en porcentaje de que sea el turno del jugador
        self.clase = "Arquero"#dependiendo de la clases, cambia stats, AI y pasivas
        self.guardar_vida = self.vida
        self.guardar_defensa = self.defensa

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
        pass

    def ORC_Qrefuerzo(self, other):
        pass

    def ARQ_Wespiral(self,other):
        pass

    def ARQ_trifecta(self, other, other2, num):
        #se stunea por un turno si falla
        if num == 0:
            self.ataque = self.ataque * 1.1
        elif num == 1:
            self.ataque = 1.3 * self.ataque
        else:
            if randint(0,99) < (20 + self.precision_debuff) -  ((20 + self.precision_debuff) / other):
                other.stun = 1
            self.ataque = 1.5 * self.ataque
        daño_0 = (self / other)
        daño_1 = (self / other2)# aqui es la mitad

        return (("%s atacó a %s con %.1f\n%s atacó a %s con %.1f" % (self.nombre, other.nombre, daño_0, self.nombre, other2.nombre, daño_1)))

    def __init__(self):
        #habilidades #listas
        self.habilidades =  "pasiva : cada vez recibe o hace daño el orco aumenta la defensa por 2% maximo 10 cargas\r\n Q: cura tu vida en 10% + 50% de la defensa actual ofende a todos sun enemigos por 50% durante 1 turno \r\n W: ataca con su bate un ataque giratotio a todos sus enemigos de un 40% de su ataque, entre mas vida te falte mas daño hace\r\nE: se libera de cualquier debuff y a sus aliados cura al aliado con el rango mas bajo de vida por 20%\r\nR : ataca a su objetivo infligiendo todo el hp que te falta + porcentuamente la defensa, lo deja stuneado un turno"
        self.ultra = False
        self.stun = 0
        self.vida = randint(50000, 55000)#vida del jugador
        self.guardar_vida = self.vida
        self.defensa = randint(18,22)#porcentaje que bloquea del ataque
        self.ataque = randint(20,25)#cantidad de puntos de vida en daño fisico que puede infligir al enemigo sin buffs o debuffs
        self.magia = 0
        self.resistencia_magica = randint(20,24)
        self.precision = randint(15,19)#probabilidad de fallar
        self.daño_critico = 1.5# porcentaje de aumento de daño ataque
        self.precision_critica = randint(20,25)#probabilidad de golpe critico
        self.precision_debuff = randint(15, 20)
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



    if not enseñar:
        return ("##############TURNO %d##############\n\nJ1\nNombre: %s\nClase: %s\nVida: %d\nDaño_Crítico: %.1f\nDefensa: %d\nprecision_critica: %d\nAtaque: %d\nMagia: %d\nResistencia_Debuff: %d\nResistencia Mágica: %d\nVelocidad: %d\nPrecision: %d\n\n\n"
                "J2\nNombre: %s\nClase: %s\nVida: %d\nDaño_Crítico: %.1f\nDefensa: %d\nprecision_critica: %d\nAtaque: %d\nMagia: %d\nResistencia Debuff: %d\nResistencia Mágica: %d\nVelocidad: %d\nPrecision: %d\n\nTurno de %s\n"
                % (turno,J1.nombre,J1.clase,J1.vida,J1.daño_critico,J1.defensa,J1.precision_critica,J1.ataque,J1.magia,J1.resistencia_debuff,J1.resistencia_magica,J1.velocidad,J1.precision,
                   J2.nombre,J2.clase,J2.vida,J2.daño_critico,J2.defensa,J2.precision_critica,J2.ataque,J2.magia,J2.resistencia_debuff,J2.resistencia_magica,J2.velocidad,J2.precision, quienComienza))
    else:
        if not Mas:
            BarraDeVida = "□"
            vida1 = J1.vida

            while True:
                if vida1 <= 0:BarraDeVida = ""
                porcentaje = vida1 - (J1.guardar_vida * (1 / 10))
                if porcentaje >= 0:
                    BarraDeVida += "□"
                    vida1-=(J1.guardar_vida * (1 / 10))
                else:
                    break

            BarraDeVida2 = "□"
            vida2 = J2.vida

            while True:
                if vida1 <= 0: BarraDeVida = ""
                porcentaje = vida2 - (J2.guardar_vida * (1 / 10))
                if porcentaje >= 0:
                    BarraDeVida2 += "□"
                    vida2-=(J2.guardar_vida * (1 / 10))
                else:
                    break
            return ("%s: \n%s\n%s: \n%s\n" % (J1.nombre, BarraDeVida,J2.nombre, BarraDeVida2))
        else:
            return (
            "##############TURNO %d##############\n\nJ1\nNombre: %s\nClase: %s\nVida: %d\nDaño_Crítico: %.1f\nDefensa: %d\nprecision_critica: %d\nAtaque: %d\nMagia: %d\nResistencia_Debuff: %d\nResistencia Mágica: %d\nVelocidad: %d\nPrecision: %d\n\n\n"
            "J2\nNombre: %s\nClase: %s\nVida: %d\nDaño_Crítico: %.1f\nDefensa: %d\nprecision_critica: %d\nAtaque: %d\nMagia: %d\nResistencia Debuff: %d\nResistencia Mágica: %d\nVelocidad: %d\nPrecision: %d\n\nTurno de %s\n"
            % (
            turno, J1.nombre, J1.clase, J1.vida, J1.daño_critico, J1.defensa, J1.precision_critica, J1.ataque,
            J1.magia, J1.resistencia_debuff, J1.resistencia_magica, J1.velocidad, J1.precision,
            J2.nombre, J2.clase, J2.vida, J2.daño_critico, J2.defensa, J2.precision_critica, J2.ataque,
            J2.magia, J2.resistencia_debuff, J2.resistencia_magica, J2.velocidad, J2.precision, quienComienza))


def ini(teclaParam="", multijugador = False):
    global n, quienComienza

    n += 1

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
        global equipoA, equipoB
        if n == 2 :
            equipoA.append(J1)
            equipoB.append(J2)

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
            if J1.precision > randint(0,99):
                J1.turno(J2, teclaParam, True)
                return ("*La precision de %s lo hizo fallar*\n%s" % (J1.nombre, info(n)))
            return (J1.turno(J2, teclaParam), "\n%s\n" % (info(n)))
        else:
            quienComienza = J1.nombre

            if J2.precision > randint(0,99):
                J2.turno(J1, teclaParam, True)
                return ("*La precision de %s lo hizo fallar*\n%s" % (J2.nombre, info(n)))
            return (J2.turno(J1, J2.opcion()), "\n%s\n" % (info(n)))
