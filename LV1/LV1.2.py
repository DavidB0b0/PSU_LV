try:
    ocjena = float(input("Unesite ocjenu izmedju 0 i 1:"))
    print(ocjena);
    if (ocjena < 0 or ocjena > 1):
        raise Exception("Number not in between 0 and 1")
except:
    print("Input error")
    exit()

if (ocjena > 0.9):
    print("Vasa ocjena je A")
elif (ocjena > 0.8):
    print("Vasa ocjena je B")
elif (ocjena > 0.7):
    print("Vasa ocjena je C")
elif (ocjena > 0.6):
    print("Vasa ocjena je D")
else:
    print("Vasa ocjena je F")
