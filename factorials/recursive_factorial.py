def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n-1)
        return temp * n

print(recur_factorial(5))

# this is slower than iterative 