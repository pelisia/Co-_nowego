class Baza_danych_pracownikow:
    def __init__(self, imie, nazwisko, adres, telefon, wyplata, *args):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.telefon = telefon
        self.wyplata = wyplata
        self.pracownicy = list(args)
    def daj_podwyzke(self, procent):
        self.wyplata = int(self.wyplata * (1 + procent))
    def __str__(self):
        return '[Pracownik: %s, %s, %s, %s, %s]' % (self.imie, self.nazwisko, self.adres, self.telefon, self.wyplata)

if __name__ =="__main__":
    Krystian = Baza_danych_pracownikow("Krystian", "Gumulinski", "Ogrodowa", "515151515", 9000)
    print(Krystian)
    Krystian.daj_podwyzke(.20)
    print(Krystian)

