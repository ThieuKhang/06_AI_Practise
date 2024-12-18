def factorial_calculate(n):
    factorials = [1] * (n + 1)
    for i in range(2, n + 1):
        factorials[i] = factorials[i - 1] * i
    return factorials[n]

while True:
    try:
        n = int(input("Enter a non_negative integer: "))
        if n >= 0:
            break
        else:
            print("Please enter a non_negative interger.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

factorial_result = factorial_calculate(n)
print(f"The factorial of {n} is : {factorial_result}")