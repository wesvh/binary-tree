class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    """Inserta un nodo en el árbol binario de búsqueda."""
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def in_order(root, result):
    """Recorrido in-order (izquierda, nodo, derecha) para visualizar el árbol completo."""
    if root:
        in_order(root.left, result)
        result.append(root.data)
        in_order(root.right, result)
    return result


def in_order_two_children(root, result):
    """Recorrido in-order para visualizar los nodos que tienen dos hijos."""
    if root:
        in_order_two_children(root.left, result)
        if root.left is not None and root.right is not None:
            result.append(root.data)
        in_order_two_children(root.right, result)
    return result


def pre_order_even_child(root, result):
    """
    Recorrido preorden para visualizar los nodos que tienen al menos un hijo par.
    Se evalúa si alguno de los hijos (si existen) es par.
    """
    if root:
        if (root.left is not None and root.left.data % 2 == 0) or (
            root.right is not None and root.right.data % 2 == 0
        ):
            result.append(root.data)
        pre_order_even_child(root.left, result)
        pre_order_even_child(root.right, result)
    return result


def pre_order_children_sum(root, result):
    """
    Recorrido preorden para visualizar la suma de los hijos inmediatos de cada nodo.
    Si un hijo no existe, se suma 0.
    """
    if root:
        suma = 0
        if root.left:
            suma += root.left.data
        if root.right:
            suma += root.right.data
        result.append(suma)
        pre_order_children_sum(root.left, result)
        pre_order_children_sum(root.right, result)
    return result


def search_path(root, target, path):
    """
    Busca recursivamente el nodo con valor 'target' y acumula el camino desde la raíz.
    Retorna True si se encuentra; de lo contrario, False.
    """
    if root is None:
        return False
    path.append(root.data)
    if root.data == target:
        return True
    if target < root.data:
        if search_path(root.left, target, path):
            return True
    else:
        if search_path(root.right, target, path):
            return True
    path.pop()  # Retrocede si el camino actual no conduce al nodo buscado
    return False


def main():
    # Solicitar la cantidad de nodos y los valores a insertar
    n = int(input("Ingrese la cantidad de nodos: "))
    print("Ingrese los nodos separados por espacios:")
    values = list(map(int, input().split()))

    if len(values) != n:
        print(
            "La cantidad de nodos ingresada no coincide con el número de valores proporcionados."
        )
        return

    # Construir el árbol binario de búsqueda
    root = None
    for v in values:
        root = insert(root, v)

    # 1. Visualice el árbol en orden (in-order)
    in_order_list = in_order(root, [])
    print("\nRecorrido en orden:")
    print(" ".join(map(str, in_order_list)))

    # 2. Visualice los nodos en donde tiene dos hijos en orden (in-order)
    two_children_list = in_order_two_children(root, [])
    print("\nNodos con dos hijos (en orden):")
    print(" ".join(map(str, two_children_list)))

    # 3. Visualice los nodos que tengan por lo menos un hijo par (en preorden)
    even_child_nodes = pre_order_even_child(root, [])
    print("\nNodos con al menos un hijo par (en preorden):")
    print(" ".join(map(str, even_child_nodes)))

    # 4. Por cada nodo, visualice la suma de sus hijos (en preorden)
    children_sum = pre_order_children_sum(root, [])
    print("\nSuma de los hijos de cada nodo (en preorden):")
    print(" ".join(map(str, children_sum)))

    # 5. El camino para llegar al nodo X
    target = int(input("\nEscriba el nodo a buscar: "))
    path = []
    if search_path(root, target, path):
        print("El camino es: " + " ".join(map(str, path)))
    else:
        print("El nodo no existe")


if __name__ == "__main__":
    main()
