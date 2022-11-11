from matplotlib import pyplot # Install matplotlib før du begynner med oppgavene 

'''
oppgave 1
    Anne har laget et program som skal regne ut hvor mye mel ho trenger til å lage a antall liter vaffelrøre.
'''
a = 2
b = (str( a * 4.5))
print("Du trenger", b, " dl mel. ")

'''
Anne prøver å taste inn 4.5 liter vaffelrøre, men programmet skriver ut en feilmelding til skjermen.
Hjelp Anne med koden slik at den vil fungere også med desimaltall.
'''
#####################################################################################################################
'''
Oppgave 2
Kari har gjort en undersøkelse i klassen sin og spurt klassekameratene hvilke type kjæledyr de har hjemme.
Svarene ble:
Katt: 7
Hund: 5
Fugl: 3
Andre dyr: 4
Ingen:6
Kari ønsker å lage et Python- program der ho kan taste inn frekvensene til de ulike observasjonene og
hun vil at programmet skal skrive ut et stolpediagram til skjermen.
'''
   
x = ["katt", "hund","fugl","andre dyr","ingen dyr"] #lager en liste x med 5 elementer 
y = [0,1,2,3,4] #lager en liste y med frekvensene til elementene i liste x¨
print ("Hvor mange har katter: ")
y[0] = input()
print ("Hvor mange har hunder: ")
y[1] = input()
print ("Hvor mange har fugler: ")
y[2] = input()
print ("Hvor mange har andre dyr: ")
y[3] = input()
print ("Hvor mange har ingen dyr: ")
y[4] = input()
z = y
z.sort
pyplot.bar(x,z) # lager stolpediagram  med elementene fra x og y
pyplot.show() # skriver diagrammet til skjermen


#############################################################################################################################
'''
oppgave 3
Kjør programmet og forklar hva det gjør.
SVAR: den printer ut alle tallene fra 7 og opp til 32, men den skriver ikke 32. den tar alle tallene fra -10 og opp til 10 untom å printe 10

Prøv å skriv ut heltall fra og med 7 til og med 32
Prøv å skriv ut heltall fra og med -10 til og med 10
'''
for tall in range (-10,10):
    print(tall)

###############################################################################################################################

'''
oppgave 4
Kjør programmet og forklar hva det gjør.
SVAR: først så printer den m til venstre som er alle numberene opp til 10 utenom og printe 10. så printer den 3 ganger m til høyre som kjør sånn at om m = 3 så ganger den seg med 3.
om jeg skriver inn 6 istedenfor så tar den m som kan være 7 så ganger den med 6.

Endre 3 tallet til andre tall og se hva som skjer.
'''
for m in range (10):
    print(m, 6*m)

################################################################################################################################

'''
Oppgave 5
Kari har laget et program der bruker kan taste inn alder å få skrevet ut pris på kinobillett til skjermen.
Kjør programmet og forklar hvordan det fungerer.
SVAR:den printer ut pris g = 0 om allderen er unnder 6. eller om alderen er mellom 6-12 så printer den ut pris b = 80. osv... opp til pris v = 120

Kinoen kommer med en tilbud til de mellom 18 og 25 år på 110 kroner per billett.
Gjør endringer på koden slik at det blir tilpasset tilbudet.
'''

b = 80  # pris for en billett barn(6-12 år)
u = 100 # pris for en billett ungdom(13-17)
c = 110 
v = 120 # pris for en billett voksen
g = 0   # under 6 år er gratis
alder = int(input("Tast inn alder: "))
if alder <= 5:
  pris = g
elif alder > 5 and alder < 13: 
  pris = b
elif alder > 12 and alder < 18:
  pris = u
elif alder > 17 and alder < 26:
  pris = c
else:
  pris = v
print("Prisen blir", pris, "kroner. ")

########################################################################################################################################

'''
Oppgave 6
En dag i Moss var det følgende temperaturer:
Klokkeslett - grader
kl 06.00 - 12
kl 12.00 - 14
kl 18.00 - 20
kl 22.00 - 21
Lag et linjediagram over temperaturutviklingen.
Tips: Bruk det du har lært i koden over i tillegg til det under.
'''
x = [12, 14, 20, 21] # lag en liste for klokkeslett
y = [6.00, 12.00, 18.00, 22.00] # lag en liste for temperaturen
pyplot.plot(x,y) # lager linjediagram med elementene fra x og y 
pyplot.show()