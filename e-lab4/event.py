from abc import ABC, abstractmethod
import plane
import random

class Event(ABC):
    @abstractmethod
    def flight_impact():
        pass


class Turbulance(Event):
    @staticmethod
    def flight_impact(plane):
        plane.set_angle(random.gauss(0, 2 * 0.5))
        return str(plane)


class Correction(Event):
    @staticmethod
    def flight_impact(plane):
        plane.set_angle(0)
