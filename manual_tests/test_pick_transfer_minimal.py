from arm_control.arm_basic import connect_arm
from arm_control.arm_sequences import pick_sequence, place_sequence

print("Test minimal pick-transfer sequence")

if not connect_arm():
    raise SystemExit("Connect failed")

pick_sequence("CENTER")
place_sequence()

print("Minimal pick-transfer test finished.")