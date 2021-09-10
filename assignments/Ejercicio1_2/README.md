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
En una tienda de celulares al mayoreo, el precio de los mismos se ha establecido como fijo de acuerdo a la cantidad de productos que lleves y si el celular es de gama alta o media. Observa la tabla de abajo. **En este problema, asumimos que un cliente se lleva celulares de una sóla gama**


|     Cantidad    |  Gama baja    |  Gama alta     | 
| :-------------: |:-------------:| :-------------:| 
|   1 - 3         |    9500       |   15500        |
|    > 3          |    8000       |   15500        |


Escribe una función, la cual **recibe como parámetros**, la gama del celular (A ó M) y la cantidad de celulares que lleva y **regresa como valor de retorno** el costo final de esa cantidad de celulares.

En la función main escribe el código necesario para preguntar al usuario la gama (A o M) y la cantidad de celulares y con el uso de la función creada anteriormente, desplegar el valor de la compra. Deberás validar en el main, que la cantidad sea mayor a 0 y la gama que te hayan dado es A o M, de lo contrario mandarás el mensaje de error como lo puedes ver en los ejemplos.

**Ejemplo de ejecución del programa:** 
``` 
Gama (A/M): M
Cantidad: 4
Total a pagar $31000 
```
**Otro ejemplo**
``` 
Gama (A/M): Media
Cantidad: 5
Error en los datos
``` 
**Otro ejemplo**
``` 
Gama (A/M): M
Cantidad: 4
Total a pagar $32000
``` 
**Uno más**
``` 
Gama (A/M): A
Cantidad: -5
Error en los datos
``` 

**Nota:** Por favor no quites nada de lo que ya tienes, simplemente agrega el código 
necesario dentro de la función main. 
`if __name__ == '__main__':` debe quedarse en tu código para que las pruebas puedan 
ejecutarse adecuadamente.

Una vez que termines tu actividad, si te da tiempo prueba con
`pytest`, si no, simplemente súbela a tu repositorio en GitHub, con el proceso de commit + push.
Debe ser enviada antes de las 9:00 de la mañana que se cierra el ejercicio.

