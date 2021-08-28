import mensajeros.*
import destinos.*

object camion {
	var acoplados = 2
	//Getter de peso del camion, necesario para el poliformismo
	method peso() {
		return acoplados * 500
	}
	//Setter de cantidad de acoplados
	method acoplados(cantAcoplados) {
		acoplados = cantAcoplados
	}
}

object bicicleta {
	//Getter de peso de la bicicleta, necesario para el poliformismo
	method peso() {
		return 1
	}
}
