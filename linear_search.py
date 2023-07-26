def linearSearch(array, n, value):
    n = len(array)
    
    # Going through array sequentially
    for i in range(0, n):
        if array[i] == value:
            return i
    return -1

# Taking user input for the array elements
input_array = input("Enter the array elements separated by spaces: ")
array = list(map(int, input_array.split()))

# Taking user input for the value to be searched
value = int(input("Enter the value to search: "))
n = len(array)

result = linearSearch(array, n, value)
if result == -1:
    print("Element not found")
else:
    print("Element found at index:", result)

















#def search(element, list):
 #   if element in list:
#        print("the element is present in list")
 #   else:
 #       print("not found")
#my_list = [10,20,30,49]
#search(10,my_list)
#search(56,my_list)