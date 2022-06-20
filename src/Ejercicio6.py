################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

""" 6. Ordenar 3 valores """
"""Escribir una función que a partir de tres variables de tipo entero retorne una tupla """
"""con dichos valores ordenados de menor a mayor. Y Viceversa """

def ordenar_mayor_a_menor(uno, dos, tres): 
	"""Se realiza una comparación entre los tres números antes de ordenar dentro de la tupla"""  
	"""Poscondiciones:"""
	"""Se imprime la tupla ordenada cuando se cumple una de las condiciones de comparación"""
	tuplaNumerosMayorAMenor= ()
	if uno>dos and dos>tres:
		""" si uno es mayor a dos y dos es mayor a tres """
		tuplaNumerosMayorAMenor= (uno,dos,tres)
		print(f"Tupla de mayor a menor es: {tuplaNumerosMayorAMenor}")
	elif dos>uno and uno>tres:
		""" sino si dos es mayor a uno y uno mayor a tres """
		tuplaNumerosMayorAMenor= (dos,uno,tres)
		print(f"Tupla de mayor a menor es: {tuplaNumerosMayorAMenor}")
	elif tres>uno and uno>dos:
		"""tres mayor a uno y uno mayor a dos """
		tuplaNumerosMayorAMenor= (tres,uno,dos)
		print(f"Tupla de mayor a menor es: {tuplaNumerosMayorAMenor}")
	elif tres>dos and dos>uno:
		"""si tres es mayor a dos y este mayor a uno"""
		tuplaNumerosMayorAMenor= (tres,dos,uno)
		print(f"Tupla de mayor a menor es: {tuplaNumerosMayorAMenor}")
	elif uno>tres and tres>dos:
		"""sino si uno es mayor a tres y este mayor a dos"""
		tuplaNumerosMayorAMenor= (uno,tres,dos)
		print(f"Tupla de mayor a menor es: {tuplaNumerosMayorAMenor}")
	elif dos>tres and tres>uno:
		"""sino si dos es mayor a tres, y éste mayor a uno"""
		tuplaNumerosMayorAMenor= (dos,tres,uno)
		print(f"Tupla de mayor a menor es: {tuplaNumerosMayorAMenor}")
	else: 
		"""si hay numeros iguales"""
		print("Error: hay números iguales")

def ordenar_menor_a_mayor(uno, dos, tres):
	"""Se realiza una comparación entre los tres números antes de ordenar dentro de la tupla"""  
	"""Poscondiciones:"""
	"""Se imprime la tupla ordenada cuando se cumple una de las condiciones de comparación"""
	tuplaNumerosMenorAMayor=()
	if uno<dos and uno<tres:
		"""Si uno es menor a dos y menor que tres"""
		tuplaNumerosMenorAMayor=(uno,dos,tres)
		print(f"Tupla de menor a mayor es: {tuplaNumerosMenorAMayor}")
	elif dos<uno and uno<tres:
		"""si dos es menor que uno y éste menor que tres"""
		tuplaNumerosMenorAMayor=(dos,uno,tres)
		print(f"Tupla de menor a mayor es: {tuplaNumerosMenorAMayor}")
	elif tres<uno and uno<dos:
		"""si tres es menor a uno y éste es menor que dos"""
		tuplaNumerosMenorAMayor=(tres,uno,dos)
		print(f"Tupla de menor a mayor es: {tuplaNumerosMenorAMayor}")
	elif tres<dos and dos<uno:
		"""si tres es menor que dos y dos es menor que uno"""
		tuplaNumerosMenorAMayor=(tres,dos,uno)
		print(f"Tupla de menor a mayor es: {tuplaNumerosMenorAMayor}")
	elif uno<tres and tres<dos:
		"sino si uno es menor que tres y este es menor que dos"
		tuplaNumerosMenorAMayor=(uno,tres,dos)
		print(f"Tupla de menor a mayor es: {tuplaNumerosMenorAMayor}")
	elif dos<tres and tres<uno:
		"""Sino si dos es menor a tres y este es menor que uno"""
		tuplaNumerosMenorAMayor=(dos,tres,uno)
		print(f"Tupla de menor a mayor es: {tuplaNumerosMenorAMayor}")
	else: 
		"""si hay numeros iguales"""
		print("Error: hay números iguales")


def principal():
	"""Precondiciones:"""
	"""Se necesitan 3 numeros enteros para realizar la comparación"""
	primerNumero = int(input("Ingrese un número: "))
	segundoNumero = int(input("Ingrese otro número: "))
	tercerNumero = int(input("Ingrese el último número: "))
	"""Luego se llama a la función que recibe los parámetros para devolver la tupla ordenada"""
	ordenar_mayor_a_menor(primerNumero, segundoNumero,tercerNumero)
	ordenar_menor_a_mayor(primerNumero, segundoNumero, tercerNumero)

if __name__ == "__main__":
	principal()