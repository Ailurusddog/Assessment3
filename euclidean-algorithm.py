def Euclidean_Algorithm(a, b):
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a

if __name__ == "__main__":
    try:
        a = int(input("Enter the first positive integer: "))
        b = int(input("Enter the second positive integer: "))
        if a <= 0 or b <= 0:
            raise ValueError("Both numbers must be positive integers.")
        gcd = Euclidean_Algorithm(a, b)
        print(f"The greatest common divisor of {a} and {b} is: {gcd}")
    except ValueError as ve:
        print(f"Error: {ve}")

