courses = []
prompt = 'A'
while prompt in ('A', 'D'):
    prompt = input("Enter A to add course, D to drop course, and E to exit: ")
    if prompt == 'A':
        new_course = input("Enter course to add: ")
        if new_course in courses:
            print("You are already registered in that course")
        else:
            print("Course added")
            courses.append(new_course)
            courses.sort()
            print("Courses registered: ", courses)
    elif prompt == 'D':
        new_course = input("Enter course to drop: ")
        if new_course not in courses:
            print("You are not registered in that course")
        else:
            print("Course dropped")
            courses.remove(new_course)
            print("Courses registered: ", courses)
    else:
        print()



