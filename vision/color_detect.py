import cv2
import numpy as np


def detect_red_object(frame):
    height, width = frame.shape[:2]

    left_boundary = width // 3
    right_boundary = 2 * width // 3

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    result = {
        "target_found": False,
        "zone": "NONE",
        "cx": None,
        "cy": None,
        "area": 0,
        "mask": mask
    }

    if contours:
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)

        if area > 800:
            x, y, w, h = cv2.boundingRect(largest)
            cx = x + w // 2
            cy = y + h // 2

            if cx < left_boundary:
                zone = "LEFT"
            elif cx < right_boundary:
                zone = "CENTER"
            else:
                zone = "RIGHT"

            result["target_found"] = True
            result["zone"] = zone
            result["cx"] = cx
            result["cy"] = cy
            result["area"] = area
            result["bbox"] = (x, y, w, h)

    return result


def run_detection_test():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        raise SystemExit

    stable_count = 0
    stable_threshold = 5

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Cannot receive frame")
            break

        frame = cv2.flip(frame, 1)
        display = frame.copy()

        height, width = display.shape[:2]
        left_boundary = width // 3
        right_boundary = 2 * width // 3

        cv2.line(display, (left_boundary, 0), (left_boundary, height), (255, 255, 255), 2)
        cv2.line(display, (right_boundary, 0), (right_boundary, height), (255, 255, 255), 2)

        result = detect_red_object(frame)
        mask = result["mask"]

        if result["target_found"]:
            stable_count += 1

            x, y, w, h = result["bbox"]
            cx = result["cx"]
            cy = result["cy"]
            zone = result["zone"]
            area = result["area"]

            cv2.rectangle(display, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(display, (cx, cy), 6, (255, 0, 0), -1)

            cv2.putText(
                display,
                f"RED | Zone: {zone} | Center: ({cx},{cy}) | Area: {int(area)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )
        else:
            stable_count = 0

        if result["target_found"] and stable_count >= stable_threshold:
            cv2.putText(
                display,
                "TARGET_FOUND",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 255),
                2
            )

        cv2.putText(
            display,
            "Press Q to quit",
            (20, height - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.imshow("Red Object Detection", display)
        cv2.imshow("Mask", mask)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_detection_test()