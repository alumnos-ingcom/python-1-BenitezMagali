################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

""" 1. Conversión de temperaturas """
"""Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa"""
"""Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal, """
"""utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""

# ************ Funciones a implementar del ejercicio   **********************

def convertir_a_centigrados(fahrenheit):
	"""Esta función toma como parámetro el número flotante ingresado en el input, guardado en la variable 'farenheit'"""
	"""Se procesa la variable dentro de la función realizando la fórmula para pasar de Farenheit a Centígrados"""
	"""Se retorna el resultado para ser impreso. """
	return (fahrenheit - 32) / 1.8


def convertir_a_fahrenheit(centigrados):
	""" Esta función toma como parámetro el número flotante ingresado en el input, guardado en la variable 'centigrados'"""
	""" Se procesa esta variable dentro de la función realizando la fórmula para pasar de Centígrados a Farenheit """
	""" Se retorna el resultado para ser impreso. """
	return (centigrados * 1.8) + 32

# ************ Programa *********************
def principal():
	"""Precondiciones: deben ingresarse números flotantes, que son guardados en las variables farenheit y centígrados """
	"""para ser procesados dentro de las funciones y retornar otra información, en este caso la conversión. """
	fahrenheit = float(input("Ingresa los grados Fahrenheit: "))

	""" Se envía la variable a la función como parámetro """
	centigrados = convertir_a_centigrados(fahrenheit)

	""" Postcondiciones: """
	"""Se imprime el resultado de la función, con la primer variable ingresada para realizar la verificación """
	print(f"Los {fahrenheit} grados Fahrenheit son {centigrados} grados centigrados")


	""" En este caso se realiza lo mismo, pero a la inversa para pasar de centígrados a fahrenheit """
	centigrados = float(input("Ingresa los grados Centigrados: "))
	fahrenheit = convertir_a_fahrenheit(centigrados)
	print(f"Los {centigrados} grados centigrados son {fahrenheit} grados Fahrenheit")

if __name__ == "__main__":
    principal()
