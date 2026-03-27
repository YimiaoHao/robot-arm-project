import serial
import time

# 1. Open the connection
# Check your Device Manager to see if it is COM9, COM3, etc.
# The baud rate for SSC-32 is usually 9600 or 115200.
ser = serial.Serial('COM9', 9600, timeout=1)

def move_flat():
    # This command tells the arm to go to the "Flat" position
    # #0 is Base, #1 is Shoulder, #2 is Elbow, #3 is Wrist
    # P1500 is the pulse width (center)
    # T1000 means "take 1000 milliseconds (1 second) to get there"
    command = "#0 P1500 #1 P1500 #2 P1500 #3 P1500 #4 P1500 T1000\r"
   
    print("Initializing arm to flat position...")
    ser.write(command.encode())
    time.sleep(2)

move_flat()
ser.close()