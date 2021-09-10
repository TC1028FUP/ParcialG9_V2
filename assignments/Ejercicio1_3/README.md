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
En una tienda departamental han llegado las ofertas. El precio de todos los productos se ha establecido como fijo de acuerdo a la cantidad de productos que lleves y el departamento de dónde provienen **En este problema, asumimos que un cliente se lleva productos de un solo departamento**


|     Cantidad    |  Hogar    |  Ferretería     | 
| :-------------: |:-------------:| :-------------:| 
|   1 - 6         |    100      |   150        |
|    > 6          |    80       |   150        |


Escribe una función, la cual **recibe como parámetros**, el departamento (H ó F) y la cantidad de productos que lleva y **regresa como valor de retorno** el costo final de la compra.

En la función main escribe el código necesario para preguntar al usuario el departamento (H o F) y la cantidad de productos, posteriormente con el uso de la función creada anteriormente, desplegar el valor de la compra. Deberás validar en el main, que la cantidad sea mayor a 0 y el departamento que te hayan dado es A o M para poder usar tu función, de lo contrario mandarás el mensaje de error como lo puedes ver en los ejemplos.

**Ejemplo de ejecución del programa:** 
``` 
Departamento (H/F): H
Cantidad: 10
Total a pagar $800 
```
**Otro ejemplo**
``` 
Departamento (H/F): Ferre
Cantidad: 5
Error en los datos
``` 
**Otro ejemplo**
``` 
Departamento (H/F): F
Cantidad: 4
Total a pagar $600
``` 
**Uno más**
``` 
Departamento (H/F): H
Cantidad: 3
Total a pagar $300
``` 

**Nota:** Por favor no quites nada de lo que ya tienes, simplemente agrega el código 
necesario dentro de la función main. 
`if __name__ == '__main__':` debe quedarse en tu código para que las pruebas puedan 
ejecutarse adecuadamente.

Una vez que termines tu actividad, si te da tiempo prueba con
`pytest`, si no, simplemente súbela a tu repositorio en GitHub, con el proceso de commit + push.
Debe ser enviada antes de las 9:00 de la mañana que se cierra el ejercicio.

