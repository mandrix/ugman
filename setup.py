import assets.files.ui as ui#Para iniciar el GUI
import logging #Para crear los logs
import os #Para borrar logs viejos, mover archivos y crear directorios
import time
import json #Parra crear el archivo de perfil

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
        cambios.append("Creacion de ",directory)
    directory = "./saves"
    if not os.path.exists(directory):
        os.makedirs(directory)
        cambios.append("Creacion de ", directory)
    directory = "./assets/img"
    if not os.path.exists(directory):
        os.makedirs(directory)
        cambios.append("Creacion de ", directory)
    directory = "./assets/sounds"
    if not os.path.exists(directory):
        os.makedirs(directory)
        cambios.append("Creacion de ", directory)
    directory = "./assets/files"
    if not os.path.exists(directory):
        os.makedirs(directory)
        cambios.append("Creacion de ", directory)

    #Un log por cada archivo python
    logging.basicConfig(filename='log\debug_setup.log',format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.info("\n\n\n************************\nInicio del debugging de setup.py")


    #Creando el json si es necesario para el perfil
    try:
        file = open("saves/guardado.json","r")
        if file.read() == "":
            raise NameError("Archivo json está corrupto")
    except:

        content="{\"Nombre\":\"\",\"Victorias\":0,\"Derrotas\":0,\"Partidas Jugadas\":0,\"Logros\":[],\"MODO_HISTORIA\":[]}"
        file = open("saves/guardado.json","w+")
        file.write(content)
    file.close()

    #Mover archivos si es necesario
    try:
        file = "./ugman.png"
        os.rename(file,"./assets/img/ugman.png")
        logging.warning("ugman.png estaba en el directorio incorrecto, se pasó a /assets/img/ugman.png")
    except:
        pass

    try:
        file = "./.guardado"
        os.rename(file,"./saves/.guardado")
        logging.warning(".guardado estaba en el directorio incorrecto, se pasó a /assets/img/.guardado")
    except:
        pass

    try:
        file = "./ugman.py"
        os.rename(file,"./assets/files/ugman.py")
        logging.warning("ugman.py estaba en el directorio incorrecto, se pasó a /assets/img/ugman.py")
    except:
        pass

    try:
        file = "./ui.py"
        os.rename(file,"./assets/files/ui.py")
        logging.warning("ui.py estaba en el directorio incorrecto, se pasó a /assets/img/ui.py")
    except:
        pass

    for cambio in cambios:
        logging.info(cambio)


    logging.info("Fin del setup en %.3fs\n************************\n\n\n" % (tiempo1 - time.time()))
    ui.setup_ui()
    logging.warning("\n************************\n*Fin del Juego*\n************************\n")




# Verificando que el archivo correcto se esté corriendo
if __name__ == "__main__":
    global tiempo1
    tiempo1 = time.time()
    setup()
else:
    raise NameError("Inició el archivo incorrecto")