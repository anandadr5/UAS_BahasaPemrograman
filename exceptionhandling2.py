def Except(a):
    if a < 4:
        b = a / (a-3)
    print ("Value of b = ", b)

try:
    Except(3)
    Except(5)

except ZeroDivisionError:
    print ("ZeroDivisionError terjadi dan ditangani")
except NameError:
    print ("NameError terjadi dan ditangani")