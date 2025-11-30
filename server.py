import socket
# setup variables
host = '0.0.0.0'
port = 64421
def start_server():
    # make the socket object
    # AF_INET is for ipv4, SOCK_STREAM is for tcp
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # bind to the ip and port
        server_socket.bind((host, port))
        # start listening for connections
        server_socket.listen(2)
        print("Server is listening on " + host + ":" + str(port))
        # accept the client connection
        # this waits here until someone connects
        client, address = server_socket.accept()
        print("Connected to: " + str(address))
        while True:
            # get input from the server user
            message = input("SERVER >>: ")
            # check if message is empty
            if message == "":
                continue
            # check for end command
            if message == "end":
                break
            # send the message to the client
            # encoding the bytes with .encode('utf-8')
            client.send(message.encode('utf-8'))
            # wait for the response from the client
            response = client.recv(1024)
            # if we get no data, the connection is closed
            if not response:
                break
            # print the client message
            print("[CLIENT]: " + response.decode('utf-8'))
    except Exception as e:
        print("Error happened: " + str(e))
    finally:
        server_socket.close()
        print("Server stopped.")
if __name__ == "__main__":
    start_server()
