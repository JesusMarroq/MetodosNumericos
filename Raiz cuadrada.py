a=2
b=0
delta = 1
while abs(b**2-a)>0.0000000000001:
    print("probando con",b,"incremento de " ,delta)
    b = b + delta
    if (b**2)>a:
        b = b-delta
        delta = delta/10
print(b)

