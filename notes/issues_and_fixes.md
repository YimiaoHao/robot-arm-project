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