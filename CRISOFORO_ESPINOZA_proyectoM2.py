# Creamos un programa para identificar la longitud de una palabra ingresada.
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

###########################################################################################

# Creamos un programa por medio de la función para identificar el cuadrante
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
