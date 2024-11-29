print("Hecho por Paola De La Fuente Alarcon")

def generar_triangulo_pascal(filas):
    triangulo = []
    i = 0

    while i < filas:
        fila = [1] * (i + 1)

        j = 1
        while j < i:
            fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
            j += 1
        
        triangulo.append(fila)
        i += 1
        
    for fila in triangulo:
        print(' '.join(map(str, fila)).center(filas * 2))

filas = int(input("Introduce el número de filas para el Triángulo de Pascal: "))
generar_triangulo_pascal(filas)