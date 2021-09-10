![Tec de Monterrey](../../images/logotecmty.png)
# Ejercicio 2 del examen parcial AD2021
Ciclos - Recibe y suma números hasta que te den un múltiplo

Escribe un programa reciba números positivos o negativos (considera el 0 como positivo) y vaya sumando esos números. El programa deberá dejar de recibir números hasta que el usuario ingrese un múltiplo de un número que haya indicado el usario al inicio del programa. Al final se desplegará la suma de los números.


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
Ciclo se detiene con un múltiplo de: 5
Número: 12
Número: 34
Número: 1
Número: 9
Número: 15  ----- > observa que es múltiplo de 5 y ya no se suma y termina el ciclo
Suma: 56
```


**Nota:** Por favor no quites nada de lo que ya tienes, simplemente agrega el código 
necesario dentro de la función main. 
`if __name__ == '__main__':` debe quedarse en tu código para que las pruebas puedan 
ejecutarse adecuadamente.

Una vez que termines tu actividad, si te da tiempo prueba con
`pytest`, si no, simplemente súbela a tu repositorio en GitHub, con el proceso de commit + push.
Debe ser enviada antes de las 11:00 de la mañana que se cierra el ejercicio.
