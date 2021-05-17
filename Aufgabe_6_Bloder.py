#Erweitern Sie das Wörterbuch-BSP mit den geeigneten Funktionen.

woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_englisch = ["apple", "pear", "cerry", "melon", "apricot", "peach"]

    
def sucheWord(wordInput):                          #Funktion für das Suchen eines Wortes ob es nicht schon im Wörterbuch vorhanden ist.
    index = 0
    for wort in woerterbuch_deutsch:               #Wenn Wort in Woerterbuch_detsch = wordinput, dann brich ab und gib den Index aus.
        if wordInput.lower() == wort.lower():  
            break
        index +=1   
    
    if index == len(woerterbuch_deutsch):
        index=0
        for wort in woerterbuch_englisch:          #Wenn Wort in Woerterbuch_englisch = wordinput, dann brich ab und gib den Index aus.
            if wordInput.lower() == wort.lower():
                break
            index +=1    
        
        if index == len(woerterbuch_englisch):
            raise Exception("Das Wort steht nicht im Wörterbuch")   #Ansonsten gib "Das Wort steht nicht im Wörterbuch" aus. 
    return (woerterbuch_deutsch[index], woerterbuch_englisch[index], index)


def einfügenWord(deutschesWort, englischesWort):   #Funktion für das einfügen eines Wortes an einer beliebigen Stelle.
    try:
        sucheWord(deutschesWort)                   #Funktion ob Wort im Wörterbuch nicht schon vorhanden ist.
        print("Wort bereits im Wörterbuch")        #Wenn vorhanden, wird "Wort bereits im Wörterbuch" ausgegeben.  
    except:
        Stelle = input("Nach der wie vielten Stelle soll das Wort im Wörterbuch eingefügt werden?: ")   #Wenn das Wort nicht vorhanden ist, wird das Wort an einer Stelle eingefügt.
        intStelle = int(Stelle)                                 #eingebenen Wert in Integer umwandeln
        woerterbuch_deutsch.insert(intStelle, deutschesWort)    # .insert zum hinzufügen von Wörter an einer Liste
        woerterbuch_englisch.insert(intStelle, englischesWort)


def loeschenWord():
    try:
        output = sucheWord(input("Welches Wort wollen Sie löschen?: "))   #Funktion für das Suchen eines Wortes ob es nicht schon im Wörterbuch vorhanden ist.
        woerterbuch_deutsch.remove(output[0])                             # .remove für das Löschen eines Wortes
        woerterbuch_englisch.remove(output[1])
    except Exception as e:                                                #Wenn try nicht funktioniert, akzeptiere die Fehlermeldung und gib sie aus.
        print(e)
        
def uebersetzenWord():
    try:
        output = sucheWord(input("Zu übersetzendes Wort: "))              #Funktion für das Suchen eines Wortes ob es nicht schon im Wörterbuch vorhanden ist.
        print(output[0] + "[DE]")                                         #Ausgabe des zu übersetzendes Wortes mit jeweiligen Index.
        print(output[1]+ "[EN]")                                        
    except Exception as e:                                                #Wenn try nicht funktioniert, akzeptiere die Fehlermeldung und gib sie aus.
        print(e)
        
        
def eingabeBefehl():                                                      #Funktion zur Eingabe des zu anwendeteden Befehls.
    while True:                                     
        auswahl = input("Befehl? \n[E]infügen \n[L]öschen \n[A]bfrage \n[Q]uit: ")
        if auswahl.lower() == "e" or  auswahl.lower() =="l" or auswahl.lower() =="a" or auswahl.lower() =="q":   #wenn die Eingabe des Buchstaben mit einem angegebenen Buchstaben übereinstimmt,
            return auswahl.lower()                                                                               #gib diesen Buchstaben weiter
        else:
            print("Falsche Eingabe!")                                                                            #ansonst "Falsche Eingabe"
    

while True:
    auswahl = eingabeBefehl()                             
    if auswahl == "e":
        einfügenWord(input("Bitte geben Sie das einzufügende Wort zuerst auf Deutsch ein: "), input("Bitte geben Sie das zugehörende Englische Wort ein: "))
        
    elif auswahl == "l":
        loeschenWord()
    elif auswahl == "q":
        break   
    else:
        uebersetzenWord()

    print(woerterbuch_deutsch)
    print(woerterbuch_englisch)