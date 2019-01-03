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


class Alkalmazott(Person):
    def __init__(self, first_name, last_name, phone_number, birth_year, email, szamlaszam):
        Person.__init__(self, first_name, last_name, phone_number, birth_year, email)
        self.szamlaszam = szamlaszam


class Ugyfel(Person):
    def idopont_foglalas(self):
        print "Időpont foglalva " + self.get_full_name() + " számára."


class Magyar(Person):
    def get_full_name(self):
        return self.last_name + " " + self.first_name


marissa = Alkalmazott("Marissa", "Mayer", 83483204032, 2005, "marissa@yahoo.com", 65165489454651651651651)

bruce = Ugyfel("Bruce", "Wayne", 902432309443, 1939, "bruce@batman.com")

hunor = Magyar("Hunor", "Ozsváth", 123456789, 1992, "en@dal.com")

bruce.idopont_foglalas()
print marissa.szamlaszam
print hunor.get_full_name()
print ""

emberek = {marissa, hunor}
for ember in emberek:
    print ember.get_full_name()
