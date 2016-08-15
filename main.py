import argparse
import sys
import time
import pila
import errores
from interprete import *
from cargacodigo import *

#Incluir en la carpeta 'programas' el programa que se desee ejecutar

def main():

    """Interprete de matacerebros escrito en Python"""
        
    parser = argparse.ArgumentParser(description='Interprete de codigo MataCerebros')
    parser.add_argument('archivo', metavar='archivo', help='archivo con codigo a interpretar')
    parser.add_argument('-d', '--debug', action='store_true', help='modo debug')
    args = parser.parse_args()

    nombre_archivo = args.archivo #String con el nombre del archivo
    modo_debug = args.debug #Guarda True si se pasa '-d' en la linea de comandos
    try:
        lista_comandos,saltos = cargar_codigo("programas/"+nombre_archivo)
    except IOError:
        print "Archivo inexistente, no se tienen permisos o no\
se encuentra dentro de la carpeta 'programas/'"
        return
    except errores.MCSyntaxError:
        print "Error de sintaxis"
        return
    
    if not modo_debug:
        interprete = MataCerebros(lista_comandos,saltos)
        interprete.__main__()
        return

    try:
        MC_Debug= MataCerebros_debug(lista_comandos,saltos)
        MC_Debug.__main_debug__()
    except IndexError:
        print "El archivo que intenta ejecutar existe, pero no contiene codigo en el lenguaje matacerebros"

main()
