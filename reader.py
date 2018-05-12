import RPi.GPIO as GPIO
import time

print("Starting reader press CTRL + C to exit")

clockPin = 4
dataInputPins = [5,6,13,19,26,16,20,21]

timeSleep = 1;

GPIO.setmode(GPIO.BCM)
mode = GPIO.getmode()
print("GPIO mode is: " + str(mode))
GPIO.setup(clockPin, GPIO.OUT)
GPIO.setup(dataInputPins, GPIO.IN)

running = True

counter = 0

try:
    while counter < 5:
        GPIO.output(clockPin, GPIO.HIGH)
        time.sleep(timeSleep)
        value = 0
        for i in range(0, 8):
            value += GPIO.input(dataInputPins[i]) << i
        print("Value from GPIO: {0}".format(str(value)))
        GPIO.output(clockPin, GPIO.LOW)
        time.sleep(timeSleep)
        counter += 1

except KeyboardInterrupt:
    print("Keyboard interrupt")

except Exception, e:
    print "An error occurred"
    print "Error message: " + str(e)

finally:
    print("Application ends")
    GPIO.cleanup()
