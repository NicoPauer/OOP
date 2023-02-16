// Uso macros del preprocesador para no compilar varias veces el mismo archivo
#ifndef PERSONAJE_HPP
#define PERSONAJE_HPP
#include <string> // Incluyo esto para poder usar la clase std :: string que provee un tipo de dato necesario

class Personaje
{

    private:
        std :: string nombre;
        int contadorHabilidades, contadorGustos;
        std :: string habilidades[13];
        std :: string gustos[13];
    public:
      // Consrtuctor
        Personaje(std :: string nom, std :: string hab[13]);
      // Metodos
        void agregarGusto(std :: string gus);
        void agregarGustos(std :: string gus[13]);
        void agregarHabilidad(std :: string hab);
        void agregarHabilidades(std :: string hab[13]);
        void renombrar(std :: string nom);
        std :: string obtenerNombre() {return nombre;};
        std :: string obtenerHabilidad(int h) {return habilidades[h];};
        std :: string obtenerGusto(int g) {return gustos[g];};
        int obtenerMaxHabilidades() {return 13;};
        int obtenerMaxGustos() {return 13;};
  // DESPUES SE DEBE IMPLEMENTAR EL CONSTRUCTOR Y LOS METODOS EN EL PROGRAMA QUE LO IMPORTE
  // Sintaxis: <tipo_de_dato> <nombre_de_clase> :: <nombre_de_miebro> {<implementacion>}
  // Nota: reemplazar lo que este dentro de "<>" y también esos simbolos que los contienen
  /*
    Ejemplo:
        Personaje :: Personaje(string nom, string hab[13])
        {
            this -> nombre = nom;
            this -> habilidades = hab
        }
   */
};

#endif
