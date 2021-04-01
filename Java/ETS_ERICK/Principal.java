//Clase principal con el menu

import java.util.Scanner;

public class Principal{

	private static int numQueja = 5;

	public static int menu(){
		Scanner scan = new Scanner( System.in );
		int dato;
		System.out.println("1. Agregar Queja General ");
		System.out.println("2. Agregar Queja Area ");
		System.out.println("3. Agregar Queja Grafica ");
		System.out.println("4. Mostrar Queja ");
		System.out.println("5. Salir ");
		dato = scan.nextInt();
		if( dato <= 0 && dato >= 6 )
			dato = 0;
		return dato;
	}

	public static String[] obtenerDatos(){
		Scanner scan = new Scanner( System.in );
		String datos[] = new String[4];
		System.out.println("******************************************");
		System.out.println(" Nombre de la queja: ");
		datos[0] = scan.nextLine();
		System.out.println(" mensaje: ");
		datos[1] = scan.nextLine();
		System.out.println(" fecha: ");
		datos[2] = scan.nextLine();
		System.out.println(" ¿quien es usted?: ");
		datos[3] = scan.nextLine();
		System.out.println("******************************************");
		return datos;
	}

	public static String obtenerArea(){
		Scanner scan = new Scanner( System.in );
		String area;
		System.out.println(" Nombre del area de queja: ");
		area = scan.nextLine();

		return area;
	}

	public static String obtenerImagen(){
		Scanner scan = new Scanner( System.in );
		String url;
		System.out.println(" url de la imagen: ");
		url = scan.nextLine();

		return url;
	}

	public static void main(String args[]){
		int pos;
		int contq = 0;
		int contqa = 0;
		int contqi = 0;
		String datos[];
		//arreglo de las quejas
		Queja q[] = new Queja[ numQueja ];
		QuejaArea qa[] = new QuejaArea[ numQueja ];
		QuejaImagen qi[] = new QuejaImagen[ numQueja ];

		do {
			pos = menu();
			if( pos == 1 ){
				System.out.println( contq );
				if( contq < 5 ){
					datos = obtenerDatos();
					q[contq] = new Queja( datos[0], datos[1], datos[2], datos[3] );
					contq ++;
				}else{
					System.out.println("Maximo de quejas generadas");
				}
			}else if( pos == 2 ){
				if( contqa < 5 ){
					datos = obtenerDatos();
					String area = obtenerArea();
					qa[contqa] = new QuejaArea( datos[0], datos[1], datos[2], datos[3], area );
					contqa ++;
				}else{
					System.out.println("Maximo de quejas generadas");
				}
			}else if ( pos == 3 ) {
				if( contqi < 5 ){
					datos = obtenerDatos();
					String url = obtenerImagen();
					qi[contqi] = new QuejaImagen( datos[0], datos[1], datos[2], datos[3], url );
					contqi ++;
				}else{
					System.out.println("Maximo de quejas generadas");
				}
			}else if( pos == 4 ){
				int i;

				System.out.println(" Quejas Generales ");
				for( i = 0; i < contq; i++ ){
					System.out.println("******************************************");
					System.out.println(" Queja Numero: " + (i+1) );
					System.out.println( q[i].mostrar_queja() );
					System.out.println("******************************************");
				}
				
				System.out.println(" Quejas de Areas ");
				for( i = 0; i < contqa; i++ ){
					System.out.println("******************************************");
					System.out.println(" Queja Numero: " + (i+1) );
					System.out.println( qa[i].mostrar_qarea() );
					System.out.println("******************************************");
				}
				
				System.out.println(" Quejas por imagen ");
				for( i = 0; i < contqi; i++ ){
					System.out.println("******************************************");
					System.out.println(" Queja Numero: " + (i+1) );
					System.out.println( qi[i].mostrar_qimg() );
					System.out.println("******************************************");
				}
			}else if( pos == 5){
				System.out.println(" Nos vemos ");
			}else{
				System.out.println(" Seleccion erronea");
			}
		}while( pos != 5 );
	}
}