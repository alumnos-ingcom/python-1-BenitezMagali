################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest
from src.Ejercicio10 import es_palindromo

def test_es_palindromo_true():
	"""Se envía una palabra para comprobar que sea palindromo"""
	stringAComprobar = "neuquen"
	resultado = es_palindromo(stringAComprobar)
	assert (resultado, str), "No es palabra o frase"
	assert "Es palíndromo", resultado; "No es palindromo"

def test_es_palindromo_false():
	"""Se envía una palabra para comprobar que sea palindromo, en este caso no deberia serlo"""
	stringAComprobar = "Rio Negro"
	resultado = es_palindromo(stringAComprobar)
	assert (resultado, str), "No es palabra o frase"
	assert "No es palíndromo", resultado; "Es palindromo"