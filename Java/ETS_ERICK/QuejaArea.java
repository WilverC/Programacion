public class QuejaArea extends Queja{
	private String area;
	
	public QuejaArea(){
		super();
	}

	public QuejaArea( String n, String m, String f, String e, String area){
		super(n, m, f, e);
		this.area = area;
	}

	public String mostrar_qarea(){
		String datos = mostrar_queja();
		datos += "\n area: " + area;
		return datos;
	}
}