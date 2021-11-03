def vraag22 ():

    print("Dit is mijn einde van mijn text-based applicatie.")
    print("a = Was het goed")
    print("b = Was het slecht.")


    antwoord21 = input ()
    if antwoord21.lower() == "a":
        print("Heb je nog tip voor mij wat beter kon of is hij goed.")
        print(vraag21())
    elif antwoord21.lower() == "b":
        print("Kan je me dan uitleggen wat me verbeter punten zijn.")
        print(vraag())
    else: 
        print("Kies a,b")

    print(vraag22())


def vraag21 ():

    print("Zijn jullie nu gellukig")
    print("a = Nee")
    print("b = Ja.")


    antwoord21 = input ()
    if antwoord21.lower() == "a":
        print("Waarom zijn jullie niet gelukkig?")
        print(vraag21())
    elif antwoord21.lower() == "b":
        print("Oke dat is fijn jullie kunnen werken nu aan jullie toekomst.")
        print(vraag())
    else: 
        print("Kies a,b")

    print(vraag21())


def vraag20 ():

    print("Hebben je ouders als werk?")
    print("a = Ja.")
    print("b = Nee.")
    print("c = Alleen me vader.")

    antwoord20 = input ()
    if antwoord20.lower() == "a":
        print("Oke dus allebij hebben werk gevonden.")
        print(vraag21())
    elif antwoord20.lower() == "b":
        print("Dan kunnen de huishouden niet betaalt worden.")
        print(vraag1())
   elif antwoord20.lower() == "c":
        print("Dus je vader werkt dat is goed dan let je moeder op jullie op.")
        print(vraag21())
    else: 
        print("Kies a,b of c")

    print(vraag20())


def vraag19 ():

    print("Hebben jullie al een opleiding en verblijs plek?")
    print("a = Ja.")
    print("b = Nee.")

    antwoord19 = input ()
    if antwoord19.lower() == "a":
        print("Jullie zijn nu echt gelukkig en jullie zijn compleet.")
        print(vraag20())
    elif antwoord19.lower() == "b":
        print("Dan moeten jullie dat snel doen voor jullie toekomst.")
        print(vraag19())
    else: 
        print("Kies a,b")

    print(vraag19())


def vraag18 ():

    print("Hebben jullie al een vergunning gekregen.")
    print("a = Ja.")
    print("b = Nee.")
    print("c = Bijna.")

    antwoord18 = input ()
    if antwoord18.lower() == "a":
        print("Oke jullie zijn nu gelukkig en veilig.")
        print(vraag19())
    elif antwoord18.lower() == "b":
        print("Dat is pech je moet nu oppasen want je bent zonder papieren je moet opnieuw aanvragen.")
        print(vraag17())
    elif antwoord18.lower() == "c":
        print("Oke nu wachten tot jullie antwoord hebben.")
        print(vraag19())
    else: 
        print("Kies a,b of c")

    print(vraag18())



def vraag17 ():

    print("Is iedereen van jullie familie compleet?")
    print("a = Bijna.")
    print("b = Ja.")
    print("c = Nee")

    antwoord17 = input ()
    if antwoord17.lower() == "a":
        print("Oke jullie hebben hem gesprokken en hij is onderweg.")
        print(vraag18())
    elif antwoord17.lower() == "b":
        print("oke dus jullie zijn nu gellukig en samen.")
        print(vraag16())
    elif antwoord8.lower() == "c":
        print("Waarom is je vader niet meer terug gekomen dus hij is dood gegaan.")
        print(vraag1())
    else: 
        print("Kies a,b of c")

    print(vraag17())



def vraag16 ():

    print("Zijn jullie veilig aangekomen in Nederland?")
    print("a = Ja Ja.")
    print("b = Nee Nee.")

    antwoord16 = input ()
    if antwoord16.lower() == "a":
        print("We zijn gelukkig en heel erg veilig aangekomen in Nederland we hebben niks meegemaakt.")
        print(vraag17())
    elif antwoord16.lower() == "b":
        print("We zijn niet veilig aangekomen want we hebben erige dingen meegemaakt.")
        print(vraag16())
    else: 
        print("Kies a,b")

    print(vraag16())


