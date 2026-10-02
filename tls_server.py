import socket
import ssl

server_ip = "192.168.10.254"
server_port = 9443

print("1. Loading security certificates...")
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

print("2. Setting up the TCP socket...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"3. TLS Server listening securely on {server_ip}:{server_port}...")

try:
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"4. Connection received from {client_address[0]}. Securing with TLS...")

        secure_client_socket = context.wrap_socket(client_socket, server_side=True)
        print("5. Connection secured! Waiting for message...")

        data = secure_client_socket.recv(1024)
        if data:
            print(f"Received encrypted message: {data.decode('utf-8')}")
            secure_client_socket.sendall(data)

        secure_client_socket.close()

except KeyboardInterrupt:
    print("\nShutting down.")
except Exception as e:
    print(f"Server error: {e}")
finally:
    server_socket.close()
