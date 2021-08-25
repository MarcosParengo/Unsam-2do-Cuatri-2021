object delfina {

	var enLaMano = play
	var diversion = 0

	method agarrar(consola){
    enLaMano=consola
  	}

	method diversion()= diversion

  	method jugar(videojuego){
    	diversion+=videojuego.diversion(enLaMano)
    	enLaMano.usar()
  }
}

object play {

	method jugabilidad() = 10

	method usar() {
	}
}

object portatil {

	var bateriaBaja = false

	method jugabilidad() {
		if (bateriaBaja) {
			return 1
		} else {
			return 8
		}
	}

	method usar() {
		bateriaBaja = true
	}
}

object arkanoid{
	method diversion(enLaMano)= 50
}

object mario{
	method diversion(enLaMano){
		if(enLaMano.jugabilidad()>5){
			return 100
		}else{
			return 15
		}
	}
}

object pokemon{
	method diversion(enLaMano)=enLaMano.jugabilidad()*10
}
