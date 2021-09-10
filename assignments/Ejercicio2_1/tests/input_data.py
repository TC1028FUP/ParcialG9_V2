# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["5", "12", "34", "9", "-5"],
        # Outputs
        ["Ciclo se detiene con un múltiplo de: ","Número: ", "Número: ","Número: ", "Número: ", "Suma: 55"],
        # Message in case of failure
        "Revisa que el ciclo se detenga con el múltiplo adecuado y que realice bien la suma"
    ),
    # Test case 2
    (
      # Inputs
        ["3", "9"],
        # Outputs
        ["Ciclo se detiene con un múltiplo de: ","Número: ", "Suma: 0"],
        # Message in case of failure
        "Revisa que el ciclo se detenga con el múltiplo adecuado y que realice bien la suma"
    ),
    # Test case 3
    (
        ["3", "1","9"],
        # Outputs
        ["Ciclo se detiene con un múltiplo de: ","Número: ", "Número: ","Suma: 1"],
        # Message in case of failure
        "Revisa que el ciclo se detenga con el múltiplo adecuado y que realice bien la suma"
    ),
]