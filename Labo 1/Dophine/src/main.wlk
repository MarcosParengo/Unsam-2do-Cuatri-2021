object georginho{
	const peso=70
	var rendimiento=0
	method consumir(cantidad,sustancia){
		rendimiento=sustancia.rendimiento(cantidad)
	}
	method velocidad(){
		 const inerciaBase=(490/peso)
		 return(rendimiento*inerciaBase)
	}
}

object cianuro{
	method rendimiento(cantidad){
		return(0)
	}
}
object whisky{
	method rendimiento(cantidad){
		return(0.9**cantidad)
	}
}
object terere{
	method rendimiento(cantidad){
		return((0.1*cantidad).max(1))
	}
}
