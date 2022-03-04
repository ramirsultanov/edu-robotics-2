import cv2
import numpy as np


def execute():
    cap = cv2.VideoCapture("resources/traffic_road_ex_1.mp4")

    if not cap.isOpened():
        print("Error opening video stream or file")
        pass

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        window = "video"
        image = frame
        cv2.putText(image, "Video shows traffic in a modern city", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)
        cv2.imshow(window, image)
        key = cv2.waitKey(20) & 0xFF
        if key == ord('c') or key == 27:  # ASCII ESCape
            break

    cap.release()

    cv2.destroyAllWindows()
