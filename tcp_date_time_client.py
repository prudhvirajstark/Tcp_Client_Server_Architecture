import socket
import encodings
import sqlite3
import time


HOST = '127.0.0.1'  
PORT = 12345       





def my_client():
    

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        conn = sqlite3.connect("DATA" )
        cursor = conn.cursor()
        data = s.recv(1024).decode('utf-8')
        print(data)

        cursor.execute("DROP TABLE IF EXISTS DATA_NAME")
        cursor.execute("CREATE TABLE DATA_NAME(Data CHAR(20))");
        
        cursor.execute("INSERT INTO DATA_NAME(data) VALUES (?)",[data]);
        conn.commit()
        print("\\connected To Db")
        conn.close()
        
        
        s.close()
        time.sleep(5)
        


if __name__ == "__main__":
    while 1:
        my_client()

            
