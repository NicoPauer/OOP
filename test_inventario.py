#!/usr/bin/python3
# Test file for inventario class

from inventario import Inventario

from invantario import Producto

def test_inventario():

  producto = Producto("Harina", 1234)
  
  contado = Inventario([producto, producto, producto])

  assert contado.cantidad(producto) == 3
