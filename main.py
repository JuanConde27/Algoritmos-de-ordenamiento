from functions import pedir_arreglo, merge_sort, timsort, radix_sort, quick_sort, shell_sort, heap_sort, insertion_sort, tree_sort, bucket_sort, selection_sort, counting_sort

import random

print("========================")
print("> [1] - Merge_Sort\n> [2] - Tim_Sort\n> [3] - Radix_Sort\n> [4] - Quick_Sort\n> [5] - Shell_Sort\n> [6] - Heap_Sort\n> [7] - Insertion_Sort\n> [8] - Tree_Sort\n> [9] - Buckey_Sort\n> [10] - Selection_Sort\n> [11] - Counting_Sort\n> [12] - Exit")
print("========================\n")

op = int(input("> Ingrese una opcion: "))

#arr = pedir_arreglo()
#Eliminar el arreglo random para usae el pedir_arreglo()

while op != 12:
    
    arr = [random.randint(0, 100) for _ in range(100)]
    
    if op == 1:
        print("\nArreglo original:", arr)
        print("\nMerge_Sort:", merge_sort(arr))
    elif op == 2:
        print("\nArreglo original:", arr)
        print("\nTim_Sort:", timsort(arr))
    elif op == 3:
        print("\nArreglo original:", arr)
        print("\nRadix_Sort:", radix_sort(arr))
    elif op == 4:
        print("\nArreglo original:", arr)
        print("\nQuick_Sort:", quick_sort(arr))
    elif op == 5:
        print("\nArreglo original:", arr)
        print("\nShell_Sort:", shell_sort(arr))
    elif op == 6:
        print("\nArreglo original:", arr)
        print("\nHeap_Sort:", heap_sort(arr))
    elif op == 7:
        print("\nArreglo original:", arr)
        print("\nInsertion_Sort:", insertion_sort(arr))
    elif op == 8:
        print("\nArreglo original:", arr)
        print("\nTree_Sort:", tree_sort(arr))
    elif op == 9:
        print("\nArreglo original:", arr)
        print("\nBucket_Sort:", bucket_sort(arr))
    elif op == 10:
        print("\nArreglo original:", arr)
        print("\nSelection_Sort:", selection_sort(arr))
    elif op == 11:
        print("\nArreglo original:", arr)
        print("\nCounting_Sort:", counting_sort(arr))
    else:
        print("Opcion no valida")
    
    op = int(input("\nIngrese una opcion: "))



        
    





