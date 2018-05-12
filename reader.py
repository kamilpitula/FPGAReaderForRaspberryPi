import RPi.GPIO as GPIO
import time

print("Starting reader press CTRL + C to exit")

clockPin = 4
dataInputPins = [5,6,13,19,26,16,20,21]

timeSleep = 0.001;

GPIO.setmode(GPIO.BCM)
mode = GPIO.getmode()
print("GPIO mode is: " + str(mode))
GPIO.setup(clockPin, GPIO.OUT)
GPIO.setup(dataInputPins, GPIO.IN)

running = True

counter = 0

try:
    f = open("output.txt","w")
    while counter < 1000:
        GPIO.output(clockPin, GPIO.HIGH)
        time.sleep(timeSleep)
        value = 0
        for i in range(0, 8):
            value += GPIO.input(dataInputPins[i]) << i
        character = str(chr(value))
        print("Value of sample {0} from GPIO: {1}".format(counter,character))
        f.write(character)
        GPIO.output(clockPin, GPIO.LOW)
        time.sleep(timeSleep)
        counter += 1
    f.close()

except KeyboardInterrupt:
    print("Keyboard interrupt")

except Exception, e:
    print "An error occurred"
    print "Error message: " + str(e)

finally:
    print("Application ends")
    GPIO.cleanup()
