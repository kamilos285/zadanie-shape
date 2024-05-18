#zadanie 2

from math import pi as pi

class Shape():
    
    def __init__(self):
        print("konstruktor figury")
        self.obwod = None # tworzymy zmienna ktorej wartosc mozemy potem zmienic
        self.pole = None


    def obwod1(self): 
        print("obwod to :", self.obwod)
    


    def pole1(self):
        print("pole :", self.pole)

        

class prostokat(Shape):
    
    def __init__(self, dlugi_bok, krotki_bok,):
        Shape.__init__(self) 
        self.dlugi_bok = dlugi_bok
        self.krotki_bok = krotki_bok
        self.obwod = 2 * self.dlugi_bok + 2 * self.krotki_bok # self obwod dziedziczymy z nadklasy
        self.pole = self.dlugi_bok * self.krotki_bok 
        #self.pole = dlugi_bok * krotki_bok
        #self.obwod = 2 * dlugi_bok + 2 * krotki_bok

    def __str__(self): # konstruktor string
        return f"dlugi bok tego obiektu to : {self.dlugi_bok}, krotki bok tego obiektu to : {self.krotki_bok}"


"""

    def obwod_p(self):
        print("bok A to:",self.dlugi_bok)
        print("bok B to:",self.krotki_bok)    
        print("Obwod to: ",self.Obwod_p)



    def pole_p(self):
        print("bok A to:",self.dlugi_bok)
        print("bok B to:",self.krotki_bok)
        print("Pole to: ",self.Pole_P)

"""        

class kolo(Shape):
    
    def __init__(self,promien):
        Shape.__init__(self)
        print("konstruktor kola")
        self.promien = promien
        self.obwod = 2 * pi * self.promien
        self.pole = pi * self.promien ** 2
        #self.obwod = 2 * pi * promien
        #self.pole = pi * promien ** 2

    def __str__(self):
        return f"promien tego obiektu to : {self.promien}" #fstring 
        

class trojkat(Shape):
    def __init__(self,bok1,bok2,bok3,wysokosc,podstawa):
        Shape.__init__(self)
        print("konstruktor trojkata")
        self.bok1 = bok1
        self.bok2 = bok2
        self.bok3 = bok3
        self.obwod = bok1 + bok2 + bok3
        self.wysokosc = wysokosc
        self.podstawa = podstawa
        self.pole  = wysokosc * podstawa / 2

    def __str__(self):
        return f"bok1 : {self.bok1}, bok2 : {self.bok2},  bok3 : {self.bok3}, wysokosc : {self.wysokosc}, podstawa : {self.podstawa} "


trojkat1 = trojkat(4,5,6,7,6)






prostokat1 = prostokat(5,4)

prostokat1.obwod1()

print(prostokat1)

kolo1 = kolo(5) 

kolo1.obwod1()

print(kolo1)

trojkat1 = trojkat(5,12,13,5,12)

trojkat1.obwod1()

trojkat1.pole1()

print(trojkat1)