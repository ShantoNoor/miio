HELLO_PACKET = '21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff'

# GET_TIMER_DATA = b'{"method":"temperature","params":[],"id":1}'

GET_INFO_DATA = b'{"method":"miIO.info","params":[],"id":1}'
GET_POWER_STATUS_DATA = b'{"method":"get_prop","params":["power","temperature","wifi_led"],"id":2}'
POWER_OFF_DATA = b'{"method":"set_power","params":["off"],"id":3}'
POWER_ON_DATA = b'{"method":"set_power","params":["on"],"id":3}'

POWER_OFF_RES = b'{"result":["off"],"id":2}'
POWER_ON_RES = b'{"result":["on"],"id":2}'
OK_RES = b'{"result":["ok"],"id":3}'
