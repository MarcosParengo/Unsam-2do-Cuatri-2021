##conjuntos (sets). Entre llaves y sin elementos repetidos. Solo puede incluir numeros,tuplas o strings 

conjunto={1,2,3,4,(5,6),"algo"}##NO {[1,2,3],1,2} (no puede incluir arrays)

##Puedo convertir arrays en conjuntos (si cumple las condiciones)
conjunto=set([1,2,3,4])
#print(set([1,2,[1,2,3],3,4]))No cumple la regla de no incluir listas, da error

conjunto=set([1,2,3,3,3,3,4])   #No cumple la regla de no repetidos, pero python se encarga de esto armando 
                                #un conjunto pero no igual al array, sino que los repetidos solo aparecen una vez

conjunto.add(5)#Para agregar un elemento
conjunto.update({6,7,8})#Para agregar otro set


conjunto.remove(7)#Para borrar un elemento, si no existe da error
conjunto.discard(8)#Para borrar un elemento, si no existe no da error

1 in conjunto#Verifico si un elemento esta incluido en el conjunto
conjunto.pop()#Descarta el primer elemento del objeto
1 in conjunto

conjunto.clear()#Vaciar el conjunto

conjunto={1,2,3,4}
conjunto2={2,3,4,5}

conjunto | conjunto2#Union (todos los balores de los dos conjuntos)
conjunto & conjunto2#Interseccion (valores que comparten)
conjunto - conjunto2#Diferencia (todos los valores del primero menos los del segundo)
conjunto2 - conjunto#Diferencia (todos los valores del primero menos los del segundo)

conjunto.clear
conjunto2.clear

conjunto={1,2,3,4,5,6,7}
conjunto2={2,3,4}

conjunto2.issubset(conjunto)#Es subconjunto
conjunto.issuperset(conjunto2)#Es superConjunto

conjunto.symmetric_difference(conjunto2)#elementos que no comparten (^)

conjunto.clear
conjunto2.clear

conjunto={1,2,3}
conjunto2={5,6,7}

conjunto.isdisjoint(conjunto2)#True si no comparten elementos