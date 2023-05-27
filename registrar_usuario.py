#!/usr/bin/python3

# Obtiene nombre, apellido, edad y mail de un usuario y muestra si tiene suficiencia de edad y si lo es, guarda datos en la clase Usuario
# Esto es un comentario y es ignorado por el interprete

# Defino la clase usuario
class Usuario():

    '''
        Modela los datos de un usuario, esto
        es una clase que es un objeto que 
        abstrae y generaliza el problema a
        resolver, en este caso obtener informacion de un
        usuario.
    '''

    def __init__(self, name, age):
      # Este es el constructor un metodo de la clase usuario para definir e inicializar sus propiedades
      # Los metodos y las propiedades son atributos de la clase 
        self.nombre = name.capitalize() 
        self.edad = age
     # La inicializo como cadena de caracteres vacia para que el interprete sepa que tipo de dato es
        self.mail = ''

    def data(self):
        '''

           (Documentación del método)

            Devuelve como cadena de caracteres 
            todos los datos del usuario.
        ''' 
      # Consulta cada atributo de la clase, lo convierte a cadena si es necesario, los suma y los devuelve
        return (self.nombre + ' ' + self.apellido + ' tiene ' + str(self.edad) + ' años y su mail es ' + self.mail + ' REGISTRADO.\n')

# Defino las variables y le asigno la entrada del usuario para cada dato 

nombre = input('Ingrese nombre: ')

while (nombre == ''):
 # Mientras el nombre este vacio, lo reingreso hasta obtener uno valido
    nombre = input('No debe estar en blanco: ')

apellido = input('Ingrese apellido: ')

while (apellido == ''):
 # Lo mismo para el apellido
 # En python la identacion de bloques es importante, se hace con tab
    apellido = input('Ingrese apellido valido: ')

# Convierte la entrada de cadena a entero y lo asigna a edad
edad = int(input('Ingrese edad: '))

if (edad <= 5):
  # Debe ser una edad razonable para seguir, sino sale del programa
    exit(1)

mail = input('Ingrese mail: ')

while ((mail == '') or (not mail.__contains__('@')) or (not mail.__contains__('.'))):
  # Debe ser un mail valido con un '@' y un dominio
  # El Atributo __contains__ dice si una cadena contiene cierto texto clave
  # or, not, and son operadores logicos 
    mail = input('Ingrese mail valido: ')

if (edad >= 18):
  # Si el usuario tiene 18 años o mas, muestra por terminal que tiene suficiencia de edad y guarda los datos en una instancia de la clase Usuario 
    print('Tienes la suficiencia de edad.\n')
  # Instancia a la clase Usuario

    adulto = Usuario(nombre, edad)
 # Similar a lo que pasó antes
    adulto.mail = mail
 # Establezco apellido de usuario
    adulto.apellido = apellido.capitalize()
 # Muesrra por terminal todos los datos que se obtuvieron
    print(adulto.data())
 # Hace lo mismo pero a un archivo de usuarios
 # Abro archivo en modo de append, agrgegar texto
    users = open('users.txt', 'a')
 # Agrego el registro   
    users.write(adulto.data() + '----------------------------------------------------------------------\n')
 # Cierro el archivo para que lo pueda usar el sistema operativo
    users.close()
else:
 # Si el usuario es menor se lo digo y no creo instancia a la clase Usuario
    print('Eres menor de edad no puedo registrarte') 
