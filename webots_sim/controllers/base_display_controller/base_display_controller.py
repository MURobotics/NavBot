#!/usr/bin/env python3.6
"""base_display_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Supervisor

#custom code
from odometry_system import *
from ui_system import *
from geometry_util import *
from robot_system import *


def grabWheelVel(robot):
    data = robot.getField("customData").getSFString()
    res = data.split(", ")

    for i in range(len(res)):
        res[i] = float(res[i])

    return res

# create the Robot instance.
robot = Supervisor()
navbot_ref = robot.getFromDef("NavBot")

display = robot.getDisplay("main_display")
ui_system = UISystem(display)

robot_pos = Point.create(
    x = ui_system.getDisplay().getWidth() // 2,
    y =  ui_system.getDisplay().getHeight() // 2
)
robot_system = RobotModel(
    init_pos = robot_pos,
    init_angle = math.pi * 2
)

odometry_system = TwoWheelOdometry(
    wheel_radius = 0.02,
    chassis_distance = 0.07
)



# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

point_log = []
log_counter = 0
log_elapsed = 500

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:

    # Render Logic
    ui_system.resetScreen(0x000000)
    robot_system.render(ui_system)
    ui_system.log_points(point_log, 0xFFFFFF)

    # Pull Raw Wheel Sensor Data
    vel = grabWheelVel(navbot_ref)

    # Pass Odometry required values
    odometry_system.updateWheelAngularVelocity(
        left_wheel_angular_vel = vel[0],
        right_wheel_angular_vel = vel[1]
    )

    # Pull odometry computation
    odometry_info = odometry_system.performOdometry(timestep)

    # apply translation
    old_robot_pos = robot_system.getPosition()

    raw_position_offset = TwoWheelOdometry.PositionOffsetInDirection(robot_system.getAngle(), odometry_info["position_offset"])
    
    robot_position_vector = Point.roundCoordinatesToInt(
        Point.scale(
            raw_position_offset,
            scale = 1000
        )
    )

    robot_system.setPosition(
        Point.move(old_robot_pos, robot_position_vector)
    )

    # apply rotation
    delta_angle = odometry_info["angle_offset"]
    robot_system.setAngle(robot_system.getAngle() + delta_angle)

    # Tracking Logic
    if (log_counter >= log_elapsed):

        new_point = Point.copy(robot_system.getPosition())
        point_log.append(new_point)

        log_counter = 0


    log_counter += timestep



# Enter here exit cleanup code.
