liczba = input("Podaj liczbę rzymską mniejszą od M: ")
liczba = liczba.upper()

orginał_liczba = liczba
def zamiana_na_arabskie(liczba):
        dic_liczb = {"I": 1, "II": 2, "III" : 3, "IV" : 4, "V" : 5,
                     "VI" : 6, "VII" : 7, "VIII" : 8, "IX" : 9,
                     "X" : 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}

        x = 0
        liczba_na_elementy = []
        for i in liczba:
            liczba_na_elementy.append(liczba[x])
            x += 1

        x = 0
        wartości_liczb_rzymskich = []
        y = 0
        for i in liczba_na_elementy:
            y = dic_liczb.get(liczba_na_elementy[x])
            wartości_liczb_rzymskich.append(y)
            x+=1

        suma = 0
        x = 0
        for i in wartości_liczb_rzymskich:
            suma = suma + wartości_liczb_rzymskich[x]
            x += 1
#<4;34> i <9:39>
        if orginał_liczba == "IV" or orginał_liczba == "IX" or orginał_liczba == "XXIV" or orginał_liczba=="XXXIV" or orginał_liczba=="XXIX" or orginał_liczba=="XXXIX" or orginał_liczba == "XIV" or orginał_liczba == "XIX":
            suma -= 2
#40,140,..,340 i 90,..,490
        if orginał_liczba == "XL" or orginał_liczba == "XC" or orginał_liczba == "CXL" or orginał_liczba == "CCXL" or orginał_liczba == "CCCXL" or orginał_liczba == "CCCCXL" or orginał_liczba == "CXC" or orginał_liczba == "CCXC" or orginał_liczba == "CCCXC" or orginał_liczba == "CCCCXC" :
            suma -= 20
#400,1400,...,4400 i 900,..4900
        if orginał_liczba == "MCD" or orginał_liczba == "MMCD" or orginał_liczba == "MMMCD" or orginał_liczba == "MMMMCD" or orginał_liczba == "MCM" or orginał_liczba == "MMCM" or orginał_liczba == "MMMCM" or orginał_liczba == "MMMMCM":
            suma -=200
#44,49,94,99
        if orginał_liczba == "XLIV" or orginał_liczba == "XLIX" or orginał_liczba == "XCIV" or orginał_liczba == "XCIX":
            suma -=2
#440,490,940,990,
        if orginał_liczba=="CDXL" or orginał_liczba=="CDXC" or orginał_liczba == "CMXL" or orginał_liczba == "CMXC":
            suma -= 220
#444,494,944,994,449,499,999,949
        if orginał_liczba=="CDXLIV" or orginał_liczba=="CDXCIV" or orginał_liczba == "CMXLIV"  or orginał_liczba == "CMXCIV" or orginał_liczba == "CMXCIX" or orginał_liczba == "CMXLIX" or orginał_liczba=="CDXCIX" or orginał_liczba=="CDXLIX":
            suma -= 22
#40,41....
        if liczba_na_elementy[0]== "X" and liczba_na_elementy[1] =="L":
            suma -= 20
#400,401...
        if liczba_na_elementy[0]== "C" and liczba_na_elementy[1] =="D":
            suma -= 200
#90,91...
        if liczba_na_elementy[0]== "X" and liczba_na_elementy[1] =="C":
            suma -= 20
#900,901...
        if liczba_na_elementy[0] == "C" and liczba_na_elementy[1] == "M":
                suma -= 200
        print(suma)

zamiana_na_arabskie(liczba)