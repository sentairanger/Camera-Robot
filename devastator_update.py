#import libraries
import curses
from gpiozero import CamJamKitRobot, LEDBoard
import os
from time import sleep

#import these libraries to enable camera and save via unique filename
from picamera import PiCamera
from datetime import datetime


#setup camera, resolution, framerate and a datetime stamp
devastator_camera = PiCamera()
devastator_camera.resolution = (640, 480)
devastator_camera.framerate = 25
moment = datetime.now()

#set variable for robot and LED
devastator_robot = CamJamKitRobot()
devastator_scary_eyes = LEDBoard(25)

#Flash the LED 4 times
for x in range(1, 5):
    devastator_eye.off()
    sleep(0.5)
    devastator_eye.on()
    sleep(0.5)

#Define the record and stop_record functions
def record():
    devastator_eye.off()
    devastator_camera.start_recording('/home/pi/Videos/video_%02d_%02d_%02d.mjpg' % (moment.hour, moment.minute, moment.second))

def stop_record():
    devastator_eye.on()
    devastator_camera.stop_recording()

#setup your actions
actions = {
    curses.KEY_UP:    devastator_robot.forward,
    curses.KEY_DOWN:  devastator_robot.down,
    curses.KEY_LEFT:  devastator_robot.left,
    curses.KEY_RIGHT: devastator_robot.right,

    }

#main curses function
def main(window):
    next_key = None
    while True:
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            #when key is pressed
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            #when key is released
            devastator_robot.stop()
        if key == ord('q'):
            break #quit the module
        if key == ord('S'):
            os.system('sudo shutdown now') #shutdown the pi
        if key == ord('r'): 
            record()
        if key == ord('t'):
            stop_record()
curses.wrapper(main)
devastator_eye.off()
devastator_robot.off()
devastator_camera.stop_recording()
