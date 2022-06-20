################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""3. Comparación de números """
"""Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:"""

"""Retornar -1 si el primero es menor que el segundo"""
"""Retornar 0 si son iguales"""
"""Retornar 1 si el primero es mayor que el segundo"""

#*********** Funciones a implementar del ejercicio *******************
def compara(numero, otro_numero):
	"""Se declara una variable para retornar"""
	"""Se comparan los numeros ingresados"""
	"""Se recorren las condiciones para retornar un resultado"""
	mayorOmenor= 0
	if numero < otro_numero:
		mayorOmenor= -1
	elif numero == otro_numero:
		mayorOmenor= 0
	else:
		mayorOmenor=1
	"""Poscondiciones:"""
	"""Se imprime el resultado y se retorna"""
	print(mayorOmenor)
	return mayorOmenor

	
def principal():
	"""Precondiciones:"""
	"""Se necesitan al menos dos numeros enteros"""
	"""Se invoca la función para comparar enviando ambos como parámetros"""
	primerNumero = int(input("Ingrese un número: "))
	segundoNumero = int(input("Ingrese otro número: "))
	compara(primerNumero, segundoNumero)

if __name__ == "__main__":
    principal()