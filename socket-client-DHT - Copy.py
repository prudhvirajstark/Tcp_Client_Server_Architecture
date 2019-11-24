import socket
import threading
import sqlite3
import time


HOST = '127.0.0.1'  
PORT = 65432       


def process_data_from_server(x):
    t, h, a, l = x.split(",")
    conn = sqlite3.connect("sensordb.db" )
    cursor = conn.cursor()
    #cursor.execute("CREATE TABLE sensorval (Temp  CHAR(100),Hum  CHAR(100),Air  CHAR(100),Light  CHAR(100))")
    #conn.commit()
    params=(t,h,a,l)
    cursor.execute("INSERT INTO sensorval(Temp,Hum,Air,Light) VALUES (?,?,?,?)",params)
    conn.commit()
    print("\\connected To Db")
    conn.close()
    return t,h,a,l


def my_client():
    threading.Timer(11, my_client).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        my = input("Enter command ")

        my_inp = my.encode('utf-8')

        s.sendall(my_inp)

        data = s.recv(1024).decode('utf-8')

        temperature,humidity,air,light = process_data_from_server(data)
        Temp=str(data.format(temperature))
        print(Temp)
        Hum=str(data.format(humidity))
        Air=str(data.format(air))
        Light=str(data.format(light))
        
        print("Temperature {}".format(temperature))
        print("Humidity {}".format(humidity))
        print("Air {}".format(air))
        print("Light {}".format(light))
        
        s.close()
        time.sleep(5)

if __name__ == "__main__":
    while 1:
        my_client()

            
