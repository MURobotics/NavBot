#!/usr/bin/env python3.6


"""base_display_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Supervisor
import math
# create the Robot instance.
robot = Supervisor()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

navbot_ref = robot.getFromDef("NavBot")
display = robot.getDisplay("main_display")

robot_pos = {
    "x": display.getWidth() // 2,
    "y": display.getHeight() // 2
}
    
    
def rotate_point(point, theta):

    cos = math.cos(theta)
    sin = math.sin(theta)

    x = point[0]
    y = point[1]

    new_point = (
        x * cos - y * sin,
        x * sin + y * cos
    )

    return new_point
    
def grabWheelVel(robot):
    data = robot.getField("customData").getSFString()
    res = data.split(", ")
    
    for i in range(len(res)):
        res[i] = float(res[i])
    
    return res
    
angle = math.pi * 2


def compute_orientation(angle):
    return {
        "x": math.cos(angle),
        "y": math.sin(angle)
    }
    
orientation_vec = compute_orientation(angle)

def drawRobotPos(display, pos, color):
    global angle
    display.setColor(color)

    s = 10
    
    triangle = [(-2,0), (1,2), (1, -2)]

    x_pos = []
    y_pos = []

    for point in triangle:
        
        point = rotate_point(point, angle)
    
        x_pos.append(point[0] * s + pos["x"])
        y_pos.append(point[1] * s + pos["y"])

    display.fillPolygon(x_pos, y_pos)

def resetScreen(display, color):
    display.setColor(color)
    display.fillRectangle(0,0,display.getWidth(), display.getHeight())

def log_point(point, color):
    
    display.setColor(color)
    display.fillRectangle(point["x"], point["y"], 10,10)
    
def log_points(points, color = 0x000000):

    for point in points:
        log_point(point, color)
    
point_log = []

log_counter = 0
log_elapsed = 500

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    
    resetScreen(display, 0x000000)
    
    
    log_points(point_log, 0xFFFFFF)
    drawRobotPos(display, robot_pos, 0xFF0000)
    
    
    vel = grabWheelVel(navbot_ref)
    
    if (vel[0] == vel[1]):
        overall_vel = vel[0] * 1
        print(orientation_vec)
        robot_pos["x"] += int(overall_vel * orientation_vec["x"])
        robot_pos["y"] += int(overall_vel * orientation_vec["y"])
        
    elif (vel[0] == -vel[1]):
        
        # magical number pls remove
        coefficient = (1/100) * 0.9
        angle += vel[0] * coefficient
    
        orientation_vec = compute_orientation(angle)
    
    
    if (log_counter >= log_elapsed):
            
        new_point = {
            "x": robot_pos["x"],
            "y": robot_pos["y"]
        }
        
        point_log.append(new_point)
        
        log_counter = 0
    
    
    log_counter += timestep
    
# Enter here exit cleanup code.
