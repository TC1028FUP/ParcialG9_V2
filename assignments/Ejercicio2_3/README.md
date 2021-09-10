![Tec de Monterrey](../../images/logotecmty.png)
# Ejercicio 2 del examen parcial AD2021
Ciclos - Promedio de estatura en mujeres.

Escribe un programa que pida la estatura (en metros) y sexo (H/M) de un **número indeterminado** de personas, mientras el usuario responda con una s (minúscula)a la pregunta de que si quiere seguir recibiendo datos. Cuando la respuesta a la pregunta anterior sea n o cualquier otra cosa deberá desplegar el promedio de estatura de las mujeres que fueron ingresadas. **Nota:** asume que el usuario ingresará bien los datos de H o M, así en mayúscula y que dará alturas válidas, así que no requieres para este examen ninguna validación para esos datos.

**TIP:** antes del ciclo while, inicializa con una 's', una variable que se llame respuesta para que entre al ciclo la primera vez, las demás veces dependerá de la respuesta del usuario a si quiere ingresar más datos, esta pregunta debe aparecer después de haber ingresado el dato de una persona, y haber contado y acumulado lo necesario, para poder calcular el promedio de estatura de las mujeres.

**Es importante que si no hubo ninguna mujer entre los datos, se despliegue el mensaje de "No capturaste mujeres" en lugar del cálculo del promedio.**

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
    #escribe todo tu código abajo de esta línea, no es necesario una función
    respuesta = 's'

if __name__ == '__main__':
    main()
```

**Ejemplo de corrida:**

```
Altura: 1.82
Sexo: H
¿Otro dato? s
Altura: 1.70
Sexo: M
¿Otro dato? s
Altura: 1.77
Sexo: M
¿Otro dato? s
Altura: 1.79
Sexo: H
¿Otro dato? n
Promedio de estatura mujeres: 1.735
```

**Otro ejemplo de corrida:**

```
Altura: 1.78
Sexo: H
¿Otro dato? s
Altura: 1.70
Sexo: H
¿Otro dato? s
Altura: 1.77
¿Otro dato? n
No capturaste mujeres
```

**Nota:** Por favor no quites nada de lo que ya tienes, simplemente agrega el código 
necesario dentro de la función main. 
`if __name__ == '__main__':` debe quedarse en tu código para que las pruebas puedan 
ejecutarse adecuadamente.

Una vez que termines tu actividad, si te da tiempo prueba con
`pytest`, si no, simplemente súbela a tu repositorio en GitHub, con el proceso de commit + push.
Debe ser enviada antes de las 11:00 de la mañana que se cierra el ejercicio.
