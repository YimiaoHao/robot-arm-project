# ===== serial port =====
COM_PORT = "COM10"   # 如果现场实际不是 COM10，只改这一行

# ===== gripper =====
# 抓取前张开
GRIPPER_PICK_OPEN = -143
# 抓住物体
GRIPPER_CLOSE = -51
# 放下时张开
GRIPPER_RELEASE_OPEN = -143

# 为了兼容 arm_basic.py 里的默认值
GRIPPER_OPEN = GRIPPER_RELEASE_OPEN

# ===== current-device poses =====
# 1. 初始位置
START_POSE = {"j1": 0, "j2": -1199, "j3": 884, "j4": 10}

# 2. 轻轻抬起位置
SAFE_RETRACT = {"j1": 1, "j2": -520, "j3": 748, "j4": 10}

# 3. 前倾位置
LEAN_FORWARD = {"j1": 1, "j2": -7, "j3": 236, "j4": 13}

# 4. 爪子下垂
WRIST_DOWN = {"j1": 3, "j2": 17, "j3": 206, "j4": 506}

# 5. 下降微调
LOWER_FINE_TUNE = {"j1": 1, "j2": 230, "j3": -73, "j4": 596}

# 6. 准备抓取（张开）
PRE_PICK = {"j1": 1, "j2": 325, "j3": -35, "j4": 463}

# 7. 爪子合上后的抓取位
CENTER_PICK = {"j1": 1, "j2": 324, "j3": -36, "j4": 462}

# 8. 抬起
POST_PICK_LIFT = {"j1": 1, "j2": 185, "j3": -85, "j4": 656}

# 9. 准备放下（拐弯）
PRE_PLACE = {"j1": -420, "j2": 53, "j3": 76, "j4": 626}

# 10. 放下位
PLACE_POS = {"j1": -420, "j2": 56, "j3": 73, "j4": 635}

# 11. 返回
RETURN_POSE = {"j1": 4, "j2": 76, "j3": 49, "j4": 638}

# 12. 收回手臂
RETRACT_ARM = {"j1": 2, "j2": -519, "j3": 625, "j4": 652}

# ===== home aliases =====
HOME_J1 = START_POSE["j1"]
HOME_J2 = START_POSE["j2"]
HOME_J3 = START_POSE["j3"]
HOME_J4 = START_POSE["j4"]

# ===== temporary limits for this device/session =====
J1_MIN = -600
J1_MAX = 100

J2_MIN = -1300
J2_MAX = 400

J3_MIN = -150
J3_MAX = 950

J4_MIN = 0
J4_MAX = 700