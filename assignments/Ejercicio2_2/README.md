![Tec de Monterrey](../../images/logotecmty.png)
# Ejercicio 2 del examen parcial AD2021
Ciclos - Cuántos pares e impares recibes

Escribe un programa que reciba números positivos (considera el 0 como positivo) y vaya contando aquellos números que son pares y vaya sumando los impares. El programa deberá dejar de recibir números hasta que el usuario ingrese un número negativo, al suceder esto, debe mostrar el mensaje de cuántos pares recibió además de la suma de los impares.

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
    #escribe todo tu código abajo de esta línea, no es necesario una función

if __name__ == '__main__':
    main()
```

Ejemplo de corrida:

```
Número: 2
Número: 5
Número: 0
Número: 12
Número: 150
Número: -1
Pares: 4
Suma de impares: 5
```


**Nota:** Por favor no quites nada de lo que ya tienes, simplemente agrega el código 
necesario dentro de la función main. 
`if __name__ == '__main__':` debe quedarse en tu código para que las pruebas puedan 
ejecutarse adecuadamente.

Una vez que termines tu actividad, si te da tiempo prueba con
`pytest`, si no, simplemente súbela a tu repositorio en GitHub, con el proceso de commit + push.
Debe ser enviada antes de las 11:00 de la mañana que se cierra el ejercicio.
