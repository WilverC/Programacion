public class Protagonista extends Personaje {

    private static final int UNIDADES_DE_SALTO = 10;
    public void recibirCura(int puntos) {
        puntosDeVida += puntos;
    }

    public void saltar() {
        posicionY += UNIDADES_DE_SALTO;
    }
}
