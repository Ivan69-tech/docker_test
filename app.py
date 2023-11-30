from pyModbusTCP.server import ModbusServer
import time 

server = ModbusServer(host = "0.0.0.0", port = 5020, no_block=True)
server.start()
while True :
  print("serveur is running")
  time.sleep(5)
  pass