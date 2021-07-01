#include <Servo.h>

// the servo that will direct the front wheel
const int servoDirectionPin = 11;
const int servoDirectionInitial = 90;

// the servo that will handle the ground of the DC motor
const int servoDCPin = 12;
const int servoDCInitial = 90;
const int servoDCForward = 10;
const int servoDCBackward = 170;

const int DCMotorPin = 10;        // connect to relay
const int DCMotorPinBackward = 9; // use this pin to move the car backward
const int servoMin = 10;
const int servoMax = 170;
Servo directionServo;
Servo DCServo;

void setup()
{
  Serial.begin(115200);
  directionServo.attach(servoDirectionPin);
  DCServo.attach(servoDCPin);
  pinMode(DCMotorPin, OUTPUT);
  pinMode(DCMotorPinBackward, OUTPUT);
  directionServo.write(servoDirectionInitial);
  DCServo.write(servoDCInitial);
  delay(1500);
}

void loop()
{
}

void moveForward()
{
  //delay(500);
  DCServo.write(servoDCForward);
  digitalWrite(DCMotorPin, HIGH);
}

void moveBackward()
{
  DCServo.write(servoDCBackward);
  digitalWrite(DCMotorPin, LOW);
}

/**
 * the parameter int wheelPosition will be a value received 
 * from the remote control via bluetooth.
 */
void wheelDirection(int wheelPosition)
{
  directionServo.write(wheelPosition);
}
