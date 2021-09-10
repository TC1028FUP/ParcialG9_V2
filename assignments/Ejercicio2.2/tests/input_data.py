# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["25", "134", "110", "-20", "0"],
        # Outputs
        ["Número: ", "Número: ","Número: ", "Número: ","Número: ", "La suma de números entre -100 y 100 es: 5"],
        # Message in case of failure
        "Revisa que estes identificando y sumando sólo los que están entre -100 y 100"
    ),
    # Test case 2
    (
       # Inputs
        ["12", "34", "-100", "0"],
        # Outputs
        ["Número: ", "Número: ","Número: ", "Número: ", "La suma de números entre -100 y 100 es: -54"],
        # Message in case of failure
        "Revisa que estes identificando y sumando sólo los que están entre -100 y 100"
    ),
    # Test case 3
    (
        # Inputs
        ["0"],
        # Outputs
        ["Número: ", "La suma de números entre -100 y 100 es: 0"],
        # Message in case of failure
        "Revisa que estes identificando y sumando sólo los que están entre -100 y 100"
    ),
    # Test case 4
    (
        # Inputs
        ["-3", "0"],
        # Outputs
        ["Número: ", "Número: ", "La suma de números entre -100 y 100 es: -3"],
        # Message in case of failure
        "Revisa que estes identificando y sumando sólo los que están entre -100 y 100"
    )
]