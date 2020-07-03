/*
 * File:          move_forward_controller.c
 * Date:
 * Description:
 * Author:
 * Modifications:
 */

/*
 * You may need to add include files like <webots/distance_sensor.h> or
 * <webots/motor.h>, etc.
 */

#include <webots/robot.h>
#include <webots/motor.h>
#include <stdlib.h>
#include <webots/lidar.h>

/*
 * You may want to add macros here.
 */
#define TIME_STEP 64
#define MOTOR_COUNT 4

/*
 * This is the main program.
 * The arguments of the main function can be specified by the
 * "controllerArgs" field of the Robot node
 */
 
WbDeviceTag * configureMotors(){
  WbDeviceTag * motors = malloc(sizeof(WbDeviceTag) * MOTOR_COUNT);
  
  const char * motorNames[MOTOR_COUNT] = {
    "wheel1",
    "wheel2",
    "wheel3",
    "wheel4"
  };
  
  unsigned int c;
  for (c = 0; c < MOTOR_COUNT; c++) {
    motors[c] = wb_robot_get_device(motorNames[c]);
  }
 
  return motors; 
}

void moveMotors(WbDeviceTag * motors) {

  unsigned int c;
  for (c = 0; c < MOTOR_COUNT; c++) {
    wb_motor_set_position(motors[c], INFINITY);
    wb_motor_set_velocity(motors[c], 3.0);
  }
  
}

void freeMotors(WbDeviceTag * motors){
  free(motors);
}

WbDeviceTag * configureLidar(){
  WbDeviceTag * lidarSensor = malloc(sizeof(WbDeviceTag));
  
  *lidarSensor = wb_robot_get_device("navbot_lidar");
  wb_lidar_enable(*lidarSensor, TIME_STEP);
  wb_lidar_enable_point_cloud(*lidarSensor);
  
  
  return lidarSensor;
}

void freeLidar(WbDeviceTag * lidar){
  free(lidar);
}

 
int main(int argc, char **argv) {
  /* necessary to initialize webots stuff */
  wb_robot_init();

  /*
   * You should declare here WbDeviceTag variables for storing
   * robot devices like this:
   *  WbDeviceTag my_sensor = wb_robot_get_device("my_sensor");
   *  WbDeviceTag my_actuator = wb_robot_get_device("my_actuator");
   */

  WbDeviceTag * motors = configureMotors();
  WbDeviceTag * lidarSensor = configureLidar();

  moveMotors(motors);

  /* main loop
   * Perform simulation steps of TIME_STEP milliseconds
   * and leave the loop when the simulation is over
   */
  while (wb_robot_step(TIME_STEP) != -1) {
    /*
     * Read the sensors :
     * Enter here functions to read sensor data, like:
     *  double val = wb_distance_sensor_get_value(my_sensor);
     */
    wb_lidar_get_point_cloud(*lidarSensor);
    /* Process sensor data here */
    /*
     * Enter here functions to send actuator commands, like:
     * wb_motor_set_position(my_actuator, 10.0);
     */
  };

  /* Enter your cleanup code here */
  freeLidar(lidarSensor);
  freeMotors(motors);

  /* This is necessary to cleanup webots resources */
  wb_robot_cleanup();

  return 0;
}
