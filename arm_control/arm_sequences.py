from arm_control.arm_basic import (
    move_joint_2, move_joint_3, move_joint_4,
    open_gripper, close_gripper
)
from arm_control.config import CENTER_PICK, PLACE_POS, SAFE_RETRACT, HOME_J2, HOME_J3, HOME_J4
import time


def pick_sequence(target_zone="CENTER"):
    pick_pose = CENTER_PICK
    print(f"Using fixed pick pose: {pick_pose}")

    open_gripper()
    time.sleep(0.8)

    move_joint_4(SAFE_RETRACT["j4"])
    time.sleep(0.6)
    move_joint_3(SAFE_RETRACT["j3"])
    time.sleep(0.6)

    move_joint_2(pick_pose["j2"])
    time.sleep(0.8)
    move_joint_3(pick_pose["j3"])
    time.sleep(0.8)
    move_joint_4(pick_pose["j4"])
    time.sleep(1.0)

    close_gripper()
    time.sleep(1.0)

    move_joint_4(SAFE_RETRACT["j4"])
    time.sleep(0.6)
    move_joint_3(SAFE_RETRACT["j3"])
    time.sleep(0.6)


def place_sequence():
    print(f"Using fixed place pose: {PLACE_POS}")

    move_joint_2(PLACE_POS["j2"])
    time.sleep(0.8)
    move_joint_3(PLACE_POS["j3"])
    time.sleep(0.8)
    move_joint_4(PLACE_POS["j4"])
    time.sleep(1.0)

    open_gripper()
    time.sleep(1.0)

    move_joint_4(SAFE_RETRACT["j4"])
    time.sleep(0.6)
    move_joint_3(SAFE_RETRACT["j3"])
    time.sleep(0.6)


def return_home_sequence():
    move_joint_4(SAFE_RETRACT["j4"])
    time.sleep(0.6)
    move_joint_3(SAFE_RETRACT["j3"])
    time.sleep(0.6)
    move_joint_2(SAFE_RETRACT["j2"])
    time.sleep(0.6)

    move_joint_2(HOME_J2)
    time.sleep(0.6)
    move_joint_3(HOME_J3)
    time.sleep(0.6)
    move_joint_4(HOME_J4)
    time.sleep(0.8)

    print("Returned to home safely.")