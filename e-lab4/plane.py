import event
import logging

class Plane:
    counter = 0

    def __init__(self):
        self.angle = 0
        self.is_flying = False
        Plane.counter += 1
        self.number = Plane.counter

    def __str__(self):
        if self.is_flying:
            return 'Plane number {} is flying. Angle: {}'.format(self.number, self.angle)
        else:
            return 'Plane number {} is standing at the airport'.format(self.number)

    def handle(self, event):
        message = ""
        if self.is_flying:
            message = event.flight_impact(self)

    def take_off(self):
        if self.is_flying:
            logging.warning("Plane {} is already flying".format(self.number))
        else:
            print("Plane {} is taking-off".format(self.number))
            self.is_flying = True

    def land(self):
        if self.is_flying:
            print("Plane {} is landing".format(self.number))
            self.is_flying = False
        else:
            logging.warning("Plane number {} has already landed".format(self.number))

    def set_angle(self, angle):
        self.angle = angle

    def check_angle(self):
        if abs(self.angle) > 10 ** (-3):
            corr = event.Correction()
            self.handle(corr)
