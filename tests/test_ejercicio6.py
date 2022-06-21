################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest
from src.Ejercicio6 import ordenar_mayor_a_menor,ordenar_menor_a_mayor

"""Se envían numeros para ser ordenados"""
"""Se espera tupla ordenada como resultado de cada una de las funciones"""
"""En la ultima función se prueba el error cuando hay dos iguales"""

def test_ordenar_mayor_a_menor_unodostres():
	primerNumero = 100
	segundoNumero = 70
	tercerNumero = 30
	resultadoMayorMenor = ordenar_mayor_a_menor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMayorMenor, tuple), "Se esperaba una tupla ordenada de Mayor a Menor"
	assert (resultadoMayorMenor, tuple(100,70,30)), "Se esperaba tupla ordenada"

def test_ordenar_menor_a_mayor_unodostres():
	primerNumero = 100
	segundoNumero = 70
	tercerNumero = 30
	resultadoMenorMayor = ordenar_menor_a_mayor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMenorMayor,tuple),"Se esperaba otra tupla ordenada de Menor a Mayor"
	assert (resultadoMenorMayor, tuple(30,70,100)), "Se esperaba tupla ordenada"

def test_ordenar_mayor_a_menor_dosunotres():
	primerNumero = 70
	segundoNumero = 100
	tercerNumero = 30
	resultadoMayorMenor = ordenar_mayor_a_menor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMayorMenor, tuple), "Se esperaba una tupla ordenada de Mayor a Menor"
	assert (resultadoMayorMenor, tuple(100,70,30)), "Se esperaba tupla ordenada"

def test_ordenar_menor_a_mayor_dosunotres():
	primerNumero = 70
	segundoNumero = 30
	tercerNumero = 100
	resultadoMenorMayor = ordenar_menor_a_mayor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMenorMayor,tuple),"Se esperaba otra tupla ordenada de Menor a Mayor"
	assert (resultadoMenorMayor, tuple(30,70,100)), "Se esperaba tupla ordenada"

def test_ordenar_mayor_a_menor_tresunodos():
	primerNumero = 70
	segundoNumero = 30
	tercerNumero = 100
	resultadoMayorMenor = ordenar_mayor_a_menor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMayorMenor, tuple), "Se esperaba una tupla ordenada de Mayor a Menor"
	assert (resultadoMayorMenor, tuple(100,70,30)), "Se esperaba tupla ordenada"

def test_ordenar_menor_a_mayor_tresunodos():
	primerNumero = 70
	segundoNumero = 30
	tercerNumero = 100
	resultadoMenorMayor = ordenar_menor_a_mayor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMenorMayor,tuple),"Se esperaba otra tupla ordenada de Menor a Mayor"
	assert (resultadoMenorMayor, tuple(30,70,100)), "Se esperaba tupla ordenada"

def test_ordenar_mayor_a_menor_tresdosuno():
	primerNumero = 30
	segundoNumero = 70
	tercerNumero = 100
	resultadoMayorMenor = ordenar_mayor_a_menor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMayorMenor, tuple), "Se esperaba una tupla ordenada de Mayor a Menor"
	assert (resultadoMayorMenor, tuple(100,70,30)), "Se esperaba tupla ordenada"

def test_ordenar_menor_a_mayor_tresdosuno():
	primerNumero = 30
	segundoNumero = 70
	tercerNumero = 100
	resultadoMenorMayor = ordenar_menor_a_mayor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMenorMayor,tuple),"Se esperaba otra tupla ordenada de Menor a Mayor"
	assert (resultadoMenorMayor, tuple(30,70,100)), "Se esperaba tupla ordenada"

def test_ordenar_mayor_a_menor_unotresdos():
	primerNumero = 100
	segundoNumero = 30
	tercerNumero = 70
	resultadoMayorMenor = ordenar_mayor_a_menor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMayorMenor, tuple), "Se esperaba una tupla ordenada de Mayor a Menor"
	assert (resultadoMayorMenor, tuple(100,70,30)), "Se esperaba tupla ordenada"

def test_ordenar_menor_a_mayor_unotresdos():
	primerNumero = 100
	segundoNumero = 30
	tercerNumero = 70
	resultadoMenorMayor = ordenar_menor_a_mayor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMenorMayor,tuple),"Se esperaba otra tupla ordenada de Menor a Mayor"
	assert (resultadoMenorMayor, tuple(30,70,100)), "Se esperaba tupla ordenada"

def test_ordenar_mayor_a_menor_dostresuno():
	primerNumero = 30
	segundoNumero = 100
	tercerNumero = 70
	resultadoMayorMenor = ordenar_mayor_a_menor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMayorMenor, tuple), "Se esperaba una tupla ordenada de Mayor a Menor"
	assert (resultadoMayorMenor, tuple(100,70,30)), "Se esperaba tupla ordenada"

def test_ordenar_menor_a_mayor_dostresuno():
	primerNumero = 30
	segundoNumero = 100
	tercerNumero = 70
	resultadoMenorMayor = ordenar_menor_a_mayor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMenorMayor,tuple),"Se esperaba otra tupla ordenada de Menor a Mayor"
	assert (resultadoMenorMayor, tuple(30,70,100)), "Se esperaba tupla ordenada"

def test_ordenar_menor_a_mayor_iguales():
	primerNumero = 30
	segundoNumero = 30
	tercerNumero = 70
	resultadoMenorMayor = ordenar_menor_a_mayor(primerNumero,segundoNumero,tercerNumero)
	assert (resultadoMenorMayor, str), "Se esperaba mensaje de error"