#-*- coding: utf-8-*-


class Auto(object):
    def __init__(self, brand, model, traveled_km, service_date):
        self.brand = brand
        self.model = model
        self.traveled_km = traveled_km
        self.service_date = service_date

    def add_km(self, new_km):
        self.traveled_km += new_km

    def update_service_date(self, new_sd):
        self.service_date = new_sd


Merci = Auto("Mercedes", "S 600", 56000, "2019.05.12")

Sport = Auto("BMW", "M3", 4000, "2019.12.30")

Adi = Auto("Audi", "S8", 156000, "2019.08.11")

Opi = Auto("Opel", "Vectra", 256000, "2019.02.25")

print Merci.brand
print Opi.traveled_km
Opi.add_km(250)
print Opi.traveled_km
print Sport.service_date
Sport.update_service_date("2020.12.30")
print Sport.service_date


