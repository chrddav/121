iterations = 0
initial_salary = int(input("Enter starting salary: "))
Salary = 0
retire_fund = 0
while iterations < 10:
    Salary = initial_salary * (1.02 ** iterations)
    retirement = Salary * 0.05
    retire_fund = retirement + retire_fund
    iterations = iterations + 1
    print("Year:", iterations, "Salary:", Salary)
    print("Retirement Fund Total:", retire_fund)
    print()  # insert a blank line to separate the quarters

