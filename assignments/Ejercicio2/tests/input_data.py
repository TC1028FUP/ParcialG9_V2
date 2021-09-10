# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["25", "34", "0", "20", "-7"],
        # Outputs
        ["Número: ", "Número: ","Número: ", "Número: ","Número: ", "Tecleaste 3 múltiplos de 5"],
        # Message in case of failure
        "Revisa que estes identificando y contabilizando bien los múltiplos de 5"
    ),
    # Test case 2
    (
       # Inputs
        ["12", "34", "1", "-1"],
        # Outputs
        ["Número: ", "Número: ","Número: ", "Número: ", "Tecleaste 0 múltiplos de 5"],
        # Message in case of failure
        "Revisa que estes identificando y contabilizando bien los múltiplos de 5"
    ),
    # Test case 3
    (
        # Inputs
        ["-100"],
        # Outputs
        ["Número: ", "Tecleaste 0 múltiplos de 5"],
        # Message in case of failure
        "Revisa que estes identificando y contabilizando bien los múltiplos de 5"
    ),
    # Test case 4
    (
        # Inputs
        ["0", "-100"],
        # Outputs
        ["Número: ", "Número: ", "Tecleaste 1 múltiplos de 5"],
        # Message in case of failure
        "Revisa que estes calculando bien todos los casos"
    )
]