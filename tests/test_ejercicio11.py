################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest
from src.Ejercicio11 import es_multiplo

def test_es_multiplo_true():
	"""Se envían dos numeros para comprobar que el segundo sea multiplo del primero"""
	primerNumero= 3
	segundoNumero=30
	resultado = es_multiplo(primerNumero,segundoNumero)
	assert (resultado, True), "No es múltiplo"
	
def test_es_multiplo_false():
	"""Se envían dos numeros para comprobar que el segundo sea multiplo del primero, en este caso no deberia serlo"""
	primerNumero= 5
	segundoNumero=34
	resultado = es_multiplo(primerNumero,segundoNumero)
	assert (resultado, False), "Es múltiplo"
	