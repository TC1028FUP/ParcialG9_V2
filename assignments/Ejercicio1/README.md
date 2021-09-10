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
Escribe un programa que calcule el monto a pagar de una cuenta de electricidad de un país cercano. Se calcula de acuerdo al consumo de KW consumidos en el mes y de acuerdo a la siguiente tabla y después ve los ejemplos:

| KW consumidos |  Monto a pagar  |  
| :-------------: |:-------------:| 
| primeros 150     | SIN COSTO    |
|entre 150 y 300 | 5 por cada KW que exceda de 150 y hasta de 300  |
|después de 300| 8 por cada KW que exceda de 300 mas los anteriores |

Así por ejemplo, si en una casa consumen 100 KW, la factura es por 0 pesos.

Otro ejemplo, si en una casa se consumen 180 KW
- por los primeros 150 no se paga nada
- por los 30 restantes se paga 150 pesos (30 * 5)
- En total se paga 150

Otro ejemplo si en una casa se consumieron 350 KW el monto de la factura se calcula:
- Por los primeros 150 no se paga nada
- Por los 150 que siguen se paga 750
- Por los 50 últimos se paga 400 (50 * 8)
- En total se paga 1150

De manera que, **escribe una función** que reciba como parámetro la **cantidad de KW** que se consumieron y que nos regrese el monto a pagar. 
En la función main escribe el código necesario para preguntar al usuario la cantidad de KW del mes y usando la función se calcule el monto a pagar y se despliegue.

**Entrada**  
La cantidad de KW consumidos (número entero)

**Salida**  
El monto de la factura con el mensaje correspondiente (ve el ejemplo).

**Ejemplo de ejecución del programa:** 
``` 
Cantidad de KW: 350
La factura de este mes es por 1150  
```
**Nota:** Por favor no quites nada de lo que ya tienes, simplemente agrega el código 
necesario dentro de la función main. 
`if __name__ == '__main__':` debe quedarse en tu código para que las pruebas puedan 
ejecutarse adecuadamente.

Una vez que termines tu actividad, si te da tiempo prueba con
`pytest`, si no, simplemente súbela a tu repositorio en GitHub, con el proceso de commit + push.
Debe ser enviada antes de las 11:00 de la mañana que se cierra el ejercicio.

