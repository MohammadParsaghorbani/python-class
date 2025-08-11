import socket
import threading
from cryptography.fernet import Fernet

# 🔐 Load encryption key from file (copy from server)
key = b'PASTE-YOUR-KEY-HERE'  # Replace with actual key from server
cipher = Fernet(key)

# 🌐 Connect to server using direct IP
server_ip = '192.168.1.10'  # Replace with actual server IP
server_port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

# 👤 Choose a username
username = input("Enter your display name: ")
encrypted_username = cipher.encrypt(username.encode())
client.send(encrypted_username)

# 📥 Receive messages from server
def receive():
    while True:
        try:
            encrypted_msg = client.recv(1024)
            msg = cipher.decrypt(encrypted_msg).decode()
            print(f"\n💬 {msg}")
        except:
            break

# 🚀 Start receiving in a separate thread
thread = threading.Thread(target=receive)
thread.start()

# ✍️ Send messages
while True:
    msg = input()
    encrypted_msg = cipher.encrypt(msg.encode())
    client.send(encrypted_msg)