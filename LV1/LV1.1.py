
def total_euro(hours, ppH):
    return hours * ppH


hours = int(input("Unesite broj radnih sati:"))
ppH = int(input("Unesite iznos place za 1 sat rada:"))
ukupno = total_euro(hours, ppH)

print("Ukupna placa : " + str(ukupno) + "€")
