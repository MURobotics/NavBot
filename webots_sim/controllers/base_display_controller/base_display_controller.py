#!/usr/bin/env python3.6


"""base_display_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Supervisor
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
print(navbot_ref)

wheel_ref = robot.getFromDef("WHEEL_1")

print("wheel1")
print (wheel_ref)

display = robot.getDisplay("main_display")
print(display)

robot_pos = {
    "x": display.getWidth() // 2,
    "y": display.getHeight() // 2
}
    
orientation_vec = {
    "x": -1,
    "y": 0
}
    
def grabWheelVel(robot):
    data = robot.getField("customData").getSFString()
    res = data.split(", ")
    
    for i in range(len(res)):
        res[i] = float(res[i])
    
    return res
    
def drawRobotPos(display, pos):

    s = 10
    triangle = [(0,0), (3,2), (3, -2)]

    x_pos = []
    y_pos = []

    for point in triangle:
        x_pos.append(point[0] * s + pos["x"])
        y_pos.append(point[1] * s + pos["y"])

    display.fillPolygon(x_pos, y_pos)
    


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    
    # Process sensor data here.
    display.setColor(0x000000)
    display.fillRectangle(0,0,display.getWidth(), display.getHeight())
    
    display.setColor(0xFF0000)
    drawRobotPos(display, robot_pos)
    vel = grabWheelVel(navbot_ref)
    
    overall_vel = vel[0] * 0.5
    
    robot_pos["x"] += int(overall_vel * orientation_vec["x"])
    robot_pos["y"] += int(overall_vel * orientation_vec["y"])
    
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    
    
    pass

# Enter here exit cleanup code.
