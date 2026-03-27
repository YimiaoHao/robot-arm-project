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