def main():
    number_of_labs = int(input("How many labs? "))
    lab_scores = []
    i = 0
    while i < number_of_labs:
        lab_scores.append(float(input("Enter a lab score: ")))
        i = i + 1
    print("Lab scores: ", lab_scores)
    number_of_tests = int(input("How many tests? "))
    test_scores = []
    j = 0
    while j < number_of_tests:
        test_scores.append(float(input("Enter a test score: ")))
        j = j + 1
    print("Test scores: ", test_scores)
    print()
    print("The default weights for course grade are 50% labs and 50% tests")
    weight = input("Enter C to change the weights or D to use default weights: ")
    if weight == 'C':
        lab_weight = float(input("Enter lab percentage (without the % sign): "))
        test_weight = float(input("Enter test percentage (without the % sign): "))
        grade_calculator(lab_scores, test_scores, c = lab_weight, d = test_weight)
    else:
        grade_calculator(lab_scores, test_scores)


def grade_calculator(lab_scores, test_scores, c=50, d=50):
    lab_total = 0
    lab_length = len(lab_scores)
    for value in lab_scores:
        lab_total = lab_total + value
    lab_average = lab_total / lab_length
    print("Lab average: ", format(lab_average, '.2f'))
    test_total = 0
    test_length = len(test_scores)
    for value in test_scores:
        test_total = test_total + value
    test_average = test_total / test_length
    print("Test average: ", format(test_average, '.2f'))
    course_grade = ((int(lab_average) * c)+(int(test_average) * d)) / 100
    print("Course grade: ", course_grade)


main()
