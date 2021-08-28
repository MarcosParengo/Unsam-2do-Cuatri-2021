import mensajeros.*
import destinos.*
import transportes.*

object paquete {
	var pago = false
	var destino = puenteDeBrooklyn

	method pagar() {
		pago = true
	}

	method estaPago() {
		return pago
	}

	method destino(lugar) {
		destino = lugar
	}

	method puedeSerEntregadoPor(mensajero) {
		return destino.dejarPasar(mensajero) and self.estaPago()
	}
}
