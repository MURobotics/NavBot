// Copyright 1996-2020 Cyberbotics Ltd.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <signal.h>
#include "ros/ros.h"

#include <sensor_msgs/Image.h>
#include <std_msgs/String.h>

#include <webots_ros/get_float.h>
#include <webots_ros/set_float.h>
#include <webots_ros/set_int.h>
#include <webots_ros/get_int.h>


#include <webots_ros/set_string.h>
#include <webots_ros/get_string.h>

#include <webots_ros/range_finder_get_info.h>
#include <webots_ros/robot_get_device_list.h>
#include <webots_ros/save_image.h>

#define TIME_STEP 32

ros::ServiceClient timeStepClient;
webots_ros::set_int timeStepSrv;

void quit(int sig) {
  ROS_INFO("User stopped the 'robot_information_parser' node.");
  ros::shutdown();
  exit(0);
}

void moveWheels(ros::NodeHandle n, std::string controllerName){
  std::string wheelNames[4] = {
    "wheel1",
    "wheel2",
    "wheel3",
    "wheel4"
  };


  webots_ros::set_float setMotorPositionSrv;
  webots_ros::set_float setMotorVelocitySrv;

  setMotorPositionSrv.request.value = INFINITY;
  setMotorVelocitySrv.request.value = 1.0f;

  unsigned int c;
  for (c = 0; c < 4; c++){

    std::string wheelName = wheelNames[c];

    //enable motor
    ros::ServiceClient motorSetPositionClient = n.serviceClient<webots_ros::set_float>(controllerName + "/" + wheelName + "/set_position");
    ros::ServiceClient motorSetVelocityClient = n.serviceClient<webots_ros::set_float>(controllerName + "/" + wheelName + "/set_velocity");

    motorSetPositionClient.call(setMotorPositionSrv);
    motorSetVelocityClient.call(setMotorVelocitySrv);


  }
}

int main(int argc, char **argv) {
  std::string controllerName = "navbot";

  float step;


  // create a node named 'robot_navbot_controller' on ROS network
  ros::init(argc, argv, "robot_navbot_controller", ros::init_options::AnonymousName);
  ros::NodeHandle n;

  signal(SIGINT, quit);

  // call get_type and get_model services to get more general information about the robot
  ros::ServiceClient getTypeClient = n.serviceClient<webots_ros::get_int>(controllerName + "/robot/get_type");
  webots_ros::get_int getTypeSrv;

  ros::ServiceClient getModelClient = n.serviceClient<webots_ros::get_string>(controllerName + "/robot/get_model");
  webots_ros::get_string getModelSrv;

  //enable Motors
  moveWheels(n, controllerName);
}
