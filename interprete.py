import sys
import time
ARREGLO_MAX = 30000
class MataCerebros(object):
    
    """Representa al interprete de MataCerebros"""
    
    def __init__(self,comandos,saltos):
        
        """ Inicializa una instancia de MataCerebros

            Pre: 'comandos' es una lista con los comandos que se iran
            ejecutando una vez que los apunte el puntero de instruccion.

            'saltos' es un diccionario con las referencias que corresponden
            para que la interpretacion funcione una vez que el puntero de
            instruccion apunta a un corchete.

            Post: Interpreta codigo MataCerebros
        """
        
        self.cinta = [0]*ARREGLO_MAX
        self.cinta_posicion_actual = 0
        self.saltos = saltos
        self.comandos = comandos
        self.puntero_de_instruccion = 0
        
    def avanzar(self):
        
        """ Pre: Se debe utilizar con una instancia de MataCerebros.

            Post: Si la posicion actual de la cinta es igual a ARREGLO_MAX,
            y devuelve None, en cualquier otro caso, se avanza una posicion.
        """
        
        if self.cinta_posicion_actual == ARREGLO_MAX:
            self.cinta_posicion_actual = 0
            return
        self.cinta_posicion_actual+=1
        
    def retroceder(self):

        """ Pre: Se debe utilizar con una instancia de MataCerebros.

            Post: Si la posicion actual de la cinta es igual a 0
            la posicion de la cinta pasa a ser ARREGLO_MAX y devuelve None,
            en cualquier otro caso, se retrocede una posicion.
        """
        
        if self.cinta_posicion_actual == -ARREGLO_MAX:
            self.cinta_posicion_actual = ARREGLO_MAX
            return
        self.cinta_posicion_actual-=1
        
    def imprimir_actual(self):

        """ Pre: Se debe utilizar con una instancia de MataCerebros.

            Post: Se muestra en la consola la interpretacion en codigo ASCII
            del valor de la celda actual.
        """
        
        sys.stdout.write(chr(self.cinta[self.cinta_posicion_actual]))
        sys.stdout.flush()
        time.sleep(0.01)
        
    def incrementar(self):

        """ Pre: Se debe utilizar con una instancia de MataCerebros.

            Post: Si el valor que contiene la celda actual es 255,
            se convierte en 0 y devuelve None,
            en cualquier otro caso, se incrementa en 1.
        """
        
        if self.cinta[self.cinta_posicion_actual] == 255:
            self.cinta[self.cinta_posicion_actual] = 0
            return
        self.cinta[self.cinta_posicion_actual]+=1
        
    def decrementar(self):
        
        """ Pre: Se debe utilizar con una instancia de MataCerebros.

            Post: Si el valor que contiene la celda actual es 0,
            se convierte en 255 y devuelve None, en cualquier otro caso,
            se produce un decremento de 1.
        """
        
        if self.cinta[self.cinta_posicion_actual] == 0:
            self.cinta[self.cinta_posicion_actual] = 255
            return
        self.cinta[self.cinta_posicion_actual]-=1
        
    def saltar(self,caracter,posicion):
        
        """ Pre: Se debe utilizar con una instancia de MataCerebros.
            Caracter debe ser '[' o ']' y posicion un entero que haga
            referencia a la posicion actual en la linea del codigo MataCerebros.
            
            Post: Si el caracter es '[' y el valor de la celda actual es cero,
            mover el puntero de instruccion hasta el comando siguiente al
            ] correspondiente.

            Si el caracter es ']' y el valor de la celda actual no es cero,
            mover el puntero de instruccion hasta el comando siguiente al
            [ correspondiente.

            Si no se cumple ninguna de las anteriores condiciones, el puntero
            de instruccion avanza un elemento.
        """
        
        salto = 1
        
        if caracter == "[" and self.cinta[self.cinta_posicion_actual] == 0:
            self.puntero_de_instruccion = self.saltos[posicion]+salto
        elif caracter == "]" and self.cinta[self.cinta_posicion_actual] != 0:
            self.puntero_de_instruccion = self.saltos[posicion]+salto
        else:
            self.puntero_de_instruccion+=1
            
    def __main__(self):
        
        """ Pre: Se debe utilizar con una instancia de MataCerebros.

            Post: Se lee el codigo de izquierda a derecha y se van efectuando
            las funciones correspondientes segun el comando al que este
            apuntando el comando de instruccion

        """
        
        dic_funciones = {"<":MataCerebros.retroceder,">":MataCerebros.avanzar,
                         ".":MataCerebros.imprimir_actual,"-":MataCerebros.decrementar,
                         "+":MataCerebros.incrementar}
        while self.puntero_de_instruccion < len(self.comandos):
            if self.comandos[self.puntero_de_instruccion] == "]" or self.comandos[self.puntero_de_instruccion] == "[":
                MataCerebros.saltar(self,self.comandos[self.puntero_de_instruccion],self.puntero_de_instruccion)
            else:              
                dic_funciones[self.comandos[self.puntero_de_instruccion]](self)
                self.puntero_de_instruccion+=1
        
