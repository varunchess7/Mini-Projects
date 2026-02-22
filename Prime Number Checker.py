while True:
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True  # 2 is the only even prime
        if n % 2 == 0:
            return False

        for i in range(3, int(n ** 0.5) + 1, 2):  # check only odd numbers
            if n % i == 0:
                return False
        return True

    # Example usage
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")