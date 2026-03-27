from arm_control.arm_basic import connect_arm, open_gripper, close_gripper
import time

if connect_arm():
    print("Open gripper")
    open_gripper()
    time.sleep(2)

    print("Close gripper")
    close_gripper()
    time.sleep(2)

    print("Open gripper again")
    open_gripper()
    time.sleep(2)
else:
    print("Failed to connect arm")