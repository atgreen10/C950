class Package:
    #Need delivery status and 2 time attributes. 1 is time the package left the hub and the other is time delivered.

    def __init__(self, packageID, address, city, state, postalCode, deadline, kilos, notes):
        self._packageID = packageID
        self._address = address
        self._city = city
        self._state = state
        self._postalCode = postalCode
        self._deadline = deadline
        self._kilos = kilos
        self._notes = notes

    def get_package_id(self):
        return self._packageID

    def get_address(self):
        return self._address

    def get_city(self):
        return self._city

    def get_state(self):
        return self._state

    def get_postalCode(self):
        return self._postalCode

    def get_deadline(self):
        return self._deadline

    def get_kilos(self):
        return self._kilos

    def get_notes(self):
        return self._notes

    def __str__(self):
        return self.get_package_id() + " " + self.get_address() + " " + self.get_city() + " " + self.get_state() + " " + self.get_postalCode() + " " + self.get_deadline() + " " + self.get_kilos() + " " + self.get_notes()

    def __repr__(self):
        return self.get_package_id() + " " + self.get_address() + " " + self.get_city() + " " + self.get_state() + " " + self.get_postalCode() + " " + self.get_deadline() + " " + self.get_kilos() + " " + self.get_notes()

