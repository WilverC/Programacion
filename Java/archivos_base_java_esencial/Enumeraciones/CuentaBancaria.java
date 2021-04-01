public class CuentaBancaria {
    String titular;
    String tipoDeCuenta;
    double saldo;

    public static final String TIPO_AHORRO = "ahorro";
    public static final String TIPO_NOMINA = "nómina";

    final double COMISION = 1.2;

    CuentaBancaria(String t, String tipo, double s) {
        titular = t;
        tipoDeCuenta = tipo;
        saldo = s;
    }

    CuentaBancaria(String t, double s) {
        titular = t;
        tipoDeCuenta = TIPO_AHORRO;
        saldo = s;
    }

    CuentaBancaria() {
        tipoDeCuenta = TIPO_AHORRO;
    }

    void sacarDinero(double cantidad) {
        if (cantidad < 0) {
            return;
        }
        double comision = calcularComision();
        saldo -= cantidad;
        saldo -= comision;
    }

    double calcularComision() {
        switch (tipoDeCuenta) {
            case TIPO_AHORRO:
                return COMISION;
            case TIPO_NOMINA:
                return 0;
            default:
                return 0;
        }
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