def vraag15 ():

    print("Hebben jullie tijd gehad om jullie spullen te pakken")
    print("a = Ja.")
    print("b = Nee.")

    antwoord15 = input ()
    if antwoord15.lower() == "a":
        print("Ja want ze zeiden tegen ons jullie zijn lief pak je spullen maar (hahaha)")
        print(vraag16())
    elif antwoord15.lower() == "b":
        print("Nee want anders zouden we de risico lopen dat we dood zouden gaan.")
        print(vraag15())
    else: 
        print("Kies a,b")

    print(vraag15())



def vraag14 ():

    print("Zijn jullie ook buiten gaan slapen?")
    print("a = Nee.")
    print("b = Ja.")

    antwoord14 = input ()
    if antwoord14.lower() == "a":
        print("Nee het was heel erg luxe en daarom was het geen probleem.")
        print(vraag15())
    elif antwoord14.lower() == "b":
        print("Ja want we hadden geen plek om te overnachten,")
        print(vraag14())
    else: 
        print("Kies a,b")

    print(vraag14())



def vraag13 ():

    print("Hebben jullie moeite gehad bij het vluchten?")
    print("a = Ja.")
    print("b = Nee.")

    antwoord13 = input ()
    if antwoord13.lower() == "a":
        print("Ja heel erg veel was wel te doen.")
        print(vraag14())
    elif antwoord13.lower() == "b":
        print("Nee was heel erg makkelijk geen problemen gehad.")
        print(vraag13())
    else: 
        print("Kies a,b")

    print(vraag13())



def vraag12 ():

    print("Onderweg kregen wij eten we hadden hoger.")
    print("a = Aangenomen.")
    print("b = Niet aangenomen.")

    antwoord12 = input ()
    if antwoord12.lower() == "a":
        print("Dan kan je nog een tijdje door.")
        print(vraag13())
    elif antwoord12.lower() == "b":
        print("Dan ga je dood door honger.")
        print(vraag11())
    else: 
        print("Kies a,b")

    print(vraag12())



def vraag11 ():

    print("Waar naar toe is hij gegaan?")
    print("a = Hij was al naar Nederland gegaan.")
    print("b = Hij komt nog.")

    antwoord11 = input ()
    if antwoord11.lower() == "a":
        print("Is hij alles van te voren gaan regelen?")
        print(vraag12())
    elif antwoord11.lower() == "b":
        print("Waarom zijn jullie niet samen gevlucht?")
        print(vraag10())
    else: 
        print("Kies a,b")

    print(vraag11())


def vraag10 ():

    print("Is hij daar gebleven?")
    print("a = Nee")
    print("b = Ja")

    antwoord10 = input ()
    if antwoord10.lower() == "a":
        print("Dat is veiliger dat hij mee is.")
        print(vraag11())
    elif antwoord10.lower() == "b":
        print("Dat is niet veilig maar is hij nog levend.")
        print(vraag11())
   
    else: 
        print("Kies a,b")

    print(vraag10())
    
    
def vraag9 ():

    print("Heb je een vader?")
    print("a = Ja")
    print("b = Nee")
 

    antwoord9 = input ()
    if antwoord9.lower() == "a":
        print("Waar is hij?")
        print(vraag10())
    elif antwoord9.lower() == "b":
        print("Dat is niet leuk geconduleerd ")
        print(vraag10())
    else: 
        print("Kies a,b")

    print(vraag9())
    
    
def vraag8 ():

    print("Met wat vlucht je")
    print("a = Auto")
    print("b = Vliegtuig")
    print("c = Lopen")

    antwoord8 = input ()
    if antwoord8.lower() == "a":
        print("Moet je grenzen voorbij dat lukt niet met vluchten.")
        print(vraag1())
    elif antwoord8.lower() == "b":
        print("Het veiligste en beste")
        print(vraag8())
    elif antwoord8.lower() == "c":
        print("Dan duurt het heel lang en kan je dood gaan")
        print(vraag9())
    else: 
        print("Kies a,b of c")

    print(vraag8())


