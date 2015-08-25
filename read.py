import time
import serial
ser = serial.Serial( 
  port='/dev/ttyAMA0',
  baudrate=9600,
  parity=serial.PARITY_ODD,
  stopbits=serial.STOPBITS_TWO,
  bytesize=serial.SEVENBITS
)
data = ''
while ser.inWaiting() > 0:
  data += ser.read(1)
if data != '':
  hexShow(data)
  
  

#
# import serial
# t = serial.Serial("/dev/ttyAMA0", 9600)
# t.portstr
# strInput = raw_input('AT')
# n = t.write(strInput)
# print n
# str = t.read(n)
# print str
# hexShow(str)
