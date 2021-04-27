# einfaches '=' : Zuweisung
strWetter = input("Wochenendwetter - 'sonnig' oder 'regnerisch'")
if strWetter == "sonnig":
    #Doppeltistgleich '==' ist ein Vergleichsoperator
    print("Gartenparty")
    
elif strWetter == "regnerisch":
    print("Kellerparty")
    print("Mist")
else:
    print("bitte entweder 'sonnig' oder 'regnerisch' eingeben!")