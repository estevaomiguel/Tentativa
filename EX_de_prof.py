def sum_even(lista):
    count = 0
    for numero in lista:
        try:
            if numero % 2 == 0:
                count = count + numero
        except:
            print("nao é um numero passei a frente")
    return count



print(sum_even([1,2,3,4,5,6,7,8]))
print(sum_even([1,2,"papagaio",7,8]))

#try except
#
