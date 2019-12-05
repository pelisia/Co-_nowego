#!/bin/bash
if [ $# -lt  2 ]; then
	echo "Podano za malo argumentow (min 2)."
elif [ -f "$1" -a -w "$1" ]; then	
	for  i in "$@"; do
		if [ -f "$i" -a -r "$i" -a -s "$i" -a $i != $1 ]; then
		      cat $i >> $1
		elif [ $i == $1 ]; then
			continue
		else
			echo "Pliki powinny by plikami zwyklymi, niepustymi oraz powinnismy posiadac prawo do ich odczytu!!"
			exit
		fi
	done
more "$1"
else 
	echo "Argument pierwszy nie jest plikiem lub nie mamy prawa do zapisu w nim"
fi
