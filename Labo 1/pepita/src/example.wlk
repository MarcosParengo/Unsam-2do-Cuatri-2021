
object pepita {
	var energia=1000
	method verEnergia()=energia
	
	method volar(kmRecorridos){
		const joulesPorKm=10
		const joulesDeInicio=10
		const resultado=joulesPorKm*kmRecorridos+joulesDeInicio
		energia-=resultado
	}
	
	method comer(comida){
		const energiaPorGramo=4
		const resultado=energiaPorGramo*comida.gramos()
		energia+=resultado
	}
}

object alpiste{
	const gramos=2
	method gramos()=gramos
}
object manzana{
	const gramos=4
	method gramos()=gramos
}

