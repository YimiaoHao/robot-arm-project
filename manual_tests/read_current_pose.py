import lss
import lss_const as lssc

PORT = "COM9"   # 以你现场真实端口为准

def main():
    lss.initBus(PORT, lssc.LSS_DefaultBaud)

    servo2 = lss.LSS(2)
    servo3 = lss.LSS(3)
    servo4 = lss.LSS(4)
    servo5 = lss.LSS(5)

    print("Reading current servo positions...")
    print("J2 =", servo2.getPosition())
    print("J3 =", servo3.getPosition())
    print("J4 =", servo4.getPosition())
    print("Gripper =", servo5.getPosition())

if __name__ == "__main__":
    main()