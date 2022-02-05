from ientregable import IEntregable


class Serie(IEntregable):

    def __init__(self, titulo, genero, creador):
        self.__titulo = titulo
        self.__temporadas = 3
        self.entregado = False
        self.__genero = genero
        self.__creador = creador

    def compareTo(self, objeto):
        if isinstance(objeto, self.__class__):
            if objeto.temporadas < self.temporadas:
                return 1
            if objeto.temporadas > self.temporadas:
                return -1
            if objeto.temporadas == self.temporadas:
                return 0
        else:
            print('objetos no comparables')

    @property
    def titulo(self):
        return self.__titulo

    @property
    def temporadas(self):
        return self.__temporadas

    @property
    def genero(self):
        return self.__genero

    @property
    def creador(self):
        return self.__creador

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @temporadas.setter
    def temporadas(self, temporadas):
        self.__temporadas = temporadas

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @creador.setter
    def creador(self, creador):
        self.creador = creador

    # overiding methods
    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado

    def __str__(self) -> str:
        return "titulo: " + str(self.__titulo) + "\n" + \
               "temporadas: " + str(self.__temporadas) + "\n" + \
               "entregado: " + str(self.entregado) + "\n" + \
               "genero: " + str(self.__genero) + "\n" + \
               "creador: " + str(self.__creador)
