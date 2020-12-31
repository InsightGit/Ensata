import time


from ensata.servicebase import ServiceBase

from constants import ADAFRUIT_IO_API, ADAFRUIT_IO_KEY, \
                      AUTOMATIC_IP_TIME_ZONE, MANUAL_TIME_ZONE, WORLD_TIME_API


class AdafruitIoApiService(ServiceBase):
    # Overriding ServiceBase's enabled function stub
    @staticmethod
    def enabled(self) -> bool:
        return isinstance(ADAFRUIT_IO_USERNAME, str) and \
               isinstance(ADAFRUIT_IO_KEY, str) and \
               len(ADAFRUIT_IO_USERNAME) > 0 and len(ADAFRUIT_IO_KEY) > 0

    def __init__(self):
        super(AdafruitIoApiService, self).__init__()

    # Overriding ServiceBase's get_data function stub
    def get_data(self):
        time_url = ADAFRUIT_IO_API + "/integrations/time/struct?x-aio-key=" + \
                   ADAFRUIT_IO_KEY

        if not AUTOMATIC_IP_TIME_ZONE:
            time_url += "&tz=" + MANUAL_TIME_ZONE

        response = self.requests.get(time_url)
        print(time_url)

        if 300 >= response.status_code >= 200:
            raw_json = response.json()

            print(raw_json)

            return time.struct_time(raw_json["year"], raw_json["mon"],
                                    raw_json["mday"], raw_json["hour"],
                                    raw_json["min"], raw_json["sec"],
                                    raw_json["wday"], raw_json["yday"],
                                    raw_json["isdst"])
        else:
            return str(response.status_code) + " on Adafruit API connection"


class WorldTimeApiService(ServiceBase):
    # Overriding ServiceBase's enabled function stub
    @staticmethod
    def enabled(self) -> bool:
        return True

    def __init__(self):
        super(WorldTimeApiService, self).__init__()

    # Overriding ServiceBase's get_data function stub
    def get_data(self):
        if AUTOMATIC_IP_TIME_ZONE:
            response = self.requests.get(WORLD_TIME_API + "/ip")
            print(WORLD_TIME_API + "/ip")
        else:
            response = self.requests.get(WORLD_TIME_API + "/" + \
                                         MANUAL_TIME_ZONE)
            print(WORLD_TIME_API + "/" + MANUAL_TIME_ZONE)

        if 300 >= response.status_code >= 200:
            raw_json = response.json()

            print(raw_json)

            datetime_array = raw_json["datetime"].split("T")

            date = datetime_array[0].split("-")
            time_array = datetime_array[1].split("+")[0].split(":")
            time_array[2] = time_array[2].split(".")[0]

            for date_element in date:
                date_element = int(date_element)

            for time_element in time_array:
                time_element = int(time_element)

            return time.struct_time(date[0], date[1], date[2],
                                    time_array[0], time_array[1],
                                    time_array[2], raw_json["day_of_week"],
                                    raw_json["day_of_year"],
                                    int(raw_json["dst"]))
        else:
            return str(response.status_code) + " on WorldTimeAPI connection"


SERVICE_PREFERENCE = [WorldTimeApiService, AdafruitIoApiService]


def get_current_time():
    last_error = ""

    for service in SERVICE_PREFERENCE:
        service_instance = service()

        data_result = service_instance.get_data()

        if isinstance(service_instance, time.struct_time):
            print("Using time data from service " + \
                  service_instance.__class__.__name__)
            return data_result
        else:
            print(service_instance.__class__.__name__ + " service returned " + \
                  str(data_result))
            last_error = data_result

    return last_error
