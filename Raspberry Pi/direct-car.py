import sys
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

servo_wheel = 27  # physical pin 13
servo_switch = 18  # physical pin 12
# relay = 17 #physical pin 11

GPIO.setup(servo_wheel, GPIO.OUT)
GPIO.setup(servo_switch, GPIO.OUT)
# GPIO.setup(relay,GPIO.OUT)

# servo initial setup
my_pwm = GPIO.PWM(servo_wheel, 50)
my_pwm.start((1/18.0) * 90 + 2)  # servo at 90 degrees

my_pwm_switch = GPIO.PWM(servo_switch, 50)
my_pwm_switch.start((1/18.0) * 90 + 2)  # servo at 90 degrees


# function to change the direction of the servo between 3 states: 20, 90, and 160 degrees
def dir_servo(servo, angle):
    servo.start((1/18.0) * angle + 2)


# to move forward, servo at 160 degree
def forward_state():
    dir_servo(my_pwm_switch, 160)
    time.sleep(1)


# to move backward, servo at 20 degree
def backward_state():
    dir_servo(my_pwm_switch, 20)
    time.sleep(1)


# to stop the car, servo at 90 degree
def stop_state():
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
    if dir == "^left":
        move_forward_left()
    elif dir == "^":
        move_forward_straight()
    elif dir == "^right":
        move_forward_right()
    elif dir == "vleft":
        move_backward_left()
    elif dir == "v":
        move_backward_straight()
    elif dir == "vright":
        move_backward_right()


direction = sys.argv[1]  # take the arg on command line
direct_car(direction)

GPIO.cleanup()
