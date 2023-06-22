from smbus import SMBus

addr = 0x8
bus = SMBus(1)
def send(angle,speeds):
    bus.write_byte(addr,angle)
    bus.write_byte(addr,speeds)
