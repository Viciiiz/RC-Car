# This is a program to control the RC car directly from the Terminal of the Raspberry Pi


import sys
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

servo_wheel = 27  # physical pin 13
servo_switch = 18  # physical pin 12
relay = 17  # physical pin 11

GPIO.setup(servo_wheel, GPIO.OUT)
GPIO.setup(servo_switch, GPIO.OUT)
GPIO.setup(relay, GPIO.OUT)

# servo initial setup
my_pwm = GPIO.PWM(servo_wheel, 50)
my_pwm.start((1/18.0) * 90 + 2)  # servo at 90 degrees

my_pwm_switch = GPIO.PWM(servo_switch, 50)
my_pwm_switch.start((1/18.0) * 90 + 2)  # servo at 90 degrees


# function to close relay and enable movement
def relay_control(state):
    if state:
        GPIO.output(relay, True)
    else:
        GPIO.output(relay, False)


# function to change the direction of the servo between 3 states: 20, 90, and 160 degrees
def dir_servo(servo, angle):
    servo.start((1/18.0) * angle + 2)


# to move forward, servo at 160 degree
def forward_state():
    relay_control(True)
    dir_servo(my_pwm_switch, 160)
    time.sleep(1)
    relay_control(False)


# to move backward, servo at 20 degree
def backward_state():
    relay_control(True)
    dir_servo(my_pwm_switch, 20)
    time.sleep(1)
    relay_control(False)


# to stop the car, servo at 90 degree
def stop_state():
    relay_control(False)
    dir_servo(my_pwm_switch, 90)
    time.sleep(1)


# to move left, servo at 160 degree
def left():
    dir_servo(my_pwm, 160)
    time.sleep(1)


# to move right, servo at 20 degree
def right():
    dir_servo(my_pwm, 20)
    time.sleep(1)


# to move straight, servo at 90 degree
def straight():
    dir_servo(my_pwm, 90)
    time.sleep(1)


def move_forward_left():
    left()
    forward_state()
    straight()
    stop_state()


def move_forward_straight():
    straight()
    forward_state()
    stop_state()


def move_forward_right():
    right()
    forward_state()
    straight()
    stop_state()


def move_backward_left():
    left()
    backward_state()
    straight()
    stop_state()


def move_backward_straight():
    straight()
    backward_state()
    stop_state()


def move_backward_right():
    right()
    backward_state()
    straight()
    stop_state()


def direct_car(dir):
    if dir == "wa":
        move_forward_left()
    elif dir == "w":
        move_forward_straight()
    elif dir == "wd":
        move_forward_right()
    elif dir == "sa":
        move_backward_left()
    elif dir == "s":
        move_backward_straight()
    elif dir == "sd":
        move_backward_right()


print("To move --> \nforward: w \nforward left: wa \nforward right: wd \nbackward: s \nbackward left: sa \nbackward right: sd\nquit: q")

while (True):
    command = input("Enter command (w, wa, wd, s, sa, sd, q): ")
    if command == "q":
        break
    direct_car(command)


direction = sys.argv[1]  # take the arg on command line
direct_car(direction)

GPIO.cleanup()
