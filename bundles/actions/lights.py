from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, LCD_FONT
from luma.led_matrix.device import max7219
from signal import pause
import time


# TODO add customs GPIO, size and orientation
class Lights:
    def __init__(self, logger):
        serial = spi(port=0, device=0, gpio=noop())

        self._logger = logger
        self._device = max7219(serial, width=32, height=8, block_orientation=-90)

        self._logger.info("Lights connected")

    def display(self, text):
        self._logger.debug("Display text: " + text)

        with canvas(self._device) as draw:
            show_message(self._device, text, fill="white", font=proportional(LCD_FONT), scroll_delay=0.5)
