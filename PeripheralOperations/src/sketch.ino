/*
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Empty.h>

ros::NodeHandle nh;

std_msgs::String str_msg;
ros::Publisher chatter("output", &str_msg);
ros::Subscriber<std_msgs::Empty> sub("toggle_chat", &messageCb );

int i = 0;
char hello[13] = "hello world!";

void messageCb( const std_msgs::Empty& toggle_msg){
  if (i == 0){
    i = 1;
  }
  else if (i == 1){
    i = 0;
  }
  else {
    i = 0;
  }
}

void setup()
{
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(chatter);
}

void loop()
{
  if(i == 1){
    str_msg.data = hello;
    chatter.publish( &str_msg );
  }
  nh.spinOnce();
  delay(1000);
}