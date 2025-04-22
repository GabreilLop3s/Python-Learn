#Modulo de operacções matematicas

def sum(x, y):
    return x + y 

def substract (x,y):
    return x - y

def multiply (x,y):
    return x * y 

def divide (x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Não é permitido divisão por Zero")