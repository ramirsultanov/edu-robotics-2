import cv2
import numpy as np

mouseX, mouseY = -1, -1


class Drawer:

    def __init__(self, image):
        self.img = image

    def draw_circle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            global mouseX, mouseY
            cv2.circle(self.img, (x, y), 3, (255, 0, 255), -1)
            mouseX, mouseY = x, y


def execute():

    cap = cv2.VideoCapture("resources/traffic_road_ex_1.mp4")

    if not cap.isOpened():
        print("Error opening video stream or file")
    else:
        ret, frame = cap.read()
        drawer = Drawer(frame)
        window = 'Frame'
        cv2.imshow(window, drawer.img)
        cv2.setMouseCallback(window, drawer.draw_circle)

        p1, p2, p3, p4 = (-1, -1), (-1, -1), (-1, -1), (-1, -1)
        while True:
            cv2.imshow(window, drawer.img)
            key = cv2.waitKey(20) & 0xFF
            if key == ord('1'):
                p1 = mouseX, mouseY
            elif key == ord('2'):
                p2 = mouseX, mouseY
            elif key == ord('3'):
                p3 = mouseX, mouseY
            elif key == ord('4'):
                p4 = mouseX, mouseY
            elif key == ord('w') or key == ord('c') or key == 27:  # ASCII ESCape
                break
        width, height = drawer.img.shape[0], drawer.img.shape[1]
        pts1 = np.float32([[p1], [p2], [p3], [p4]])
        pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        img = cv2.warpPerspective(drawer.img, matrix, (width, height))
        window_perspective = 'Perspective'
        cv2.imshow(window_perspective, img)
        cv2.waitKey(0)
        cv2.destroyWindow(window_perspective)

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:

                img = cv2.warpPerspective(frame, matrix, (width, height))

                cv2.imshow('Frame', img)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            else:
                break

    cap.release()

    cv2.destroyAllWindows()
