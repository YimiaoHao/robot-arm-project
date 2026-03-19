# Issues and Fixes

## Issue 1
- Problem: main_pick_place.py could not import pick_sequence at first.
- Cause: arm_sequences.py did not match the expected function structure.
- Fix: rewrote arm_sequences.py and saved the correct functions.
- Result: the import problem was solved and the main program started successfully.

## Issue 2
- Problem: robotic arm actions could not run locally.
- Cause: the LSS library was not installed locally and no real robot was connected.
- Fix: kept the system running in vision test mode.
- Result: the software logic could still be tested safely without crashing.

## Issue 3
- Problem: emergency stop message appeared multiple times.
- Cause: repeated key input / no debounce yet.
- Fix: marked as a later optimisation task.
- Result: emergency stop logic exists, but it should be improved later.