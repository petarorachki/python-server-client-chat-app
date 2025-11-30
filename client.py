import socket
port = 64421
def start_client():
    # get the ip address
    ip_address = input("Enter Server IP [127.0.0.1]: ")
    # default to localhost if empty
    if ip_address == "":
        ip_address = "127.0.0.1"
    # create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # try to connect to the server
        s.connect((ip_address, port))
        print("Connected to the server!")
        while True:
            # receive data from server first
            data = s.recv(1024)
            # if no data, server closed connection
            if not data:
                break
            # decode and print
            print("[SERVER]: " + data.decode('utf-8'))
            # ask user for input
            user_input = input("CLIENT >>: ")
            # send data back
            s.send(user_input.encode('utf-8'))
    except Exception as e:
        print("Connection failed: " + str(e))
    finally:
        # close the connection
        s.close()
        print("Client closed.")

if __name__ == "__main__":
    start_client()
