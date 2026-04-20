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

## Lab Session 3
- Date: 16/04/2026
- Team members present: Yimiao, Hafza

## What We Tested
- Real-arm reconnect on a different lab setup / device state
- COM-port rechecking before Python testing
- Python read_current_pose.py on the currently connected arm
- Manual FlowArm pose collection for the current device only
- Rebuilding a new fixed pick/transfer path using the current device’s pose values

## What Worked
- The arm could connect again after updating the COM port to match the current machine
- read_current_pose.py worked reliably for the current device
- A current-device start pose was captured successfully:
  - J2 = -1191
  - J3 = 893
  - J4 = 575
- New working candidate poses were also captured on the same current device:
  - Candidate PRE_PICK:
    - J2 = 338
    - J3 = -96
    - J4 = 465
  - Candidate POST_PICK_LIFT:
    - J2 = 263
    - J3 = -161
    - J4 = 668
  - Candidate PRE_PLACE / release area:
    - J2 = 90
    - J3 = 67
    - J4 = 614

## What Did Not Work Smoothly
- COM-port values were not stable across different sessions / setups, so older COM assumptions were no longer fully reliable
- Previously collected pose values from another setup could not safely be assumed to match the current device
- Candidate SAFE_RETRACT values became inconsistent when switching between different hardware states / ports
- The new full path was not yet physically validated before the arm was taken back

## Current Conclusion
- The project now needs to treat the current lab setup as its own calibration context
- Old pose values and current-device pose values should not be mixed without validation
- The next real-arm session should use one consistent set of current-device poses only
- The short-term action path is now better understood as:
  - START_POSE
  - PRE_PICK
  - POST_PICK_LIFT
  - PRE_PLACE
  - PLACE_POS / release
- At this stage, the fixed transfer workflow is more realistic than multi-zone behaviour

## Safety Notes
- Real-arm values should be collected and tested on the same device/session whenever possible
- A pose captured on one setup should not automatically be trusted on a different setup
- Motion planning remains the main safety risk, more than basic camera detection
- Conservative testing is still required before any full automatic sequence is trusted

## Next Actions
- Clean config.py so it contains only one active current-device pose set
- Re-test PRE_PICK only on the same current device
- Re-test PRE_PICK -> POST_PICK_LIFT
- Re-test POST_PICK_LIFT -> PRE_PLACE
- Then test a minimal fixed transfer:
  - PRE_PICK -> close
  - POST_PICK_LIFT
  - PRE_PLACE -> open
- Only after that, continue to a lower final place pose and then return-home

## Lab Session 4
- Date: 20/04/2026
- Team members present: Yimiao, Hafza

## What We Tested
- Reconnected the robotic arm on the previous COM10 setup
- Rechecked the real COM port before testing
- Updated read_current_pose.py so that J1 / J2 / J3 / J4 / Gripper could all be read
- Rebuilt the motion code to include base rotation (J1), not only planar arm motion
- Re-measured a new device-specific fixed sequence for:
  - start pose
  - light retract / lift
  - forward-lean approach
  - wrist-down approach
  - lower fine-tuning
  - pre-pick
  - grasp
  - post-pick lift
  - pre-place / turning pose
  - release pose
  - return / retract poses
- Re-tested the fixed pick-transfer sequence
- Re-tested the camera + robotic-arm integration through main_pick_place.py

## What Worked
- The arm connected successfully on COM10
- read_current_pose.py worked correctly on the current device and returned J1 together with J2, J3, J4, and gripper values
- The main previous limitation was identified more clearly: earlier code only moved within one main plane because base rotation was not fully included
- After adding J1 into the control logic, the arm could perform a real turning motion toward the place side instead of only moving in a 2D-style plane
- A fuller device-specific fixed motion sequence was captured for the current device
- The fixed sequence could now run through pick, lift, turn, and release more completely than before
- The camera still detected the red target successfully
- The camera-triggered workflow and the real-arm sequence were connected again through main_pick_place.py

## What Did Not Work Smoothly
- Some slight contact still occurred near the final release / place stage
- The final release required a larger gripper opening than earlier versions
- Because the hardware setup changed again, older values from previous sessions were not safe to reuse directly
- Final demonstration behaviour depended on using one fixed object position and one fixed place area

## Current Conclusion
- The project has now moved from separate vision tests and separate arm tests to a linked fixed-position workflow
- A key improvement in this session was adding base rotation (J1) into the real motion path, which allowed an actual left/right transfer instead of only planar movement
- The current project should be demonstrated as a fixed-position, camera-guided pick-and-transfer system
- For the final demo, the safest approach is:
  - use one fixed red object position
  - use one fixed place area
  - use the current-device pose set only
  - keep release behaviour conservative

## Safety Notes
- Always confirm the real COM port before testing
- Close FlowArm completely before running Python scripts
- Do not mix pose values from different devices / sessions without validation
- Keep the workspace clear during all real-arm tests
- The final place / release stage should still be treated conservatively

## Next Actions
- Freeze the final demo parameters instead of continuing to expand scope
- Use the fixed-position workflow for the teacher demonstration
- Prepare screenshots / video evidence from the final sequence
- Use the final notes to complete the short review / report sections