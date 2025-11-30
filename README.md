# Python TCP Chat Tool 💬

I built this application to understand the fundamentals of network programming. Instead of using high-level libraries, I implemented a raw Client-Server architecture using Python's standard `socket` module to manually handle TCP handshakes, data encoding, and connection states.

## 🧠 What I Learned
* **Socket Primitives:** Manually initializing sockets with `socket.AF_INET` (IPv4) and `socket.SOCK_STREAM` (TCP).
* **The TCP Lifecycle:** Implementing the full sequence: `bind()` → `listen()` → `accept()` → `connect()`.
* **Resource Management:** Using `try...finally` blocks to ensure sockets are explicitly closed, preventing resource leaks.
* **Flow Control:** Managing a synchronous chat loop where the server initiates communication and the client responds.

## 💻 How to Run (Read Carefully)
You must run the files in the specific order below.

### Step 1: Start the Server (Do this first)
The server must be running and "listening" before a client can connect.
```bash
python [/path/to/the/folder] server.py
```
### Step 2: Start the Client & Enter IP
```bash
python [/path/to/the/folder] server.py
```
### Step 3: Input the IP Address
The client will prompt you to enter the Server IP:
* Local Test: If testing on the same machine, just press Enter (defaults to 127.0.0.1).
* Network Test: If the server is on a different computer, type that computer's IP address (e.g., 192.168.1.5) and hit Enter.
