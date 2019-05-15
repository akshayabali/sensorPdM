import PCF8591 as ADC
import socket
UDP_IP = "192.168.43.147"
UDP_PORT = 5005

def setup():
	ADC.setup(0x48)
      
      

def loop():
      print "Connected"
      sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
      while True:
            MESSAGE = str(ADC.read(0)) + " " + str(ADC.read(1)) + " " + str(ADC.read(2)) + " " + str(ADC.read(3)) 
            #MESSAGE = str(ADC.read(3)) 
            #print (MESSAGE)
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def destroy():
	ADC.write(0)

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
