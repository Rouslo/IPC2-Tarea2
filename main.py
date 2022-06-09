from sqlite3 import DateFromTicks


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaCircularDoble:
    def __init__(self) :
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos()

    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.__unir_nodos

    def __unir_nodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def recorrer_inicio_fin(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break
    
    def busqueda(self, elemento):
        aux = self.primero
        while aux:
            if elemento == aux.dato:
                print(f"Anterior: {aux.anterior.dato}, Actual: {aux.dato}, Siguiente: {aux.siguiente.dato}")
                break
            aux = aux.siguiente 






lista = ListaCircularDoble()

print('-- Lista Completa: --')
lista.agregar_final(12)
lista.agregar_final(10)
lista.agregar_final(8)
lista.agregar_final(58)
lista.agregar_final(20)

lista.recorrer_inicio_fin()
print('---------------------')

numero = int(input("Seleccione número: "))

lista.busqueda(numero)