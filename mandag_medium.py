''''
Oppgave 1
Opprett en klasse 'bil' med følgende egenskaper:
1.- motor  ##
2.- antall_seter
3.- farge
4.- speed
5.- max_speed
6.- dimensjon_dekk (størrelse)
7.- drivstoff
8.- dimensjon_bil
9.- konsum
10.- distance_vision
i tillegg må du implementere følgende metoder:
## lag egne variabler som påvirker egenskaper 
weather_condition()
## været påvirker mange egenskaper f.eks: konsum, max_speed, distance_vision
## lag egne variabler som påvirker egenskaper 
daylight()
## megden av lys påvirker max_speed og andre egenskaper
Hurry_up()
## Speed påvirker distnace_vision, konsum osv.
'''
class bil():
    motor = 383
    antall_seter = 2
    farge = "gul"
    speed = 420
    max_speed = 20000
    dimensjon_dekk = 50
    drivstoff = "vann"
    dimensjon_bil = 500
    konsum = 240
    disance_vision = 269

def weather_condition(weather):
    if weather == "regn":
        max_speed = 5000
        distance_vision = 69
        konsum = 230



'''
Oppgave 2
opprett en klasse motorsykkel som har følgende egenskaper:
1.- speed
2.- max_speed
3.- motorstørrelse
4.- konsum
i tillegg må du implementere følgende metoder:
asfalt_in_badConditions()
#veitilstand vil påvirke speed, max_speed og andre egenskaper.
## lag egne variabler som påvirker egenskaper 
dancing_in_the_rain()
været påvirker mange egenskaper.
## lag egne variabler som påvirker egenskaper 
like_A_ferrari()
max_speed vil påvirker konsum, men også sikkerhet i trafikken.
## lag egne variabler som påvirker egenskaper 
'''