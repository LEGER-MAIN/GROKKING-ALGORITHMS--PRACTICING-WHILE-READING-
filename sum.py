# EXERCISES
# 4.1 Write out the code for the earlier sum function.
# 4.2 Write a recursive function to count the number of items in a list.
# 4.3 Find the maximum number in a list.
# 4.4  Remember binary search from chapter 1? It’s a divide-and-conquer 
# algorithm, too. Can you come up with the base case and recursive 
# case for binary search?


def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([1,2,4,15,1,51,124]))

def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:]) # Es un slice de Python.
                              # Significa:
                              # “Dame la lista desde la posición 1 hasta el final.”
print(count([50,30]))

# 4.3 Find the maximum number in a list

def find_max(arr):

    # Base case
    if len(arr) == 1:
        return arr[0]

    # Recursive case
    max_rest = find_max(arr[1:])

    if arr[0] > max_rest:
        return arr[0]
    else:
        return max_rest


numbers = [3, 7, 2, 9, 5]

print(find_max(numbers))
