import destinos.*
import transportes.*

object roberto{
	/*Roberto: Roberto viaja en bicicleta o camión. Si viaja en bicicleta, el peso que cuenta es el 
	suyo propio más 1, que es lo que pesa la bici. Si viaja en camión, el peso es el propio más del del camión,
	a razón de media tonelada por cada acoplado. Roberto no tiene un mango, gracias que tiene cubiertas, 
	y no puede llamar a nadie.*/
	var peso = 100
	var transporte = camion
	
	
	method peso() {
		return peso + transporte.peso()
	}

	method peso(cantidad){
		peso=cantidad
	}
	
	method transporte(vehiculo) {
		transporte = vehiculo
	}

	method puedeLlamar() {
		return false
	}
	
}
object chuckNorris{
	/*Chuck Norris: Chuck norris pesa 900 kg y puede llamar a cualquier persona del universo con sólo llevarse
	el pulgar al oído y el meñique a la boca*/
	method peso() {
		return 900
	}
	
	method puedeLlamar() {
		return true
	}
}
object neo{
	/*Neo vuela, así que no pesa nada. Y anda con celular, el muy canchero. 
  	El tema es que a veces no tiene crédito para hacer llamadas.*/
	var credito=0
	
	method peso() {
		return 0
	}
	
	method credito()=credito
	
	method credito(cantidad){
		credito=cantidad
	}
	
	method cargarCredito(cantidad){
		credito+=cantidad
	}
	
	method puedeLlamar() {
		return self.credito()>0
	}
}

