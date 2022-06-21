################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest
from src.Ejercicio7 import decimal_a_sexadecimal,sexadecimal_a_decimal

def test_decimal_a_sexagesimal():
	"""Se envían numeros para ser convertidos a sexagesimal"""
	decimalAConvertir = 100.8
	resultado= decimal_a_sexadecimal(decimalAConvertir)
	assert (resultado, float), "Se esperaba un numero sexagesimal"

def sexadecimal_a_decimal():
	"""Se envían las tres variables para ser convertidos a sexagesimal"""
	gradosAConvertir = 109
	minutosAConvertir= 54
	segundosAConvertir= 564
	resultado= sexadecimal_a_decimal(gradosAConvertir,minutosAConvertir,segundosAConvertir)
	assert (resultado, float), "Se esperaba un numero decimal"


