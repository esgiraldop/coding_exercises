def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

num = 5
print(f'The factorial of {num} is {factorial(num)}')