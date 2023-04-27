from vuelo import Vuelo
import json

class Aeropuerto:
    def __init__(self):
        self.__vuelos = []

    def agregar_final(self, vuelo:Vuelo):
        self.__vuelos.append(vuelo)

    def agregar_inicio(self, vuelo:Vuelo):
        self.__vuelos.insert(0,vuelo)
    
    def mostrar(self):
        for vuelo in self.__vuelos:
            print(vuelo)
            
    def __str__(self):
        return "".join(
            str(v) + "\n" for v in self.__vuelos
        )
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                
                self.__vuelos = [Vuelo(**vuelo) for vuelo in lista]
        except:
            return 0

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [Vuelo.to_dict() for Vuelo in self.__vuelos]

                print(lista)

                json.dump(lista, archivo, indent = 4)

                return 1
        except:
            return 0

aeropuerto = Aeropuerto()
aeropuerto.mostrar()