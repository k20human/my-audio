from gpiozero import Button
from signal import pause
from .story import Story
from .sound import Sound
from .lights import Lights


# TODO add customs GPIO
class Choices:
    def __init__(self, logger):
        self._logger = logger
        self._story = Story(logger)
        self._sound = Sound(logger)
        self._lights = Lights(logger)

        self._select_choice = Button(pin=14, bounce_time=1)

        self._choice_pin_a = Button(5, pull_up=True)
        self._choice_pin_b = Button(6, pull_up=True)

        self._init()

    def _init(self):
        self._current_selector = 0
        self._selects = [-1, -1, -1]  # Hero / Place / Object

    def _new_increment(self, increment):
        new_increment = self._selects[self._current_selector] + increment
        choices = self._story.selects[self._current_selector]

        print(new_increment)
        print(choices)

        if new_increment >= len(choices):
            new_increment = 0
        elif new_increment <= -1:
            new_increment = len(choices) - 1

        print(new_increment)
        print(self._story.selects)

        self._selects[self._current_selector] = new_increment

        text = self._story.selects[self._current_selector][new_increment]

        self._sound.play(text)
        self._lights.display(text)

    def _select(self):
        self._logger.info("Selection")
        self._current_selector = self._current_selector + 1

        if self._current_selector == len(self._selects):
            self._story.play(self._selects)
            self._init()
        else:
            # TODO choose with array
            if self._current_selector == 1:
                self._sound.play("Maintenant, choisi ton lieu")
            elif self._current_selector == 2:
                self._sound.play("Pour finir, choisi ton objet")

    def _choice(self):
        if self._choice_pin_a.is_pressed:
            self._logger.info("1")
            self._new_increment(1)
        if self._choice_pin_b.is_pressed:
            self._logger.info("-1")
            self._new_increment(-1)

    def start(self):
        self._logger.info("Choices connected")

        self._sound.play("Bonjour, choisi ton héro")

        self._select_choice.when_released = self._select
        self._choice_pin_a.when_pressed = self._choice
        self._choice_pin_b.when_pressed = self._choice

        pause()
