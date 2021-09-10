# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["25", "34", "0", "20", "-1"],
        # Outputs
        ["Número: ", "Número: ","Número: ", "Número: ","Número: ", "Pares: 3", "Suma de impares: 25"],
        # Message in case of failure
        "Revisa que estes identificando y contabilizando bien los pares y sumando los impares"
    ),
    # Test case 2
    (
       # Inputs
        ["11", "34", "1", "-1"],
        # Outputs
        ["Número: ", "Número: ","Número: ", "Número: ", "Pares: 1", "Suma de impares: 12"],
        # Message in case of failure
        "Revisa que estes identificando y contabilizando bien los pares y sumando los impares"
    ),
    # Test case 3
    (
        # Inputs
        ["-100"],
        # Outputs
        ["Número: ", "Pares: 0", "Suma de impares: 0"],
        # Message in case of failure
        "Revisa que estes identificando y contabilizando bien los pares y sumando los impares"
    ),
    # Test case 4
    (
        # Inputs
        ["0", "-100"],
        # Outputs
        ["Número: ", "Número: ", "Pares: 1", "Suma de impares: 0"],
        # Message in case of failure
        "Revisa que estes identificando y contabilizando bien los pares y sumando los impares"
    )
]