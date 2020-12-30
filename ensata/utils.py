import adafruit_requests
import socketpool
import ssl
import wifi

from constants import AUTOMATIC_IP_TIME_ZONE, SSID_NAME, SSID_PASSWORD, \
                      MANUAL_TIME_ZONE, WORLD_TIME_API


# TODO(Bobby): Implement multiple wifi hotspot support + hotspot scanning
def attempt_wifi_connection() -> bool:
    try:
        wifi.radio.connect(SSID_NAME, SSID_PASSWORD)

        return True
    except ConnectionError:
        return False


# I would do -> Union[str, int] but it seems CircuitPython doesn't 
# implement the typing library :/
def get_current_time():
    if not attempt_wifi_connection():
        return "Couldn't connect to Wifi"

    pool = socketpool.SocketPool(wifi.radio)
    requests = adafruit_requests.Session(pool, ssl.create_default_context())

    if AUTOMATIC_IP_TIME_ZONE:
        response = requests.get(WORLD_TIME_API + "/ip")
    else:
        response = requests.get(WORLD_TIME_API + "/" + MANUAL_TIME_ZONE + ".txt")

    if 300 >= response.status_code > 200:
        return response.json()["unixtime"]
    else:
        return "Couldn't connect to WorldTimeAPI (" + \
               str(response.status_code) + ")"
