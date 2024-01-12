import os
import readchar


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def convert_to_matrix(maze_string):
    return [list(row) for row in maze_string.split("\n") if row]


def print_maze(maze_matrix):
    for row in maze_matrix:
        print(''.join(row))


def find_valid_start_position(maze_matrix):
    for y, row in enumerate(maze_matrix):
        for x, char in enumerate(row):
            if char == '.':
                return x, y
    raise ValueError("No se encontró una posición inicial válida en el laberinto.")

def find_valid_end_position(maze_matrix):
    for y in range(len(maze_matrix) - 1, -1, -1):
        for x in range(len(maze_matrix[y]) - 1, -1, -1):
            if maze_matrix[y][x] == '.':
                return x, y
    raise ValueError("No se encontró una posición final válida en el laberinto.")


def main_loop(maze_matrix, start_position, end_position):
    px, py = start_position
    maze_matrix[py][px] = 'P' 

    while (px, py) != end_position:
        key = readchar.readkey()

        next_px, next_py = px, py  

        if key == readchar.key.UP and py > 0 and maze_matrix[py - 1][px] != '#':
            next_py -= 1
        elif key == readchar.key.DOWN and py < len(maze_matrix) - 1 and maze_matrix[py + 1][px] != '#':
            next_py += 1
        elif key == readchar.key.LEFT and px > 0 and maze_matrix[py][px - 1] != '#':
            next_px -= 1
        elif key == readchar.key.RIGHT and px < len(maze_matrix[0]) - 1 and maze_matrix[py][px + 1] != '#':
            next_px += 1

        
        if (next_px, next_py) != (px, py):
            maze_matrix[py][px] = '.'
            px, py = next_px, next_py
            maze_matrix[py][px] = 'P'

            clear_screen()  
            print_maze(maze_matrix)

    print("¡Has llegado al final del laberinto!")


maze_string = """
###################
.................#.
#.###.#######.#.#.#.
#...#...#.......#...
#.#.#.#.###.#.#######
#.#.#.#.#.#.#...#...
###.#.#.#.#.#.#.#.###
#...#.#.#.#.#.#.....
###.#.###.#.#######.
#.#.#...#...#.....#.
#.#.#####.###.#.###.
#...#.#...#...#.#...
###.#.#.###.#.#####.
#...#...#.#.#.......
#.###.###.#.#.#.###.
#.....#...#.#.#.#...
#####.#.#######.#.#.
#.#.....#...#.#.#.#.
#.#.#.#####.#.#.###.
#...#.......#.....#.
###################.
"""

def main():
    maze_matrix = convert_to_matrix(maze_string)
    start_position = find_valid_start_position(maze_matrix)
    end_position = find_valid_end_position(maze_matrix)

    # Imprimir las instrucciones
    print("Instrucciones:")
    print("Usa las teclas de flecha para moverte por el laberinto.")
    print("Presiona '↑' para moverte hacia arriba.")
    print("Presiona '↓' para moverte hacia abajo.")
    print("Presiona '←' para moverte hacia la izquierda.")
    print("Presiona '→' para moverte hacia la derecha.")
    print("Encuentra el camino hasta el final del laberinto.")
    input("Presiona Enter para comenzar...")

    clear_screen()  # Limpiar la pantalla antes de imprimir el laberinto inicial
    main_loop(maze_matrix, start_position, end_position)

if __name__ == "__main__":
    main()
