# Dado um array chamado an_array de números inteiros não negativos, retorne um array composto de 
# todos os elementos pares seguidos de todos os elementos ímpares de an_array

import array

def algo(an_array):
    arr = array.array('i')

    for i in range(len(an_array)):
        if an_array[i] % 2 == 0:
            arr.append(an_array[i])

    for j in range(len(an_array)):
        if an_array[j] % 2 != 0:
            arr.append(an_array[j])

    return arr

print(algo(array.array('i', (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))))
# done
