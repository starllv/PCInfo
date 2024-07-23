from server import Server
from TestClient import TestClient

server = Server(period=0.1)
server.start()

client = TestClient()
client.start()
