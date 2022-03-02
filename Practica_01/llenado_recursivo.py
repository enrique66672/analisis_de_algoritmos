array = []

def llenado_recursivo(lim):
    if lim < 20:
        value = int(input('Ingrese el valor un valor entero: '))
        while value < 0:
            value = int(input('Ingrese el valor un valor entero: '))
        array.append(value)
        lim += 1
        llenado_recursivo(lim)

llenado_recursivo(0)
print(array)
