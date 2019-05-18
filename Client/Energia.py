import serial
import csv
import time

serialPort = serial.Serial(port="COM4", baudrate=500000,
                           bytesize=8, timeout=None, stopbits=serial.STOPBITS_ONE)

x = []
y = []

while True:
    try:
        bytesToRead = serialPort.inWaiting()
        text = serialPort.readline(bytesToRead)
        # text = serialPort.readline()
        a, b = text.decode("utf-8").split(",")
        print(a, b)
        with open("test_data.csv", "a") as f:
            writer = csv.writer(f, delimiter=",")
            # writer.writerow([time.time(), a])
            writer.writerow([a])
    except:
        pass

