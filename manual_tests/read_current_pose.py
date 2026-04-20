import lss
import lss_const as lssc
from arm_control.config import COM_PORT

def main():
    lss.initBus(COM_PORT, lssc.LSS_DefaultBaud)

    servo1 = lss.LSS(1)
    servo2 = lss.LSS(2)
    servo3 = lss.LSS(3)
    servo4 = lss.LSS(4)
    servo5 = lss.LSS(5)

    print("Reading current servo positions...")
    print("J1 =", servo1.getPosition())
    print("J2 =", servo2.getPosition())
    print("J3 =", servo3.getPosition())
    print("J4 =", servo4.getPosition())
    print("Gripper =", servo5.getPosition())

if __name__ == "__main__":
    main()