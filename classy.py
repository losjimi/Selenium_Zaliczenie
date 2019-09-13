#Klasa to szablon
class Czlowiek(): # nazwy klas z duzej litery
    def __init__(self, imie): #konstruktor wywoluje pythonowe Metody
            print("Wywoluje sie konstruktor")
            self.imie=imie
    #cialo klasy
    gatunek = "human"
    def podskocz(self):
        print('podskoczylem')
    def __del__(self): #destruktora
            print("Do widzenia - Destruktor zadzialal")

#klasa dziecko dziedziczy po klasie czlowiek
class Dziecko(Czlowiek):
    def bawimy_sie(self):
        print("juhuuuu!")


#self dotyczy instancji klasy - czyli np marcin stworz SIEBIE
#Teraz tworzymy obiekty (instancje klasy)
marcin=Czlowiek('Marcin')
#odwolanie do metody
marcin.podskocz()
#odwolanie do atrybutu
print(marcin.gatunek)
print(marcin.imie)
del marcin
#Python konstruktora i destruktora dodaje za nas
#Metoda to funkcja w klasie
basia=Czlowiek('Barbara')
barcin=Dziecko('Barcin') # zaciaga parametry z klasy Czlowiek
print(barcin.imie)
barcin.bawimy_sie()
