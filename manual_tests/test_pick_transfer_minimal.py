from arm_control.arm_basic import (
    connect_arm,
    move_joint_2,
    move_joint_3,
    move_joint_4,
    open_gripper,
    close_gripper,
)
from arm_control.config import PRE_PICK, POST_PICK_LIFT, PRE_PLACE
import time


def move_pose(pose, name):
    print(f"Moving to {name}: {pose}")
    move_joint_2(pose["j2"])
    time.sleep(0.8)
    move_joint_3(pose["j3"])
    time.sleep(0.8)
    move_joint_4(pose["j4"])
    time.sleep(1.0)


print("Test minimal pick-transfer sequence")

if not connect_arm():
    raise SystemExit("Connect failed")

# 1. open gripper first
open_gripper()
time.sleep(1)

# 2. go to pick pose
move_pose(PRE_PICK, "PRE_PICK")

# 3. close gripper to grab
close_gripper()
time.sleep(1)

# 4. lift object
move_pose(POST_PICK_LIFT, "POST_PICK_LIFT")

# 5. move to place area
move_pose(PRE_PLACE, "PRE_PLACE")

# 6. release object
open_gripper()
time.sleep(1)

print("Minimal pick-transfer test finished.")