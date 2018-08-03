class Dinner_combo:

    def __init__(self):

        """constructor creates variables to for dishes to create combos"""

        self._main_dish = 0
        self._soup = 0
        self._total = 0.0


    def choose_dish(self, dish):

        """choose between pork, chicken, or shrimp dishes"""

        self._main_dish = dish

        if self._main_dish == 1:
            self._total = self._total + 7
        elif self._main_dish == 2:
            self._total = self._total + 8
        elif self._main_dish == 3:
            self._total = self._total + 9


    def choose_soup(self, soup):

        """choose between egg drop and wanton"""

        self._soup = soup

        if self._soup == 1:
            self._total = self._total + 1.25
        elif self._soup == 2:
            self._total = self._total + 1.50


    def displayOrder(self):

        """ displays the order"""

        dish_list = ['sweet and sour pork', 'sesame chicken', 'shrimp fried rice']
        soup_list = ['egg drop soup', 'wanton soup']
        print('Items ordered: ', dish_list[self._main_dish - 1],",", soup_list[self._soup - 1])
        print("Please pay this amount:", self._total)
