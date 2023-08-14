#######################################################################################
'''
Codigo Realizado por Rolando Alvarado  
EL SALVADOR
'''
#######################################################################################

import os
import readchar
#funcion para borrar pantalla
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
#funcion para lectura de caracter
def read_char():
    return readchar.readkey()
number = 0 #Variable auxiliar
#Ciclo para crear el bucle

while number <= 50:
    caracter = read_char()
    if caracter == 'n':
        clear_screen()
    else:
        print(number)
        number += 1 
        #break

input('Preciona cualquier salir del bucle...')
