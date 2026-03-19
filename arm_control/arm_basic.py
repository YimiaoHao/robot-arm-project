import time
from arm_control.config import (
    COM_PORT,
    HOME_J2, HOME_J3, HOME_J4,
    GRIPPER_OPEN, GRIPPER_CLOSE,
    J2_MIN, J2_MAX,
    J3_MIN, J3_MAX,
    J4_MIN, J4_MAX,
)

try:
    import lss
    import lss_const as lssc
except ImportError:
    lss = None
    lssc = None


servo2 = None
servo3 = None
servo4 = None
servo5 = None


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def connect_arm():
    global servo2, servo3, servo4, servo5

    if lss is None or lssc is None:
        print("LSS library not installed yet. Use lab machine or install the required robot libraries first.")
        return False

    lss.initBus(COM_PORT, lssc.LSS_DefaultBaud)

    servo2 = lss.LSS(2)
    servo3 = lss.LSS(3)
    servo4 = lss.LSS(4)
    servo5 = lss.LSS(5)

    print(f"Connected to robotic arm on {COM_PORT}")
    return True


def move_joint_2(position):
    if servo2 is None:
        print("Servo 2 not connected")
        return
    safe_pos = clamp(position, J2_MIN, J2_MAX)
    servo2.move(safe_pos)
    time.sleep(0.3)


def move_joint_3(position):
    if servo3 is None:
        print("Servo 3 not connected")
        return
    safe_pos = clamp(position, J3_MIN, J3_MAX)
    servo3.move(safe_pos)
    time.sleep(0.3)


def move_joint_4(position):
    if servo4 is None:
        print("Servo 4 not connected")
        return
    safe_pos = clamp(position, J4_MIN, J4_MAX)
    servo4.move(safe_pos)
    time.sleep(0.3)


def open_gripper():
    if servo5 is None:
        print("Gripper not connected")
        return
    servo5.move(GRIPPER_OPEN)
    time.sleep(0.5)


def close_gripper():
    if servo5 is None:
        print("Gripper not connected")
        return
    servo5.move(GRIPPER_CLOSE)
    time.sleep(0.5)


def go_home():
    move_joint_2(HOME_J2)
    move_joint_3(HOME_J3)
    move_joint_4(HOME_J4)
    print("Returned to home position")


def safe_stop():
    print("Emergency stop triggered")
    # Expand later if teacher library provides a better stop method