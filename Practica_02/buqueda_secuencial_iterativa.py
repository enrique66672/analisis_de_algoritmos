# Análisis de Algoritmos
# Programador: Roque Ramos Miguel Enrique
def busqueda_secuencial_iterativa():
    array = [1,2,3,4,5]
    i = 0
    find = False
    data_input = int(input('Ingrese un valor: '))

    while i < len(array) and find == False:
        if array[i] == data_input:
            find = True
        i = i+1

    print("Valor: {} encontrado en la posicion: {}".format(data_input, i) if find else "Valor: {} no encontrado".format(data_input))

busqueda_secuencial_iterativa()
