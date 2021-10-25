from djitellopy import tello
from time import sleep

t = tello.Tello()
t.connect()
print(t.get_battery())

t.takeoff()
#forward - = backward
t.send_rc_control(0, 50, 0, 0)
sleep(2)
#right - = left
t.send_rc_control(30 , 0, 0, 0)
sleep(2)
t.send_rc_control(0, 0, 0, 0)
t.land()
