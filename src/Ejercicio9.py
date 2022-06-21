################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
"""

def factores_primos(numero):
	"""Se copia la variable 'numero' en 'numeroSinFactorear' para poder operar sobre ella, sin perder la referencia"""
	"""Se declara la variable lista factoresPrimos para almacenar los resultados que arroje la función"""
	""" cuando el resto de la división exacta sea 0"""
	"""Y la variable 'i' será el número divisible exacto del parámetro número"""

	numeroSinFactorear = numero
	factoresPrimos = []
	i=0
	for i in range(2, numero+1):
		while  numero%i == 0:
			factoresPrimos.append(i)
			numero = numero / i

	"""Poscondiciones:"""
	"""El resultado final se convierte en una tupla y es lo que se retorna, primero como una impresión y luego al final de la función"""
	factoresPrimosTuple = tuple(factoresPrimos)
	print(f"Los factores primos de {numeroSinFactorear} son {factoresPrimosTuple}")
	return factoresPrimosTuple
	
def principal():
	"""Precondiciones:"""
	"""Se ingresa un número entero positivo para saber cuales son sus factores primos """
	numeroAFactorear = int(input("Ingrese un número: "))
	factores_primos(numeroAFactorear)

if __name__ == "__main__":
    principal()