def vraag7 ():

    print("Waar ga je na Libanon naar toe?")
    print("a = Duitsland")
    print("b = Nederland")
    

    antwoord7 = input ()
    if antwoord7.lower() == "a":
        print("Dat is Munchen denk even nog een keer na.")
        print(vraag6())
    elif antwoord7.lower() == "b":
        print("Dat is hollandse glorie")
        print(vraag8())
    else: 
        print("Kies a,b of c")

    print(vraag7())


def vraag6 ():

    print("Welke land vlucht je eerst naar toe?")
    print("a = Libanon")
    print("b = Turkije")

    antwoord6 = input ()
    if antwoord6.lower() == "a":
        print("Is een goed keuze")
        print(vraag7())
    elif antwoord6.lower() == "b":
        print("Dat is ook verstandig, denk nog een keer.")
        print(vraag5())
    else: 
        print("Kies a,b")

    print(vraag6())


def vraag5 ():

    print("Is het veilig om te vluchten")
    print("a = ja")
    print("b = Nee")
    print("c = Weet het niet")

    antwoord5 = input ()
    if antwoord5.lower() == "a":
        print("Dat is het beste")
        print(vraag6())
    elif antwoord5.lower() == "b":
        print("Dan ga je dood.")
        print(vraag1())
    elif antwoord5.lower() == "c":
        print("Je heb de goede keuze gemaakt.")
        print(vraag6())
    else: 
        print("Kies a,b of c")

    print(vraag5())


def vraag4 ():

    print("Wil je vluchten")
    print("a = Ja")
    print("b = Nee")
    print("c = Nee toch vluchten")

    antwoord4 = input ()
    if antwoord4.lower() == "a":
        print("Dat is het veiligste en verstandigste")
        print(vraag5())
    elif antwoord4.lower() == "b":
        print("Dan ga je dood")
        print(vraag1())
    elif antwoord4.lower() == "c":
        print("Vluchten is het beste keuze")
        print(vraag5())
    else: 
        print("Kies a,b of c")

    print(vraag4())


def vraag3 ():

    print("Met wie vlucht je?")
    print("a = Moeder, Zusje, Zelf")
    print("b = Zusje, Zelf")
    print("c = Moeder, Zelf")

    antwoord3 = input ()
    if antwoord3.lower() == "a":
        print("Dan gaan jullie samen.")
        print(vraag4())
    elif antwoord3.lower() == "b":
        print("Dan gaat je moeder dood.")
        print(vraag1())
    elif antwoord3.lower() == "c":
        print("Dan gaat je zusje dood")
        print(vraag1())
    else: 
        print("Kies a,b of c")

    print(vraag3())


def vraag2 ():

    print("Waarom vlucht je?")
    print("a = Ruzie familie")
    print("b = Oorlog")
    

    antwoord2 = input ()
    if antwoord2.lower() == "a":
        print("Dan ga je gewoon weg")
        print(vraag2())
    elif antwoord2.lower() == "b":
        print("Vluchten is het verstandigste")
        print(vraag3())
    else: 
        print("Kies a,b")

    print(vraag2())


def vraag1():

    print("Waar wil je naar toe vluchten")
    print("a = Europa")
    print("b = Buur landen")
    print("c = Niet vluchten")

    antwoord1 = input ()
    if antwoord1.lower() == "a":
        print("Waarom wil je naar Europa vluchten")
        print(vraag2())
    elif antwoord1.lower() == "b":
        print("Waarom wil je naar je buurlanden")
        print(vraag2())
    elif antwoord1.lower() == "c":
        print ("Dan ga je dood")
        print(vraag1())
    else: 
        print("Kies a,b of c")

print(vraag1())    

