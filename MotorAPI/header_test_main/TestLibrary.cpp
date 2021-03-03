#include "TestLibrary.h"

TestLib::TestLib(bool displayMsg) {
  // Variables, print messages, or anything else needed when instatiating our library object goes here
  _msg = displayMsg; // setting our input constructor boolean equal to a private variable to control begin message output
}

// This is the 'begin' function that starts the program
void TestLib::begin(int baudRate) {
  Serial.begin(baudRate);
  if (_msg) {
  Serial.println("TestLib constructor instantiated successfully.");
  }
}

// For the sake of testing here is a function that literally just gets a random number
long TestLib::getRandomNumber() {

  unsigned long specialNumber = random(5, 1000); // gets random number between 5 and 1000

  specialNumber *= getPi(); // multiplies by Pi and reassigns

  specialNumber -= 5; // subtracts 5 and reassigns

  return specialNumber;
  
}

// Private method that is used as example to show how private methods work
float TestLib::getPi() {
  return PI;
}
