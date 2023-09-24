# myList = [['blueberries', 'fruit', 5.20], [
#     'bean sprouts', 'vegetable', 9.25], ['tulip', 'flower', 8.93]]

# for i in range(3):
#     print(sorted(myList, key=lambda x: x[i]))

# sorted 2d array using selection sort
# bubble sort 

def bubble(L):
    size = len(L)
    for i in range(size):
        swap = False
        for j in range(0, size-i-1):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
                swap = True
        # no swapping means that array already sorted
        if not swap:
            break

    return L


print(r)

arr = [['Mohamed','SMI',17.75],['Adam','SMI',15.75],['Amina','SMI',18.00],['Douaa','SMI',13.00]]

#sort this arr in ascending order but sort by the note 
for i in range(3):
    print(sorted(arr, key=lambda x: x[i]))
def sort_array(a):
    size = len(a)
    idx_note = 2
    for i in range(size):
        min_ = i
        swap = False
        for j in range(i+1, size):
            if a[min_][idx_note] > a[j][idx_note]:
                a[min_][idx_note],a[j][idx_note] = a[j][idx_note],a[min_][idx_note]
                swap = True 
        if not swap:
            break 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j][2] > arr[j+1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j][2] < arr[min_idx][2]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][2] > key[2]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

selection_sort(arr)
        



