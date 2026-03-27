# Lab Log

## Lab Session 1
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

## Next Actions
- Refine config.py with conservative real-arm values
- Fix return_home_sequence()
- Re-test safe return-home only
- Re-test full fixed sequence
- Then move to main_pick_place.py on real hardware

## Lab Session 2
- Date: 27/03/2026
- Team members present: Yimiao, Hafza

## What We Tested
- main_pick_place.py on real hardware
- FlowArm manual pose adjustment for fixed pick position
- Python read_current_pose.py for real servo-value capture
- Preliminary safe intermediate pose identification

## What Worked
- main_pick_place.py could detect the red object in the camera view
- The gripper action could be triggered during the integrated test
- A manually adjusted low pick pose was found in FlowArm that appeared able to pick the object from the table
- The servo values of that low pick pose were read successfully in Python:
  - J2 = -1029
  - J3 = 894
  - J4 = 372
- A higher and safer intermediate pose was also identified and read successfully:
  - J2 = -610
  - J3 = 689
  - J4 = 373

## What Did Not Work Smoothly
- In the integrated main_pick_place.py test, the arm did not automatically move correctly to pick the object
- The arm movement was still too limited in practice and did not clearly perform the intended left/right transfer
- The gripper opened, but automatic pick and release were not yet achieved reliably
- Direct movement toward the low pick pose caused a collision/contact problem during testing
- Therefore, moving directly from the current pose to the low pick pose is currently unsafe

## Current Conclusion
- Vision detection is working at a basic level
- The remaining issue is mainly motion planning / pose calibration rather than simple camera failure
- The project should now prioritise a fixed pick position and a fixed place position instead of trying to handle multiple zones first
- A safer multi-step path is needed:
  - SAFE_RETRACT
  - PRE_PICK
  - CENTER_PICK
- The same idea will later be used for placing

## Safety Notes
- The arm should not move directly from the current pose to the low pick pose
- A higher intermediate safe pose is required before descending to the table
- The workspace must remain clear during all real-arm tests
- Conservative movement remains important, especially when testing low poses near the table

## Next Actions
- Update config.py using the newly captured real-arm values
- Use the low validated pose as CENTER_PICK
- Use the higher validated pose as SAFE_RETRACT
- Introduce PRE_PICK between SAFE_RETRACT and CENTER_PICK
- Re-test movement to SAFE_RETRACT only
- Re-test SAFE_RETRACT -> PRE_PICK only
- Re-test PRE_PICK -> CENTER_PICK only
- After that, continue toward fixed pick -> fixed place -> return-home