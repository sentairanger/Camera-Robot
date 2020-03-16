# Camera-Robot

## Overview of the Project

This is based on a video tutorial that Christopher J. Barnatt did on his YouTube channel. This is the [video](https://www.youtube.com/watch?v=pK0XvjiP2qk&t=24s) where he showed how to do it. However there are some things I did differently from the tutorial. 

### Required hardware

These are the things I used for the robot, however there are some things I changed from Christopher's tutorial due to availabililty. You can swap things out at your discretion:

* Chassis. I used DFRobot's Devastator Tank Mobile Platform similar to Chris's. You can use any chassis you want.
* Raspberry Pi Zero W. You can use any Pi you want as long as you have adequate cooling and power.
* 3D printed camera mount. You can get the STL file [here](https://www.youtube.com/redirect?redir_token=fj1ZqILzr4zLJ4-KnCQUHMVyDjd8MTU4NDA1NzQ0MkAxNTgzOTcxMDQy&q=https%3A%2F%2Fwww.tinkercad.com%2Fthings%2Fhn6jajTg5Sv-pidevcammount&event=video_description&v=pK0XvjiP2qk)
* Pi Camera with Pi Zero adapter cable
* 2 HDD LEDs. These aren't required. You can use plain old LEDs with dupont wires, resistors and bezels and assemble as you wish.
* Any USB Power Bank. Use a UBEC if you wish but be careful.
* 6AA batteries. Use rechargable NiMi batteries if you wish.
* Keyboard Controller. Can be USB or Bluetooth
* USB OTG connector if you won't use Bluetooth.
* A Micro SD Card

### Required software

* Raspbian Buster. Download [here](https://www.raspberrypi.org/downloads/raspbian/)
* Image Writer. You can use etcher or any other imaging software to write the image to your Micro SD Card.

### Getting Started

Here are the steps you need to take in order to get things running:

* Assemble the robot
* Download the Raspbian image and write the image to the card. Insert it into the Pi and make sure things are set up. Then once you have it installed shut down the pi. Remove the SD card and place it into a card reader on your PC. Clone this repository and then move the downloaded files into the card, specifically the `/home/pi` directory. Eject the card and reinsert it into the pi.
* Turn on the pi and move the downloaded files into the `Documents` directory to make things easier. 
* Make sure your camera is enabled by going into Menu > Preferences > Raspberry Pi Configuration > Interfaces > Camera > Enable
* Next, go into the `/home/pi/Documents/Camera-Robot` directory. Run the code using `python devastator_update.py`. The LED should blink 4 times and you can use your keyboard controller to run the robot. Press r to enable the camera. The LED should turn off indicating the camera has been enabled. Run the robot around and then see what happens. Press t to stop or q to quit.
* You will now have a video on your `Videos` directory with a time stamp. To play it go to the terminal, type `cd Videos` and then type `omxplayer <name of video>` to play your video. Now you are good to go.

### Running code on boot

To run the code on boot without having to attach an HDMI cable I included the `bootup.sh` file to make it easier to implement. The full paths are added because when the Pi boots it won't know where to search. Be sure to make it executable by typing `chmod +x bootup.sh`. Next, since Buster does require this, go into Menu > Preferences > Raspberry Pi Configuration > Resolution > Set Resolution. Set the resolution to anything other than Default or else it won't work. You'll have to reboot for this to work. Once that's done, go back to the terminal, type `cd /etc/xdg/lxsession/LXDE-pi` to edit the autostart file. Since this requires root privileges type `sudo nano autostart` and then on a new line type `@lxterminal -e /home/pi/Documents/Camera-Robot/bootup.sh`. Once that's done make sure to save it and exit. Then reboot the pi to test it out and a terminal should pop up and the code should run. Now, you can boot the pi without any monitor and run the robot as you wish. To gracefully shutdown, hold Shift and S to shutdown. 

### Converting mjpg to mp4

If you want to convert your saved videos to mp4 go into VLC media player, go to Media > Convert/Save > File. Add your files and use the .mp4 file extension and it should be converted. On windows you can download 3rd party sofware to convert mjpg files. 
