woerterbuch_deutsch = ['Apfel','Birne','Kirsche','Melone','Marille','Pfirsich']
max1 = len(woerterbuch_deutsch)

woerterbuch_english = ['apple','pear','cherry','melon','apricot','peach']
max2 = len(woerterbuch_english)

#max1 und 2 beinhalten dieselbe Zahl -> pro Durchlauf wird eine Position pro Liste überprüft

Eingabe = (input('Gib das zu übersetzende Wort ein: '))

index = 0

while index < max1:
    
    if woerterbuch_deutsch[index].lower() == Eingabe.lower(): 
        print('Übersetzung: ',woerterbuch_english[index], '(EN)') #läuft durch = max wenn nichts passendes dabei war
        break
    
    if woerterbuch_english[index].lower() == Eingabe.lower():
        print('Übersetzung: ',woerterbuch_deutsch[index], '(DE)')
        break
    
    index +=1
    
if index == max1:
    print('Übersetzung konnte nicht gefunden werden!') 