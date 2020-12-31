import adafruit_requests
import socketpool
import ssl
import wifi

from constants import SSID_NAME, SSID_PASSWORD


# TODO(Bobby): Implement multiple wifi hotspot support + hotspot scanning
def attempt_wifi_connection() -> bool:
    try:
        wifi.radio.connect(SSID_NAME, SSID_PASSWORD)

        return True
    except ConnectionError:
        return False


def center_text_x_axis(text_size: int, letters: int) -> int:
    return (296 / 2) - (text_size * letters)


# TODO(Bobby): multi-line centering support
def center_text_y_axis(text_size: int, lines: int) -> int:
    # 128: height of e-ink MagTag display
    return (128 / 2) - (text_size * lines)


def center_text(text_size: int, letters: int, lines: int = 0):
    return (center_text_x_axis(text_size, letters),
            center_text_y_axis(text_size, lines))


# TODO(Bobby): Implement Wifi request session retention for efficency's sake
def get_new_request_session():
    if not attempt_wifi_connection():
        return "Couldn't connect to Wifi"

    pool = socketpool.SocketPool(wifi.radio)
    return adafruit_requests.Session(pool, ssl.create_default_context())
