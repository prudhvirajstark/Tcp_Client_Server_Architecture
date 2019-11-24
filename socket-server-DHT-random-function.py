import socket
import encodings
import random


HOST = '127.0.0.1'  
PORT = 65432       

def random_data():
    temp = random.randint(25,45)
    hum = random.randint(50,60)
    air = random.randint(55,60)
    light = random.randint(100,180)
    
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, hum))
    print('Air={0:0.1f}*PPM  Light={1:0.1f}*LUX'.format(air, light))
    print("data was written on database T{} H{} A{} L{}".format(temp, hum, air, light))
    data = '{},{},{},{}'.format(temp, hum, air, light)
    return data

def my_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server Started waiting for client to connect ")
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()

        with conn:
            print('Connected by', addr)
            while True:

                data = conn.recv(1024).decode('utf-8')

                if str(data) == "Data":

                    print("Ok Sending data ")

                    my_data = random_data()

                    x_encoded_data = my_data.encode('utf-8')

                    conn.sendall(x_encoded_data)

                elif  str(data) == "Quit":
                    print("shutting down server ")
                    break
                else:
                    pass


if __name__ == '__main__':
    while 1:
        my_server()

