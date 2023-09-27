import os
import readchar

mapa="..###################\n......#.#...........#\n #.#####.#.###.###.###\n #.....#.#...#.#.#...#\n #####.#.#.#####.#.###\n #...#.....#.#.......#\n ###.#.#.#.#.#####.###\n #.#...#.#.....#.....#\n #.#.#.###.#.#.###.#.#\n #...#.#...#.#...#.#.#\n ###.#.###########.#.#\n #...#...#.....#.#.#.#\n #.#.#.#######.#.#####\n #.#.#.#...#.........#\n #.#######.#####.#.#.#\n #.#...........#.#.#.#\n #.#########.#.#####.#\n #.#...#.....#.......#\n #.#.###.###.#######.#\n #.........#...#.....#\n ###################.#\n"
map=list(mapa.split("\n"))
matriz=[]
for fila in map:
    matriz.append(list(fila))

def imprimir_matriz(laberinto):
    os.system('cls' if os.name=='nt' else 'clear')
    for filas in laberinto:
        print("".join(filas))

def main_loop(mapa,posicion_inicial,posicion_final):
    px=posicion_inicial[0]
    py=posicion_inicial[1]

    mapa[px][py] = "p"
    imprimir_matriz(mapa)
    print("\n"+"Posicion"+str(px)+", "+str(py))

    while True:
        k=readchar.readkey()
        if k==readchar.key.UP:
            if 0<px<=len(mapa):
                if mapa[px -1][py] != "#":
                    mapa[px][py] = "."
                    px-=1
        elif k==readchar.key.DOWN:
            if 0<px<=len(mapa):
                    if mapa[px + 1][py] != "#":
                        mapa[px][py] = "."
                        px+=1
        elif k==readchar.key.LEFT:       
            if 0<py<=len(mapa):
                    if mapa[py - 1][py] != "#":
                        mapa[px][py] = "."
                        px-=1
        elif k==readchar.key.RIGHT:       
            if 0<py<=len(mapa):
                    if mapa[py + 1][py] != "#":
                        mapa[px][py] = "."
                        px+=1        
        mapa[px][py]
        imprimir_matriz(mapa)

        if px==posicion_final[0]and py==posicion_final[1]:
             print("felicidades")
             break
main_loop((matriz),(0,0),(10,10))
