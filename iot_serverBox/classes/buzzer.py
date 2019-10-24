import RPi.GPIO as GPIO  # bibliothèque pour utiliser les GPIO
from classes.GPIO import GPIO_initialize
import time              # bibliothèque pour gestion du temps
from threading import Thread

class Buzzer:
    def __init__(self,numGPIO):
        self.numGPIO = numGPIO
        GPIO.setup(numGPIO,GPIO.OUT)  # la pin 18 réglée en sortie (output)

    def on(self):
        GPIO.output(self.numGPIO,GPIO.HIGH)   # sortie au niveau logique haut (3.3 V)

    def off(self):
        GPIO.output(self.numGPIO,GPIO.LOW)   # sortie au niveau logique haut (3.3 V)

    def bip(self, sleepTime):
        self.on()
        time.sleep(sleepTime)
        self.off()

    def asyncBuzz (self, sleepTime):
        thread = Thread(target=self.bip, args=(sleepTime))
        thread.start()
        return thread

    @classmethod
    def initialize(cls):
        GPIO.setmode(GPIO.BCM)   # mode de numérotation des pins
        GPIO.setwarnings(False)

    @classmethod
    def  clean(cls):
        GPIO.cleanup()

GPIO_initialize()