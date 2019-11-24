import socket

import datetime
import encodings




HOST = '127.0.0.1'  
PORT = 12345       


def my_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server Started waiting for client to connect ")
        s.bind((HOST, PORT))
        s.listen(5)
        c, addr = s.accept()

        with c:
            print('Connected by', addr)
            while True:

                date = datetime.datetime.now()   
                d = str(date)
                print("date and time =%d",d)
                encoded_data = d.encode('utf-8')

                c.sendall(encoded_data)
                

                
if __name__ == '__main__':
    while 1:
        my_server()

