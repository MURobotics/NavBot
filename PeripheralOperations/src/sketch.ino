#include <ros.h>
#include <std_msgs/String.h>

int ledPin = LED_BUILTIN;

void setup(){
    pinMode(ledPin, OUTPUT);
}

void loop(){
    digitalWrite(ledPin, HIGH);
    delay(3000);
    digitalWrite(ledPin, LOW);
    delay(3000);
}
