import java.util.Scanner;

/*
    Programa que emula la interfaz de un cajero automático. El programa presentará las siguientes opciones al usuario:

    Elija una de las siguientes opciones:
           Escriba 1 para consultar su saldo
           Escriba 2 para ingresar dinero
           Escriba 3 para sacar dinero
           Escriba 4 para consultar sus últimos movimientos
       Una vez escrita la opción, pulse la tecla Enter

       Una vez el usuario ha elegido la opción, el programa le mostrará por pantalla el número correspondiente a la opción elegida
*/
public class Interfaz {
    public static void main(String[] args) {
        System.out.println("Elija una de las siguientes opciones:");
        System.out.println("   Escriba 1 para consultar su saldo");
        System.out.println("   Escriba 2 para ingresar dinero");
        System.out.println("   Escriba 3 para sacar dinero");
        System.out.println("   Escriba 4 para consultar sus últimos movimientos");

        Scanner scanner = new Scanner(System.in);

        int opcionSeleccionada = scanner.nextInt();

        System.out.println("La opción que usted ha elegido es: " + opcionSeleccionada);
    }
}