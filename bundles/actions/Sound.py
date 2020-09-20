from signal import pause
from gtts import gTTS
import os


# TODO add custom langage and temp folder
class Sound:
    def __init__(self, logger):
        self._logger = logger

    def play(self, message):
        self._logger.debug("Play message: " + message)

        try:
            tts = gTTS(text=message, lang="fr")

            testfile = "/tmp/temp.mp3"
            tts.save(testfile)

            os.system("mpg123 /tmp/temp.mp3")
            os.system("clear")
            os.system("rm %s" % testfile)
        except UnicodeDecodeError:
            self._logger.debug("Some characters are not supported")

    def start(self):
        self._logger.info("Sound connected")
