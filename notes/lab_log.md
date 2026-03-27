# Lab Log

## Lab Session
- Date: 20/03/2026
- Team members present: Yimiao, Hafza

## Hardware Setup
- FlowArm worked successfully
- Real serial port confirmed as COM9
- Python LSS library was added to the project
- Python connection to the arm on COM9 was successful

## What We Tested
- teacher_samples/testLEDs.py
- teacher_samples/testRanges.py
- test_arm_minimal.py
- test_pick_center_only.py
- test_place_only.py
- test_return_home_only.py
- test_return_home_safe.py
- test_pick_place_real.py

## What Worked
- testLEDs.py passed
- testRanges.py passed on COM9
- Minimal arm test passed
- Pick-only test passed
- Place-only test passed
- Camera and red-object detection had already been tested successfully before lab

## What Did Not Work Smoothly
- During the first run of testRanges.py, one collision/contact-like sound was heard once
- test_return_home_only.py caused collision/contact and a red error indication
- test_pick_place_real.py was not stable because the return-home part was too aggressive

## Current Conclusion
- Pick and place are mostly workable
- The main issue is the return-home path / home configuration
- A safer retract-and-home strategy is needed before running the full sequence again

## Safety Notes
- The workspace must remain clear
- Joint 4 should be treated conservatively
- The extreme end of the sample range should not be assumed safe for normal project use

## Screenshots Taken
- FlowArm working on COM9
- testLEDs.py success
- testRanges.py terminal output
- minimal arm test success
- fixed-sequence / return-home test observations

## Next Actions
- Refine config.py with conservative real-arm values
- Fix return_home_sequence()
- Re-test safe return-home only
- Re-test full fixed sequence
- Then move to main_pick_place.py on real hardware