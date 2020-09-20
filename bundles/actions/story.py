import yaml
from pathlib import Path
from .sound import Sound


class Story:
    def __init__(self, logger):
        self._logger = logger
        self._sound = Sound(logger)

        self._heroes = []
        self._places = []
        self._objects = []
        self.selects = [self._heroes, self._places, self._objects]

        with open(str(Path('.')) + '/../../stories/index.yaml') as file:
            self._stories = yaml.full_load(file)

    # TODO
    def play(self, selects):
        for item in self._stories.stories.items():
            self._logger.info("LED connected")

