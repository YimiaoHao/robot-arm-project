# ===== serial port =====
COM_PORT = "COM9"   # 现场如果不是 COM9，就改成真实端口

# ===== gripper (temporary, update after re-measuring) =====
GRIPPER_OPEN = -99
GRIPPER_CLOSE = -31

# ===== current working poses (j1 is temporary now; re-measure later) =====
START_POSE = {"j1": 0, "j2": -926, "j3": 919, "j4": 302}
SAFE_RETRACT = {"j1": 0, "j2": -723, "j3": 463, "j4": 564}
PRE_PICK = {"j1": 0, "j2": 267, "j3": 41, "j4": 458}
CENTER_PICK = {"j1": 0, "j2": 297, "j3": 61, "j4": 408}
POST_PICK_LIFT = {"j1": 0, "j2": 126, "j3": 19, "j4": 623}
PRE_PLACE = {"j1": 0, "j2": 23, "j3": 133, "j4": 613}
PLACE_POS = {"j1": 0, "j2": 23, "j3": 133, "j4": 613}

# ===== home aliases (keep these names so old imports do not break) =====
HOME_J1 = START_POSE["j1"]
HOME_J2 = START_POSE["j2"]
HOME_J3 = START_POSE["j3"]
HOME_J4 = START_POSE["j4"]

# ===== temporary safe limits (broad enough for measurement) =====
J1_MIN = -1200
J1_MAX = 1200

J2_MIN = -1200
J2_MAX = 600

J3_MIN = -300
J3_MAX = 1200

J4_MIN = 200
J4_MAX = 900