import socket
import pickle
import threading
import time
from PCInfo import PCInfo

class Server:
    def __init__(self, host='127.0.0.1', port=8000, period=1):
        self.__host = host
        self.__port = port
        self.__period = period
        
    def handle_client(self, client_socket):
        """处理客户端连接并每秒发送一次数据"""
        try:
            while True:
                info = PCInfo()
                # 使用 pickle 序列化数据
                serialized_data = pickle.dumps(info.get())
                        
                client_socket.sendall(serialized_data)

                print("[+] Data sent successfully")
                    
                time.sleep(self.__period)
                
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            print("客户端断开连接")
        finally:
            client_socket.close()

    def start(self):
        # 创建一个 IPv4 TCP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定地址和端口
        server_socket.bind((self.__host, self.__port))
        # 开始监听，最多允许一个连接排队
        server_socket.listen(5)
        print(f"[*] Listening on {self.__host}:{self.__port}")
        
        try:
            while True:
                # 等待客户端连接
                client_socket, client_address = server_socket.accept()
                print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

                client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_handler.start()
        
        except Exception as e:
            print(f"[-] Error running server: {e}")
        
        finally:
            # 关闭服务器 socket
            server_socket.close()

if __name__ == '__main__':
    server = Server(period=0.1)
    server.start()
