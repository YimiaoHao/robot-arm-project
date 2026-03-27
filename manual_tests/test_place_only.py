from arm_control.arm_basic import connect_arm
from arm_control.arm_sequences import place_sequence
import time

print("Test PLACE only")

connected = connect_arm()
if not connected:
    raise SystemExit("Connect failed")

place_sequence()
time.sleep(1)
print("Done")