#!/usr/bin/python3

'''

 Autor: Nicolas Pauer, 10 de mayo al 16 de julio del 2023 v1.3.1

    Arma el inventario de productos con sus precios, nombre de
    producto, cantidad de unidades disponibles y su respectivo codigo.
'''


class Producto():
    '''
        Define el producto y sus caracteristicas.
    '''
    def __init__(self, nom, cod):

        self.nombre = nom 

        self.codigo = cod
      # Inicializo el precio en un valor de coma flotante(real de 32 bits o 4 bytes) 
        self.precio = float(0)
        '''
            Inicializo con las unidades medidas con numeros enteros, cero al principio.
        '''
        self.unidades = int(0)

    def remarcar(self, p):
        '''
            Actualiza el precio de producto al
            precio expresado en numero real con notacion 
            de punto que recibe como parametro.
        '''
        self.precio = p

    def retirar(self, cantidad):
        '''
            Retira una cantidad entera de unidades del
            producto, si es mayor a la cantidad de unidades
            disponibles muestra por consola un mensaje de
            error y escribe un log al archivo 'inventario.logs'.
        '''
        if (cantidad <= self.unidades):
          # Retiro de las unidades disponibles la cantidad,por lo tanto, reduzco las unidades disponibles a la cantidad del parametro
            self.unidades -= cantidad
        else:
          # Si se quieren retirar mas unidades que las disponibles muestro mensaje de error y escribo al log 
            print('Te pasaste por ' + str(cantidad - self.unidades) + ', hay tan solo %s unidades disponibles.\n' % self.unidades)
          # Agrego log 
            log = open('inventario.logs', 'a')
            log.write('* Cantidad Solicitada No Disponible, se pidieron %s unidades y tan solo hay %s disponibles.\n' % cantidad % self.unidades)
            log.close()

    def agregar(self, cantidad):
        '''
            Agrega a unidades la cantidad de productos que
            se agregaron.
        '''
        self.unidades += cantidad

    def mostrar(self):
        '''
            Muestra el valor de las principales caracteristicas del producto.
        '''
        print(self.nombre + (' de codigo %s' % self.codigo) + ' vale $' + str(self.precio) + ' c/u de las %s unidades disponibles.\n' % self.unidades)

    def registrar(self, archivo):
        '''
            Guarda datos de un producto en un archivo con el inventario.
        '''
      # Define la salida al archivo
        salida = ('  * ' + self.nombre + ' de codigo ' + str(self.codigo) + ' vale $' + str(self.precio) + ' c/u de las ' + str(self.unidades) + ' disponibles.\n')
      # Guarda salida a archivo de inventario 
        inventario = open(archivo, 'a')
        inventario.write(salida)
        inventario.close()


class Inventario():
    '''
        Inventario con los distintos productos de la clase Producto.
    '''
    def __init__(self, productos):

        self.inventario = productos

    def cantidad(producto):
        '''
            Cuenta cuanta unidades de un producto hay en el inventario.
        '''

        unidades = 0

        if (type(producto) == 'int'):
          # Si es un codigo de producto lo busco en el inventario comparando al codigo de cada producto
            for buscar in inventario:
              # Relizo la busqueda entre todos los productos del inventario
                if (buscar.codigo == producto):
                  # Encontre que se registro el producto, sumo al cpnteo las unidades
                    unidades += producto.unidades
    pass

# Hago una prueba implementado las clases para hacer un mini gestor de inventarios

print('Hago el inventario de productos.\n')

nombre = input('\tIngrese nombre de producto: ')
codigo = input('\tIngrese código de producto: ')
unidades = int(input('\tIngrese unidades disponibles: '))
precio = float(input('\tIngrese precio del producto: '))

# Hago instancia a la clase Producto
prod = Producto(nombre, codigo)
# Actulizo datos que no han sido alterados por el constructor
prod.remarcar(precio)
prod.agregar(unidades)
# Muestro la informacion del producto y la guardo en archivo 'inventario.txt'
prod.mostrar()
prod.registrar('inventario.txt')
