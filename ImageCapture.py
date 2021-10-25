from djitellopy import tello
from time import sleep
import cv2

t = tello.Tello()
t.connect()
print(t.get_battery())

t.streamon()

while True:
    img = t.get_frame_read().frame
    img = cv2.resize(img, (720, 1080))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
