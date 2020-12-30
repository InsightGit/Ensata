from constants import SSID_NAME, SSID_PSW, WEATHER_URL

from main_screen import MainScreen

from adafruit_magtag.magtag import MagTag

import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests
import json
import time

current_screen = None
magtag = MagTag()

def set_text(text: str, line: int) -> None:    
    magtag.add_text(
        text_position=(
            0,
            50 + (line * 5),
        ),
        text_scale=1
    )
    
    magtag.set_text(text)
    

def main() -> None:
    print("Connecting to %s"%SSID_NAME)
    try:
        wifi.radio.connect(SSID_NAME, SSID_PSW)
    except:
        magtag.exit_and_deep_sleep(2)
    print("Connected to %s!"%SSID_NAME)
    print("My IP address is", wifi.radio.ipv4_address)
     
    
    pool = socketpool.SocketPool(wifi.radio)
    requests = adafruit_requests.Session(pool, ssl.create_default_context())
    
    print("Fetching json from", WEATHER_URL)
    
    response = requests.get(WEATHER_URL)
    
    if response.status_code < 200 or response.status_code >= 300:
        if response.status_code == 500:
            set_text("Got 500 status! Kuuki might be down!", 0)
        
        magtag.exit_and_deep_sleep(60)
    
    json_dict = response.json()
    
    set_text(json_dict["TimeData"] + "\n" + \
             "Temperature: " + str(json_dict["Temp"]) + " C\n" + \
             "Humidity: " + str(json_dict["Humid"]) + " %\n" + \
             "Air Pressure: " + str(json_dict["AirPressure"]) + "\n" + \
             "PM25Standard/Env: " + str(json_dict["PM25Standard"]) + " / " + str(json_dict["PM25Env"]) + "\n" + \
             "PM100Standard/Env: " + str(json_dict["PM100Standard"]) + " / " + str(json_dict["PM100Env"]), 0)
    
    magtag.exit_and_deep_sleep(60)
        

if __name__ == "__main__":
    main()
