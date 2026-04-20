# ===== serial port =====
COM_PORT = "COM10"
# ===== gripper =====
# 普通默认张开 / 闭合
GRIPPER_OPEN = -83
GRIPPER_CLOSE = -40

# 抓取前张开得更大一点，释放时张开到最新测的值
GRIPPER_PICK_OPEN = -159
GRIPPER_RELEASE_OPEN = -83

# ===== current-device poses =====
START_POSE = {"j1": 3, "j2": -1143, "j3": 879, "j4": 634}
SAFE_RETRACT = {"j1": 3, "j2": -291, "j3": 597, "j4": -111}

PRE_PICK = {"j1": 2, "j2": 270, "j3": 90, "j4": 350}
CENTER_PICK = {"j1": 0, "j2": 271, "j3": 98, "j4": 341}

POST_PICK_LIFT = {"j1": 0, "j2": -35, "j3": 75, "j4": 363}

PRE_PLACE = {"j1": -461, "j2": -180, "j3": 202, "j4": 529}
PLACE_POS = {"j1": -461, "j2": -180, "j3": 202, "j4": 529}

# ===== home aliases =====
HOME_J1 = START_POSE["j1"]
HOME_J2 = START_POSE["j2"]
HOME_J3 = START_POSE["j3"]
HOME_J4 = START_POSE["j4"]

# ===== temporary limits for this device/session =====
J1_MIN = -600
J1_MAX = 100

J2_MIN = -1200
J2_MAX = 400

J3_MIN = 0
J3_MAX = 950

J4_MIN = -200
J4_MAX = 700