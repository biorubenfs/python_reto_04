def contar_entregados(array_entregables):
    """ Imprime los elementos entregados de un array dado
    y el número total """
    total_entregados = 0
    for entregable in array_entregables:
        if entregable.entregado:
            total_entregados += 1
            print('Entregado: ' + str(entregable.titulo))
    print("total entregados: ", total_entregados)