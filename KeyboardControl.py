import KeyPressModule as kp
from djitellopy import tello
from time import sleep

kp.init()
t = tello.Tello()
t.connect()
print(t.get_battery())


def GetKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 100

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
    if kp.getKey("e"):
        t.takeoff()

    return [lr, fb, ud, yv]


while True:
    vals = GetKeyboardInput()
    t.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.005)
