from arm_control.arm_basic import connect_arm, move_joint_2, move_joint_3, move_joint_4, open_gripper
from arm_control.config import CENTER_PICK
import time

print("Preview CENTER_PICK pose only")

if not connect_arm():
    raise SystemExit("Connect failed")

print("Opening gripper...")
open_gripper()
time.sleep(1)

print("Moving to CENTER_PICK pose:", CENTER_PICK)

move_joint_2(CENTER_PICK["j2"])
time.sleep(1.2)

move_joint_3(CENTER_PICK["j3"])
time.sleep(1.2)

move_joint_4(CENTER_PICK["j4"])
time.sleep(1.2)

print("Pose preview complete. Observe the final arm position.")