
import logging #Para crear los logs
import os #Para borrar logs viejos, mover archivos y crear directorios
import time


def setup():
    #Lista de todos los cambios
    cambios = []

    #Borrando los logs viejos
    try:
        os.remove("log\debug_ui.log")
        cambios.append("Se borró log\debug_ui.log")
    except:
        pass

    try:
        os.remove("log\debug_setup.log")
        cambios.append("Se borró log\debug_setup.log")
    except:
        pass
    try:
        os.remove("log\debug_ugman.log")
        cambios.append("Se borró log\debug_ugman.log")
    except:
        pass



    #Creando directorios para los logs y los perfiles
    directory = "./log"
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = "./saves"
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = "./assets/img"
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = "./assets/sounds"
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = "./assets/files"
    if not os.path.exists(directory):
        os.makedirs(directory)


    #Verificando que todos los archivos están
    try:
        open("./assets/sounds/musica/batalla.mp3")
        open("./assets/sounds/musica/ini.mp3")
        open("./assets/sounds/sonidos/alerta.mp3")
        open("./assets/sounds/sonidos/boton.mp3")
        open("./assets/sounds/sonidos/menu_boton.mp3")
        open("./assets/sounds/sonidos/critical.mp3")
    except:
        assert NameError("Uno de los archivos de sonido no existen o no están donde deberian.")

    try:
        open("./assets/img/ugman.png")
        open("./assets/img/ugman.ico")
    except:
        assert NameError("Uno de los archivos de imagen no existen o no están donde deberian.")

    try:
        open("./files/img/ugman.py")
        open("./files/img/ui.py")
    except:
        assert NameError("Uno de los archivos de programación no existen o no están donde deberian.")






    #Objeto de logging
    logging.basicConfig(filename='log\debug_setup.log',format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.info("\n\n\n************************\nInicio del debugging de setup.py")


    #Creando el json si es necesario para el perfil
    try:
        file = open("saves/guardado.json","r")
        if file.read() == "":
            raise NameError("Archivo json está corrupto")
        print("n")

    except:
        print("a")
        content="{\"Nombre\":\"\",\"Fecha\":\"\",\"Victorias\":0,\"Derrotas\":0,\"Partidas Jugadas\":0,\"Logros\":[],\"MODO_HISTORIA\":[]}"
        file = open("saves/guardado.json","w+")
        file.write(content)
    file.close()


    for cambio in cambios:
        logging.info(cambio)


    logging.info("Fin del setup en %.3fs\n************************\n\n\n" % (tiempo1 - time.time()))
    import assets.files.ui as ui  # Para iniciar el GUI
    ui.setup_ui()
    logging.warning("\n************************\n*Fin del Juego*\n************************\n")




# Verificando que el archivo correcto se esté corriendo
if __name__ == "__main__":
    global tiempo1
    tiempo1 = time.time()
    setup()
else:
    raise NameError("Inició el archivo incorrecto")
