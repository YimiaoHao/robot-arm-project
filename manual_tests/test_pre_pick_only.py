from arm_control.arm_basic import connect_arm, open_gripper, move_joint_2, move_joint_3, move_joint_4
from arm_control.config import SAFE_RETRACT, PRE_PICK
import time

print("Test SAFE_RETRACT -> PRE_PICK")

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

move_joint_2(PRE_PICK["j2"])
time.sleep(1)
move_joint_3(PRE_PICK["j3"])
time.sleep(1)
move_joint_4(PRE_PICK["j4"])
time.sleep(1)

print("PRE_PICK test finished.")