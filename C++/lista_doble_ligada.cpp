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

//Clase que tiene la informacion de un nodo de la lista
class nodo{
public:
	int valor; //valor contenedor
	nodo *siguiente; //el apuntador al siguiente nodo
	nodo *anterior; //apunta al nodo anterior
	nodo(int); //constructor 
};

//Definicion del contructor
nodo::nodo(int i){
	valor = i; //asigna valor a un nodo determinado
}
/*-----------------------------------------------------------------------*/

//Una lista :v
class lista{
public:
	nodo *inicio, *fin; //aputnadores a inicio y fin de la lista
	nodo *usuario; //guarda la posicion en la que esta el usuario
	void menu(); //menu de opciones 
	void insertar(); //inserta un elemento en la lista
	void primero(int x); //inserta el primer elemento de la lista
	void otro(int x); //coloca el elemento en cualquier posicion que no es el inicio
	void mostrar(); //muestra el contenido de toda la lista
	void siguiente(); //mueve el apuntador del usuario a la siguiente posicion
	void anterior(); //mueve el apuntador del usuario al elemento anterior
	void borrar(); //borra el nodo de la lista
	void ve_inicio(); //mueve el apuntador del usuario al inicio de la lista
	void ve_fin(); // mueve el apuntador del usuario al final de la lista
	lista(); //constructor
};

//inicializacion de datos de la lista
lista::lista(){
	inicio = NULL;
	fin = NULL;
	usuario = NULL;
}

/*funciones publicas de la clase lista*/
void lista::menu(){
	int x;
	do{
		system("cls");

		cout<<"1. INSERTAR\n";
		cout<<"2. MOSTRAR\n";
		cout<<"3. SIGUIENTE\n";
		cout<<"4. ANTERIOR\n";
		cout<<"5. BORRAR\n";
		cout<<"6. PRIMERO\n";
		cout<<"7. ULTIMO\n";
		cout<<"8. SALIR\n";

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
				anterior();
				break;
			case 5:
				borrar();
				break;
			case 6:
				ve_inicio();
				break;
			case 7:
				ve_fin();
				break;
			case 8:
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

	}while(x != 8);
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
	i->siguiente = NULL; // apunta a nulo el nodo siguiente
	i->anterior = NULL; //apunta a nulo el nodo anterior
	inicio = i; //los apuntadores inicio, fin y usuario apuntaran al primer nodo
	fin = i;
	usuario = i;
}

void lista::otro(int x){
	nodo *i = new nodo(x); //crea un nuevo nodo
	if(usuario = fin){ //verifica si el usuario se encuentra al final de la lista
		i->siguiente = NULL; //siguiente nodo apuntara a nulo
		i->anterior = fin; // su predecesor sera fin
		fin->siguiente = i; //el siguiente de fin sera i
		fin = i; //actualiza el apuntador fin al nuevo nodo
		usuario = fin; //coloca al usuario en el nodo insertado
	}else{//si no esta al final de la lista
		i->siguiente = usuario->siguiente; //el siguiente del neuvo nodo es el siguiente donde esta el usuario
		usuario->siguiente->anterior = i; //predecesor del siguiente de usuario sera el nuevo nodo
		usuario->siguiente = i; //el siguiente apuntador de usuario es el nuevo nodo
		i->anterior = usuario; //el anterior del nuevo nodo sera el usuario
		usuario = i; //ubicamos al usuario en el nuevo nodo
	}
}

void lista::mostrar(){
	nodo *pivote; //apuntador auxiliar apara recorrer la lista
	pivote = inicio; //se coloca al inicio
	system("cls"); //lipia pantalla
	while(pivote!=NULL){ //imprimira el pivote mientras no sea nulo
		cout<< pivote->valor << "\n"; //imprime valor
		pivote = pivote->siguiente; //se mueve al siguiente nodo
	}
	usuario=inicio; //pone apuntador del usuario al inicio
	system("pause");
}

void lista::siguiente(){
	system("cls");
	if(usuario->siguiente != NULL){ //si hay nodo siguiente
		usuario = usuario->siguiente; //actualizo el apuntador del usuario
		cout<<"valor "<< usuario->valor<<"\n"; //imprime el valor
	}else{ //no hay siguiente nodo
		cout<<"esta en el ultimo elemento";
		cout<<"valor "<<usuario->valor<<"\n";
	}
	system("pause");
}

void lista::anterior(){
	system("cls");
	if(usuario->anterior == NULL){ //si no hay nodo anterior
		cout<<"Esta en el primer elemento";
		cout<<"valor "<<usuario->valor<<"\n";
	}else{ //no hay siguiente nodo
		usuario = usuario->anterior;
		cout<<"elemento anterior: "<<usuario->valor<<"\n";
	}
	system("pause");
}

void lista::borrar(){
	nodo *temp;
	system("cls");
	cout<<"Elemento a borrar: "<<usuario->valor<<"\n";
	if(usuario == inicio){ //borra el primero
		inicio = usuario->siguiente; //inicio va a ser igual al siguiente del inicio
		inicio->anterior = NULL; //el anterior de inicio va a valer nulo
		usuario = inicio; //y el usuario se queda en el primer elemento
		delete usuario->anterior; //borro el nodo
	}
	else if(usuario == fin){ //borra el ultimo elemento
		fin = usuario->anterior; //el nuevo fin sera la posicion del usuario
		fin->siguiente = NULL; //el siguiente de fin es nulo
		usuario = fin; //usuario sera igual a fin
		delete usuario->siguiente; //borro el ultimo elemento
	}
	else{
		usuario->anterior->siguiente = usuario->siguiente; //el siguiente del anterior del usuario sera el siguiente de usuario
		usuario->siguiente->anterior = usuario->anterior; //el anterior del usuario siguientesera el anterior del usuario
		temp = usuario->anterior; //se guarda el nodo siguiente a usuario
		delete usuario; //borra usuario
		usuario = temp; //
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