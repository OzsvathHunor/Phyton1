# -*- coding: utf-8 -*-

vilagos_sor_mennyiseg = 0;
barna_sor_mennyiseg = 0;
while True:
    sor = raw_input("Mit kérnek? (v - világos, b - barna): ")
    if sor == "v":
        vilagos_sor_mennyiseg +=1
    elif sor == "b":
        barna_sor_mennyiseg +=1
    else:
        break

vilagos_sor_ar = 500
barna_sor_ar = 600
vilagos_osszar = vilagos_sor_mennyiseg * vilagos_sor_ar
barna_osszar = barna_sor_mennyiseg * barna_sor_ar
akcio = ((vilagos_sor_mennyiseg % 5) * vilagos_sor_ar) + ((barna_sor_mennyiseg % 5) * barna_sor_ar)

print "A végösszeg: %s.-" % (vilagos_osszar + barna_osszar)

ossz = int(raw_input("Mennyiből kérnek vissza? "))
borravalo = ossz - vilagos_osszar - barna_osszar
if ossz < (vilagos_osszar + barna_osszar):
    ossz = vilagos_osszar + barna_osszar


print "================"
print "Lajbiszaggattó Kocsma"
print "Budapest, Árpád út 13."
print "H-P: 6:00-01:00"
print "Sz-V: 8:00-22:00"
print ""

if vilagos_sor_mennyiseg > 0:
    print "Világos  %s db %s.-" % (vilagos_sor_mennyiseg, vilagos_osszar)

if barna_sor_mennyiseg > 0:
    print "Barna    %s db %s.-" % (barna_sor_mennyiseg, barna_osszar)
if akcio > 0:
    print "Akció        -%s.-" % (akcio)
if borravalo > 0:
    print "Borravaló:    %s-" % borravalo

print ""
print "Végösszeg:    %s.-" % (ossz - akcio)

if borravalo > 0:
    print "Visszavárunk!"