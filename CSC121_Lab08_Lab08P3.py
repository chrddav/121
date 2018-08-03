print("This program creates a list of odd numbers in the range of yor choice.")
start_num = int(input("Enter a starting number: "))
end_num = int(input("Enter ending number: "))
my_list = list(i for i in range(start_num, end_num) if i % 2 == 1)
print("odd numbers in the range:", my_list)



