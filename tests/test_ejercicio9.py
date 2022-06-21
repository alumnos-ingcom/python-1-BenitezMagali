################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest
from src.Ejercicio9 import factores_primos

def test_factores_primos_tuplaDe5():
	"""Se envía un numero para comprobar cuales son sus factores primos"""
	numeroAComprobar = 500
	resultado = factores_primos(numeroAComprobar)
	assert (resultado, tuple), "No tiene factores primos"
	assert (3, resultado.count(5)), "5 no es factor primo"

def test_factores_primos_tuplaCorta():
	"""Se envía un numero para comprobar cuales son sus factores primos, en este caso,sí mismo"""
	numeroAComprobar = 13
	resultado = factores_primos(numeroAComprobar)
	assert (resultado, tuple), "No tiene factores primos"
	assert (1, resultado.count(13)), "13 no es factor primo"