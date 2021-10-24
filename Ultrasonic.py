import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIG = 18
GPIO_ECHO = 23
GPIO_PWM = 32

GPIO.setup(GPIO_PWM, GPIO.OUT)
GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def dist():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    pwm = GPIO.PWM(GPIO_PWM, 50)
    pwm.start(0)
    
    try:
        while True:
            dist = distance()
            print ("Distance = %.1f cm" % dist)
            time.sleep(0.1)
            if dist <= 100:
                danger = 100 - dist
                pwm.ChangeDutyCycle(danger)
    except KeyboardInterrupt:
        print("stopped")
        GPIO.cleanup()
