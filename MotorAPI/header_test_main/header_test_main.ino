#include "TestLibrary.h"

TestLib testlib(true);  // instantiates our object in the file

//main test file for dummy header
void setup() {
    // put setup code here, to run once:
    //Serial.begin(9600);
    testlib.begin(9600);  // replaces Serial.begin and allows us to send debug message to make sure test library compiles correctly
    randomSeed(analogRead(A0));
    
}

void loop() {
    // put your main code here, to run repeatedly:
    long rndNo = testlib.getRandomNumber(); // function that returns a random number to be printed

    // This cannot be done - it is PRIVATE
    // float test = testlib.getPi();

    Serial.println(rndNo);

    delay(2000);
    
}
