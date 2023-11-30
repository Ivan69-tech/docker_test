#!/bin/python

from pyModbusTCP.client import ModbusClient

c = ModbusClient(host="127.0.0.1", port=5020, unit_id=1,auto_open=True)
print(c.open())

c.write_single_register(1,1)
c.write_multiple_registers(1,[2,3,4,5,6,7,8,9])

print(c.read_holding_registers(1))
print(c.read_holding_registers(4))
print(c.read_holding_registers(5))