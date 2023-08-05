#######################################################################################
'''
Codigo Realizado por Rolando Alvarado 
'''
#######################################################################################
'''
Escribir un programa que corra un bucle infinito 
leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP
'''
import readchar

while True:
    key = readchar.readkey()
    if key == readchar.key.UP:
        break # con el comando break cortamos el ciclo infinito
    print(key)
