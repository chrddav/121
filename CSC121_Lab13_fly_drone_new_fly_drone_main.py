from drone import Drone

def main():

    drone1 = Drone()

    user_input = 5
    while user_input != 0:
        user_input = int(input("Enter 1 for accelerate, 2 for decelerate, "
                               "3 for ascend, 4 for descend, 0 for exit: "))
        if user_input == 1:
            drone1.accelerate()
            print(drone1)
        elif user_input == 2:
            drone1.decelerate()
            print(drone1)
        elif user_input == 3:
            drone1.ascend()
            print(drone1)
        elif user_input == 4:
            drone1.descend()
            print(drone1)
        else:
            print("Error please input 1, 2, 3, 4, or 0")
            print(drone1)

main()
