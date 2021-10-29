a=2
b=0
delta = 1
while(b**2)<a:
    print("probando con",b)
    b = b + delta
    if (b**2)>a:
        b = b-delta
        delta = delta/10
print(b)

