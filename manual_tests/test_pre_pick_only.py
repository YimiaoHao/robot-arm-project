from arm_control.arm_basic import connect_arm, go_home, open_gripper, move_joint_2, move_joint_3, move_joint_4
from arm_control.config import PRE_PICK
import time

print("=== Test PRE_PICK only ===")

if not connect_arm():
    raise SystemExit("Connect failed")

go_home()
time.sleep(1)

open_gripper()
time.sleep(1)

print("Moving to PRE_PICK:", PRE_PICK)
move_joint_2(PRE_PICK["j2"])
time.sleep(1)

move_joint_3(PRE_PICK["j3"])
time.sleep(1)

move_joint_4(PRE_PICK["j4"])
time.sleep(1)

print("PRE_PICK test finished. Observe whether the pose is correct and safe.")