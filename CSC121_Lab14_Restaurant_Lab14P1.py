from Dinner import Dinner_combo
from Deluxe_Dinner import Deluxe_dinner_combo


def main():
    DinnerCombo = int(input("Enter 1 for dinner combo and 2 for deluxe dinner combo: "))
    if DinnerCombo == 1:
        Dinner_Combo()
    elif DinnerCombo == 2:
        DeluxeDinnerCombo()


def Dinner_Combo():
    dinner1 = Dinner_combo()
    soup = int(input("Enter 1 for egg drop soup [$1.25] or 2 for wanton soup [$1.50]: "))
    dinner1.choose_soup(soup)
    dish = int(input("Enter 1 for sweet and sour pork [$7], 2 for sesame chicken  [$8], or 3 for shrimp fried rice [$9]: "))
    dinner1.choose_dish(dish)
    dinner1.displayOrder()


def DeluxeDinnerCombo():
    dinner1 = Deluxe_dinner_combo()
    appetizer = int(input("Enter 1 for spring roll [$1.25] or 2 for chicken wing [$1.50]: "))
    dinner1.choose_appetizer(appetizer)
    soup = int(input("Enter 1 for egg drop soup [$1.25] or 2 for wanton soup [$1.50]: "))
    dinner1.choose_soup(soup)
    dish = int(input("Enter 1 for sweet and sour pork [$7], 2 for sesame chicken [$8], or 3 for shrimp fried rice [$9]: "))
    dinner1.choose_dish(dish)
    dinner1.displayOrder()


main()
