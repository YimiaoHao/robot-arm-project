from arm_control.arm_basic import (
    move_joint_2,
    move_joint_3,
    move_joint_4,
    open_gripper,
    close_gripper,
    go_home,
)
from arm_control.config import LEFT_PICK, CENTER_PICK, RIGHT_PICK, PLACE_POS


def pick_sequence(zone):
    open_gripper()

    if zone == "LEFT":
        target = LEFT_PICK
    elif zone == "CENTER":
        target = CENTER_PICK
    elif zone == "RIGHT":
        target = RIGHT_PICK
    else:
        print("Unknown zone")
        return

    move_joint_2(target["j2"])
    move_joint_3(target["j3"])
    move_joint_4(target["j4"])
    close_gripper()


def place_sequence():
    move_joint_2(PLACE_POS["j2"])
    move_joint_3(PLACE_POS["j3"])
    move_joint_4(PLACE_POS["j4"])
    open_gripper()


def return_home_sequence():
    go_home()