import readchar

def get_key_press():
    key = readchar.readkey()
    return key

def main():
    print("Bienvenido al juego del laberinto ASCII!")
    player_name = input("Por favor, introduce tu nombre: ")
    print(f"Hola, {player_name}. Usa las teclas de dirección para moverte. Presiona '↑' para salir.")

    while True:
        key = get_key_press()
        
        if key == readchar.key.UP:
            print("Tecla UP detectada, terminando el programa.")
            break
        else:
            print(f"Tecla presionada: {key}")


if __name__ == "__main__":
    main()
