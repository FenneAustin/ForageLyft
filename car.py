from abc import ABC, abstractmethod


class Car(Engine, Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
