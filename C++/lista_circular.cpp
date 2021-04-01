/*
*Autor: Leo
*Modificado: Cortez Enriquez Jovanny Wilver
*09/04/2020
*/

#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

using namespace std;

class nodo{
public:
	int valor;
	nodo *siguiente;
	nodo(int);
};

nodo::nodo(int x){
	valor=x;
}

class lista{
public:
	nodo *inicio, *fin;
	nodo *usuario;
	void menu();
	void insertar();
	void primero(int x);
	void otro(int x);
	void mostrar();
	void borrar();
	void siguiente();
	void ve_inicio();
	void ve_fin();
	lista();
};

lista::lista(){
	inicio = NULL;
	fin = NULL;
	usuario = NULL;
}

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
				insertar();
				break;
			case 2:
				mostrar();
				break;
			case 3:
				siguiente();
				break;
			case 4:
				borrar();
				break;
			case 5:
				ve_inicio();
				break;
			case 6:
				ve_fin();
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

void lista::insertar(){
	int x; //guarda el valor del nodo
	system("cls");
	cout<<"\nElemento a insertar: ";
	cin>>x;
	if(inicio==NULL)
		primero(x);
	else
		otro(x);
}

void lista::primero(int x){
	nodo *i = new nodo(x); //crea un nodo, asigna memoria
	i->siguiente = i; // el siguiente del nodo sera el mismo
	inicio = i; //los apuntadores inicio, fin y usuario apuntaran al primer nodo
	fin = i;
	usuario = i;
}

void lista::otro(int x){
	nodo *i = new nodo(x); //crea un nuevo nodo
	if(usuario == fin){ //verifica si el usuario se encuentra al final de la lista
		i->siguiente = inicio; //siguiente nodo apuntara a nulo
		fin->siguiente = i; //el siguiente de fin sera i
		fin = i; //actualiza el apuntador fin al nuevo nodo
		usuario = fin; //coloca al usuario en el nodo insertado
	}else{//si no esta al final de la lista
		i->siguiente = usuario->siguiente; //el siguiente del neuvo nodo es el siguiente donde esta el usuario
		usuario->siguiente = i; //el siguiente apuntador de usuario es el nuevo nodo
		usuario = i; //ubicamos al usuario en el nuevo nodo
	}
}

void lista::mostrar(){
	nodo *pivote; //apuntador auxiliar apara recorrer la lista
	pivote = inicio; //se coloca al inicio
	system("cls"); //lipia pantalla
	if(pivote==NULL){ //verifica si hay elementos
		cout<<"Lista vacia \n"; //imprime salida
		return;
	}
	do{
		cout<<pivote->valor<<"\n";
		pivote=pivote->siguiente;
	}while(pivote!=inicio);
	usuario=inicio; //pone apuntador del usuario al inicio
	system("pause");
}

void lista::siguiente(){
	system("cls");
	if(usuario != NULL){ //si hay nodo
		usuario = usuario->siguiente; //actualizo el apuntador del usuario
		cout<<"valor "<< usuario->valor<<"\n"; //imprime el valor
		system("pause");
	}else{ //no hay siguiente nodo
		cout<<"No hay elementos";
		system("pause");
	}
}

void lista::borrar(){
	nodo *temp;
	system("cls");
	cout<<"Elemento a borrar: "<<usuario->siguiente->valor<<"\n";
	if(usuario->siguiente == inicio){ //borra el primero
		temp=inicio->siguiente; //temp sera el siguiente de inicio
		fin->siguiente = temp; //el siguiente de fin sera el siguiente de inicio
		delete inicio; //borro inicio
		inicio = temp; //inicio sera temp
	}
	else if(usuario->siguiente == fin){ //borra el ultimo elemento
		fin = usuario; //el nuevo fin sera la posicion del usuario
		delete usuario->siguiente; //borra el siguiente de usuario
		fin->siguiente = inicio; //el siguiente de fin sera inicio
		usuario = fin; //usuario sera igual a fin
	}
	else{
		temp = usuario->siguiente; //se guarda el nodo siguiente a usuario
		usuario->siguiente = usuario->siguiente->siguiente; //el siguiente del usuario es el siguiente del siguiente del usuario
		delete temp; //boorr temp
	}
	system("pause");
}

void lista::ve_inicio(){
	system("cls");
	if(inicio==NULL){ //no hay elementos
		cout<<"No hay elementos\n";
		system("pause");
	}else{ //si hay elementos
		usuario = inicio; //actualiza el apuntador usuario al inicio
	}
}

void lista::ve_fin(){
	system("cls");
	if(fin == NULL){ //no hay elementos
		cout<<"No hay elementos\n";
		system("pause");
	}else{ //si hay elementos
		usuario = fin; // actualiza el apuntador usuario al final de la lista
	}
}

int main(){
	lista l1;
	l1.menu();
}