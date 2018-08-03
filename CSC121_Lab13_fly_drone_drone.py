class Drone:

    def __init__(self):

        """ constructor """

        self.speed = 0.0
        self.height = 0.0

    def accelerate(self):

        """ increases speed of drone """

        self.speed = self.speed + 10

    def decelerate(self):

        """ decreases speed of drone, speed cannot be negative """

        if self.speed -10 < 0:
            print("Error speed cannot be negative")
            self.speed = 0
        else:
            self.speed = self.speed - 10

    def ascend(self):

        """ increase height of drone """

        self.height = self.height + 10

    def descend(self):

        """ decrease height of drone, cannot be negative """

        if self.height - 10 < 0:
            print("Error height cannot be negative")
            self.height = 0
        else:
            self.height = self.height - 10
