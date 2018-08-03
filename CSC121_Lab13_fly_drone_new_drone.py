class Drone:

    def __init__(self):

        """ constructor """

        self.__speed = 0.0
        self.__height = 0.0

    def accelerate(self):

        """ increases speed of drone """

        self.__speed = self.__speed + 10

    def decelerate(self):

        """ decreases speed of drone, speed cannot be negative """

        if self.__speed -10 < 0:
            print("Error speed cannot be negative")
            self.__speed = 0
        else:
            self.__speed = self.__speed - 10

    def ascend(self):

        """ increase height of drone """

        self.__height = self.__height + 10

    def descend(self):

        """ decrease height of drone, cannot be negative """

        if self.__height - 10 < 0:
            print("Error height cannot be negative")
            self.__height = 0
        else:
            self.__height = self.__height - 10


    def __str__(self):
        return "Speed: " + str(self.__speed) + " Height: " + str(self.__height)
