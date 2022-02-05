# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from serie import Serie
from videojuego import Videojuego
from utils import contar_entregados

# Creando series
foo1 = Serie("foo1", "foo1", "foo1")
foo2 = Serie("foo2", "foo2", "foo2")
foo3 = Serie("foo3", "foo3", "foo3")
foo4 = Serie("foo4", "foo4", "foo4")
foo5 = Serie("foo5", "foo5", "foo5")

# Array de series
series = [foo1, foo2, foo3, foo4, foo5]

# Entregando algunas series
foo2.entregar()
foo3.entregar()

# Contando entregados
contar_entregados(series)

# Definiendo temporadas
foo4.temporadas = 10
foo1.temporadas = 4
foo2.temporadas = 2
foo3.temporadas = 7
foo5.temporadas = 3

# Serie con mayor número de temporadas
max_temp_serie = series[0]
for serie in series:
    if serie.temporadas > max_temp_serie.temporadas:
        max_temp_serie = serie
print(max_temp_serie)

print("-------------------------------------------")

# Creando videojuegos
bar1 = Videojuego("bar1", "bar1", "bar1")
bar2 = Videojuego("bar2", "bar2", "bar2")
bar3 = Videojuego("bar3", "bar3", "bar3")
bar4 = Videojuego("bar4", "bar4", "bar4")
bar5 = Videojuego("bar5", "bar5", "bar5")

# Array de videjuegos
videojuegos = [bar1, bar2, bar3, bar4, bar5]

# Entregando videojuegos
bar2.entregar()

# Contando el número de videojuegos entregados
contar_entregados(videojuegos)

# Juego con mayor número de horas estimadas
max_horas_videojuego = videojuegos[0]
for videojuego in videojuegos:
    if videojuego.horas_estimadas > max_horas_videojuego.horas_estimadas:
        max_horas_videojuego = videojuego
print(max_horas_videojuego)
