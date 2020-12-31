from ensata.utils import get_new_request_session


class ServiceBase:
    requests = None

    # Whether we should even attempt to use this service
    @staticmethod
    def enabled() -> bool:
        raise NotImplementedError()

    def __init__(self):
        self.requests = get_new_request_session()

    # What data can we get from this service?
    def get_data(self):
        raise NotImplementedError()
