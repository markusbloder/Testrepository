# Aufgabe Python 5

# Ändern Sie das Wörterbuch-Beispiel so, dass Sie anstelle der Listen Dictionaries verwenden.
# Mittels try/except soll die Abfrage nach nicht-existenten Begriffen fehlerfrei gestaltet werden,
# bzw. die wahlweise Eingabe von deutschen od. englischen Begriffen möglich sein. Ein Ergänzung bzw.
# das Löschen von Begriffen ist nicht gefordert.

woerterbuch_deutsch = ['apfel','birne','kirsche','melone','marille','pfirsich']
woerterbuch_englisch = ['apple','pear','cherry','melon','apricot','peach']

# Umwandlung der Listen in Dictionary's
deutsch_englisch = zip (woerterbuch_deutsch,woerterbuch_englisch)
englisch_deutsch = zip (woerterbuch_englisch,woerterbuch_deutsch)
d_e = dict (deutsch_englisch)
e_d = dict (englisch_deutsch)

# Schleife für Abfrage der Dictionary's
while True:
    
    try:
        Eingabe = input ('Gib das zu übersetzende Wort ein: ')
        
        print ('Übersetzung: ', d_e[Eingabe], ' [EN]')
        break
    
    except KeyError: # 1. except: falls Wort im ersten Dictionary nicht vorhanden ist mit dem 2. abgleichen
        
        print ('Übersetzung: ', e_d[Eingabe], ' [DE]')
        break
    
    except KeyError: # 2. except falls Eingabe nicht im 2. dictionary vorhanden ist wird das Programm erneut gestartet
        
        print('Übersetzung konnte nicht gefunden werden, bitte um erneute Eingabe!')
        break
    
print ('Programm beendet.')
