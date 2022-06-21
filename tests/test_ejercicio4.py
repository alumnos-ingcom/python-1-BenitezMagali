################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest
from src.Ejercicio4 import suma_lenta

def test_sumaLenta_positivos():
	"""Se envían numeros para la suma"""
	"""Se espera un integer positivo como resultado de la función"""
	primerNumero = 100
	segundoNumero = 5
	resultado = suma_lenta(primerNumero,segundoNumero)
	assert (resultado, str), "Se esperaba el texto con resultado de suma"
	assert resultado > 0, "Se esperaba un numero positivo"

def test_sumaLenta_negativos():
	"""Se envían numeros para la suma"""
	"""Se espera un integer negativo como resultado de la función"""
	primerNumero = -10
	segundoNumero = 5
	resultado = suma_lenta(primerNumero,segundoNumero)
	assert (resultado, str), "Se esperaba el texto con resultado de suma"
	assert resultado < 0, "Se esperaba un numero negativo"