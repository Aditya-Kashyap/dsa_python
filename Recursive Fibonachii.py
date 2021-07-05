def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1

    else:
        return fib(num-2) + fib(num-1)


def fibonacci(num):
    fib_list = []
    for i in range(num):
        fib_list.append(fib(i))

    return fib_list


# Printing the Fibonacci Series:
print(fibonacci(10))
