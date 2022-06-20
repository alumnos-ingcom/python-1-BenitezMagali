################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

""" 2. Números positivos y negativos """
""" Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas"""

#*********** Funciones a implementar del ejercicio *******************
def signo(numero):
	""" Si a un n° que puede ser negativo lo sumamos a sí mismo, nos da 0 """
	""" 0 + 1 = 1 y es la pauta para saber que numero es negativo """
	""" Si realizamos lo mismo con un n° que podria ser positivo"""
	"""el resultado es -1, confirmando que es positivo"""
	"""Finalmente, si no es ninguna de las opciones, será 0"""
	"""Poscondiciones:"""
	"""Se imprimen mensajes con el resultado de la función"""
	if numero + (- numero) + 1 == 1:
		print(f"{numero} es negativo")
	elif numero - numero - 1 == (-1):
		print(f"{numero} es positivo")
	else:
		print(f"{numero} es cero")

	"""Precondiciones:"""
	"""Los numeros a ingresar deben ser enteros""" 
def principal():
	numeroParaDeterminar = int(input("Ingrese un número: "))
	signo(numeroParaDeterminar)

if __name__ == "__main__":
    principal()
