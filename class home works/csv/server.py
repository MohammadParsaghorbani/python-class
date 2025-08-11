import socket
import threading
from cryptography.fernet import Fernet

# 🔐 Generate encryption key and save to file
key = Fernet.generate_key()
with open("secret.key", "wb") as f:
    f.write(key)

cipher = Fernet(key)
print("🔐 Encryption key generated and saved to 'secret.key'")
print("🔑 Share this key with your friends to connect securely.")

# 🌐 Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))  # Listen on all interfaces
server.listen(5)

print("✅ Server is running and waiting for connections...")

clients = []
usernames = {}

# 📤 Broadcast message to all clients except sender
def broadcast(sender_socket, encrypted_msg):
    for client in clients:
        if client != sender_socket:
            client.send(encrypted_msg)

# 🎯 Handle each client connection
def handle_client(client_socket):
    try:
        # First message is the username
        encrypted_username = client_socket.recv(1024)
        username = cipher.decrypt(encrypted_username).decode()
        usernames[client_socket] = username
        print(f"👤 {username} connected.")

        while True:
            encrypted_msg = client_socket.recv(1024)
            if not encrypted_msg:
                break
            msg = cipher.decrypt(encrypted_msg).decode()
            full_msg = f"{username}: {msg}"
            print(f"📨 {full_msg}")
            encrypted_broadcast = cipher.encrypt(full_msg.encode())
            broadcast(client_socket, encrypted_broadcast)
    except:
        pass
    finally:
        print(f"❌ {usernames.get(client_socket, 'Unknown')} disconnected.")
        clients.remove(client_socket)
        client_socket.close()

# 🚀 Accept clients
while True:
    conn, addr = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()