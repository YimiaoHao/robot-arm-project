from arm_control.arm_basic import connect_arm
from arm_control.arm_sequences import pick_sequence

print("Test CENTER pick only")

if not connect_arm():
    raise SystemExit("Connect failed")

pick_sequence("CENTER")

print("Pick-only test finished.")