import time

from adafruit_magtag.magtag import MagTag

from ensata.utils import get_current_time

from constants import USER_NAME

class MainScreen:
    _magtag = None

    def __init__(self, magtag : MagTag) -> None:
        self._magtag = magtag

    def init_screen(self):
        self._magtag.graphics.auto_refresh = True

        self._magtag.graphics.set_background("/assets/icons/homebar2.bmp",
                                             (0, 92))

        self._magtag.add_text(
            text_color=0xFFFFFF,
            text_font="/assets/fonts/RalewayBold.bdf",
            text_position=(
                105,
                10,
            ),
            text_scale=1,
        )

        current_timestamp = get_current_time()

        if isinstance(current_timestamp, int):
            current_time = time.localtime(current_timestamp)

            if current_time.tm_hour >= 17 or current_time.tm_hour < 3:
                time_text = "Good evening "
            elif current_time.tm_hour >= 12:
                time_text = "Good afternoon "
            elif current_time.tm_hour >= 3:
                time_text = "Good morning "
            else:
                #time_text = "Hello "
                pass
        else:
            time_text = str(current_timestamp) + " "

        self._magtag.set_text(time_text + USER_NAME + "!")

    def update(self):
        pass
