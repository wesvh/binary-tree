import socket


def main():
    HOST = "127.0.0.1"
    PORT = 9999

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Conectado al servidor.")
        try:
            while True:
                # Espera el mensaje de inicio de ronda
                data = s.recv(1024)
                if not data:
                    break
                msg = data.decode().strip()
                if msg == "NUEVO":
                    # Comienza la ronda: solicitar adivinanza
                    guess = input(
                        "Ingrese su adivinanza (o 'terminar' para finalizar): "
                    )
                    s.sendall(guess.encode())
                elif msg == "ACIERTO":
                    print("¡Adivinaste correctamente!")
                elif msg == "FALLO":
                    print("Fallaste, inténtalo en la siguiente ronda.")
                elif msg == "Perdiste":
                    print("Perdiste: 3 fallos consecutivos. Fin del juego.")
                    break
                else:
                    print("Mensaje del servidor:", msg)
        except Exception as e:
            print("Error:", e)
    print("Juego finalizado.")


if __name__ == "__main__":
    main()
