#ifndef motor_h
#define motor_h

#if (ARDUINO >=100) //this is checking our arduino version
  #include "Arduino.h"
#endif

//Mock function that prints out a random number
class motor {
  public:
    //Constructor
    motor(bool displayMSG);

    //Methods
    long getRandomNumber();

    private:

    
};
#endif
