

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from maquina_cafe import MaquinaCafe

def test_seleccionar_vaso_pequeno():
    maquina = MaquinaCafe()
    mensaje = maquina.seleccionar_vaso("pequeño")
    assert mensaje == "Vaso pequeño seleccionado: 3 Oz"

def test_seleccionar_vaso_invalido():
    maquina = MaquinaCafe()
    mensaje = maquina.seleccionar_vaso("extra grande")
    assert mensaje == "Tamaño de vaso no válido"

def test_seleccionar_azucar():
    maquina = MaquinaCafe()
    mensaje = maquina.seleccionar_azucar(2)
    assert mensaje == "2 cucharadas de azucar seleccionadas"

def test_vaso_no_disponible():
    maquina = MaquinaCafe()
    maquina.vasos.pequenos = 0
    mensaje = maquina.seleccionar_vaso("pequeño")
    assert mensaje == "No hay vasos disponibles"

def test_cafe_no_disponible():
    maquina = MaquinaCafe()
    maquina.cafetera.cantidad_cafe = 0
    maquina.seleccionar_vaso("mediano")
    mensaje = maquina.preparar_cafe()
    assert mensaje == "No hay suficiente cafe"

def test_azucar_no_disponible():
    maquina = MaquinaCafe()
    maquina.azucarero.cantidad = 0
    maquina.seleccionar_vaso("grande")
    maquina.seleccionar_azucar(2)
    mensaje = maquina.preparar_cafe()
    assert mensaje == "No hay suficiente azucar"

def test_preparar_cafe_completo():
    maquina = MaquinaCafe()
    maquina.seleccionar_vaso("mediano")
    maquina.seleccionar_azucar(3)
    mensaje = maquina.preparar_cafe()
    assert mensaje == "Aquí está su cafe"
