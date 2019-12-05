#!/bin/bash
p=0
if [ $# -lt 1 -o  $# -gt 3 ]; then #Sprawdzanie czy liczba arg jest od 1 do 3
	echo "Liczba parametrow powinna znajodowac sie w przedziale od 1 do 3"
	let "p=1" #pokazanie ze wystapil blad, zeby nie wchodzil w drugiego ifa
else
	for i in "$@"; do
		if [ $i != 'f' -a $i != 'l' -a $i != 'd' ]; then
			echo "Zly parametr. Wpisz f, l lub d" #sprawdzanie czy f, d, l
			let "p=1"
		else
			continue
		fi
	done
fi

if [ "$p" -eq 0 ]; then
 	for i in "$@"; do
		if [  $i == 'f' ]; then
			pliki=$(ls -l | grep '^-'| wc -l) # liczenie i wypisywanie l, d, f 
			echo  "Plikow zwyklych: $pliki"
		elif [ $i == 'd' ]; then
			katalogi=$(ls -l | grep '^d' | wc -l)
			echo "Katalogow: $katalogi"
		elif [ $i == 'l' ]; then
			dowiazania=$(ls -l | grep '^l' | wc -l)
			echo "Dowiazan symbolicznych: $dowiazania"
		fi
	done
	echo -e "\n"
	for i in "$@";do
		if [ $i == 'f' ]; then
			echo -n -e  "\nPliki: "
			for i in $(seq 1 $pliki); do
				echo -n  "+"
				 done
		elif [ $i == 'd' ]; then #wyswietlanie tyle plusow ile jest f, d, l
			echo -n -e  "\nKatalogow: "
			for i in $(seq 1 $katalogi); do
				echo -n "+"
				done
		elif [ $i == 'l' ]; then
			echo -n -e " \nDowiazania symboliczne "
			for i in $(seq 1 $dowiazania); do
				echo -n "+"
				done
		fi
	done
	echo -e "\n"
fi
 
