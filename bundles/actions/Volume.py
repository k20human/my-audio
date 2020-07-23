from gpiozero import Robot
import time


class Volume:
    def __init__(self, logger):
        self._logger = logger
        #self._robot = Robot(left=(24, 23, 21), right=(20, 16, 18))

    # def _up(self):
    #     self._robot.forward()
    #     time.sleep(2)
    #     self._robot.stop()
    #     print('up')


    def start(self):
        self._logger.info("Volume connected")
