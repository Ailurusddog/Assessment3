def euclidean_algorithm(a, b):
    """
    Calculate the greatest common divisor (GCD) of two positive integers
    using the Euclidean algorithm.
    """
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a


def get_positive_integer(prompt):
    """
    Get a positive integer from user input.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input, please enter a positive integer.")


if __name__ == "__main__":
    a = get_positive_integer("Please enter the first positive integer: ")
    b = get_positive_integer("Please enter the second positive integer: ")

    gcd = euclidean_algorithm(a, b)
    print(f"The greatest common divisor of {a} and {b} is: {gcd}")


