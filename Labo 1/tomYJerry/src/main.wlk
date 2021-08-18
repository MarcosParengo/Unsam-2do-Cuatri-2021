object tom {

	var energia = 80
	var posicion = 0

	method velocidad() {
		return (5 + ( energia / 10))
	}

	method posicion() {
		return (posicion)
	}

	method esMasVeloz(comparado) {
		return(comparado.velocidad()<self.velocidad())
	}

	method correrA(corrido) {
		const energiaAGastar=(0.5 * self.velocidad() * (self.posicion() - corrido.posicion()).abs())
		
			energia = energia - energiaAGastar
			posicion = corrido.posicion()
		
	}

}

object jerry {

	const peso = 3

	method velocidad() {
		return (10 - peso)
	}

	method posicion() {
		return (10)
	}

}

object robotRaton {

	method velocidad() {
		return (8)
	}

	method posicion() {
		return (12)
	}

}