def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selectionSort(arr):
    newArr = []

    while len(arr) > 0: # because each time you run the loop the original array length decrease 1 due to pop method
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr


print(selectionSort([5, 3, 3, 6, 2, 10]))