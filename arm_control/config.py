COM_PORT = "COM9"

# safer temporary home
HOME_J2 = -850
HOME_J3 = 800
HOME_J4 = 100

# gripper: keep conservative first
GRIPPER_OPEN = 0
GRIPPER_CLOSE = -220

# only trust one working pick pose first
LEFT_PICK = {"j2": -820, "j3": 720, "j4": 120}
CENTER_PICK = {"j2": -680, "j3": 580, "j4": 20}
RIGHT_PICK = {"j2": -780, "j3": 680, "j4": 80}

SAFE_RETRACT = {"j2": -780, "j3": 720, "j4": 80}

PLACE_POS = {"j2": -730, "j3": 650, "j4": 100}

# conservative limits
J2_MIN = -900
J2_MAX = -550

J3_MIN = 250
J3_MAX = 850

# keep far away from the -800 extreme for now
J4_MIN = -500
J4_MAX = 220