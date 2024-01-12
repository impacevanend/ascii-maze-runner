import os
import readchar
import random
from functools import reduce

class Juego:
    def __init__(self, mapa, start, end):
        self.mapa = self.convert_to_matrix(mapa)
        self.start_position = start
        self.end_position = end
        self.px, self.py = self.start_position

    def convert_to_matrix(self, mapa):
        return [list(row) for row in mapa.split("\n")]

    def print_maze(self):
        for row in self.mapa:
            print("".join(row))

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def main_loop(self):
        while (self.px, self.py) != self.end_position:
            self.print_maze()
            key = readchar.readkey()

            next_px, next_py = self.px, self.py

            if key == readchar.key.UP and self.py > 0 and self.mapa[self.py - 1][self.px] != "#":
                next_py -= 1
            elif key == readchar.key.DOWN and self.py < len(self.mapa) - 1 and self.mapa[self.py + 1][self.px] != "#":
                next_py += 1
            elif key == readchar.key.LEFT and self.px > 0 and self.mapa[self.py][self.px - 1] != "#":
                next_px -= 1
            elif key == readchar.key.RIGHT and self.px < len(self.mapa[0]) - 1 and self.mapa[self.py][self.px + 1] != "#":
                next_px += 1

            if (next_px, next_py) != (self.px, self.py):
                self.mapa[self.py][self.px] = "."
                self.px, self.py = next_px, next_py
                self.mapa[self.py][self.px] = "P"
                self.clear_screen()

        print("¡Has llegado al final del laberinto!")

    def play(self):
        self.clear_screen()
        self.main_loop()


class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        nombre_archivo = random.choice(os.listdir(path_a_mapas))
        path_completo = os.path.join(path_a_mapas, nombre_archivo)
        mapa, start, end = self.leer_archivo_mapa(path_completo)
        super().__init__(mapa, start, end)

    def leer_archivo_mapa(self, path_completo):
        with open(path_completo, "r") as file:
            start_end = file.readline().strip().split()
            start = tuple(map(int, start_end[:2]))
            end = tuple(map(int, start_end[2:]))
            mapa = reduce(lambda acc, x: acc + x.strip() + "\n", file.readlines(), "")
            return mapa, start, end


def main2():
    juego = JuegoArchivo("laberintos")
    juego.play()

if __name__ == "__main__":
    main2()
