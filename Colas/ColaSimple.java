public class ColaSimple {
	private Nodo frente;
	private Nodo atras;
	private int longitud;

	public ColaSimple() {
		frente = null;
		longitud = 0;
	}

	public void insertar(int dato) {
		Nodo nuevoNodo = new Nodo(dato);
		if (frente == null) {
			frente = nuevoNodo;
			atras = nuevoNodo;
			atras.setSiguiente(frente);
		} else {
			atras.setSiguiente(nuevoNodo);
			atras = nuevoNodo;
			atras.setSiguiente(frente);
		}
		longitud++;
	}

	public void eliminar() {
		if (frente != null) {
			frente = frente.getSiguiente();
			longitud--;
		}
	}

	public boolean estaVacia() {
		return frente == null;
	}

	public Nodo getFrente() {
		return frente;
	}

	public int getLongitud() {
		return longitud;
	}
}