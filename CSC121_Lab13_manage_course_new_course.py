class Course:

    def __init__(self, course_code, quota):

        """constructor creates the variables course code,
        quota, and enrollment """

        self.__course_code = course_code
        self.__quota = quota
        self.__enrollment = 0

    def add_student(self):

        if self.__enrollment >= self.__quota:
            print('Course already full')
        else:
            print("One student added")
            self.__enrollment += 1

    def drop_student(self):

        if self.__enrollment < 1:
            print("Course is empty")
        else:
            print("One student dropped")
            self.__enrollment -= 1


    def getEnrollment(self):
        return self.__enrollment

    def getCourse_code(self):
        return self.__course_code

    def getQuota(self):
        return self.__quota

    def setQuota(self, quota):
        if quota < 0:
            print("Quota cannot be negative")
        else:
            self.__quota = quota
            print("Quota changed")
