################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

""" 8. Números primos """
"""Escribir una función que indique con True si un numero indicado es Primo.
"""

def es_primo(numero):
	"""Esta funcion devuelve un valor booleano luego de procesar la variable"""
	"""se utiliza 'i' como primer numero intermedio para probar en la operación de division exacta o modulo"""
	"""la variable 'esPrimo' es la que se retorna al final"""
	esPrimo = True
	i = 2
	while esPrimo and i < numero:
		"""Mientras la variable sea true y el numero mayor a i, se chequea que no tenga 0 como resto de la division exacta"""
		chequeando = numero%i
		if chequeando==0 :
			"""En caso que que sí sea 0, se cambia la variable booleana a false"""
			esPrimo = False
			print(f"{numero} No es un numero primo")
		i+=1
	if esPrimo == True:
		print(f"{numero} Es un número primo")
	"""Postcondiciones:"""
	"""Antes de terminar se imprimen los resultados y se retorna el valor booleano final"""
	return esPrimo

def principal():
	"""Precondiciones:"""
	"""Se necesita un numero entero"""
	numero = int(input("Ingrese un numero: "))
	es_primo(numero)

if __name__ == "__main__":
    principal()