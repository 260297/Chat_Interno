import socket
import threading

def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
    except:
        print("Erro na conexão com o servidor.")
        client_socket.close()

def main():
    server_ip = '127.0.0.1'  # Endereço IP do servidor (neste exemplo, é o localhost)
    server_port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    receiver = threading.Thread(target=receive_messages, args=(client_socket,))
    receiver.start()

    username = input("Digite seu nome de usuário: ")
    print(f"Bem-vindo, {username}!")

    try:
        while True:
            message = input()
            if message.lower() == 'sair':
                break
            client_socket.send(f"{username}: {message}".encode('utf-8'))

    except KeyboardInterrupt:
        print("Saindo...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
