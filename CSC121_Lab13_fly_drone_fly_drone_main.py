from drone import Drone

def main():

    drone1 = Drone()

    user_input = 5
    while user_input != 0:
        user_input = int(input("Enter 1 for accelerate, 2 for decelerate, "
                               "3 for ascend, 4 for descend, 0 for exit: "))
        if user_input == 1:
            drone1.accelerate()
            print("Speed ", drone1.speed, "Height", drone1.height)
        elif user_input == 2:
            drone1.decelerate()
            print("Speed ", drone1.speed, "Height", drone1.height)
        elif user_input == 3:
            drone1.ascend()
            print("Speed ", drone1.speed, "Height", drone1.height)
        elif user_input == 4:
            drone1.descend()
            print("Speed ", drone1.speed, "Height", drone1.height)
        else:
            print("Error please input 1, 2, 3, 4, or 0")
            user_input = int(input("Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: "))
            print("Speed ", drone1.speed, "Height", drone1.height)

main()
