from arm_control.arm_basic import connect_arm
from arm_control.arm_sequences import pick_sequence, place_sequence, return_home_sequence
import time

print("Starting real pick-place test...")

connected = connect_arm()
if not connected:
    print("Failed to connect arm.")
    raise SystemExit

print("Pick CENTER...")
pick_sequence("CENTER")
time.sleep(1)

print("Place...")
place_sequence()
time.sleep(1)

print("Return home...")
return_home_sequence()

print("Real pick-place test complete.")