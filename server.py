import socket
import threading

clients = {}

def broadcast_message(sender_username, message):
    for client_username, client_socket in clients.items():
        if client_username != sender_username:
            client_socket.send(message.encode('utf-8'))

def handle_client(client_socket, client_address):
    try:
        username = client_socket.recv(1024).decode('utf-8')
        clients[username] = client_socket

        print(f"[*] Cliente {username} conectado do endereço {client_address[0]}:{client_address[1]}")

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{username}: {message}")
            broadcast_message(username, f"{message}")

    except:
        print(f"[*] Cliente {username} desconectado.")
        del clients[username]
        client_socket.close()

def main():
    server_ip = '0.0.0.0'  # Endereço IP do servidor, deixe '0.0.0.0' para aceitar conexões de qualquer endereço
    server_port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"[*] Servidor ouvindo em {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    main()
