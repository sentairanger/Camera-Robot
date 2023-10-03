import pygame
from gpiozero import Robot, LED
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

#Define the record and stop_record functions
def record():
    print("recording!")
    eye.on()
    picam2.start_recording(encoder, '/home/torvalds/Videos/video_pygame_%02d_%02d_%02d.h264' % (moment.hour, moment.minute, moment.second))

def stop_record():
    print("stop recording!")
    eye.off()
    picam2.stop_recording()

screen = pygame.display.set_mode([240, 160])

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                devastator_robot.right()
            if event.key == pygame.K_LEFT:
                devastator_robot.left()
            if event.key == pygame.K_UP:
                devastator_robot.forward()
            if event.key == pygame.K_DOWN:
                devastator_robot.backward()
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == pygame.K_r:
                record()
            if event.key == pygame.K_s:
                stop_record()
        elif event.type == pygame.KEYUP:
            devastator_robot.stop()
