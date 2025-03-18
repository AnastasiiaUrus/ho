from utils import factorial, is_prime, is_power_of_2

def main():
    number = 5
    print(f"Factorial of {number} is {factorial(number)}")
    print(f"Is {number} prime? {is_prime(number)}")
    print(f"Is {number} a power of 2? {is_power_of_2(number)}")

if __name__ == "__main__":
    main()
