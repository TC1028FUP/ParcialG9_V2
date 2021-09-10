# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    ["M", "5"],
    ["Gama (A/M): ","Cantidad: ","Total a pagar $40000" ],
    ["Revisa los ejemplos y la tabla para saber si estás cubriendo todos los casos"]
    ),
    # Test case 2
    (
    ["M", "2"],
    ["Gama (A/M): ","Cantidad: ","Total a pagar $19000" ],
    ["Revisa los ejemplos y la tabla para saber si estás cubriendo todos los casos"]
    ),

    # Test case 3
    (
    ["M", "-5"],
    ["Gama (A/M): ","Cantidad: ","Error en los datos" ],
    ["Revisa los ejemplos y la tabla para saber si estás cubriendo todos los casos"]
    ),
    # Test case 4
    (
    ["baja", "5"],
    ["Gama (A/M): ","Cantidad: ","Error en los datos" ],
    ["Revisa los ejemplos y la tabla para saber si estás cubriendo todos los casos"]
    ),
    # Test case 5
    (
    ["A", "1"],
    ["Gama (A/M): ","Cantidad: ","Total a pagar $15500" ],
    ["Revisa los ejemplos y la tabla para saber si estás cubriendo todos los casos"]
    )
]
