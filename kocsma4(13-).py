# -*- coding: utf-8 -*-

vilagos_sor_ar = 500
barna_sor_ar = 600

def rendeles_felvetel():
    while True:
        vilagos_sor_mennyiseg = 0;
        barna_sor_mennyiseg = 0;
        sor = raw_input("Mit kérnek? (v - világos, b - barna): ")
        if sor == "v":
            vilagos_sor_mennyiseg += 1
        elif sor == "b":
            barna_sor_mennyiseg += 1
        else:
            break

    return [vilagos_sor_mennyiseg, barna_sor_mennyiseg]


def vegosszeg_kiszamitasa(vilagos_sor_mennyiseg, barna_sor_mennyiseg, van_akcio):
    akcio = ((vilagos_sor_mennyiseg % 5) * vilagos_sor_ar) + ((barna_sor_mennyiseg % 5) * barna_sor_ar)
    if akcio > 0:
       van_akcio = True
    return (vilagos_sor_mennyiseg * vilagos_sor_ar) + (barna_sor_mennyiseg * barna_sor_ar) - akcio

def borravalo_kerese(vegosszeg):
    vegosszeg = int(raw_input("Mennyiből kérnek vissza? "))
    borravalo = vegosszeg - vegosszeg_kiszamitasa(mennyisegek[0], mennyisegek[1], False)
    return borravalo

#def blokk_nyomtatasa(vilagos_sorok_szama, barna_sorok_szama, vegosszeg, borravalo):
   # kinyomtatja a blokkot és nem tér vissza semmivel


mennyisegek = rendeles_felvetel()
vegosszeg = vegosszeg_kiszamitasa(mennyisegek[0], mennyisegek[1], False)
print  vegosszeg
borravalo = borravalo_kerese(vegosszeg)
