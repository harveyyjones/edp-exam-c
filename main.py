# University System
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

# University and Student classe
class University:
    def __init__(self, name):
        self.name = name
        self.applications = []  # List of applications
        self.queue = []         # Event queue
        print(f"Debug: University '{self.name}' initialized.")

    def apply(self, student):
        print(f"Debug: {student.name} is applying to {self.name}.")
        event = ApplicationSentEvent({"student": student.name})
        self.queue.append(event)
        print(f"Debug: ApplicationSentEvent added to queue for {student.name}.")

    def process_applications(self):
        print("Debug: Starting to process applications.")
        while self.queue:
            event = self.queue.pop(0)
            print(f"Processing application for {event.payload['student']}...")
            if isinstance(event, ApplicationSentEvent):
                # Simple logic to accept or reject
                if len(self.applications) < 5:  # Let's say we accept only 5 students
                    self.applications.append(event.payload["student"])
                    accept_event = ApplicationAcceptedEvent(event.payload)
                    print(f"Debug: Application accepted for {event.payload['student']}.")
                else:
                    reject_event = ApplicationRejectedEvent(event.payload)
                    print(f"Debug: Application rejected for {event.payload['student']}.")

class Student:
    def __init__(self, name):
        self.name = name
        print(f"Debug: Student '{self.name}' created.")

# Demonstrating the implementation
if __name__ == "__main__":
    # Initialize university and students
    university = University("Tech University")
    students = [Student(f"Student {i}") for i in range(7)]

    # Students apply to the university
    for student in students:
        university.apply(student)

    # Process applications
    university.process_applications()