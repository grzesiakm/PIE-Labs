# Take your partners improved solution to task_1
# And make 10 tests with unittest
# Your code should be runnable as:
# "python -m unittest test_task1"
# If there is not enough code to make 10 tests,
# or the code can't be tested you need to alter the solution,
# so that it would be possible to test it.
# How to get your partners solution:
#  1. go to your own solution on github
#  2. go the adress bar in the browser
#  4. change your username, to your partners username
#  5. enjoy the easy and cheerful task of working with someone's else code
#  6. There is no point 3
#
# On your own, you need to copy his code into this repository!!!
# Remember to include it while commiting.
#
# Fill the data here in the comments
#
# I am using solution by {GITHUB_USERNAME}
# from the commit {GIT_HASH}
#


import unittest
from plane import Plane
from event import Event, Turbulance, Correction


class TestCasePlane(unittest.TestCase):
    def setUp(self):
        self.plane = Plane()
        
    def test_construction(self):
        self.assertNotEqual(self.plane, None, msg = 'Error occurred while creating the plane.')
        
    def test_information(self):
        to_string = self.plane.__str__()
        self.assertIsInstance(to_string, str, 'Plane does not convert to string.')

    def test_init_tilt(self):
        new_plane = Plane()
        self.assertEqual(new_plane.angle, 0, 'Plane tilt angle is not initialize with 0.') 

    def test_tilt_changing(self):
        tilt = self.plane.angle
        Turbulance.flight_impact(self.plane)
        self.assertNotEqual(tilt, self.plane.angle, msg = 'Error - turbulence did not change plane angle.')

    def test_setting_angle(self):
        self.plane.set_angle(-2)
        self.assertEqual(self.plane.angle, -2, 'Setting tilt angle does not work.') 

    def test_correction(self):
        Turbulance.flight_impact(self.plane)
        Correction.flight_impact(self.plane)
        self.assertEqual(self.plane.angle, 0, 'Correction after turbulance was not fixed.') 

    def test_correction_with_positive_angle(self): 
        self.plane.set_angle(2)
        Correction.flight_impact(self.plane)
        self.assertEqual(self.plane.angle, 0, 'Correction with positive value was not fixed.') 

    def test_correction_with_negative_angle(self): 
        self.plane.set_angle(-2)
        Correction.flight_impact(self.plane)
        self.assertEqual(self.plane.angle, 0, 'Correction with negative value was not fixed.')    

    def test_taking_off(self):
        self.plane.take_off()
        self.assertEqual(self.plane.is_flying, True, 'Plane did not take off.') 

    def test_landing(self):
        self.plane.land()
        self.assertEqual(self.plane.is_flying, False, 'Plane did not land.')


if __name__ == '__main__':
    unittest.main()
