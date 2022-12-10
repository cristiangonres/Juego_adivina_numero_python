from random import randint

intentos = 8
numero = randint(1, 100)
numero_input = 0

while numero != numero_input and intentos >= 0:
    
    numero_input = int(input(f'Adivina un número entre el 1 y 100: '))
        
    if numero_input not in range(1,101):
        print('El número debe estar dentro del rango.')
        continue
    
    intentos -=1
    
    if numero == numero_input:
            print(f'HAS GANADO. Has acertado en {8-intentos} intentos')
            break
    else:
        print(f'Has fallado')
        if numero_input > numero:
            print('Te has pasado, el numero es menor, sigue probando')
        elif numero_input < numero:
            print('El número es mayor, sigue probando')
        print(f'Te quedan {intentos} intentos')
else:
    print('GAME OVER')