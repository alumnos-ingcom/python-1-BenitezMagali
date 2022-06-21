################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""7. Transformación de un número """
"""Escribir un programa que permita transformar un número solicitado expresado en grados, """
"""minutos y segundos a segundos a segundos. Y otra que haga el cambio en el sentido contrario, """
"""devolviendo una tuple.
Recuerden que un grado son 60 minutos y un minuto son 60 segundos. """

def sexadecimal_a_decimal(grados, minutos, segundos):
	"""Esta funcion transforma el numero sexagesimal y mediante la formula establecida"""
	"""convierte esos grados, minutos y segundos a un número decimal """
	numero = grados
	decimales = (minutos/60)+(segundos/3600)
	numeroDecimal = numero + decimales
	"""Postcondicion:"""
	"""Se imprime el resultado obtenido de la función"""
	print(f"El número es decimal es: {numeroDecimal}")
	
def decimal_a_sexadecimal(numero):
	"""Esta funcion transforma un número decimal mediante la formula establecida"""
	"""y lo convierte a grados, minutos y segundos"""
	grados =  int(numero)
	minutos = int((numero - grados) * 60)
	segundos =  (numero -grados - minutos/60 ) * 3600

	"""Postcondicion:"""
	"""Se imprime el resultado obtenido de la función"""
	print(f"{grados}° {minutos}' {segundos}''")

	"""Se envían los nuevos dígitos a la otra función"""
	sexadecimal_a_decimal(grados,minutos,segundos)

def principal():
	"""Precondiciones:"""
	"""Se necesita un número decimal, puede ser float, para convertilo a sexagesimal"""
	numeroAConvertir = float(input("Ingrese un número para convertir a grados, horas y segundos: "))
	decimal_a_sexadecimal(numeroAConvertir)

if __name__ == "__main__":
    principal()