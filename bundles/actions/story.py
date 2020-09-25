import yaml
from pathlib import Path
from .sound import Sound


class Story:
    def __init__(self, logger):
        self._logger = logger
        self._sound = Sound(logger)

        self._heroes = ['Hero 1']
        self._places = ['Lieu 1']
        self._objects = ['Objet 1']
        self.selects = [self._heroes, self._places, self._objects]

        with open(self._get_path() + '/stories/index.yaml') as file:
            self._stories = yaml.full_load(file)

    def _get_path(self):
        return str(Path().absolute())

    def play(self, selects):
        not_found = True

        for story in self._stories['stories']:
            keys = story['keys']
            if keys['hero'] == self._heroes[selects[0]] and keys['place'] == self._places[selects[1]] and keys['object'] == self._objects[selects[2]]:
                file = open(self._get_path() + '/stories/' + story['file'], 'r')
                self._sound.play(file.read())
                not_found = False
                break

        if not_found:
            self._sound.play('Impossible de trouver cette histoire')
