print ("Hecho por Paola De La Fuente Alarcón y Sara Maylea Ramirez Reyes")
def fibonacci(n):
    if n <= 0:
        return [] 
    elif n == 1:
        return [0] 
    elif n == 2:
        return [0, 1] 
    fib_sequence = [0, 1]
    i = 2 
    while i < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2] 
        fib_sequence.append(next_fib) 
        i += 1 
        return fib_sequence
# Fase de prueba
if __name__ == "_main_":
 n = int (input ("Ingresa la cantidad de términos de Fibonacci: "))
 resultado = fibonacci(n)
 print ("Serie de Fibonacci es:", resultado)