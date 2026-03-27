COM_PORT = "COM9"

# safer temporary home
HOME_J2 = -850
HOME_J3 = 800
HOME_J4 = 100

# gripper: keep conservative first
GRIPPER_OPEN = 0
GRIPPER_CLOSE = -220

LEFT_PICK = {"j2": -820, "j3": 720, "j4": 120}
SAFE_RETRACT = {"j2": -610, "j3": 689, "j4": 373}
CENTER_PICK = {"j2": -1029, "j3": 894, "j4": 372}
RIGHT_PICK = {"j2": -780, "j3": 680, "j4": 80}

PRE_PICK = {"j2": -1029, "j3": 760, "j4": 373}
PLACE_POS = {"j2": -730, "j3": 650, "j4": 100}

J2_MIN = -1100
J2_MAX = -550

J3_MIN = 250
J3_MAX = 950

J4_MIN = -500
J4_MAX = 450