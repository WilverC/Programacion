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
	i->siguiente = NULL; // apunta a nulo el nodo siguiente
	inicio = i; //los apuntadores inicio, fin y usuario apuntaran al primer nodo
	fin = i;
	usuario = i;
}

void lista::otro(int x){
	nodo *i = new nodo(x); //crea un nuevo nodo
	if(usuario = fin){ //verifica si el usuario se encuentra al final de la lista
		i->siguiente = NULL; //siguiente nodo apuntara a nulo
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
		system("pause");
	}else{ //no hay siguiente nodo
		cout<<"esta en el ultimo elemento";
		cout<<"valor "<<usuario->valor<<"\n";
		system("pause");
	}
}

void lista::borrar(){
	nodo *temp;
	system("cls");
	if(usuario->siguiente == NULL){ //borra el ultimo elemento
		cout<<"No hay elemento siguiente\n";
	}else{ //borra el elemento en que esta el usuario
		if(usuario->siguiente->siguiente == NULL){ //borrando el ultimo
			cout<<"elemento borrado: "<< usuario->siguiente->valor;
			delete usuario->siguiente; //borra el ultimo nodo
			usuario->siguiente = NULL; //asigna nulo a siguiente
			fin = usuario; //actualiza el apuntador de fin a usuario
		}else{ //borra el nodo donde esta el usuario
			temp = usuario->siguiente->siguiente; //asigna a al nodo temporal el nodo siguiente del nodo a borar
			delete usuario->siguiente; //se borra el nodo seguido del usuario
			usuario->siguiente = temp; //se actualiza el nodo siguiente del usuario
		}
		system("pause");
	}
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