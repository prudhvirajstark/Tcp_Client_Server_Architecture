import socket
import encodings


HOST = '127.0.0.1'  
PORT = 65432       

def host_name():
    host_name = socket.gethostname()
    data = '{}'.format(host_name)
    return data



def my_server():    

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(host_name())
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()
        with conn:            
            while True:
                data = conn.recv(1024).decode('utf-8')
                if str(data) == "HostName":
                    print("Ok Sending data ")
                    my_data = host_name()
                    x_encoded_data = my_data.encode('utf-8')
                    conn.sendall(x_encoded_data)              

if __name__ == '__main__':
    while 1:
        my_server()
