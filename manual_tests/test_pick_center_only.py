from arm_control.arm_basic import connect_arm
from arm_control.arm_sequences import pick_sequence
import time

print("Test CENTER pick only")

connected = connect_arm()
if not connected:
    raise SystemExit("Connect failed")

pick_sequence("CENTER")
time.sleep(1)
print("Done")