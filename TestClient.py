# 导入 socket模块
import socket
import pickle

class Client:
    def __init__(self, host='127.0.0.1', port=8000):
        self.__host = host
        self.__port = port
        
    def start(self):
        """启动客户端并连接服务器"""
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.__host, self.__port))
        print(f"连接到服务器 {self.__host}:{self.__port}")
        
        try:
            while True:
                msg = client_socket.recv(1024)
                if not msg:
                    break
                self.data = pickle.loads(msg)
                print (self.data)
                # print(f"收到数据: {data.decode('utf-8')}")
        except KeyboardInterrupt:
            print("客户端关闭")
        finally:
            client_socket.close()

if __name__ == '__main__':
    client = Client()
    client.start()
