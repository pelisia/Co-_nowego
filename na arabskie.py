liczba = input("Podaj liczbę rzymską mniejszą od MMM: ")
liczba = liczba.upper()

#Napisać klasę BazaDanychPracowników
# Można dodać, usunac pracownika, zmienic jego imie, nazwisko, adres, telefon, wypłąte
# Znaleźć pracownika po takiej danej
# Znaleźć X najlepiej zarabiajacych pracownikó
# Wypisac pracownikow spelniajacych jakies kryteria
# Zapisać stan bazy do pliku i wczytać z pliku

def znajdz_czlon(tekst, dozwolone_znaki):
    czlon = []
    for znak in tekst:
        if znak in dozwolone_znaki:
            czlon.append(znak)
            continue
        break
    return ''.join(czlon)

def zamiana_na_arabskie(liczba):
    tysiace = znajdz_czlon(liczba, ["M"])
    liczba = liczba[len(tysiace):]
    setki = znajdz_czlon(liczba, ["C", "M", "D"])
    liczba = liczba[len(setki):]
    dziesiatki = znajdz_czlon(liczba, ["X", "C", "L"])
    liczba = liczba[len(dziesiatki):]
    cyfry = znajdz_czlon(liczba, ["V", "X", "I"])
    pozostałe_liczby = liczba[len(cyfry):]

    rzymskie_na_arabskie = {"": 0, "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, \
                            "X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90,
                            "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800,
                            "CM": 900, "M": 1000, "MM": 2000, "MMM": 3000}

    if len(pozostałe_liczby) != 0:
        return "Taka liczba nie istnieje!"

    else:
        return rzymskie_na_arabskie[tysiace] + rzymskie_na_arabskie[setki] + rzymskie_na_arabskie[dziesiatki] + \
           rzymskie_na_arabskie[cyfry]


print(zamiana_na_arabskie(liczba)) 
import unittest

class TestujKonwersjeArabskichNaRzymskie(unittest.TestCase):
    def test_tylko_cyfry(self):
        self.assertEqual(0, zamiana_na_arabskie(""))
        self.assertEqual(1, zamiana_na_arabskie("I"))
        self.assertEqual(2, zamiana_na_arabskie("II"))
        self.assertEqual(3, zamiana_na_arabskie("III"))
        self.assertEqual(4, zamiana_na_arabskie("IV"))
        self.assertEqual(5, zamiana_na_arabskie("V"))
        self.assertEqual(6, zamiana_na_arabskie("VI"))
        self.assertEqual(7, zamiana_na_arabskie("VII"))
        self.assertEqual(8, zamiana_na_arabskie("VIII"))
        self.assertEqual(9, zamiana_na_arabskie("IX"))

    def test_rozne_dziesiatki(self):
        self.assertEqual(10, zamiana_na_arabskie("X"))
        self.assertEqual(15, zamiana_na_arabskie("XV"))
        self.assertEqual(16, zamiana_na_arabskie("XVI"))
        self.assertEqual(19, zamiana_na_arabskie("XIX"))
        self.assertEqual(27, zamiana_na_arabskie("XXVII"))
        self.assertEqual(39, zamiana_na_arabskie("XXXIX"))
        self.assertEqual(42, zamiana_na_arabskie("XLII"))
        self.assertEqual(51, zamiana_na_arabskie("LI"))
        self.assertEqual(63, zamiana_na_arabskie("LXIII"))
        self.assertEqual(74, zamiana_na_arabskie("LXXIV"))
        self.assertEqual(85, zamiana_na_arabskie("LXXXV"))
        self.assertEqual(98, zamiana_na_arabskie("XCVIII"))
    
    def test_rozne_setki(self):
        self.assertEqual(199, zamiana_na_arabskie("CXCIX"))
        self.assertEqual(288, zamiana_na_arabskie("CCLXXXVIII"))
        self.assertEqual(377, zamiana_na_arabskie("CCCLXXVII"))
        self.assertEqual(466, zamiana_na_arabskie("CDLXVI"))
        self.assertEqual(555, zamiana_na_arabskie("DLV"))
        self.assertEqual(644, zamiana_na_arabskie("DCXLIV"))
        self.assertEqual(733, zamiana_na_arabskie("DCCXXXIII"))
        self.assertEqual(822, zamiana_na_arabskie("DCCCXXII"))
        self.assertEqual(911, zamiana_na_arabskie("CMXI"))
        
    def test_rozne_tysiace(self):
        self.assertEqual(1919, zamiana_na_arabskie("MCMXIX"))
                
if __name__ == '__main__':
    unittest.main()