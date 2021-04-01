public class Queja{
	private String nombre_queja;
	private String mensaje;
	private String fecha_queja;
	private String emisor_qja;

	public Queja(){
		nombre_queja = "";
		mensaje = "";
		fecha_queja = "";
		emisor_qja = "";
	}

	public Queja( String n, String m, String f, String e){
		this.nombre_queja = n;
		this.mensaje = m;
		this.fecha_queja = f;
		this.emisor_qja = e;
	}

	public String mostrar_queja(){
		return "\n nombre_queja: " + nombre_queja + 
				"\n mensaje: " + mensaje +
				"\n fecha_queja: " + fecha_queja +
				"\n emisor_qja: " + emisor_qja;
	}
}