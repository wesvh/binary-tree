import socket
import random
import threading


# --- Implementación del árbol binario ---
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def in_order(root, result):
    if root:
        in_order(root.left, result)
        result.append(root.data)
        in_order(root.right, result)
    return result


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# --- Lógica del juego en el servidor ---
def handle_client(conn, addr):
    total_hits = 0
    total_misses = 0
    consecutive_misses = 0
    tree_root = None  # Árbol binario para almacenar los números secretos generados

    print("Conexión establecida con", addr)
    try:
        while True:
            # Genera un número secreto para la ronda (entre 1 y 10)
            secret = random.randint(1, 10)
            print(f"[{addr}] Nueva ronda. Número secreto: {secret}")
            # Inserta el número secreto en el árbol
            tree_root = insert(tree_root, secret)

            # Inicia la ronda enviando "NUEVO"
            conn.sendall("NUEVO".encode())

            # Espera la respuesta del cliente
            data = conn.recv(1024)
            if not data:
                break
            guess_str = data.decode().strip()
            # Permitir terminar el juego si el cliente escribe "terminar"
            if guess_str.lower() == "terminar":
                print(f"[{addr}] El cliente solicitó terminar la partida.")
                break
            try:
                guess = int(guess_str)
            except ValueError:
                conn.sendall("Formato de número inválido.".encode())
                continue

            # Comparación: ¿acierto o fallo?
            if guess == secret:
                total_hits += 1
                consecutive_misses = 0
                conn.sendall("ACIERTO".encode())
                print(f"[{addr}] Cliente adivinó correctamente: {guess}")
            else:
                total_misses += 1
                consecutive_misses += 1
                conn.sendall("FALLO".encode())
                print(f"[{addr}] Cliente falló: adivinó {guess} en vez de {secret}")
                if consecutive_misses >= 3:
                    conn.sendall("Perdiste".encode())
                    print(f"[{addr}] Perdiste: 3 fallos consecutivos.")
                    break
    except Exception as e:
        print(f"[{addr}] Error: {e}")
    finally:
        # Fin de la partida: mostrar estadísticas y el árbol
        print(
            f"[{addr}] Resultados finales => Aciertos: {total_hits}, Desaciertos: {total_misses}"
        )
        if tree_root:
            numeros = in_order(tree_root, [])
            numeros_ordenados = bubble_sort(numeros.copy())
            print(f"[{addr}] Números secretos (in-order): {numeros}")
            print(
                f"[{addr}] Números secretos ordenados con bubble sort: {numeros_ordenados}"
            )
        conn.close()


def main():
    HOST = "127.0.0.1"
    PORT = 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Servidor escuchando en {HOST}:{PORT} ...")

    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
    except KeyboardInterrupt:
        print("Servidor detenido.")
    finally:
        server.close()


if __name__ == "__main__":
    main()
