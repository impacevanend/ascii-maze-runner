import os
import readchar

# Función para borrar la terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para actualizar el número en la pantalla
def update_number(num):
    clear_screen()
    print(f"El número actual es: {num}")

def main():
    number = 0
    update_number(number)
    
    print("Presiona 'n' para incrementar el número o '↑' para salir.")

    while number < 50:
        key = readchar.readkey()
        
        if key == 'n':
            number += 1
            update_number(number)
        elif key == readchar.key.UP:
            break

    print("Has alcanzado el número 50 o has decidido salir. ¡Hasta la próxima!")

if __name__ == "__main__":
    main()