# Eje 3 - Modelos de Programación

Este repositorio contiene el material y los ejercicios correspondientes al Eje 3 del curso de Modelos de Programación de la Universidad Areandina.

## Descripción del Proyecto

Este proyecto integra dos funcionalidades principales:

1. **Juego de Adivinanza con Árbol Binario:**
   - **Servidor:** Genera un número secreto (entre 1 y 10) para cada ronda, lo inserta en un árbol binario y envía una señal de inicio ("NUEVO") al cliente. El servidor cuenta los aciertos y desaciertos (fallos consecutivos) del cliente. Si el cliente falla 3 veces seguidas, el servidor envía el mensaje "Perdiste" y termina el juego. Al finalizar, se muestra un recorrido in-order de todos los números secretos generados, y se ordena la lista utilizando el algoritmo bubble sort.
   - **Cliente:** Al recibir la señal "NUEVO" del servidor, solicita al usuario ingresar una adivinanza a través del teclado. El cliente envía su intento y, según la respuesta del servidor ("ACIERTO", "FALLO" o "Perdiste"), muestra el resultado de la ronda. El juego se puede finalizar en cualquier momento escribiendo "terminar".

2. **Integración con Árbol Binario:**
   - Cada número secreto generado por el servidor se almacena en un árbol binario. Esto permite, al final del juego, visualizar la lista de números en el orden en que fueron almacenados (recorrido in-order) y, adicionalmente, la lista ordenada usando bubble sort.

## Estructura del Repositorio

- `server.py`: Código del servidor. Se encarga de generar los números secretos, manejar la lógica del juego, insertar los números en el árbol binario y gestionar la comunicación con los clientes usando hilos.
- `client.py`: Código del cliente. Permite que el usuario adivine los números secretos enviados por el servidor. La comunicación se realiza a través de sockets, y el cliente puede finalizar la aplicación escribiendo "terminar".
- `README.md`: Este archivo, con las instrucciones y descripción del proyecto.

## Requisitos

- **Python 3:** Asegúrese de tener instalado Python 3.
- **Acceso a la terminal:** Para ejecutar los scripts desde la línea de comandos.

## Uso

### Ejecutar el Servidor

1. Abra una terminal y navegue hasta la carpeta del repositorio.
2. Ejecute el servidor con el siguiente comando:

   ```bash
   python server.py

El servidor se iniciará y quedará a la espera de conexiones en 127.0.0.1:9999.

Ejecutar el Cliente
	1.	Abra otra terminal (o una nueva pestaña) y navegue hasta la carpeta del repositorio.
	2.	Ejecute el cliente con el siguiente comando:

python client.py

Al conectarse al servidor, el cliente esperará el inicio de una ronda. Cuando reciba el mensaje "NUEVO", ingrese su adivinanza (un número entre 1 y 10) o la palabra "terminar" para finalizar el juego.

Flujo del Juego
	•	Inicio de Ronda: El servidor genera un número secreto, lo almacena en el árbol binario y envía "NUEVO" al cliente.
	•	Adivinanza: El cliente ingresa su intento. El servidor compara la adivinanza con el número secreto:
	•	Si el intento es correcto, se envía "ACIERTO" y se reinicia el contador de fallos consecutivos.
	•	Si es incorrecto, se envía "FALLO" y se incrementa el contador de fallos. Al llegar a 3 fallos consecutivos, se envía "Perdiste" y el juego finaliza.
	•	Terminación: El juego se puede finalizar en cualquier momento escribiendo "terminar" en el cliente. Al finalizar, el servidor muestra estadísticas y la lista de números secretos generados (ordenados de dos maneras).

Notas
	•	El proyecto utiliza sockets para la comunicación cliente-servidor en la misma máquina (localhost).
	•	El manejo de múltiples clientes se realiza mediante hilos en el servidor, permitiendo atender a más de un cliente simultáneamente.
	•	La integración del árbol binario permite almacenar y procesar los números secretos, demostrando el manejo de estructuras de datos junto a la lógica del juego.

Autor

Esteban Villada - Curso de Modelos de Programación

