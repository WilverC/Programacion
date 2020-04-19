/*
*Autor: Leonel 
*Seguido: Cortez Enriquez Jovanny Wilver 
*Programa: lista con liga simple
*/

#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

using namespace std;

class lista{
public:
	void menu(); //menu de opciones 
};

/*Menu de instrucciones e inicio de programa*/
void lista::menu(){
	int x;
	do{
		system("cls");

		cout<<"1. INSERTAR\n";
		cout<<"2. MOSTRAR\n";
		cout<<"3. SIGUIENTE\n";
		cout<<"4. BORRAR\n";
		cout<<"5. PRIMERO\n";
		cout<<"6. ULTIMO\n";
		cout<<"7. SALIR\n";

		cout<<"Elige una opcion: ";
		cin>>x;

		switch(x){
			case 1:
				break;
			case 2:
				break;
			case 3:
				break;
			case 4:
				break;
			case 5:
				break;
			case 6:
				break;
			case 7:
				system("cls");
				cout<<"*********************\n";
				cout<<"Hasta luego\n";
				cout<<"*********************\n";
				break;
			default:
				system("cls");
				cout<<"*********************\n";
				cout<<"Opcion incorrecta\n";
				cout<<"*********************\n";
				system("pause");
		}

	}while(x != 7);
}

int main(){
    cout<<"Hola"<<endl;
    lista l1;
    l1.menu();
}