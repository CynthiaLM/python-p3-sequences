#!/usr/bin/env python3

def print_fibonacci(length):
    def fibonacci(n):
        fib_sequence = []
        a, b = 0, 1
        for _ in range(n):
            fib_sequence.append(a)
            a, b = b, a + b
        return fib_sequence

    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib_sequence = fibonacci(length)
        print(fib_sequence)

fib_length = 10  
print_fibonacci(fib_length)
