![Tec de Monterrey](../../images/logotecmty.png)
# Ejercicio 1 del examen parcial AD2021
Funciones y condicionales

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
# Escribe debajo de esta línea tu función


def main():
  #escribe aquí el código para interactuar con el usuario y usar la función


if __name__ == '__main__':
    main()
```

## Descripción del programa  
Escribe una función suma_loca que **recibe como parámetros** tres valores enteros que representan edades y **debe regresar** (uso de return) la suma de los 3 números bajo las siguientes condiciones:
-  Datos menores a 0 y mayores 100 no se deben sumar su valor es **0** para la suma loca.  
-  Si alguno de los números representa la edad de un adolescente (13-18 inclusive), no se debe sumar, de manera que su valor es también 0 para la suma loca.

**Tip:** Crea una segunda función que reciba un sólo número y determine cuál es su valor para la suma anterior, es decir, si es 0 o menor o si es mayor a 100, o si es de las edades entre 13 y 18 el valor que debe regresar es 0, si no, su valor normal. De manera que la función suma_loca sólo llame a esta función para resolver el problema.

Una vez que tengas tus funciones anteriores, en la función main escribe toda las instrucciones de interacción con el usuario, es decir solicitar los 3 números al usuario y posteriormente con el uso de la función suma_loca determinar el valor de la suma y desplegar a pantalla el resultado con el mensaje correspondiente (ver ejemplo para ver cómo deben de ser los mensajes de entrada y salida)

**Entrada**  
Tres números enteros

**Salida**  
La suma de los números bajo las condiciones descritas anteriormente.

**Ejemplo de ejecución del programa:** 
``` 
Número 1: 1
Número 2: 13
Número 3: 34
La suma loca es de 35 
```

**Ejemplo 2 de ejecución del programa:** 
``` 
Número 1: 11
Número 2: 23
Número 3: 10
La suma loca es de 44 
```

**Nota:** Por favor no quites nada de lo que ya tienes, simplemente agrega el código de la función donde se te indica y agrega también el código necesario dentro de la función main. 
`if __name__ == '__main__':` debe quedarse en tu código para que las pruebas puedan 
ejecutarse adecuadamente.

Una vez que termines tu actividad, si te da tiempo prueba con
`pytest`, si no, simplemente súbela a tu repositorio en GitHub, con el proceso de commit + push.
Debe ser enviada antes de las 11:00 de la mañana que se cierra el ejercicio.

