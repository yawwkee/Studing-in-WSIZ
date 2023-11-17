n = int(input("enter values for fibonacci "))
def fibonacci(n):
    a = [0,1]
    while len(a)< n:
        a.append(a[-1]+a[-2])
    return a
print(fibonacci(n))