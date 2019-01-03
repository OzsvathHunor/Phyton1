#-*- coding: utf-8-*-
class Person(object):
    def __init__(self, first_name, last_name, phone_number, birth_year, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_year = birth_year
        self.email_address = email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def is_adult(self):  # ha 18 fölött van, akkor igaz, amúgy hamis
        return 18 <= self.get_age()

    def get_age(self):
        return 2019 - self.birth_year


john = Person(first_name="John", last_name="Clark", phone_number=89348239429, birth_year=1979, email="john@clark.com")

marissa = Person("Marissa", "Mayer", 83483204032, 2005, "marissa@yahoo.com")

bruce = Person("Bruce", "Wayne", 902432309443, 1939, "bruce@batman.com")

hunor = Person("Hunor", "Ozsváth", 123456789, 1992, "en@dal.com")

print john.birth_year
print marissa.last_name
print john.get_full_name()
print john.is_adult()
print marissa.is_adult()

contact_book = [john, marissa, bruce, hunor]

for person in contact_book:
    print person.first_name
    print person.last_name
    print person.birth_year
    print person.email_address
    print ""  # empty line
