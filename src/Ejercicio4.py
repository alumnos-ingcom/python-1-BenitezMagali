################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""4. Suma lenta """
"""Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa"""
"""Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1"""
"""La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo."""

#*********** Funciones a implementar del ejercicio *******************
def suma_lenta(numero, otro_numero):
	"""Se declara la variable sumando que será quien en cada vuelta sume +1"""
	"""Si el otro_numero ingresado es positivo se suma +1 en cada vuelta"""
	sumando = 0
	if otro_numero > 0:
		while sumando < otro_numero:
			numero +=1
			sumando +=1
	else:
		"""Si el otro_numero ingresado es negativo, se lo pasa a positivo"""
		"""Para tener la cantidad de veces que debe sumarse (-1) a numero"""
		conteoPositivo= otro_numero*(-1)
		while sumando < conteoPositivo:
			numero -=1
			sumando +=1
			
	"""Poscondiciones:"""
	"""Se imprime el resultado de la suma lenta, habiendo procesado las variables"""
	print(f"El resultado de la suma lenta es= {numero}")

def principal():
	"""Es la funcion que interactua y pide las variables de entrada"""
	"""Precondiciones:"""
	"""Se necesitan dos numeros enteros, positivos o negativos"""
	primerNumero = int(input("Ingrese un número: "))
	segundoNumero = int(input("Ingrese otro número: "))
	suma_lenta(primerNumero, segundoNumero)

if __name__ == "__main__":
    principal()