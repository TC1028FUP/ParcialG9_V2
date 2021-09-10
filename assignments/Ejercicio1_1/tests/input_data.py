# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    ["123.50", "234.50", "234.0"],
    ["Precio producto: ", "Precio producto: ", "Precio producto: ", "Total a pagar por promoción: $468.5"],
    ["Revisa los ejemplos y los casos de prueba"]
    ),
    # Test case 2
    (
    ["1230.50", "200.50", "234.0"],
    ["Precio producto: ", "Precio producto: ", "Precio producto: ", "Total a pagar por promoción: $1464.5"],
    ["Revisa los ejemplos y los casos de prueba"]
    ),
    # Test case 3
    (
    ["1230.50", "200.50", "34.0"],
    ["Precio producto: ", "Precio producto: ", "Precio producto: ", "Total a pagar por promoción: $1431.0"],
    ["Revisa los ejemplos y los casos de prueba"]
    ),
    # Test case 4
    (
    ["200.50", "200.50", "200.50"],
    ["Precio producto: ", "Precio producto: ", "Precio producto: ", "Total a pagar por promoción: $401.0"],
    ["Revisa los ejemplos y los casos de prueba"]
    ),
    # Test case 5
    (
    ["-1", "200.50", "200.50"],
    ["Precio producto: ", "Precio producto: ", "Precio producto: ", "Error en los datos"],
    ["Revisa los ejemplos y los casos de prueba"]
    ),
]
