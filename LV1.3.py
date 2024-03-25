lista=[]
while True:
    user_input=input("Unesite broj ili Done :")
    if user_input.lower()=='done':
        break
    

    try:
        number=float(user_input)
        lista.append(number)
    except ValueError:
        print("Pogresan unos")

if lista:
    print("Broj brojeva koje ste unijeli :",lista)
    print("Broj unesenih brojeva :",len(lista))
    print("Srednja vrijednost :",sum(lista)/len(lista))
    print("Min vrijednost :",min(lista))
    print("Max vrijednost :",max(lista))

    lista.sort()
    print("Sortirani brojevi :", lista)

else:
    print("Niste unijeli broj")  