import event
import logging
import multiprocessing
import plane
import random
import time

def simulate(plane):
    while True:
        turb = event.Turbulance()
        plane.handle(turb)
        print(plane)
        plane.check_angle()

        time.sleep(1)      

if __name__ == "__main__":

    planes = []
    processes = []

    number_of_planes = 4

    for i in range(number_of_planes):
        planes.append(plane.Plane())

    planes[1].take_off()
    planes[2].take_off()
    planes[3].take_off()
    planes[3].take_off()
    planes[3].land()


    try:
        for i in range(number_of_planes):
            planes.append(plane.Plane())
            process = multiprocessing.Process(target=simulate, args=[planes[i]])
            process.start()
            processes.append(process)

        for process in processes:
            process.join()
    except KeyboardInterrupt:
        message = "_____________________THE END_____________________"
        print(message)
        logging.debug(message)   
