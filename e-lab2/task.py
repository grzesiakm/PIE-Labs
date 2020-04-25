import random
import time
import logging
from abc import ABC


class Event(ABC):
    def __init__(self):
        pass


class Turbulation(Event):
    def __init__(self):
        self._shift = random.gauss(0, 2*rate_of_correction)
       
    @property
    def mayday(self):
        return self._shift


class Plane(Event):
    def __init__(self, rate_of_correction):
        self._tilt = 0.0 
        self.set_tilt = 0.0
        self.rate_of_correction = rate_of_correction
        self._correction = 0.0

    def got_turbulation(self):
        self._tilt += Turbulation().mayday

    def correct_tilt(self):
        self._correction = round(self.rate_of_correction * (self.set_tilt - self._tilt), 8)
        self._tilt += self._correction

    def __str__(self):
        return f"***Current orientation: {round(self._tilt, 8)}. Correction made by {self._correction}.***\n"
                 
    def simulation(self):
        i = 0
        while True:
            self.got_turbulation()
            self.correct_tilt()
            print(plane)
            logging.info(f"Loop #{i}. Correction: {self._correction} and orientation: {round(self._tilt, 8)}\n")
            i += 1
            time.sleep(0.9)


if __name__ == "__main__":
    logging.basicConfig(filename='plane.log', filemode='w', level=logging.INFO)
    rate_of_correction = 0.4
    plane = Plane(rate_of_correction)
    try:
        plane.simulation()
    except:
        logging.error('ctrl+c used - program terminated')
