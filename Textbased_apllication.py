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
        print(vraag10())
    elif antwoord11.lower() == "b":
        print("Waarom zijn jullie niet samen gevlucht?")
        print(vraag12())
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
        print(vraag9())
    elif antwoord8.lower() == "c":
        print("Dan duurt het heel lang en kan je dood gaan")
        print(vraag8())
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

