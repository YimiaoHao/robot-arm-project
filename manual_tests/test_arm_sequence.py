from arm_control.arm_basic import connect_arm
from arm_control.arm_sequences import pick_sequence, place_sequence, return_home_sequence

print("Test full fixed sequence")

if not connect_arm():
    raise SystemExit("Connect failed")

pick_sequence("CENTER")
place_sequence()
return_home_sequence()

print("Full sequence test finished.")