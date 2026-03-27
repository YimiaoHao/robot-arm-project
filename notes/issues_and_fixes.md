# Issues and Fixes

## Issue 1
- Problem: Python sample code could not run at first because lss and lss_const were missing
- Cause: required LSS Python library files were not yet available in the project
- Fix: downloaded the official Lynxmotion LSS Python library and copied lss.py and lss_const.py into the project
- Result: Python could import the LSS library successfully

## Issue 2
- Problem: teacher_samples/testLEDs.py could not open COM9 at one stage
- Cause: the serial port was already occupied by FlowArm
- Fix: closed FlowArm completely before running Python scripts
- Result: testLEDs.py ran successfully

## Issue 3
- Problem: one collision/contact-like sound was heard during the first run of testRanges.py
- Cause: exact value was not identified, likely near a more extreme part of the tested sweep
- Fix: repeated the test and recorded the issue as an intermittent safety observation
- Result: the issue did not repeat immediately, but the extreme range is now treated conservatively

## Issue 4
- Problem: full-sequence movement tests caused collision/contact and red error indication
- Cause: the movement sequence was too aggressive, especially in the return-home part
- Fix: split the full sequence into smaller tests: pick only, place only, return-home only
- Result: the main problem was isolated to the return-home stage

## Issue 5
- Problem: return-home behaviour caused collision/contact and red indicator
- Cause: the direct path back to home appears unsafe or the current home configuration is too aggressive
- Fix: introduced a safer return-home testing approach and planned conservative configuration updates
- Result: return-home is now identified as the main remaining technical issue

## Issue 6
- Problem: main_pick_place.py could detect the red object, but the arm did not automatically move to the object correctly and did not complete a full automatic pick-and-place
- Cause: the remaining issue appears to be motion path / pose calibration rather than basic camera detection
- Fix: changed the short-term strategy to a simpler fixed-position workflow (fixed pick point + fixed place point) instead of relying on multiple zones first
- Result: the project direction is now more realistic and easier to calibrate safely on real hardware

## Issue 7
- Problem: the arm still did not reach a correct low pick position when tested from code
- Cause: the current preset pick pose was not yet properly calibrated against the real arm
- Fix: used FlowArm to manually move the arm to a low pose that could pick the object, then read the real servo values in Python
- Result: a validated candidate pick pose was captured:
  - J2 = -1029
  - J3 = 894
  - J4 = 372

## Issue 8
- Problem: direct movement to the low pick pose caused collision/contact behaviour
- Cause: the final low pick pose may be workable, but the direct path to reach it is too aggressive and unsafe
- Fix: introduced the idea of an intermediate safe pose before descending
- Result: a safer higher pose was identified and captured as a candidate SAFE_RETRACT:
  - J2 = -610
  - J3 = 689
  - J4 = 373

## Issue 9
- Problem: duplicate definitions were found in the control code (including repeated move_joint_3 / move_joint_4 style logic and repeated SAFE_RETRACT values in configuration work)
- Cause: code had evolved through multiple quick test edits and old versions were not fully cleaned up
- Fix: planned cleanup so that only one active definition is kept for each movement function and only one active SAFE_RETRACT value is kept in config.py
- Result: configuration is now being simplified around one fixed pick pose and one fixed safe intermediate pose