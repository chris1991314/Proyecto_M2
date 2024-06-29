# creamos un programa para identificar la longitud de una palabra ingresada.
while True:    
    
    palabra = input('\nIngresa la palabra de menos de 4 y maximo 8 caracteres:\n')

    N = len(palabra)

    if len (palabra) > 3 and len(palabra)  < 9:
        print('\nHas ingresado una palabra correcta.')
        break   # Salir del bucle si la palabra es correcta
    elif len(palabra) < 4:
        print(f'\nHase falta letras solo tienes {N} letras.')
        continue    # Volver al inicio del bucle
    else:
        print(f'\nSobran letras, tienenes {N} letras, intenta con una palabra mas corta.')
        continue    # Volver al inicio del bucle

print('\nGracias, Hasta la proxima.')

# Usamos un bucle while True para continuar solicitando una palabra hasta que sea correcta.
# Dentro del bucle, se solicita al usuario que ingrese una palabra.
# Calculamos la longitud de la palabra usando len().
# Usamos una estructura de control if-elif-else para verificar la longitud de la palabra:
# Si la longitud está entre 4 y 8 letras, imprime "La palabra es correcta." y usa break para salir del bucle.
# Si la longitud es menor a 4 letras, imprime un mensaje indicando cuántas letras faltan /
# e indica al usuario que lo intente de nuevo usando continue.
# Si la longitud es mayor a 8 letras, imprime un mensaje indicando cuántas letras sobran /
# e indica al usuario que lo intente de nuevo usando continue.

###########################################################################################

# Función para identificar el cuadrante
def identificar_cuadrante(x, y):
    if x == 0 or y == 0:
        return "Las coordenadas no pueden ser cero."
    elif x > 0 and y > 0:
        return "El punto se encuentra en el cuadrante I."
    elif x < 0 and y > 0:
        return "El punto se encuentra en el cuadrante II."
    elif x < 0 and y < 0:
        return "El punto se encuentra en el cuadrante III."
    elif x > 0 and y < 0:
        return "El punto se encuentra en el cuadrante IV."

# Solicitar las coordenadas al usuario
try:
    x = float(input("Ingrese X: \n"))
    y = float(input("Ingrese Y: \n"))

    # Llamar a la función y mostrar el resultado
    resultado = identificar_cuadrante(x, y)
    print(resultado)

except ValueError:
    print("Por favor, ingrese valores numéricos válidos para las coordenadas.")

# Creamos una función llamada identificar_cuadrante(x, y)
# La cual toma dos parámetros, x y y, que representan las coordenadas del punto.
# Verifica si alguna de las coordenadas es 0 y devuelve un mensaje indicando que las coordenadas no pueden ser cero.
# Determina en qué cuadrante se encuentra el punto basado en los signos de x y y.
# Solicitamos al usuario que ingrese las coordenadas x y y. con los valores 4 y -5
# Utilizamos  un bloque "try" y "except" para manejar posibles errores de entrada \
# por ejemplo, si el usuario ingresa un valor no numérico).
