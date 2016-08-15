import pila
import errores

def referenciar_saltos(caracter,pila_saltos,pos_actual,dic):
    
    """Pre: Caracter es un string ']' o '[', pila_saltos una instancia de pila,
    pos_actual un entero y dic un diccionario.

    Post: Si el caracter es '[' apila un nuevo elemento en pila_saltos con el mismo
    y su posicion en la linea de comandos.
    Si el caracter es ']' y el tope de la pila no es el caracter '[' lanza una excepcion.
    En cambio si el tope contiene '[', desapila este elemento, se guarda su posicion,
    y se guarda en el diccionario la posicion actual como clave y la anterior como valor,
    y viceversa.
    En ambos casos se devuelve la pila y el diccionario
    """
    
    if caracter == "[":
        pila_saltos.apilar([caracter,pos_actual])
    else:
        try:
            pos,comando = 1,0
            if pila_saltos.ver_tope()[comando]  == "[":
                pos_anterior = pila_saltos.desapilar()[pos] 
                dic[pos_actual],dic[pos_anterior] = pos_anterior,pos_actual             
        except pila.PilaVaciaError:
            raise errores.MCSyntaxError
    return pila_saltos,dic

def cargar_codigo(archivo):
    
    """ Pre: Archivo es un string que hace referencia a un archivo que
        se deberia poder leer para ejecutar el programa.
        
        Post: Devuelve una lista con los comandos que reconoce
        un interprete de matacerebros y un diccionario con las referencias de
        de saltos de cada corchete en el codigo.
        En caso de que el archivo no se pueda abrir porque no se tienen permisos
        o no existe, se lanza IOError, y en caso de que la pila con referencias de
        los corchetes no este vacia al finalizar  el recorrido por el archivo, se
        lanza MCSyntaxError.
    """
    
    with open(archivo) as archivo_matacerebros:
        comandos_matacerebro = "<>+-[]."
        comandos_archivo,dic_saltos,pila_saltos,pos_actual = [],{},pila.Pila(),0
        for linea in archivo_matacerebros:
            for caracter in linea:
                if caracter in comandos_matacerebro:     
                    if caracter == "[" or caracter == "]":
                        referenciar_saltos(caracter,pila_saltos,pos_actual,dic_saltos)
                    comandos_archivo.append(caracter)
                    pos_actual+=1
    if pila_saltos.esta_vacia():
        return comandos_archivo,dic_saltos
    raise errores.MCSyntaxError
