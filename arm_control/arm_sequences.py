from arm_control.arm_basic import (
    move_joint_2,
    move_joint_3,
    move_joint_4,
    open_gripper,
    close_gripper,
)
from arm_control.config import (
    SAFE_RETRACT,
    HOME_J2,
    HOME_J3,
    HOME_J4,
    LEFT_PICK,
    CENTER_PICK,
    RIGHT_PICK,
    PLACE_POS,
)
import time


def _get_pick_pose(target_zone):
    if not target_zone:
        return CENTER_PICK

    zone = str(target_zone).lower()

    if zone == "left":
        return LEFT_PICK
    elif zone == "right":
        return RIGHT_PICK
    else:
        return CENTER_PICK


def pick_sequence(target_zone):
    pick_pose = _get_pick_pose(target_zone)

    print(f"Pick sequence started for zone: {target_zone}")

    open_gripper()
    time.sleep(0.8)

    # go to safer retract pose first
    move_joint_4(SAFE_RETRACT["j4"])
    time.sleep(0.6)

    move_joint_3(SAFE_RETRACT["j3"])
    time.sleep(0.6)

    move_joint_2(pick_pose["j2"])
    time.sleep(0.6)

    # descend to pick pose
    move_joint_3(pick_pose["j3"])
    time.sleep(0.6)

    move_joint_4(pick_pose["j4"])
    time.sleep(0.8)

    close_gripper()
    time.sleep(1.0)

    # retract after grabbing
    move_joint_4(SAFE_RETRACT["j4"])
    time.sleep(0.6)

    move_joint_3(SAFE_RETRACT["j3"])
    time.sleep(0.6)

    print("Pick sequence completed.")


def place_sequence():
    print("Place sequence started.")

    move_joint_2(PLACE_POS["j2"])
    time.sleep(0.6)

    move_joint_3(PLACE_POS["j3"])
    time.sleep(0.6)

    move_joint_4(PLACE_POS["j4"])
    time.sleep(0.8)

    open_gripper()
    time.sleep(1.0)

    # retract after release
    move_joint_4(SAFE_RETRACT["j4"])
    time.sleep(0.6)

    move_joint_3(SAFE_RETRACT["j3"])
    time.sleep(0.6)

    print("Place sequence completed.")


def return_home_sequence():
    print("Return-home sequence started.")

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