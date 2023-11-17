import socket

proxy_host = '127.0.0.1'
proxy_port = 10999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((proxy_host, proxy_port))

print("Connected to Proxy. Type 'exit' to disconnect.")

while True:
    message = input("Enter a message: ")

    client.sendall(message.encode('utf-8'))

    if message.lower() == 'exit':
        print("Disconnecting from Proxy...")
        break

    response = client.recv(1024)
    print(f"Received response from proxy: {response.decode('utf-8')}")

client.close()
