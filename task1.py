import cv2
import numpy as np


class Drawer:

    def __init__(self, image):
        self.img = image
        self.x_prev = -1
        self.y_prev = -1
        self.distance = 0

    def draw(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(self.img, (x, y), 10, (255, 0, 255), -1)
            if self.x_prev != -1 and self.y_prev != -1:
                cv2.line(self.img, (self.x_prev, self.y_prev), (x, y), (255, 255, 0), 8)
                self.distance += np.sqrt((x - self.x_prev) * (x - self.x_prev) + (y - self.y_prev) * (y - self.y_prev))
            self.x_prev, self.y_prev = x, y


def on_trackbar_change(value):
    pass


def execute():
    image = cv2.imread("resources/simple_map.png")
    image = cv2.resize(image, (1200, 800))
    drawer = Drawer(image)
    window = 'image'
    cv2.imshow(window, drawer.img)
    cv2.setMouseCallback(window, drawer.draw)

    while True:
        cv2.imshow(window, drawer.img)
        key = cv2.waitKey(20) & 0xFF
        if key == ord('c') or key == 27:  # ASCII ESCape
            break
    cv2.createTrackbar('distance [m]', window, 50, 3000, on_trackbar_change)
    while True:
        cv2.imshow(window, drawer.img)
        key = cv2.waitKey(20) & 0xFF
        if key == ord('c') or key == 27:  # ASCII ESCape
            break
    real_distance = cv2.getTrackbarPos('distance [m]', window)
    cv2.putText(drawer.img, "resolution: " + str(real_distance / drawer.distance), (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    cv2.imshow(window, drawer.img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
