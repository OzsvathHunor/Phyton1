while True:
    km = float(raw_input("Kerek egy tavolsagot kilometerbe: "))
    print str(km) + " az " + str(km/1.6) + " merfold."
    akar = raw_input("Akarsz meg konvertalni? (y or n): ")
    if akar == "n":
        break