import random
import time

class Plane:
    def __init__(self):
        self._tilt = 0  # plane starts so tilt degree equals to 0

    def got_turbulation(self):
        shift = (random.gauss(0, 2*rate_of_correction) * ((90 - abs(self._tilt)) / 90))
        self._tilt += shift
        
    def correct_tilt(self):
        return self._tilt * 0.2

    def fly(self):
        correct = self.correct_tilt()
        if self._tilt <= 0:
            self._tilt += self.correct_tilt()
        else:
            self._tilt -= self.correct_tilt()
        print("Current orientation is {}. Correction made by {}.\n".format(self._tilt, correct))
           

    def simulation(self):
        while True:
            self.got_turbulation()
            self.fly()
            time.sleep(0.6)

rate_of_correction = 0.2 * 90
plane = Plane()
plane.simulation()

