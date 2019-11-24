import socket
import threading
import sqlite3
import time

HOST = '127.0.0.1'  
PORT = 65432  


def my_client():
    #threading.Timer(11, my_client).start()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        conn = sqlite3.connect("HOST" )
        cursor = conn.cursor()
        my = input("Enter command ")
        my_inp = my.encode('utf-8')
        s.sendall(my_inp)
        data = s.recv(1024).decode('utf-8')
        print(data)
        
        cursor.execute("DROP TABLE IF EXISTS HOST_NAME")
        cursor.execute("CREATE TABLE HOST_NAME(Host CHAR(20))");
        cursor.execute("INSERT INTO HOST_NAME(Host) VALUES (?)",[data]);
        conn.commit()
        conn.close()
        s.close()
        time.sleep(5)

if __name__ == "__main__":
    while 1:
        my_client()
