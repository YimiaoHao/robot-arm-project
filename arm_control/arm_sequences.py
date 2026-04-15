import time
from arm_control.arm_basic import (
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
    PRE_PLACE,
    PLACE_POS,
    HOME_J2,
    HOME_J3,
    HOME_J4,
)


def pick_sequence(target_zone="CENTER"):
    print("Pick sequence started.")

    open_gripper()
    time.sleep(0.8)

    # 1) go to safe retract first
    move_joint_2(SAFE_RETRACT["j2"])
    time.sleep(0.8)
    move_joint_3(SAFE_RETRACT["j3"])
    time.sleep(0.8)
    move_joint_4(SAFE_RETRACT["j4"])
    time.sleep(0.8)

    # 2) move above the object
    move_joint_2(PRE_PICK["j2"])
    time.sleep(0.8)
    move_joint_3(PRE_PICK["j3"])
    time.sleep(0.8)
    move_joint_4(PRE_PICK["j4"])
    time.sleep(0.8)

    # 3) descend to low pick pose
    move_joint_2(CENTER_PICK["j2"])
    time.sleep(0.8)
    move_joint_3(CENTER_PICK["j3"])
    time.sleep(0.8)
    move_joint_4(CENTER_PICK["j4"])
    time.sleep(1.0)

    close_gripper()
    time.sleep(1.0)

    # 4) lift back up
    move_joint_2(PRE_PICK["j2"])
    time.sleep(0.8)
    move_joint_3(PRE_PICK["j3"])
    time.sleep(0.8)
    move_joint_4(PRE_PICK["j4"])
    time.sleep(0.8)

    # 5) return to safe retract
    move_joint_2(SAFE_RETRACT["j2"])
    time.sleep(0.8)
    move_joint_3(SAFE_RETRACT["j3"])
    time.sleep(0.8)
    move_joint_4(SAFE_RETRACT["j4"])
    time.sleep(0.8)

    print("Pick sequence completed.")


def place_sequence():
    print("Place sequence started.")

    # 1) move above place area
    move_joint_2(PRE_PLACE["j2"])
    time.sleep(0.8)
    move_joint_3(PRE_PLACE["j3"])
    time.sleep(0.8)
    move_joint_4(PRE_PLACE["j4"])
    time.sleep(0.8)

    # 2) descend to place pose
    move_joint_2(PLACE_POS["j2"])
    time.sleep(0.8)
    move_joint_3(PLACE_POS["j3"])
    time.sleep(0.8)
    move_joint_4(PLACE_POS["j4"])
    time.sleep(1.0)

    open_gripper()
    time.sleep(1.0)

    # 3) lift back up
    move_joint_2(PRE_PLACE["j2"])
    time.sleep(0.8)
    move_joint_3(PRE_PLACE["j3"])
    time.sleep(0.8)
    move_joint_4(PRE_PLACE["j4"])
    time.sleep(0.8)

    # 4) return to safe retract
    move_joint_2(SAFE_RETRACT["j2"])
    time.sleep(0.8)
    move_joint_3(SAFE_RETRACT["j3"])
    time.sleep(0.8)
    move_joint_4(SAFE_RETRACT["j4"])
    time.sleep(0.8)

    print("Place sequence completed.")


def return_home_sequence():
    print("Return-home sequence started.")

    move_joint_2(SAFE_RETRACT["j2"])
    time.sleep(0.8)
    move_joint_3(SAFE_RETRACT["j3"])
    time.sleep(0.8)
    move_joint_4(SAFE_RETRACT["j4"])
    time.sleep(0.8)

    move_joint_2(HOME_J2)
    time.sleep(0.8)
    move_joint_3(HOME_J3)
    time.sleep(0.8)
    move_joint_4(HOME_J4)
    time.sleep(0.8)

    print("Returned to home safely.")