import random
import time

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSort(left) + middle + quickSort(right)

# Caso 1: Melhor Caso - Valores em ordem crescente
print("\nMelhor Caso: Valores em ordem crescente (já ordenados)")
arr1 = [5, 6, 7, 8, 9]
arr1 = quickSort(arr1)
print("Lista ordenada: ", arr1)

# Caso 2: Caso Médio - Valores desordenados com números aleatórios
print("\nCaso Médio: Valores desordenados com números aleatórios")
arr2 = [5, 2, 9, 1, 7]
arr2 = quickSort(arr2)
print("Lista ordenada: ", arr2)

# Caso 3: Pior Caso - Valores em ordem decrescente
print("\nPior Caso: Valores em ordem decrescente")
arr3 = [9, 8, 7, 6, 5]
arr3 = quickSort(arr3)
print("Lista ordenada: ", arr3)

# Teste de desempenho para os três casos e tamanhos de lista
for n in [1000, 10000, 100000]:
    for caso in [1, 2, 3]:
        if caso == 1:
            arr = [random.randint(1, n) for _ in range(n)]
            arr.sort()
        elif caso == 2:
            arr = [random.randint(1, n) for _ in range(n)]
        else:
            arr = [random.randint(1, n) for _ in range(n)]
            arr = arr[::-1]
        
        start_time = time.time()
        arr = quickSort(arr)
        end_time = time.time()
        
        print("\nCaso: ", caso, " | Tamanho da lista: ", n, " | Tempo de execução: ", end_time - start_time, " segundos")