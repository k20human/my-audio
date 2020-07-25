from gpiozero import MCP3008
import time
import alsaaudio

# TODO add custom config for volume manager
class Volume:
    def __init__(self, logger):
        self._logger = logger
        self._volume = 0
        self._system_volume = alsaaudio.Mixer()
        self._volume_manager = MCP3008(channel=0, clock_pin=21, mosi_pin=20, miso_pin=19, select_pin=18)

    def start(self):
        self._logger.info("Volume connected")

        while True:
            new_volume = self._volume_manager.value
            self._logger.debug("Volume pot:" + str(new_volume))

            if self._volume != new_volume:
                self._volume = new_volume
                self._system_volume.setvolume(int(round(self._volume * 100)))

            time.sleep(0.5)
