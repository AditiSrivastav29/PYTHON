def binarySearch(array, val, low, high):

    if high >= low:

        mid = (low + high) //2

        # If found at mid, then return it
        if array[mid] == val:
            return mid         #here mid+1 will increment the index value of element

        # Search the left half
        elif array[mid] > val:
            return binarySearch(array, val, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, val, mid + 1, high)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
val = 4
n= len(array)           #n=length of array

result = binarySearch(array, val, 0, n-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")