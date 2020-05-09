Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@Christianschrodahl 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


CamJam-EduKit
/
EduKit3
34
9679
 Code
 Issues 3
 Pull requests 4 Actions
 Projects 0
 Wiki
 Security 0
 Insights
EduKit3/CamJam Edukit 3 - GPIO Zero/Code/9-avoidance.py /
@GeekyTim GeekyTim Updated RPi.GPIO and GPIO Zero Versions
50706a4 on 16 May 2018
67 lines (52 sloc)  1.57 KB
  
Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more

# CamJam EduKit 3 - Robotics
# Worksheet 9 - Obstacle Avoidance

import time  # Import the Time library
from gpiozero import CamJamKitRobot, DistanceSensor  # Import the GPIO Zero Libraries

# Define GPIO pins to use for the distance sensor
pintrigger = 17
pinecho = 18

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pinecho, trigger=pintrigger)

# Distance Variables
hownear = 15.0
reversetime = 0.5
turntime = 0.75

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 0.5
rightmotorspeed = 0.5

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, 0)
motorright = (0, rightmotorspeed)


# Return True if the ultrasonic sensor sees an obstacle
def isnearobstacle(localhownear):
    distance = sensor.distance * 100

    print("IsNearObstacle: " + str(distance))
    if distance < localhownear:
        return True
    else:
        return False


# Move back a little, then turn right
def avoidobstacle():
    # Back off a little
    print("Backwards")
    robot.value = motorbackward
    time.sleep(reversetime)
    robot.stop()

    # Turn right
    print("Right")
    robot.value = motorright
    time.sleep(turntime)
    robot.stop()


# Your code to control the robot goes below this line
try:
    # repeat the next indented block forever
    while True:
        robot.value = motorforward
        time.sleep(0.1)
        if isnearobstacle(hownear):
            robot.stop()
            avoidobstacle()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    robot.stop()
