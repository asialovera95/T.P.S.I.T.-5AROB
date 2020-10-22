import socket as sck


def client():
    # get the server name
    host = "127.0.0.1"
    port = 6000  # server port number

    c = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  # instantiate

    c.connect((host, port))  # connect to the server

    print("Enter 'exit' to end the connection")
    msg = input("->")  # take input

    while True:
        c.sendall(msg.encode())  # send message

        data = c.recv(1024).decode()  # receive response
        print(f"Received from server: {data}")  # show response

        msg = input("->")  # again take input

        if msg == "exit":
            c.sendall(msg.encode())  # send message
            print("Close the connection")
            break

    c.close()  # close the connection


if __name__ == '__main__':
    client()
