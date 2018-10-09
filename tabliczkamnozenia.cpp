#include <iostream>

using namespace std;

int main()
{
    int liczba1 = 0, liczba2 = 0, wynik = 0;

    for(liczba2 = 10 ; liczba2 > 0 ; liczba2--){
        for(liczba1 = 1; liczba1<=10; liczba1++){
            wynik = liczba1 * liczba2;
            cout << liczba1 << "*" << liczba2 << "=" << wynik << endl;

        }
        cout << "\n";
    }

    return 0;
}
