from arm_control.arm_basic import connect_arm
from arm_control.arm_sequences import return_home_sequence
import time

print("Test RETURN HOME only")

connected = connect_arm()
if not connected:
    raise SystemExit("Connect failed")

return_home_sequence()
time.sleep(1)
print("Done")