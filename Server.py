import socket

HOST = "127.0.0.1"  # Localhost
PORT = 5000         # Puerto de escucha

def start_server():
    """Inicia un servidor TCP que escucha conexiones entrantes y reenvía mensajes tal cual los recibe."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"🔵 Servidor escuchando en {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            print(f"✅ Cliente conectado desde {addr}")

            with conn:
                while True:
                    data = conn.recv(1024).decode("utf-8")  # Decodificar en UTF-8
                    if not data:
                        break
                    
                    print(f"📩 Mensaje recibido: {data}")

                    if data.upper() == "DESCONEXION":
                        print("🔴 Cliente solicitó desconexión.")
                        break  # Salimos del bucle interno, cerrando la conexión
                    
                    conn.sendall(data.upper().encode("utf-8"))  # Responder con el mismo mensaje sin modificar

            print("🚪 Conexión cerrada con el cliente.")

if __name__ == "__main__":
    start_server()
