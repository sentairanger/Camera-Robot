#import libraries
import curses
from gpiozero import Robot, LED
import os
from time import sleep
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from datetime import datetime

#set variable for robot and eye
devastator_robot = Robot(left=(13, 21), right=(17, 27))
eye = LED(25)

# Define the new camera and the configurations
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(10000000)
moment = datetime.now()

# Blink eye 2 times to ensure the code is running correctly
eye.blink(n=2)

#Define the record and stop_record functions
def record():
    print("recording!")
    eye.on()
    picam2.start_recording(encoder, '/home/torvalds/Videos/video2_%02d_%02d_%02d.h264' % (moment.hour, moment.minute, moment.second))

def stop_record():
    eye.off()
    print("stop recording!")
    picam2.stop_recording()

#setup your actions
actions = {
    curses.KEY_UP:    devastator_robot.forward,
    curses.KEY_DOWN:  devastator_robot.backward,
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
        if key == ord('s'):
            os.system('sudo shutdown now') #shutdown the pi
        if key == ord('r'):
            record()
        if key == ord('t'):
            stop_record()
curses.wrapper(main)
devastator_robot.stop()
