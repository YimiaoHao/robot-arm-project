from arm_control.arm_basic import connect_arm, go_home, open_gripper, close_gripper
import time

print("=== Minimal arm test ===")

if not connect_arm():
    raise SystemExit("Connect failed")

open_gripper()
time.sleep(1)

close_gripper()
time.sleep(1)

open_gripper()
time.sleep(1)

go_home()
time.sleep(1)

print("Minimal arm test finished.")