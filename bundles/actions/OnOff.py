from gpiozero import Button
from subprocess import check_call
from signal import pause


# TODO add custom button GPIO
class OnOff:
    def __init__(self, logger):
        self._logger = logger
        self._off = Button(3)

    def _shutdown(self):
        check_call(['sudo', 'poweroff'])

    def start(self):
        self._logger.info("On / Off connected")

        self._off.when_released = self._shutdown
        pause()
