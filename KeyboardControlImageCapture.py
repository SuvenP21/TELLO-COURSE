import KeyPressModule as kp
from djitellopy import tello
import time
import cv2

kp.init()
t = tello.Tello()
t.connect()
print(t.get_battery())

global img
t.streamon()


def GetKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 600

    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = -speed
    elif kp.getKey("d"):
        yv = speed

    if kp.getKey("q"):
        t.land()
        time.sleep(3)
    if kp.getKey("e"):
        t.takeoff()

    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    if kp.getKey("u"):
        t.flip_forward()
    elif kp.getKey("n"):
        t.flip_back()
    if kp.getKey("h"):
        t.flip_left()
    elif kp.getKey("j"):
        t.flip_right()

    return [lr, fb, ud, yv]


while True:
    vals = GetKeyboardInput()
    t.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = t.get_frame_read().frame
    img = cv2.resize(img, (1080, 1080))
    cv2.imshow("Image", img)
    time.sleep(0.005)
