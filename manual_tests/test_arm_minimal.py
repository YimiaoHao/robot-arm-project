from arm_control.arm_basic import connect_arm, go_home, open_gripper, close_gripper
import time

print("Starting minimal arm test...")

connected = connect_arm()
if not connected:
    print("Failed to connect arm.")
    raise SystemExit

print("Connected successfully.")

print("Going home...")
go_home()
time.sleep(1)

print("Opening gripper...")
open_gripper()
time.sleep(1)

print("Closing gripper...")
close_gripper()
time.sleep(1)

print("Opening gripper again...")
open_gripper()
time.sleep(1)

print("Returning home again...")
go_home()

print("Minimal arm test complete.")