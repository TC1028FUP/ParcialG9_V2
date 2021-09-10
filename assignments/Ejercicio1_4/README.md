![Tec de Monterrey](../../images/logotecmty.png)
# Ejercicio 1 del examen parcial AD2021
Funciones y condicionales

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
# Escribe debajo de esta línea tu función


def main():
  #escribe aqupi el código para interactuar con el usuario y usar la función


if __name__ == '__main__':
    main()
```

## Descripción del programa  
Escribe un programa que calcule el monto a pagar de una cuenta por datos consumidos en un plan celular de una compañia telefónica. Se calcula de acuerdo al consumo de gigabytes consumidos en el mes y de acuerdo a la siguiente tabla y después ve los ejemplos:

| Datos consumidos en GB |  Monto a pagar  |  
| :-------------: |:-------------:| 
| primeros 2      | SIN COSTO    |
|entre 2 y 5 | 115 por cada GB que exceda de 2 y hasta 5  |
|después de 5| 225 por cada GB que exceda de 5 mas el consumo de 2 a 5 |

Así por ejemplo, si en una celular consumen 1.5 GB, la factura es por 0 pesos.

Otro ejemplo, si en un celular se consumen 2.5 GB
- por los primeros 2 no se paga nada
- por el 0.5 restantes se paga 57.5 pesos (115 * 0.5)
- En total se paga 115

Otro ejemplo si en un celular se consumieron 7.5 GB el monto de la factura se calcula:
- Por los primeros 2 no se paga nada
- Por los 3 que siguen se paga 345 (115 * 3)
- Por los 2.5 últimos se paga 562.5 (225 * 2.5)
- En total se paga 907.5

De manera que, **escribe una función** que reciba como parámetro la **cantidad de GB** que se consumieron y que nos regrese el monto a pagar. 
En la función main escribe el código necesario para preguntar al usuario la cantidad de GB del mes y usando la función se calcule el monto a pagar y se despliegue.

**Entrada**  
La cantidad de GB consumidos (número entero)

**Salida**  
El monto de la factura con el mensaje correspondiente (ve el ejemplo).

**Ejemplo de ejecución del programa:** 
``` 
Cantidad de GB: 7.5
La factura de este mes es por 907.5  
```
**Nota:** Por favor no quites nada de lo que ya tienes, simplemente agrega el código 
necesario dentro de la función main. 
`if __name__ == '__main__':` debe quedarse en tu código para que las pruebas puedan 
ejecutarse adecuadamente.

Una vez que termines tu actividad, si te da tiempo prueba con
`pytest`, si no, simplemente súbela a tu repositorio en GitHub, con el proceso de commit + push.
Debe ser enviada antes de las 11:00 de la mañana que se cierra el ejercicio.

