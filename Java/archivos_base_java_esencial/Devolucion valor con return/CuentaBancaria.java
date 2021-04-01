public class CuentaBancaria {
    String titular;
    String tipoDeCuenta;
    double saldo;

    void sacarDinero(double cantidad) {
        saldo -= cantidad;
    }

    void ingresarDinero(double cantidad) {
        saldo += cantidad;
    }

    void cambiarTipoDeCuenta(String nuevoTipo) {
        tipoDeCuenta = nuevoTipo;
    }
}
