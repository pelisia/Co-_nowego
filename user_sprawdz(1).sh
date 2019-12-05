#!/bin/bash
if [  $# != 0 ];  then
echo 'Skrypt nie powinien przyjmowa zadnych parametrow!'
else 
zmienna=$(who | wc -l)
zmienna2=$(who | awk '{print $3, $4,  $1, $2}')
echo "Liczba zalogowanych uzytkownikow, to: $zmienna"
echo "$zmienna2"
fi
