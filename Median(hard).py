cisla = []
print("Vložte čísla a nakoniec stlačte klávesu ENTER pre ukončenie vkladania")

# Načítanie čísel od používateľa
while True:
    cislo_str = input("Vložte číslo: ")
    if cislo_str == "":
        break
    try:
        cislo = float(cislo_str)
        cisla.append(cislo)
    except ValueError:
        print("Neplatné číslo, skúste to znova.")

if not cisla:
    print("Neboli vložené žiadne čísla")
else:
    # Výpočet mediánu
    dlzka = len(cisla)
    if dlzka % 2 == 0:
        # Ak máme párny počet prvkov, medián je priemerom dvoch stredných prvkov
        median = (sorted(cisla)[dlzka // 2 - 1] + sorted(cisla)[dlzka // 2]) / 2
    else:
        # Ak máme nepárny počet prvkov, medián je stredný prvok
        median = sorted(cisla)[dlzka // 2]

    # Výpis odchýlok pre každé vložené číslo
    for cislo in cisla:
        odchylka = cislo - median
        if odchylka > 0:
            print(f"{int(cislo)} sa líši od mediánu o {int(abs(odchylka))}")
        elif odchylka < 0:
            print(f"{int(cislo)} sa líši od mediánu o -{int(abs(odchylka))}")
        else:
            print(f"{int(cislo)} sa líši od mediánu o 0")
