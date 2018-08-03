from Dinner import Dinner_combo


class Deluxe_dinner_combo(Dinner_combo):

    def __init__(self):
        base = super()
        base.__init__()
        self._appetizer = 0

    def choose_appetizer(self, appetizer):

        """choose spring roll or chicken wing"""

        self._appetizer = appetizer

        if self._appetizer == 1:
            self._total = self._total + 1.25
        elif self._appetizer == 2:
            self._total = self._total + 1.50


    def displayOrder(self):

        """display food ordered"""

        dish_list = ['sweet and sour pork', 'sesame chicken', 'shrimp fried rice']
        soup_list = ['egg drop soup', 'wanton soup']
        appetizer_list = ['spring roll', 'chicken wing']

        print("Items order: ", dish_list[self._main_dish - 1],",", soup_list[self._soup - 1],",",appetizer_list[self._appetizer -1])
        print("Please pay this amount: ",self._total)
