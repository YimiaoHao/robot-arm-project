from arm_control.arm_basic import connect_arm, go_home, move_joint_2, move_joint_3, move_joint_4
import lss
import time

TARGET = {"j2": -1029, "j3": 894, "j4": 372}

print("Verify saved pick candidate")

if not connect_arm():
    raise SystemExit("Connect failed")

print("Going home first...")
go_home()
time.sleep(2)

print("Moving to target:", TARGET)
move_joint_2(TARGET["j2"])
time.sleep(1.2)

move_joint_3(TARGET["j3"])
time.sleep(1.2)

move_joint_4(TARGET["j4"])
time.sleep(1.2)

servo2 = lss.LSS(2)
servo3 = lss.LSS(3)
servo4 = lss.LSS(4)

print("Target J2 =", TARGET["j2"], "| Actual J2 =", servo2.getPosition(), "| Status =", servo2.getStatus())
print("Target J3 =", TARGET["j3"], "| Actual J3 =", servo3.getPosition(), "| Status =", servo3.getStatus())
print("Target J4 =", TARGET["j4"], "| Actual J4 =", servo4.getPosition(), "| Status =", servo4.getStatus())