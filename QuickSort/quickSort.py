import random
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

# Caso 1: Melhor Caso - Valores em ordem crescente
print("\nMelhor Caso: Valores em ordem crescente (já ordenados)")
arr1 = [5, 6, 7, 8, 9]
quickSort(arr1, 0, len(arr1) - 1)
print("Lista ordenada: ", arr1)

# Caso 2: Caso Médio - Valores desordenados com números aleatórios
print("\nCaso Médio: Valores desordenados com números aleatórios")
arr2 = [5, 2, 9, 1, 7]
quickSort(arr2, 0, len(arr2) - 1)
print("Lista ordenada: ", arr2)

# Caso 3: Pior Caso - Valores em ordem decrescente
print("\nPior Caso: Valores em ordem decrescente")
arr3 = [9, 8, 7, 6, 5]
quickSort(arr3, 0, len(arr3) - 1)
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
        quickSort(arr, 0, len(arr) - 1)
        end_time = time.time()
        print("\nCaso: ", caso, " | Tamanho da lista: ", n, " | Tempo de execução: ", end_time - start_time, " segundos")