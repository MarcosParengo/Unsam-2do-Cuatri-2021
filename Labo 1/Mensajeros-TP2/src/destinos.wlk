import mensajeros.*
import transportes.*

object  puenteDeBrooklyn{
	//deja pasar a todo lo que pese hasta una tonelada.
	method dejarPasar(mensajero) {
		return mensajero.peso() < 1000
	}
}

object laMatrix{
	//deja entrar a quien pueda hacer una llamada.
	method dejarPasar(mensajero) {
		return mensajero.puedeLlamar()
	}
}
