################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest
from src.Ejercicio5 import division_lenta

def test_division_lenta_positivos():
	"""Se envían numeros para la división"""
	"""Se espera un integer positivo como resultado de la función"""
	primerNumero = 100
	segundoNumero = 5
	resultado = division_lenta(primerNumero,segundoNumero)
	assert (resultado, str), "Se esperaba el texto con resultado de la división"
	assert resultado > 0, "Se esperaba un numero positivo"

def test_division_lenta_negativos():
	"""Se envían numeros para la división"""
	"""Se espera un integer positivo como resultado de la función"""
	primerNumero = -100
	segundoNumero = 5
	resultado = division_lenta(primerNumero,segundoNumero)
	assert (resultado, str), "Se esperaba el texto con resultado de la división"
	assert resultado < 0, "Se esperaba un numero negativo"
	

