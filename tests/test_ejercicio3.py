################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest
from src.Ejercicio3 import compara

def test_compara_menor_mayor():
	"""Se envía un n° menor"""
	"""Luego un n° mayor"""
	"""Se espera un integer negativo como resultado de la función"""
	nroAComparar = 34
	otroAComparar= 54
	resultado = compara(nroAComparar,otroAComparar)
	assert (resultado, int), "El resultado debe ser un integer"
	assert resultado < 0, "Se esperaba -1"

def test_compara_mayor_menor():
	"""Se envía un n° mayor"""
	"""Luego un n° menor"""
	"""Se espera un integer positivo como resultado de la función"""
	nroAComparar = 100
	otroAComparar= -100
	resultado = compara(nroAComparar,otroAComparar)
	assert (resultado, int), "El resultado debe ser un integer"
	assert resultado > 0, "Se esperaba 1"

def test_compara_iguales():
	"""Se envía el mismo numero ambas veces"""
	"""Se espera 0 como resultado de la función"""
	nroAComparar = 17
	otroAComparar= 17
	resultado = compara(nroAComparar,otroAComparar)
	assert (resultado, int), "El resultado debe ser un integer"
	assert resultado == 0, "Se esperaba 0"

