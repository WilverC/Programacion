public class QuejaImagen extends Queja{
	private String url_imagen;
	
	public QuejaImagen(){
		super();
	}

	public QuejaImagen( String n, String m, String f, String e, String u){
		super(n, m, f, e);
		this.url_imagen = u;
	}

	public String mostrar_qimg(){
		String datos = mostrar_queja();
		datos += "\n url: " + url_imagen;
		return datos;
	}
}