#!/bin/bash
if [ $# -lt 2 -o $# -ge 5 ]; then
	echo "Liczba argumentow powinna byc niemniejsza niz 2 i niewieksza niz 4." 
elif [[ ! $1 =~ ^[0-7]{3}+$ ]]; then
	echo "Pierwszy arg. musi by prawem numerycznym np.755!"
else
 	for i in "$@"; do
		if [ $i != $1 -a $i != 'f' -a $i != 'l' -a $i != 'd' ]; then
			echo "Zly parametr. Wpisz f, l lub d" 
			exit #sprawdzanie czy f, d, l
		else 
			continue
		fi
	done
	for i in "$@"; do
		if [  $i == 'f' -a $i != $1 ]; then
			find . -type f -exec chmod $1 {} + # liczenie i wypisywanie l, d, f 
			echo  "Plikow zwyklych: $pliki"
		elif [ $i == 'd' -a $i != $1 ]; then
			find . -type d -exec chmod $1 {} + #
	
		elif [ $i == 'l' -a $i != $1 ]; then
			find . -type l -exec chmod $1 {} + #
		fi
	done
fi
