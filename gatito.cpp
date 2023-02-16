/* Clase principal que usa la implementacion de la clase Personaje para
 crear como seria un gatito */

// Agrego el archivo de cabecera con la clase ya implementada
#include "Personaje_implementacion.hpp"
// Agrego otras bibliotecas estandar importantes
#include <iostream>
#include <string>

using namespace std;

int main()
{
    std :: string destrezas[13] = {"Dormir", "Comer", "Cazar", "Jugar", "Maullar", "Ronronear"};
  // Construye el objeto temporal 'gato'
    Personaje gato("Un Gatito", destrezas);
   // Agrego habilidades extra
    gato.agregarHabilidad("Oir mas que un humano");
    gato.agregarHabilidad("Oler mas que un humano");
  // Muestro el nombre del personaje y sus habilidades
    cout << endl << "El personaje de hoy es: " << gato.obtenerNombre() << ".\n" << endl;
    cout << "Sus habilidades son: \n" << endl;
    for (int index = 0; index < gato.obtenerMaxHabilidades(); index++)
    {
        if (gato.obtenerHabilidad(index) != "")
        {
            cout << " -- " << gato.obtenerHabilidad(index) << endl;
        }
    }
    cout << endl;
 // Muestro sus gustos agregandolos previamente con el metodo agregarGusto
    gato.renombrar("Al Gato Le gusta: \n");
    cout << gato.obtenerNombre() << endl;
  // No voy agregar el maximo de gustos que son 6 para abstraermo de esos datalles
    gato.agregarGusto("Estar bien Alto");
    gato.agregarGusto("Comer Atún");
    gato.agregarGusto("Correr");
    for (int index = 0; index < gato.obtenerMaxGustos(); index++)
    {
      // Como no agregue todo lo que puede tener solo muestro los gustos solo si están definidos, que no muestre espacios en blanco
        if (gato.obtenerGusto(index) != "")
        {
            cout << " -- " << gato.obtenerGusto(index) << endl;
        }
    }
    cout << endl;
    return 0;
}
