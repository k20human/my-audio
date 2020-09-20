from gpiozero import LED
from signal import pause


# TODO add custom LED GPIO
class Led:
    def __init__(self, logger):
        self._logger = logger
        self._led = LED(4)

    def start(self):
        self._logger.info("LED connected")

        self._led.on()
        pause()
