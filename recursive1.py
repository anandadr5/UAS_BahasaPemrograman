def recursive(n):
    if n == 0:
        return 1
    else:
        return n * recursive(n-1)

n = int(input("Masukan bilangan: "))

print (n, " ! = ", recursive(n))