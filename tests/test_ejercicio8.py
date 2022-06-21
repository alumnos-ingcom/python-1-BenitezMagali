################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest
from src.Ejercicio8 import es_primo

def test_es_primo_caso_positivo():
	"""Se envía un numero para saber si es primo"""
	numeroAComprobar = 347
	resultado = es_primo(numeroAComprobar)
	assert (resultado, True), "No es un numero primo"

def test_es_primo_caso_negativo():
	"""Se envía un numero para saber si es primo, en este caso debería no serlo"""
	numeroAComprobar = 345
	resultado = es_primo(numeroAComprobar)
	assert (resultado, False), "Es un numero primo"