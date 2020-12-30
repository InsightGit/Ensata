from secrets import secrets

# User configuration constants
# These are probably the constants you are looking to adjust.
# TODO(Bobby): Have some-way within the app to set these(soft AP?)

# If AUTOMATIC_IP_TIME_ZONE is set to True the timezone will be determined
# from the determined location of the current public IP address. Otherwise,
# the timezone specified in MANUAL_TIME_ZONE will be used.
# Timezone list can be found here: http://worldtimeapi.org/api/timezone
AUTOMATIC_IP_TIME_ZONE = True
MANUAL_TIME_ZONE = "Asia/Tokyo"

USER_NAME = "Bobby"

# API path constants
# You probably don't need to mess with these constants unless you are getting
# various API-related errors (i.e. Connected to the Internet but can't get
# the time).
WORLD_TIME_API = "https://worldtimeapi.org/api"

# secrets.py based constants
# Adjust these constants accordingly if you have an abnormal secrets.py file.
SSID_NAME = secrets["ssid_name"]
SSID_PASSWORD = secrets["ssid_password"]
