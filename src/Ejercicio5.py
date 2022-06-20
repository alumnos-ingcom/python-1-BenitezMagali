################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""5. Divisiones """
"""Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
"""

#*********** Funciones a implementar del ejercicio *******************

def division_lenta(dividendo, divisor):
	"""Se declara la variable cociente para acumular las restas que se hacen"""
	"""En la variable resto se genera 'una copia' de dividendo, para operar"""
	"""Mientras a resto se le pueda restar el divisor, se contabiliza cociente"""
	"""y se actualiza el valor de resto'resto'"""
	"""La función puede recibir dividendos negativos que son procesados en el else"""
	cociente= 0
	resto= dividendo
	if dividendo > 0:
		while resto >= divisor:
			resto = resto - divisor 
			cociente +=1
	else:
		resto= resto * (-1)
		while resto >= divisor:
			resto = resto - divisor 
			cociente +=1
	"""Poscondiciones:"""
	"""Se imprimen los valores de cociente y resto obtenidos"""
	print(f"El cociente de la división es: {cociente}")
	print(f"El resto de la división es: {resto}")

def principal():
	"""Precondiciones:"""
	"""Se necesitan 2 numeros enteros para realizar la division"""
	"""Ambos se pasan como parámetro de la función"""
	primerNumero = int(input("Ingrese un número: "))
	segundoNumero = int(input("Ingrese otro número: "))
	division_lenta(primerNumero, segundoNumero)

if __name__ == "__main__":
    principal()