# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["0.5", "5"],
        # Outputs
        ["Km primer día: ", "Km meta: ", "Días de entrenamiento que faltan: 25"],
        # Message in case of failure
        "Revisa que estés aumentando el 10% de lo que corres el día anterior y no olvides contabilizar los días"
    ),
    # Test case 2
    (
        # Inputs
        ["0.25", "5"],
        # Outputs
        ["Km primer día: ", "Km meta: ", "Días de entrenamiento que faltan: 32"],
        # Message in case of failure
        "Revisa que estés aumentando el 10% de lo que corres el día anterior y no olvides contabilizar los días"
    ),
    # Test case 3
    (
        # Inputs
        ["0.7", "10"],
        # Outputs
        ["Km primer día: ", "Km meta: ", "Días de entrenamiento que faltan: 28"],
        # Message in case of failure
        "Revisa que estés aumentando el 10% de lo que corres el día anterior y no olvides contabilizar los días"
    ),
    # Test case 4
    (
        # Inputs
        ["1.2", "42"],
        # Outputs
        ["Km primer día: ", "Km meta: ", "Días de entrenamiento que faltan: 38"],
        # Message in case of failure
        "Revisa que estés aumentando el 10% de lo que corres el día anterior y no olvides contabilizar los días"
    )
]