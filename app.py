from pyModbusTCP.server import ModbusServer
import time 

server = ModbusServer(host = "localhost", port = 502, no_block=True)
server.start()
while True :
  print("serveur is running")
  time.sleep(5)
  pass