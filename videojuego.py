from ientregable import IEntregable


class Videojuego(IEntregable):

    def __init__(self, titulo, genero, companya):
        self.__titulo = titulo
        self.__horas_estimadas = 10
        self.entregado = False
        self.__genero = genero
        self.__companya = companya

    @property
    def titulo(self):
        return self.__titulo

    @property
    def horas_estimadas(self):
        return self.__horas_estimadas

    @property
    def genero(self):
        return self.__genero

    @property
    def companya(self):
        return self.__companya

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @horas_estimadas.setter
    def horas_estimadas(self, horas_estimadas):
        self.__horas_estimadas = horas_estimadas

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @companya.setter
    def genero(self, companya):
        self.__companya = companya

    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado

    def compareTo(self, objeto):
        if isinstance(objeto, self.__class__):
            if objeto.horas_estimadas < self.horas_estimadas:
                return 1
            if objeto.horas_estimadas > self.horas_estimadas:
                return -1
            if objeto.horas_estimadas == self.horas_estimadas:
                return 0
        else:
            print('objetos no comparables')

    def __str__(self) -> str:
        return "titulo: " + str(self.__titulo) + "\n" + \
               "horas_estimadas: " + str(self.__horas_estimadas) + "\n" + \
               "entregado: " + str(self.entregado) + "\n" + \
               "genero: " + str(self.__genero) + "\n" + \
               "companya: " + str(self.__companya)