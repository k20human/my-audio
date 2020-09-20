from gpiozero import Button
from signal import pause


# TODO add customs GPIO
class Choices:
    def __init__(self, logger):
        self._logger = logger
        self._select_choice = Button(pin=14, bounce_time=1)

        self._choice_pin_a = Button(5, pull_up=True)  # Rotary encoder pin A connected to GPIO2
        self._choice_pin_b = Button(6, pull_up=True)

    def _select(self):
        self._logger.info("Selection")

    def _choice(self):  # Pin B event handler
        if self._choice_pin_a.is_pressed: self._logger.info("1")  # pin B rising while A is active is a clockwise turn
        if self._choice_pin_b.is_pressed: self._logger.info("-1")  # pin A rising while A is active is a clockwise turn

    def start(self):
        self._logger.info("Choices connected")

        self._select_choice.when_released = self._select
        self._choice_pin_a.when_pressed = self._choice
        self._choice_pin_b.when_pressed = self._choice

        pause()
