#ifndef tl
#define tl

// This is just saying if our Arduino is newer than 1.0 we just include Arduino.h
// otherwise we need to include WProgram.h
#if (ARDUINO >=100)
  #include "Arduino.h"
#else
  #include "WProgram.h"
#endif

class TestLib {
  public:
  // Constructor
  TestLib(bool displayMsg=false);

  // Methods
  void begin(int baudRate=9600); // instantiating function (objects don't like when Serial.begin is put into constructor), default baudRate set to 9600
  long getRandomNumber();

  private:
    bool _msg;
    float getPi();
 
};
#endif
