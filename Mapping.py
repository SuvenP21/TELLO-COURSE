import KeyPressModule as kp
from djitellopy import tello
import numpy as np
import cv2
import math
import time

fSpeed = 117 / 10  # forward speed in cm/s
aSpeed = 360 / 10  # Angular speed Degrees/s
interval = 0.25

dInterval = fSpeed * interval
aInterval = aSpeed * interval

x, y = 500, 500
a = 0
yaw = 0

kp.init()
t = tello.Tello()
t.connect()
print(t.get_battery())

points = []


def GetKeyboardInput():
    global yaw, a, x, y
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    d = 0

    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180
        print("Please Work")
    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180
        print("Please Work")

    if kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270
        print("Please Work")
    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90
        print("Please Work")

    if kp.getKey("w"):
        ud = speed
        print("Please Work")
    elif kp.getKey("s"):
        ud = -speed
        print("Please Work")

    if kp.getKey("a"):
        yv = speed
        yaw -= aInterval
        print("Please Work")
    elif kp.getKey("d"):
        yv = -speed
        yaw += aInterval
        print("Please Work")

    if kp.getKey("q"):
        t.land(); time.sleep(3)
        print("Please Work")
    if kp.getKey("e"):
        t.takeoff()
        print("Please Work")

    time.sleep(interval)
    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y]


def drawPoints(img, points):
    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)


while True:
    vals = GetKeyboardInput()
    t.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000, 1000, 3), np.uint8)
    points.append((vals[4], vals[5]))
    drawPoints(img, points)
    kp.main()
    cv2.imshow("Output", img)
    cv2.waitKey(1)
