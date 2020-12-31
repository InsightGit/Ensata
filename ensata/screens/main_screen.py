import time

from adafruit_magtag.magtag import MagTag

from ensata.services.timeservices import get_current_time
from ensata.utils import center_text_x_axis

from constants import USER_NAME

class MainScreen:
    current_timestamp: int = -1
    current_timestamp_at_local: int = -1

    _magtag = None

    def __init__(self, magtag : MagTag) -> None:
        self._magtag = magtag

    def init_screen(self):
        self._magtag.graphics.set_background("/assets/icons/homebar2.bmp",
                                             (0, 92))

        current_time = get_current_time()

        if isinstance(current_time, time.struct_time):
            if current_time.tm_hour >= 17 or current_time.tm_hour < 3:
                time_text = "Good evening "
            elif current_time.tm_hour >= 12:
                time_text = "Good afternoon "
            elif current_time.tm_hour >= 3:
                time_text = "Good morning "
            else:
                time_text = "Hello "
        else:
            time_text = str(current_time) + " "

        self.current_timestamp = time.mktime(current_timestamp)
        self.current_timestamp_at_local = time.time()

        self._magtag.add_text(
            text_color=0xFFFFFF,
            text_font="/assets/fonts/RalewayBold.bdf",
            text_position=(
                center_text_x_axis(7, len(time_text)),
                10
            ),
            text_scale=1,
        )

        self._magtag.set_text(time_text + USER_NAME + "!")

        self._magtag.add_text(
            text_color=0xFFFFFF,
            text_font="/assets/fonts/RalewayRegular.bdf",
            text_position=(
                10,
                24
            ),
            text_scale=1,
        )

        self.update()

    def update(self):
        self._magtag.set_text("", index=1)
