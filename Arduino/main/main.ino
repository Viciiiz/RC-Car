#include <Servo.h> 

// the servo that will direct the front wheel
const int servoDirectionPin = 11;
const int servoDirectionInitial = 105; // middle = 105 
const int servoDirectionMinRight = 75; // Full right = 75
const int servoDirectionMaxLeft = 135; // Full left = 135

// the servo that will handle the ground of the DC motor
//const int servoDCPin = 12;
//const int servoDCInitial = 90;
//const int servoDCForward = 10;
//const int servoDCBackward = 170;

const int DCMotorPin = 10; // connect to relay. LOW to move forward, HIGH backward.
const int DCMotorPin2 = 9; // this will control the second relay to move the car backward. LOW to move forward, HIGH backward.
const int servoMin = 10;
const int servoMax = 170;
Servo directionServo;

void setup() {
  Serial.begin(115200);
  directionServo.attach(servoDirectionPin);
  pinMode(DCMotorPin, OUTPUT);
  pinMode(DCMotorPin2, OUTPUT);
  directionServo.write(servoDirectionInitial);
  delay(1500);
}

// MAIN
void loop() {
//  for (int i = servoDirectionMinRight ; i < servoDirectionMaxLeft; i++){
//    directionServo.write(i);
//    delay(10);
//  }
//  delay(30);
//  for (int i = servoDirectionMaxLeft ; i > servoDirectionMinRight; i--){
//    directionServo.write(i);
//    delay(10);
//  }
//  delay(30);
}

/**
 * Function to move the car forward, calling wheeldirection() to 
 * handle the direction of the front wheels.
 * The parameters will be values received from the remote control 
 * via bluetooth.
 */
void moveForward(boolean isMoving, int servoDirection){
  wheelDirection(servoDirection);
  forwardState();
  while(isMoving){
    moveForward(isMoving, servoDirection);  
  }
  stopState();
}

/**
 * Function to move the car backward, calling wheeldirection() to 
 * handle the direction of the front wheels.
 * The parameters will be values received from the remote control 
 * via bluetooth.
 */
void moveBackward(boolean isMoving, int servoDirection){
  wheelDirection(servoDirection);
  backwardState();
  while(isMoving){
    moveBackward(isMoving, servoDirection);  
  }
  stopState();
}

/**
 * Function to give an int position to the servo motor 
 * that controls the direction of the front wheel.
 */
void wheelDirection(int wheelPosition){
  directionServo.write(wheelPosition);
}

/**
 * State of the two relays when the car moves forward
 */
void forwardState(){
  digitalWrite(DCMotorPin, LOW);
  digitalWrite(DCMotorPin2, LOW);
}

/**
 * State of the two relays when the car moves backward
 */
void backwardState(){
  digitalWrite(DCMotorPin, HIGH);
  digitalWrite(DCMotorPin2, HIGH);
}

/**
 * State of the two relays when the car doesn't move
 */
void stopState(){
  digitalWrite(DCMotorPin, LOW);
  digitalWrite(DCMotorPin2, HIGH);
}
