#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Empty.h>

void messageCb( const std_msgs::Empty& toggle_msg);
//creates the prototype for reference by the subscriber

ros::NodeHandle nh;
//creates the interfacable ros node

std_msgs::String str_msg;

ros::Publisher chatter("output", &str_msg);
ros::Subscriber<std_msgs::Empty> sub("toggle_chat", &messageCb );
//deploys the topics to publish and subscribe for communicating

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
//toggle functions called by the 'toggle_chat' topic

void setup()
{
  nh.getHardware()->setBaud(9600);
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(chatter);
}
//posts the topics and creates the nodes with 9600 baud

void loop()
{
  if(i == 1){
    str_msg.data = hello;
    chatter.publish( &str_msg );
  }
  nh.spinOnce();
  delay(1000);
}
//iykyk