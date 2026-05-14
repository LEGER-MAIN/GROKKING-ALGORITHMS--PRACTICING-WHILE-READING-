def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        
        if guess > item:
            high = mid -1 # when the highest index is greater than the item we are looking for

        else:
            low = mid +1 # when the highest index is minor than the item we are looking for

    return None

my_list = list(range(1, 128))

print(binary_search(my_list, 40))