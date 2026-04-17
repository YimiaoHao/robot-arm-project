# Safe Range Notes

## Joint 2
- Teacher sample reference suggests around -900 is near a parallel-ground style pose
- No major abnormal behaviour was specifically identified during current testing
- Final safe working range still needs to be refined in our own configuration

## Joint 3
- Teacher sample reference suggests around 850 is near a more extended/parallel pose
- No major abnormal behaviour was specifically identified during current testing
- Final safe working range still needs to be refined in our own configuration

## Joint 4
- Teacher sample sweep was tested
- During the first run, one collision/contact-like sound was heard once
- The same sound did not occur in the second run
- Later return-home testing also caused contact/red error behaviour
- Therefore, the extreme lower end of joint 4 movement should be treated conservatively
- Do not assume the full sample sweep range is safe for normal project actions

## Gripper
- Open and close actions worked in minimal testing
- Final grip values may still need adjustment depending on the object used in the demo

## Home Position
- Current home path is not fully reliable yet
- Return-home behaviour still needs further refinement
- A safer retract pose may be needed before final home

## Pick Position
- CENTER pick appears broadly workable in current testing
- LEFT and RIGHT are not yet fully validated on real hardware

## Place Position
- Place-only test was broadly workable
- Final place pose still needs confirmation after return-home logic is fixed

## Updated Motion Strategy
- A direct movement from the current pose to the low table-level pick pose is currently not considered safe
- A multi-step motion strategy is now preferred:
  - first move to SAFE_RETRACT
  - then move above the object (PRE_PICK)
  - then descend to CENTER_PICK

## Confirmed Candidate CENTER_PICK
- Real-arm pose captured from FlowArm and read in Python:
  - J2 = -1029
  - J3 = 894
  - J4 = 372
- This low pose appeared able to pick the object from the table
- However, it should not be approached directly from arbitrary current poses

## Confirmed Candidate SAFE_RETRACT
- Real-arm pose captured from FlowArm and read in Python:
  - J2 = -610
  - J3 = 689
  - J4 = 373
- This pose is higher and safer than the low pick pose
- It is a suitable candidate for an intermediate retract/travel position

## Current Safety Interpretation
- The low pick pose itself may be workable
- The unsafe part is more likely the direct path to reach that pose
- Therefore, motion planning is now treated as a key safety issue, not just final pose selection

## Updated Current-Device Pose Notes
The latest session indicated that pose values should be treated as device/session-specific. Earlier values collected on a previous setup should not automatically be mixed with the current device’s values.

## Current-Device START_POSE
- Captured after opening the current machine/setup:
  - J2 = -1191
  - J3 = 893
  - J4 = 575

## Current-Device PRE_PICK Candidate
- Captured as a working “prepare to grab” style pose:
  - J2 = 338
  - J3 = -96
  - J4 = 465

## Current-Device POST_PICK_LIFT Candidate
- Captured as a higher lifted pose after grab:
  - J2 = 263
  - J3 = -161
  - J4 = 668

## Current-Device PRE_PLACE Candidate
- Captured as a transfer/release-area pose:
  - J2 = 90
  - J3 = 67
  - J4 = 614

## Current Safety Interpretation
- The current session suggests that one consistent set of current-device poses is safer than mixing older and newer calibration values
- Motion safety should be validated again using this one current-device path:
  - START_POSE
  - PRE_PICK
  - POST_PICK_LIFT
  - PRE_PLACE
  - PLACE_POS / release
- A full automatic sequence has not yet been confirmed using this newer pose set