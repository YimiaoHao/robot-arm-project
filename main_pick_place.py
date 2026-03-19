import cv2
import time

from vision.color_detect import detect_red_object
from arm_control.arm_basic import connect_arm, safe_stop
from arm_control.arm_sequences import pick_sequence, place_sequence, return_home_sequence

STATE_IDLE = "IDLE"
STATE_SEARCHING = "SEARCHING"
STATE_TARGET_FOUND = "TARGET_FOUND"
STATE_MOVING_TO_PICK = "MOVING_TO_PICK"
STATE_GRABBING = "GRABBING"
STATE_MOVING_TO_PLACE = "MOVING_TO_PLACE"
STATE_RELEASING = "RELEASING"
STATE_RETURNING_HOME = "RETURNING_HOME"
STATE_EMERGENCY_STOP = "EMERGENCY_STOP"


def main():
    state = STATE_IDLE
    target_zone = None
    stable_count = 0
    stable_threshold = 5

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return

    print("Trying to connect robotic arm...")
    connected = connect_arm()
    if not connected:
        print("Arm not connected yet. Vision test mode only.")

    print("System started. Press S to start searching, E for emergency stop, Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Cannot receive frame")
            break

        frame = cv2.flip(frame, 1)
        display = frame.copy()

        result = detect_red_object(frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

        if key == ord("e"):
            state = STATE_EMERGENCY_STOP

        if state == STATE_IDLE:
            cv2.putText(display, "STATE: IDLE | Press S to start", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            if key == ord("s"):
                state = STATE_SEARCHING

        elif state == STATE_SEARCHING:
            cv2.putText(display, "STATE: SEARCHING", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            if result["target_found"]:
                stable_count += 1
            else:
                stable_count = 0

            if result["target_found"] and stable_count >= stable_threshold:
                target_zone = result["zone"]
                state = STATE_TARGET_FOUND

        elif state == STATE_TARGET_FOUND:
            cv2.putText(display, f"STATE: TARGET_FOUND | Zone: {target_zone}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            time.sleep(0.5)
            state = STATE_MOVING_TO_PICK

        elif state == STATE_MOVING_TO_PICK:
            cv2.putText(display, f"STATE: MOVING_TO_PICK | Zone: {target_zone}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 200, 0), 2)
            print(f"Moving to pick position: {target_zone}")
            pick_sequence(target_zone)
            state = STATE_GRABBING

        elif state == STATE_GRABBING:
            cv2.putText(display, "STATE: GRABBING", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 200, 0), 2)
            time.sleep(0.5)
            state = STATE_MOVING_TO_PLACE

        elif state == STATE_MOVING_TO_PLACE:
            cv2.putText(display, "STATE: MOVING_TO_PLACE", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 200, 0), 2)
            print("Moving to place position")
            place_sequence()
            state = STATE_RELEASING

        elif state == STATE_RELEASING:
            cv2.putText(display, "STATE: RELEASING", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 200, 0), 2)
            time.sleep(0.5)
            state = STATE_RETURNING_HOME

        elif state == STATE_RETURNING_HOME:
            cv2.putText(display, "STATE: RETURNING_HOME", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 200, 0), 2)
            print("Returning home")
            return_home_sequence()
            stable_count = 0
            target_zone = None
            state = STATE_IDLE

        elif state == STATE_EMERGENCY_STOP:
            cv2.putText(display, "STATE: EMERGENCY_STOP", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            print("Emergency stop triggered")
            safe_stop()
            state = STATE_IDLE

        if result["target_found"]:
            cx = result["cx"]
            cy = result["cy"]
            zone = result["zone"]
            area = int(result["area"])
            x, y, w, h = result["bbox"]

            cv2.rectangle(display, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(display, (cx, cy), 6, (255, 0, 0), -1)

            cv2.putText(display, f"Zone: {zone} | Center: ({cx},{cy}) | Area: {area}",
                        (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.putText(display, "Q: Quit | S: Start | E: Emergency Stop",
                    (20, display.shape[0] - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow("Main Pick and Place", display)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()