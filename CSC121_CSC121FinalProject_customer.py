class Customer:

    def __init__(self, email):

        """creates instance of customer object"""

        self.__last_name = ""
        self.__first_name = ""
        self.__age = 0
        self.__email = email
        self.__password = ""
        self.__card_number = ""
        self.__security_code = ""

    def Input_age(self):
        age_valid = True
        while age_valid == True:
            negative_valid = True
            numeric_valid = True
            age = input('Enter age: ')
            if age.isnumeric() == False:
                numeric_valid = False
                print('Age must be a number')
            if numeric_valid == True:
                if int(age) < 0:
                    negative_valid = False
                    print('Age cannot be negative.')
            if negative_valid == True and numeric_valid == True:
                age_valid = False
        self.__age = int(age)
        print()

    def Input_password(self):
        print("Your password must be 8-12 characters long containing at least one upper-case letter, one lower-case letter and one number.")
        password_valid = True
        while password_valid == True:
            password = input('Enter password: ')
            length_valid = True
            digit_valid = True
            alpha_valid = True
            lower_valid = True
            upper_valid = True
            if len(password) < 8:
                length_valid = False
                print("Your password must be at least 8 characters long.")
            if len(password) > 12:
                length_valid = False
                print("Your password must be no greater than 12 characters.")
            if password.isdigit() == True:
                digit_valid = False
                print("Your password ")
            if password.isalpha() == True:
                alpha_valid = False
                print("Your password must contain digits and letters.")
            if password.islower() == True:
                lower_valid = False
                print("Your password must contain upper-case and lower-case letters.")
            if password.isupper() == True:
                upper_valid = False
                print("Your password must contain upper-case and lower-case letters.")
            if length_valid == True and digit_valid == True and alpha_valid == True and lower_valid == True and upper_valid == True:
                password_valid = False
        self.__password = self.__password + password
        print("Valid password.")
        print()


    def input_card_number(self):
        card_valid = True
        while card_valid == True:
            num_valid = True
            len_valid = True
            card_num = input("Enter 16 digit credit card number: ")
            if card_num.isdigit() == False:
                print("Card number must only be numbers")
                num_valid = False
            if len(card_num) != 16:
                print("Card number must be 16 digits.")
                len_valid = False
            if num_valid == True and len_valid == True:
                card_valid = False
            self.__card_number = card_num
        print()

    def input_security_code(self):
        security_valid = True
        while security_valid == True:
            len_valid = True
            digit_valid = True
            security_code = input("Enter three digit security code: ")
            if len(security_code) != 3:
                print("PIN must be three digits long. ")
                len_valid = False
            if security_code.isdigit() == False:
                print("PIN must be three digits.")
                digit_valid = False
            if len_valid == True and digit_valid == True:
                security_valid = False
        self.__security_code = security_code
        print()

    def input_info(self):
        first_name = input("Enter first name: ")
        self.__first_name = first_name
        last_name = input("Enter last name: ")
        self.__last_name = last_name
        self.Input_age()
        self.Input_password()
        self.input_card_number()
        self.input_security_code()

    def verify_info(self):
        change_v = 1
        while change_v != 0:
            print("1. First Name: ", self.__first_name)
            print("2. Last Name: ", self.__last_name)
            print("3. Email Address: ", self.__email)
            print("4. Password: ", self.__password)
            print("5. Age: ", str(self.__age))
            print("6. Card Number: ", str(self.__card_number))
            print("7. Security Code: ", str(self.__security_code))
            print()
            change_v = int(input("To correct any entry, enter the number and press RETURN. If everything is correct press 0:"))
            print()
            if change_v == 1:
                self.__first_name = input("Enter first name: ")
            if change_v == 2:
                self.__last_name = input("Enter last name: ")
            if change_v == 3:
                self.__amil = input("Enter email address: ")
            if change_v == 4:
                self.Input_password()
            if change_v == 5:
                self.Input_age()
            if change_v == 6:
                self.input_card_number()
            if change_v == 7:
                self.input_security_code()
        print("Registration and verification completed for this customer.")

    def output_info(self):
        customer_info = ""
        customer_info = customer_info + self.__first_name + " "
        customer_info = customer_info + self.__last_name + " "
        customer_info = customer_info + str(self.__age) + " "
        customer_info = customer_info + self.__email + " "
        customer_info = customer_info + self.__password + " "
        customer_info = customer_info + self.__card_number + " "
        customer_info = customer_info + self.__security_code + "\n"
        return customer_info


