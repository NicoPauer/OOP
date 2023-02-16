/* Agrego la clase que quiero implementar para no tener que implementarla cada vez que la quiero usar ya que no se requiere
 personalizar los metodos a distintos contextos */
// DONDE SE CONCENTRAN LOS ERRORES
#include "Personaje.hpp"
#include <string>
// Directivas de preprocesador para que el archivo no compile dos veces(macro PERSONAJE_IMPLEMENTACION_HPP)
#ifndef PERSONAJE_IMPLEMENTACION_HPP
#define PERSONAJE_IMPLEMENTACION_HPP

Personaje :: Personaje(std :: string nom, std :: string hab[13])
{
    this -> nombre = nom;
    for (int i = 0; i < 13; i++)
    {
      // Agrego cada habilidad por separado porque sino hay incompoatibilidad de tipos(Un item de la lista es distinto a una lista completa)
        this -> habilidades[i] = hab[i];
    }
    this -> contadorGustos = 0;
    this -> contadorHabilidades = 0;
};

void Personaje :: agregarGusto(std :: string gus)
{
  // Si no supero el maximo de gustos, sigo agregando
    if (contadorGustos < 13)
    {
        gustos[contadorGustos] = gus;
      // Ya que no supere el maximo de gusto puedo ir incrementando para el siguiente gusto si es que se agrega
        contadorGustos += 1;
    }
};

void Personaje :: agregarGustos(std :: string gus[13])
{
  // Agrego cada habilidad por separado para no mezclar tipos de datos
    for (int i = 0; i < 13; i++)
    {
        gustos[i] = gus[i];
    }
    contadorGustos = 13;
};

void Personaje :: agregarHabilidad(std :: string hab)
{
  // Si no supero el maximo de habilidades puedo agregar otra habilidad
    if (contadorHabilidades < 13)
    {
        habilidades[contadorHabilidades] = hab;
     // Ya que no supere el maximo de habilidades puedo agregar por lo menos una habilidad mas
        contadorHabilidades += 1;
    }
};

void Personaje :: agregarHabilidades(std :: string hab[13])
{
  // Agrego por separado para no mezclar tipos de datos
    for (int i = 0; i < 13; i++)
    {
        habilidades[i] = hab[i];
    }
    contadorHabilidades = 13;
};

void Personaje :: renombrar(std :: string nom)
{
    nombre = nom;
};

#endif
