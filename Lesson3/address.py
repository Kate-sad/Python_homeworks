class Address:

    def __init__(self, index, city, street, home, apartment):
        self.adressIndex = index
        self.adressCity = city
        self.adressStreet = street
        self.adressHome = home
        self.adressApartment = apartment

    def __str__(self):
        return (f"{self.adressIndex}, {self.adressCity}, {self.adressStreet}, "
                f"{self.adressHome}, {self.adressHome} - "
                f"{self.adressApartment}")