class MataCerebros_debug(MataCerebros):

    """Representa al modo debug de un interprete de MataCerebros"""
    
    def __init__(self,comandos,saltos):

        """Inicializa una instancia de MataCerebros_debug

            Pre: Ver la documentacion para una instancia de MataCerebros.
            Ademas,Si la lista comandos es de longitud 0, lanza IndexError.

            Post: Interpreta codigo MataCerebros y muestra como se desarrolla
            esta interpretacion.
            
        """
        
        MataCerebros.__init__(self,comandos,saltos)
        if len(comandos) == 0:
            raise IndexError
        self.cantidad_comandos = len(comandos)
        self.mensaje_actual = ""

    def anadir_caracter(self):

        """ Pre: Se debe utilizar con una instancia de MataCerebros_debug.

            Post: Agrega el caracter que representa en codigo ASCII el valor de
            la celda actual a el atributo mensaje_actual
        """
        
        self.mensaje_actual+=(chr(self.cinta[self.cinta_posicion_actual]))

    def recortar_cinta(self):
        """ Pre: Se debe utilizar con una instancia de MataCerebros.

            Post: Devuelve una representacion de un slice de una lista de
            tamano 10, siendo el centro de la misma la posicion actual en
            la cinta, y los demas elementos son los 5 anteriores y los 4
            posteriores
        """
        
        recorte = 5

        if self.cinta_posicion_actual == recorte:
            return MataCerebros_debug.representar_cinta(self,self.cinta[self.cinta_posicion_actual-recorte:self.cinta_posicion_actual+recorte])
        if (self.cinta_posicion_actual < recorte and self.cinta_posicion_actual >= 0) or (self.cinta_posicion_actual < 0 and self.cinta_posicion_actual > -recorte):
            return MataCerebros_debug.representar_cinta(self,self.cinta[self.cinta_posicion_actual-recorte-1:-1]+\
            self.cinta[0:(recorte*2)+self.cinta_posicion_actual-recorte])
        else:
            return MataCerebros_debug.representar_cinta(self,self.cinta[self.cinta_posicion_actual-recorte:self.cinta_posicion_actual+recorte])
            
    def representar_cinta(self,lista):

        """ Pre: Se debe utilizar con una instancia de MataCerebros.
            lista es una lista no vacia.

            Post: Devuelve un string que representa a la lista
            para mostrarla de manera diferente
        """
        
        representacion = ""
        for x in range(len(lista)):
            if x == len(lista)/2:
                representacion+=">>"+str(lista[x])+"<<"+"|"
                continue
            elif x == len(lista)-1:
                representacion+=str(lista[x])
            else:
                representacion+=str(lista[x])+"|"
        return representacion
    
    def mostrar_estado_actual(self,lista):
        
        """ Pre: Se debe utilizar con una instancia de MataCerebros.

            Post: Imprime por pantalla el estado actual del interprete,
            mostrando que comando se esta ejecutara, la cinta en un radio de 10
            elementos, sus valores actuales y la salida actual del programa.
        """
        
        print "El comando que se ejecutara es: ",self.comandos[self.puntero_de_instruccion],"\n"
        print "El estado actual de la cinta es: ",lista,"\n"
        print "La salida actual del programa es: \n",self.mensaje_actual,"\n"
        
    def mostrar_ultimo_estado(self,lista):

        """ Pre: Se debe utilizar con una instancia de MataCerebros.

            Post: Imprime por pantalla el ultimo estado del interprete,
            mostrando cual fue el ultimo comando en ejecutarse, la cinta
            en un radio de 10 elementos, sus valores al finalizar
            la interpretacion y la salida final del programa.
        """
        
        print "El ultimo comando en ejecutarse fue: ",self.comandos[self.puntero_de_instruccion-1],"\n"
        print "El estado final de la cinta es: ",lista,"\n"
        print "La salida del programa es: \n",self.mensaje_actual,"\n"
        print "Finalizo la interpretacion del codigo"
        
    def __main_debug__(self):

        """ Pre: Se debe utilizar con una instancia de MataCerebros.

            Post: Se lee el codigo de izquierda a derecha y se van efectuando
            las funciones correspondientes segun el comando al que este
            apuntando el comando de instruccion, ademas, se muestra el
            estado de la ejecucion del programa.
        """
        
        dic_funciones = {"<":MataCerebros.retroceder,">":MataCerebros.avanzar,
                         ".":MataCerebros_debug.anadir_caracter,"-":MataCerebros.decrementar,
                         "+":MataCerebros.incrementar}
        entrada = ""
        
        print "----------------- Interprete de matacerebros en modo debug -------------------\n"
        print "La notacion >>x<< indica la posicion actual de la cinta"
        print "Escriba 'finalizar' en el momento en el que desee dejar de correr el interprete en modo debug\n"

        while self.puntero_de_instruccion < len(self.comandos) and entrada != "finalizar":
            cinta_corte_actual = MataCerebros_debug.recortar_cinta(self)
            MataCerebros_debug.mostrar_estado_actual(self,cinta_corte_actual)
            entrada = raw_input("Ingrese 'finalizar' para salir, cualquier cosa para continuar:\n ")
            if self.comandos[self.puntero_de_instruccion] == "]" or self.comandos[self.puntero_de_instruccion] == "[":
                MataCerebros.saltar(self,self.comandos[self.puntero_de_instruccion],self.puntero_de_instruccion)
            else:              
                dic_funciones[self.comandos[self.puntero_de_instruccion]](self)
                self.puntero_de_instruccion+=1

        cinta_corte_actual = MataCerebros_debug.recortar_cinta(self)
        MataCerebros_debug.mostrar_ultimo_estado(self,cinta_corte_actual)

