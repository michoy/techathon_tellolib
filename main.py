from dronelib.dronelib_tello import TelloDrone
from dronelib.util import *
from time import sleep

def main():
    drone = TelloDrone()
    drone.activate()

    drone.takeoff(1.0)

    drone.set_target(0, 0, yaw=1.57)

    print(drone.position)
    print(drone.yaw)

    image = drone.camera_image
    save_image(image)

    drone.set_target(0, 0.5)

    image = drone.camera_image
    save_image(image)

    drone.land()



if __name__ == "__main__":
        main()