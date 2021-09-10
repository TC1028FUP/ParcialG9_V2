# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["1.82", "H", "s", "1.67", "M", "s", "1.59", "M", "s","1.68", "H", "s","1.75", "M", "n"],
        # Outputs
        ["Altura: ", "Sexo: ","¿Otro dato? ","Altura: ", "Sexo: ","¿Otro dato? ","Altura: ", "Sexo: ","¿Otro dato? ","Altura: ", "Sexo: ","¿Otro dato? ","Altura: ", "Sexo: ","¿Otro dato? ", "Promedio de estatura mujeres: 1.67" ],
        # Message in case of failure
        "Revisa que estes contando y acumulando los datos adecuados para el cálculo del promedio"
    ),
    # Test case 2
    (
        # Inputs
        ["1.82", "H", "s", "1.67", "H", "s", "1.59", "H", "s","1.68", "H", "s", "1.75", "H", "n"],
        # Outputs
        ["Altura: ", "Sexo: ","¿Otro dato? ","Altura: ", "Sexo: ","¿Otro dato? ","Altura: ", "Sexo: ","¿Otro dato? ","Altura: ", "Sexo: ","¿Otro dato? ", "Altura: ", "Sexo: ","¿Otro dato? ", "No capturaste mujeres" ],
        # Message in case of failure
        "Revisa que estes contando y acumulando los datos adecuados para el cálculo del promedio"
    ),
    # Test case 3
    (
         # Inputs
        ["1.82", "M", "n"],
        # Outputs
        ["Altura: ", "Sexo: ","¿Otro dato? ", "Promedio de estatura mujeres: 1.82" ],
        # Message in case of failure
        "Revisa que estes contando y acumulando los datos adecuados para el cálculo del promedio"
    ),
    # Test case 4
    (
         # Inputs
        ["1.82", "M", "s", "1.67", "M", "s", "1.59", "M", "n"],
        # Outputs
        ["Altura: ", "Sexo: ","¿Otro dato? ","Altura: ", "Sexo: ","¿Otro dato? ","Altura: ", "Sexo: ","¿Otro dato? ", "Promedio de estatura mujeres: 1.6933333333333334" ],
        # Message in case of failure
        "Revisa que estes contando y acumulando los datos adecuados para el cálculo del promedio"
    )
]