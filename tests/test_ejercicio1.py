################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest
from src.Ejercicio1 import convertir_a_centigrados, convertir_a_fahrenheit

def test_farenheit_a_centigrados():
    """
    Pasamos un numero para convertir a centigrados
    """
    nroFahrenheit = 1345
    resultado = convertir_a_centigrados(nroFahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un número flotante"
    assert resultado == 729.4444, "No obtenemos el resultado esperado"
    
def test_centigrados_a_fahrenheit():
	"""
	Pasamos un numero para convertir a fahrenheit
	"""
	nroCelsius = 37
	resultado = convertir_a_fahrenheit(nroCelsius)
	assert isinstance(resultado, float), "El resultado debe ser un número flotante"
	assert resultado == 98.6, "No obtenemos el resultado esperado"
