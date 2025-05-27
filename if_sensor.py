# GPIO-Bibliothek laden
import RPi.GPIO as GPIO
import time

def micros():
    return round(time.time() * 1_000_000)

def run():

    # GPIO Lass IR Diode flackern
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, True)
    GPIO.cleanup()

    # GPIO 4 auslesen
    GPIO.setup(4, GPIO.IN)

    measurement_time= micros()

    # GPIO 18 (Pin 12) lesen und ausgeben
    while GPIO.input(4) and micros() - time < 3000:
        pass
    diff = micros() - measurement_time
    GPIO.cleanup()
    return diff

if __name__ == "__main__":
    # BCM-Nummerierung verwenden
    GPIO.setmode(GPIO.BCM)

    while True:
        value = run()
        print(value)