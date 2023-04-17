class Deportista:
    def __init__(self, añosPracticando, deporte="Futbol"):
        self.deporte = deporte
        self.añosPracticando = añosPracticando

    def getDeporte(self):
        return self.deporte

    def setNombre(self, deporte):
        self.deporte = deporte

    def getAñosPracticando(self):
        return self.añosPracticando

    def setAñosPracticando(self, añosPracticando):
        self.añosPracticando = añosPracticando
