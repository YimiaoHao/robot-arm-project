# AI in the Wild Group Project

## Project Title
Camera-Based Intelligent Pick-and-Place System for a Lynxmotion Robotic Arm

## Core Goal
Use a camera to detect a target object, then control the robotic arm to:
- detect the object
- move to the pick position
- grab the object
- move it to the place area
- release it
- return to the home position safely

## Team Roles
- Yimiao: integration, robotic arm control, state machine, safety, report organisation
- Hafza: camera input, colour detection, threshold tuning, demo explanation

## Current Structure
- teacher_samples/testLEDs.py
- teacher_samples/testRanges.py
- arm_control/config.py
- arm_control/arm_basic.py
- arm_control/arm_sequences.py
- vision/test_camera.py
- vision/color_detect.py
- main_pick_place.py

## Current Port
COM9