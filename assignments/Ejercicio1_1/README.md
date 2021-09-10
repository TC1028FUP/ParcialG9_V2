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
En una tienda prestigiosa de cuyo nombre no quiero acordarme, están en promoción, te dicen que te elijas 3 productos y **te lleves el de menor precio de manera gratuita**. Para esto, requieren un programa que determine cuánto va a pagar el cliente por los 3 productos con esta promoción. 

De manera que, **escribe una función** que reciba como parámetro los ** 3 precios de los productos** que se lleva el cliente y que **nos regrese** (uso de return) el monto a pagar por la promoción.

En la función main escribe el código necesario para preguntar al usuario los 3 precios de los productos y usando la función definida anteriormente, se calcule el monto a pagar y se despliegue.

**Entrada**  
3 valores númericos que pueden ser con punto decimal

**Salida**  
El monto del ticket con el mensaje correspondiente (ve el ejemplo).

**Ejemplo de ejecución del programa:** 
``` 
Precio producto: 1234.50
Precio producto: 725.60
Precio producto: 1150.25
Total a pagar por promoción: $2384.75 
```
**Otro ejemplo:**
```
Precio producto: 123.45
Precio producto: 231.50
Precio producto: 123.45
Total a pagar por promoción: $354.95
```
**Nota:** Por favor no quites nada de lo que ya tienes, simplemente agrega el código 
necesario dentro de la función main. 
`if __name__ == '__main__':` debe quedarse en tu código para que las pruebas puedan 
ejecutarse adecuadamente.

Una vez que termines tu actividad, si te da tiempo prueba con
`pytest`, si no, simplemente súbela a tu repositorio en GitHub, con el proceso de commit + push.
Debe ser enviada antes de las 11:00 de la mañana que se cierra el ejercicio.

