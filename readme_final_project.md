# Camera-Based Intelligent Pick-and-Place System for a Lynxmotion Robotic Arm

## Overview
This project was developed for the **AI in the Wild** group robot assignment. The aim was to combine **camera input** with **robot movement** to create one complete intelligent behaviour.

The system uses an external camera to detect a **red target object**, and then attempts to control a **Lynxmotion robotic arm** to:

- detect the object
- move to a pick position
- grab the object
- move it to a place area
- release it
- return to the home position

This repository reflects the version reached during lab-based development and testing on the real hardware.

## Project Goal
The main goal of the project was to build a camera-guided robotic arm system rather than a simple scripted movement. The idea was to make the arm respond to visual input and perform a full pick-and-place sequence with basic safety considerations.

## Current Project Status
At the current stage, the project can:

- open the external camera feed
- detect a red object in the scene
- trigger the robotic arm sequence
- perform arm movement, gripper action, and return-home behaviour
- support basic hardware testing and sequence testing

However, the final result is **not fully stable or fully accurate yet**.

Current limitations:

- the arm does not always pick the object accurately
- some trials still need **manual assistance**
- there can still be **minor collisions or contact** at the beginning of the movement sequence
- some joint position values still need more tuning
- because of limited lab time, the project could only be developed to this stage

So this should be seen as a **working but not fully optimised prototype**.

## Main Features
- Red object detection using an external camera
- Simple vision-guided triggering of robotic arm behaviour
- Modular arm control functions
- Pick, place, and return-home action sequences
- Manual test scripts for hardware checking
- Basic safety logic, including conservative movement design and stop control

## Project Structure
```text
.
├── arm_control/
│   ├── arm_basic.py
│   ├── arm_sequences.py
│   └── config.py
├── manual_tests/
│   ├── test_arm_minimal.py
│   ├── test_pick_center_only.py
│   ├── test_place_only.py
│   ├── test_return_home_only.py
│   └── test_arm_sequence.py
├── teacher_samples/
│   ├── testLEDs.py
│   └── testRanges.py
├── vision/
│   ├── test_camera.py
│   └── color_detect.py
├── lss.py
├── lss_const.py
├── main_pick_place.py
├── requirements.txt
└── README.md
```

### Folder Summary
- **arm_control/**: robotic arm connection, movement functions, sequence logic, and configuration values
- **vision/**: camera testing and red object detection
- **manual_tests/**: smaller real-hardware tests used during debugging and calibration
- **teacher_samples/**: original starter files used for LED and range testing
- **main_pick_place.py**: main integration script combining camera detection and arm behaviour

## Hardware and Environment
This project was tested using:

- **Lynxmotion Robotic Arm (4 DoF)**
- **external laptop camera**
- **Python**
- **serial connection on COM9** during testing

Important note:
If the serial port on another computer is different, the value in `arm_control/config.py` should be updated before running the arm.

## Requirements
Install the required packages using:

```bash
pip install -r requirements.txt
```

Typical dependencies include:

- opencv-python
- pyserial
- numpy

The repository also includes local `lss.py` and `lss_const.py` files used for arm communication.

## How to Run
### 1. Test the camera only
```bash
python -m vision.test_camera
```

### 2. Test red object detection
```bash
python -m vision.color_detect
```

### 3. Run a small robotic arm hardware test
```bash
python -m manual_tests.test_arm_minimal
```

### 4. Run sequence tests
```bash
python -m manual_tests.test_return_home_only
python -m manual_tests.test_pick_center_only
python -m manual_tests.test_place_only
python -m manual_tests.test_arm_sequence
```

### 5. Run the full integrated program
```bash
python main_pick_place.py
```

## Suggested Testing Order
A practical order during lab sessions is:

1. confirm the arm connection and serial port
2. run teacher sample tests if needed
3. test minimal arm movement
4. test return-home only
5. test pick and place sequences separately
6. test the full arm sequence
7. run the full integrated program

This helped reduce risk during real hardware testing.

## Safety Notes
Because the robotic arm is real hardware, safety was important during testing.

Basic safety steps used in this project:

- keep the workspace clear before running the arm
- use conservative joint values instead of aggressive movement
- test individual actions before running the full sequence
- stop testing if a movement looks unsafe or inaccurate
- adjust position values gradually rather than changing everything at once

This project does not claim perfect safety or precision, but safety was considered throughout development.

## Development Approach
The project was built in stages:

1. confirm hardware and serial connection
2. run teacher sample files to check communication and safe ranges
3. build basic arm control functions
4. build the vision module for red object detection
5. integrate detection with arm behaviour
6. test and adjust movement values on the real robot

This staged approach was useful because real lab time with the robot was limited.

## What Worked
- camera input worked
- red object detection worked
- basic arm communication worked
- the gripper and movement sequences could be triggered
- the full system structure was built and tested on real hardware

## What Still Needs Improvement
- more accurate object alignment before grasping
- more reliable pick success without manual help
- more stable placement behaviour
- better tuning of position values
- smoother movement at the start of the sequence

## Final Note
This project reached the stage of a working real-hardware prototype, but not a fully polished final system. Even though the arm could detect and respond to the target, the overall pick-and-place behaviour still needs more tuning to become fully accurate and consistent.

Even so, the project was valuable because it showed the real challenges of combining computer vision with physical robot control under limited lab time.
