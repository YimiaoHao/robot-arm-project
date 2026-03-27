from arm_control.arm_basic import connect_arm
from arm_control.arm_sequences import pick_sequence, place_sequence, return_home_sequence
import time

print("Starting fixed sequence test...")

connected = connect_arm()
if not connected:
    print("Failed to connect arm.")
    raise SystemExit

print("Running CENTER pick sequence...")
pick_sequence("CENTER")
time.sleep(1)

print("Running place sequence...")
place_sequence()
time.sleep(1)

print("Returning home...")
return_home_sequence()

print("Fixed sequence test complete.")