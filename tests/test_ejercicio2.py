################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest
from src.Ejercicio2 import signo

def test_signo_positivo():
	"""Se envía un n° positivo"""
	"""Se espera un string con el resultado de la función"""
	numeroPositivo = 34
	resultado = signo(numeroPositivo)
	assert isinstance(resultado,str)
	assert resultado >0, "Se esperaba un resultado positivo"

def test_signo_negativo():
	"""Se envía un n° negativo"""
	"""Se espera un string con el resultado de la función"""
	numeroNegativo = -15
	resultado = signo(numeroNegativo)
	assert isinstance(resultado,str)
	assert resultado < 0, "Se esperaba un resultado negativo"

def test_cero():
	"""Se envía el cero"""
	"""Se espera un string con el resultado de la función"""
	numeroCero = 0
	resultado = (numeroCero)
	assert isinstance(resultado,str)
	assert resultado == 0, "Se esperaba que sea cero"
