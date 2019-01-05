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


def list_all_vehicles(autok):
    if vehicles == []:
        print "Nincs egyetlen autó sem az állományban!"
    else:
        for index, auto in enumerate(autok):
            print "%s) %s %s with %s km driven so far. Last service date: %s" % (index+1, auto.brand, auto.model,
                                                                                 auto.km_done, auto.service_date)


def add_auto(brand, model, traveled_km, service_date, name):

    new_auto = Auto(brand=brand, model=model, traveled_km=traveled_km, service_date=service_date)

    name = Auto.append(new_auto)


def main():
    print "Üdv az autóállomány programban!"
    print ""

    vehicles = []

    with open("kocsik.txt", "r") as k_file:
        for line in k_file:
            try:
                brand, model, traveled_km, service_date, name = line.split(",")
                print brand
                print model
                traveled_km = float(traveled_km)
                print traveled_km
                print service_date
                print name
                add_auto(brand, model, traveled_km, service_date, name)
            except ValueError:
                continue

    k_file.closed()

    print list_all_vehicles(vehicles)


if __name__ == '__main__':
    main()
