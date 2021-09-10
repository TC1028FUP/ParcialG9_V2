![Tec de Monterrey](../../images/logotecmty.png)
# Ejercicio 2 del examen parcial AD2021
Ciclos while - Preparándote para correr

Te estás preparando para una carrera, hace mucho que no corres y necesitas aumentar poco a poco la distancia que corres en tus prácticas. 
Dado que el primer día corres *X* cantidad de kilómetros y para la carrera debes poder correr *Y* cantidad de kilometros, calcula con un programa el número de días necesarios para que finalmente alcances la distancia que vas a correr en la carrera, considerando que tu entrenamiento consiste en aumentar la distancia que corres cada día en un 10% con respecto al día anterior. Se requiere que el programa calcule e imprima un número entero que represente el número de días que faltan para alcanzar la distancia requerida.

**TIP:** Debes recibir del usuario la cantidad de km que corriste el primer día de práctica, además de la cantidad de km que vas a correr en la carrera. Recuerda que cada día deberás correr un **10% más que el anterior** (eso es lo que incrementas cada día) y la meta es llegar a correr los km de la carrera o más y el objetivo es calcular los días que te tomará llegar a correr esa distancia. 

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
    #escribe todo tu código abajo de esta línea, no es necesario una función
    

if __name__ == '__main__':
    main()
```

**Ejemplo de corrida:**

```
Km primer día: 0.7
Km meta: 10
Días de entrenamiento que faltan: 28
```

**Otro ejemplo de corrida:**

```
Km primer día: 0.5
Km meta: 5
Días de entrenamiento que faltan: 25
```

**Nota:** Por favor no quites nada de lo que ya tienes, simplemente agrega el código 
necesario dentro de la función main. 
`if __name__ == '__main__':` debe quedarse en tu código para que las pruebas puedan 
ejecutarse adecuadamente.

Una vez que termines tu actividad, si te da tiempo prueba con
`pytest`, si no, simplemente súbela a tu repositorio en GitHub, con el proceso de commit + push.
Debe ser enviada antes de las 11:00 de la mañana que se cierra el ejercicio.
