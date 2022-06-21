################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de
Escribir una función que indique con True si un número entero es multiplo de otro, utilizando sumas y restas.
"""
def es_multiplo(numero, multiplo):
	"""Esta funciion toma ambas funciones, primero establece una condicion booleana para retornar y """
	"""luego se guarda en resultado una copia del parámetro 'multiplo', para poder operar sobre ella"""
	"""En caso de no ser multiplo, la variable booleana cambia para ser retornada"""
	esMultiplo= True
	resultado = multiplo
	while resultado >= numero:
		resultado= resultado - numero
	if resultado == 0:
		print(f"{multiplo} Es múltiplo de {numero}")
	else:
		esMultiplo = False
		print(f"{multiplo} No es multiplo de {numero}")
	"""Poscondiciones:"""
	"""Se retorna el resultado del proceso en la variable booleana"""
	return esMultiplo


def principal():
	"""Precondiciones:"""
	"""Se necesitan 2 variables, la segunda será la que se compruebe si es multiplo de la primera"""
	numeroEntero= int(input("Ingrese un numero entero: "))
	posibleMultiplo= int(input("Ingrese otro numero, para saber si es múltiplo: "))
	es_multiplo(numeroEntero,posibleMultiplo)

if __name__ == "__main__":
    principal()