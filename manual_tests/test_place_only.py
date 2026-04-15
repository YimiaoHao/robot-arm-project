from arm_control.arm_basic import connect_arm
from arm_control.arm_sequences import place_sequence

print("Test place only")

if not connect_arm():
    raise SystemExit("Connect failed")

place_sequence()

print("Place-only test finished.")