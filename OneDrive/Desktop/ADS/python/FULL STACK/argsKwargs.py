"""ARGS - utilizamos quando nao temos certeza de quantos argumentos queremos ter em uma função, os argumentos sao passados com uma tupla"""


def sum(*num):
    sumTotal = 0 
    for n in num:
        sumTotal += n
        print(f"Soma é: {sumTotal}")
        
sum(7,8,9,10,11)