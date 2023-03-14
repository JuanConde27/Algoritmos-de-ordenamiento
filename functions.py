# Description: This file contains the functions used in the main file

def pedir_arreglo():
    
    #Esta funcion es para usar en el main como pedir al usuario el tamaño de un arreglo y los valores
    #Se puede reemplazar por la lista random generada
    #llamarla asi arr = pedir_arreglo()
    
    n = int(input("\nIngrese el tamaño del arreglo: "))

    arr = [0] * n
    
    for i in range(n):
        arr[i] = int(input(f"\nIngrese el valor {i+1}: "))

    return arr

#==================================================================================================

def merge_sort(arr):
    if len(arr) > 1:   # si la longitud de la lista es mayor que 1, se procede a ordenar
        mid = len(arr) // 2  # se encuentra el punto medio de la lista
        left_half = arr[:mid]  # se divide la lista en dos mitades
        right_half = arr[mid:]

        merge_sort(left_half)  # se llama recursivamente merge_sort con la mitad izquierda
        merge_sort(right_half)  # se llama recursivamente merge_sort con la mitad derecha

        i = j = k = 0   # se inicializan tres índices para las listas

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:  # se compara el primer elemento de cada mitad
                arr[k] = left_half[i]  # si el de la izquierda es menor, se agrega a la lista
                i += 1   # se incrementa el índice para la mitad izquierda
            else:
                arr[k] = right_half[j]  # si el de la derecha es menor, se agrega a la lista
                j += 1   # se incrementa el índice para la mitad derecha
            k += 1   # se incrementa el índice para la lista final

        while i < len(left_half):  # se agregan los elementos restantes de la mitad izquierda
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):  # se agregan los elementos restantes de la mitad derecha
            arr[k] = right_half[j]
            j += 1
            k += 1

        return arr  # se devuelve la lista ordenada

#==================================================================================================

def insertion(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    
    return arr


def merge(arr1, arr2):
    new_arr = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
    new_arr += arr1[i:]
    new_arr += arr2[j:]
    
    return new_arr


def timsort(arr):
    min_run = 32
    n = len(arr)
    
    # Divide el arreglo en cubetas de tamaño min_run
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion(arr, start, end)
    
    # Combinar cubetas
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            arr[left:right + 1] = merge(arr[left:mid + 1], arr[mid + 1:right + 1])
        size *= 2
    
    return arr

#==================================================================================================

def radix_sort(arr):
    # Encuentra el número de dígitos más grande en el arreglo
    max_digit = max([len(str(abs(i))) for i in arr])
    
    # Ordena el arreglo por cada dígito, comenzando por el dígito menos significativo
    for digit in range(max_digit):
        buckets = [[] for _ in range(10)]
        for num in arr:
            # Obtiene el dígito en la posición "digit" del número
            d = num // 10 ** digit % 10
            buckets[d].append(num)
        # Reordena el arreglo con los elementos de cada cubeta
        arr = [num for bucket in buckets for num in bucket]
    
    return arr

#==================================================================================================

def quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)
    
    return arr

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    
    return i

#==================================================================================================

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

#==================================================================================================

def heap_sort(arr):
    n = len(arr)
    
    # Construir el heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    # Extraer elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Intercambiar el primer y último elemento
        heapify(arr, i, 0)  # Reconstruir el heap máximo sin el último elemento
        
    return arr

def heapify(arr, n, i):
    largest = i  # Inicializar el nodo más grande como la raíz
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Si el hijo izquierdo es más grande que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Si el hijo derecho es más grande que el nodo más grande hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    # Si el nodo más grande no es la raíz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar la raíz y el nodo más grande
        heapify(arr, n, largest)  # Reconstruir el subárbol afectado
        
#==================================================================================================

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#==================================================================================================

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        
def tree_sort(arr):
    root = None
    for key in arr:
        root = insert(root, key)
    arr = []
    inorder(root, arr)
    return arr

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root, arr):
    if root is not None:
        inorder(root.left, arr)
        arr.append(root.key)
        inorder(root.right, arr)

#==================================================================================================

def bucket_sort(arr):
    n = len(arr)
    max_val = max(arr)
    size = max_val / n
    
    # Inicializar los cubos
    buckets = [[] for _ in range(n)]
    
    # Poner cada elemento en su cubo correspondiente
    for i in range(n):
        j = int(arr[i] / size)
        if j != n:
            buckets[j].append(arr[i])
        else:
            buckets[n - 1].append(arr[i])
    
    # Ordenar los cubos individuales
    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])
    
    # Concatenar los cubos ordenados
    sorted_arr = []
    for i in range(n):
        sorted_arr = sorted_arr + buckets[i]
        
    return sorted_arr
    
#==================================================================================================

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#==================================================================================================

def counting_sort(arr):
    n = len(arr)
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    count_arr = [0 for _ in range(range_val)]
    output_arr = [0 for _ in range(n)]
    
    for i in range(n):
        count_arr[arr[i] - min_val] += 1
        
    for i in range(1, range_val):
        count_arr[i] += count_arr[i - 1]
        
    for i in range(n - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1
        
    for i in range(n):
        arr[i] = output_arr[i]
        
    return arr

#==================================================================================================