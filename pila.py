class PilaVaciaError(Exception):
    pass
class Pila(object):
    
    """Representa a una pila."""
    
    def __init__(self):
        self.elementos = []

    def apilar(self,dato):
        
        """Pre: Dato es de cualquier tipo.

        Post: Apila el dato al final de la pila.
        """
        
        self.elementos.append(dato)

    def desapilar(self):
        
        """ Pre: Se debe utilizar con una instancia de pila.

            Post: Devuelve el ultimo dato agregado a la pila.
            En caso de estar vacia, lanza una excepcion.
        """
        
        try:    
            quitar_dato = self.elementos.pop()
            return quitar_dato
        except IndexError:
            raise PilaVaciaError("La pila esta vacia")

    def ver_tope(self):
        
        """ Pre: Se debe utilizar con una instancia de pila.

            Post: Devuelve el ultimo elemento apilado sin desapilarlo.
            En caso de estar vacia, lanza una excepcion.
        """
        
        try:
            return self.elementos[-1]
        except IndexError:
            raise PilaVaciaError()
    def esta_vacia(self):
        """ Pre: Se debe utilizar con una instancia de pila.

            Post: Devuelve True si la pila esta vacia, en caso contrario,
            False
        """
        return len(self.elementos) == 0


