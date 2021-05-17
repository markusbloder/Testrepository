#Aufgabe 4
#Erweitern Sie das Wörterbuch-Beispiel um die Möglichkeit, Einträge zu ergänzen bzw. ...
#... zu löschen (Fertigstellung des Beispiels aus der Online-Übung).


woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_englisch = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

max = len(woerterbuch_deutsch)

running = True
while running:

    auswahl = input("Befehl? [E]Einfügen, [L]Löschen, [A]Abfragen, [B]Beenden: ")   #Abfrage des Befehles


#Code für das EINFÜGEN von Wörtern:
    if auswahl == 'E' or auswahl == 'e':
        Stelle = input("Nach der wie vielten Stelle soll das Wort im Wörterbuch eingefügt werden?: ")
        Stelle = int(Stelle)
        DeutschesWort = input("Bitte geben Sie das einzufügende Wort zuerst auf Deutsch ein: ")
        woerterbuch_deutsch.insert(Stelle, DeutschesWort)    #.insert(Stelle, einzufügendes Wort) -> fügt ein Wort in der Liste ein
        EnglischesWort = input("Bitte geben Sie das zugehörende Englische Wort ein: ")
        woerterbuch_englisch.insert(Stelle, EnglischesWort)
        print(woerterbuch_deutsch)
        print(woerterbuch_englisch)


#Code für das LÖSCHEN von Wörtern:   
    elif auswahl == 'L' or auswahl == 'l':
        Löschwort = input("Welches Wort möchten Sie löschen?: ")
        index = 0
        while index < max:                                              
            if woerterbuch_deutsch[index].lower() == Löschwort.lower():    
                woerterbuch_deutsch.remove(woerterbuch_deutsch[index])   #.remove löscht ein Wort aus der Liste                    
                woerterbuch_englisch.remove(woerterbuch_englisch[index])
                print(woerterbuch_deutsch)
                print(woerterbuch_englisch)
                break
            index +=1
        if index == max:
            index = 0
            while index < max: 
                if woerterbuch_englisch[index].lower() == Löschwort.lower():    
                    woerterbuch_deutsch.remove(woerterbuch_deutsch[index])                      
                    woerterbuch_englisch.remove(woerterbuch_englisch[index])
                    print(woerterbuch_deutsch)
                    print(woerterbuch_englisch)
                    break
                index +=1
            if index == max:
                print("Zu löschendes Wort nicht gefunden")


#Code für das BEENDEN des Vorganges:
    elif auswahl == 'B' or auswahl == 'b':
        running = False   #hier wird der Vorgang druch das setzen von "False" beendet
   
   
#Code für das ABFRAGEN von Wörtern:   
    elif auswahl == 'A' or auswahl == 'a':
        eingabe = input("Deutscher Begriff: ")   
        index = 0   

        while index < max:                                              
            if woerterbuch_deutsch[index].lower() == eingabe.lower():    
                print(woerterbuch_englisch[index])                      
                break
            index +=1
    
        if index == max:                 
            print("nicht gefunden")
            