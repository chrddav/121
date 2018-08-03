class Utility_bill:

    def __init__(self, name, address):

        """constructor creates utility bill"""

        self._name = name
        self._address = address
        self._total = 0.0

    def calculate_charge(self):

        """abstract method, Not Implemented Error"""

        raise NotImplementedError("Method calculate_charge not implemented")

    def display_bill(self):

        """abstract method, Not Implemented Error"""

        raise NotImplementedError("Method display_bill not implemented")
