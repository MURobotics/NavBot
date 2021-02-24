#include "motor.h"

motor::motor(bool displayMsg) {
  // Anything you need when instantiating your object goes here
}

// Mock function to print out a random number to the terminal
long getRandomNumber() {

  unsigned long specialNumber = random(5, 1000);

  specialNumber *= PI;

  specialNumber -= 5;

  return specialNumber;
}
