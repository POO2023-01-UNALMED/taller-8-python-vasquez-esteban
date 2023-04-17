from persona import Persona
from deportista import Deportista


class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, añosPracticando)

        self.golesMarcados = golesMarcados
        self.tarjetasRojas = tarjetasRojas
        self.piernaHabil = piernaHabil

        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self.golesMarcados

    def setGolesMarcados(self, golesMarcados):
        self.golesMarcados = golesMarcados

    def getTarjetasRojas(self):
        return self.tarjetasRojas

    def setTarjetasRojas(self, tarjetasRojas):
        self.tarjetasRojas = tarjetasRojas

    def getPiernaHabil(self):
        return self.piernaHabil

    def setPiernaHabil(self, piernaHabil):
        self.piernaHabil = piernaHabil

    def __str__(self):
        return f"Mi nombre es {self.nombre} " \
               f"soy profesional en el deporte {self.deporte} " \
               f"Tengo {self.edad} años de edad " \
               f"y llevo {self.añosPracticando} años en el deporte"
