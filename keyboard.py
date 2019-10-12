from dronelib.dronelib_tello import TelloDrone
from dronelib.util import save_image
from time import sleep


drone = TelloDrone()
drone.activate()

drone.takeoff()


while True:
        cmd = raw_input("w, a, s, d to control: ")

        yaw = drone.yaw
        pos = drone.position
        x = pos[0]
        y = pos[1]

        print(yaw)

        if cmd == "w":
            drone.set_target(x+1, y, yaw=yaw)

        elif cmd == "a":
            drone.set_target(x, y+1, yaw=yaw)

        elif cmd == "s":
            drone.set_target(x-1, y, yaw=yaw)

        elif cmd == "d":
            drone.set_target(x, y-1, yaw=yaw)

        elif cmd == "q":
            if yaw + 90 > 360:
                yaw = yaw + 90 - 360
            else:
                yaw = yaw + 90
            drone.set_target(x, y, yaw=yaw)

        elif cmd == "e":
            if yaw - 90 < 0:
                yaw = 360 + (yaw - 90)
            else:
                yaw = yaw - 90
            drone.set_target(x, y, yaw=yaw)

        elif cmd == "p":
            image = drone.camera_image
            save_image(image)

        elif cmd == "l":
            drone.land()
            break
        else: 
            print("what?")
