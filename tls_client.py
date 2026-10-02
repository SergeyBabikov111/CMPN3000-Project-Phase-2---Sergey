import socket
import ssl

server_ip = "192.168.10.254"
server_port = 9443

# Set up TLS context and load the server's certificate for verification
context = ssl.create_default_context()
context.load_verify_locations("server.crt")
# Disable hostname checking since we used a basic self-signed cert without a domain name
context.check_hostname = False 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Wrap your TCP socket with TLS context[cite: 8]
    secure_socket = context.wrap_socket(client_socket, server_hostname=server_ip)
    secure_socket.connect((server_ip, server_port))
    
    # Prompt for and then send user input[cite: 8]
    message = input("Enter a message for the secure TLS server: ")
    secure_socket.sendall(message.encode('utf-8'))
    
    # Receive a reply from the server and display it on the screen[cite: 8]
    data = secure_socket.recv(1024)
    print(f"Secure echo received: {data.decode('utf-8')}")

except Exception as e:
    print(f"TLS Connection Error: {e}")
finally:
    # Close the TLS socket to release resources[cite: 8]
    client_socket.close()
