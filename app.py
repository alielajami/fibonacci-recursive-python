''' Fibonacci sequence generator using recursion '''
def fibonacci(n):
    """Recursive function to generate Fibonacci sequence up to n"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    return fibonacci(n - 1) + [fibonacci(n - 1)[-1] + fibonacci(n - 1)[-2]]
    # for n = 4
    # fibonacci(3) + [fibonacci(3)[-1] + fibonacci(3)[-2]]
    #[0,1,1] + [1 + 1]
    #[0,1,1] + [2]
    #[0,1,1,2]

num = int(input("Enter a number n to generate the Fibonacci sequence: "))
print("Fibonacci sequence:", fibonacci(num))
