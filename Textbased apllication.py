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
        print(vraag9())
    else: 
        print("Kies a,b of c")

    print(vraag6())


def vraag7 ():

    print("Waar ga je na Libanon naar toe?")
    print("a = Duitsland")
    print("b = Nederland")
    

    antwoord7 = input ()
    if antwoord7.lower() == "a":
        print("Dat is Munchen")
        print(vraag8())
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
        print("Kies a,b of c")

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
        print("Kies a,b of c")

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

