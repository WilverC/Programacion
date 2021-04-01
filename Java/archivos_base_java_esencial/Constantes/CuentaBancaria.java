public class CuentaBancaria {
    String titular;
    String tipoDeCuenta;
    double saldo;

    CuentaBancaria(String t, String tipo, double s) {
        titular = t;
        tipoDeCuenta = tipo;
        saldo = s;
    }

    CuentaBancaria(String t, double s) {
        titular = t;
        tipoDeCuenta = "ahorro";
        saldo = s;
    }

    CuentaBancaria() {
        tipoDeCuenta = "ahorro";
    }

    void sacarDinero(double cantidad) {
        if (cantidad < 0) {
            return;
        }
        saldo -= cantidad;
    }

    void ingresarDinero(double cantidad) {
        if (cantidad < 0) {
            return;
        }
        saldo += cantidad;
    }

    void cambiarTipoDeCuenta(String nuevoTipo) {
        tipoDeCuenta = nuevoTipo;
    }

    double obtenerSaldo() {
        return saldo;
    }
}
