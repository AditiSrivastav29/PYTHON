# Bubble sort in Python

def bubbleSort(array):
  n= len(array)
    
  # loop to access each array element
  for i in range(n - 1):

    # loop to compare array elements
    for j in range(0, n - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [90,80,70,50,-40,60,20,30]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)