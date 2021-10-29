#funciones

def factorialIter(n):
    print("entrando al factorial iterativo")
    temp = 1
    for i in range(1,n+1):
        temp= temp*i
    return (temp)

def factorialRecur(n):
    print("entrando al factorial recursivo")
    if(n==0):
        return(1)
    else:
        return n*factorialRecur(n-1)
    
print(factorialIter(5))
print(factorialRecur(5))
