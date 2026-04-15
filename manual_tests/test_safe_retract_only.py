from arm_control.arm_basic import connect_arm, open_gripper, move_joint_2, move_joint_3, move_joint_4
from arm_control.config import SAFE_RETRACT
import time

print("Test SAFE_RETRACT only")

if not connect_arm():
    raise SystemExit("Connect failed")

open_gripper()
time.sleep(1)

move_joint_2(SAFE_RETRACT["j2"])
time.sleep(1)
move_joint_3(SAFE_RETRACT["j3"])
time.sleep(1)
move_joint_4(SAFE_RETRACT["j4"])
time.sleep(1)

print("SAFE_RETRACT test finished.")