class Event:
    def __init__(self, payload: dict):
        self.payload = payload
        print(f"Debug: Event created with payload: {self.payload}")

class ApplicationSentEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)
        print(f"Event: Application submitted for {payload['student']}.")

class ApplicationAcceptedEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)
        print(f"Event: Application accepted for {payload['student']}.")

class ApplicationRejectedEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)
        print(f"Event: Application rejected for {payload['student']}.") 