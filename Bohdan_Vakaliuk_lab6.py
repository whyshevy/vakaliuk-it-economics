m = int(input("Enter your m = "))
k = int(input("Enter your k = "))

def fact(n):
    fact = 1
    while (n > 0):
        fact *= n
        n -= 1
    return fact

def root(n, number):
    x = 1
    for i in range(10):
        x = (1 / n) * ((n - 1)* x + number / x**(n - 1))
    return x

y = (fact(k) / fact(m)) * (root(3, k))**2 - m**2 * (root(5,k))**3

print("Your y is ", y)

input("Press Enter to exit...")
