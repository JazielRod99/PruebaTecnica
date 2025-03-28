import socket

# Localhost y puerto del servidor
HOST = "127.0.0.1"  
PORT = 5000        

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"🔵 Conectado al servidor {HOST}:{PORT}")

        # Mantenemos corrioendo el servidor
        while True:
            message = input("✉️ Ingresa un mensaje ('DESCONEXION' para salir): ")
            client_socket.sendall(message.encode())

            if message.upper() == "DESCONEXION":
                print("🔴 Desconectando del servidor...")
                break  # Salimos del bucle y cerramos la conexión
            
            response = client_socket.recv(1024).decode()
            print(f"📩 Respuesta del servidor: {response}")

if __name__ == "__main__":
    start_client()
