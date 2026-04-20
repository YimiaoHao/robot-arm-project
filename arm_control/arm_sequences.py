import time
from arm_control.arm_basic import (
    move_joint_1,
    move_joint_2,
    move_joint_3,
    move_joint_4,
    open_gripper,
    close_gripper,
)
from arm_control.config import (
    SAFE_RETRACT,
    PRE_PICK,
    CENTER_PICK,
    POST_PICK_LIFT,
    PRE_PLACE,
    PLACE_POS,
    HOME_J1,
    HOME_J2,
    HOME_J3,
    HOME_J4,
    GRIPPER_PICK_OPEN,
    GRIPPER_RELEASE_OPEN,
)


def move_pose(pose, name):
    print(f"Moving to {name}: {pose}")
    move_joint_1(pose["j1"])
    time.sleep(0.8)
    move_joint_2(pose["j2"])
    time.sleep(0.8)
    move_joint_3(pose["j3"])
    time.sleep(0.8)
    move_joint_4(pose["j4"])
    time.sleep(1.0)


def pick_sequence(target_zone="CENTER"):
    print("Pick sequence started.")

    open_gripper(GRIPPER_PICK_OPEN)
    time.sleep(1)

    move_pose(SAFE_RETRACT, "SAFE_RETRACT")
    move_pose(PRE_PICK, "PRE_PICK")
    move_pose(CENTER_PICK, "CENTER_PICK")

    close_gripper()
    time.sleep(1)

    move_pose(POST_PICK_LIFT, "POST_PICK_LIFT")

    print("Pick sequence completed.")


def place_sequence():
    print("Place sequence started.")

    move_pose(PRE_PLACE, "PRE_PLACE")
    move_pose(PLACE_POS, "PLACE_POS")

    open_gripper(GRIPPER_RELEASE_OPEN)
    time.sleep(1)

    print("Place sequence completed.")


def return_home_sequence():
    print("Return-home sequence started.")

    move_pose(SAFE_RETRACT, "SAFE_RETRACT")

    move_joint_1(HOME_J1)
    time.sleep(0.8)
    move_joint_2(HOME_J2)
    time.sleep(0.8)
    move_joint_3(HOME_J3)
    time.sleep(0.8)
    move_joint_4(HOME_J4)
    time.sleep(0.8)

    print("Returned to home safely.")