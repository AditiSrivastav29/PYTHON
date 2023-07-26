def binarySearch(array, val, low, high):
    if high >= low:
        mid = (low + high) // 2
        if array[mid] == val:
            return mid
        elif array[mid] > val:
            return binarySearch(array, val, low, mid - 1)
        else:
            return binarySearch(array, val, mid + 1, high)
    else:
        return -1

# Take user input for array elements
input_array = input("Enter the array elements separated by space: ")
array = list(map(int, input_array.split()))

# Take user input for the value to search for
val = int(input("Enter the value to search for: "))

n = len(array)
result = binarySearch(array, val, 0, n - 1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
