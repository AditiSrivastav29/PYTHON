arr = [18, 30, 15, 70, 12]
n = 5

print("Array elements before insertion")
for i in range(n):
    print(arr[i], end=" ")
print()

x = 50  # element to be inserted
pos = 4
n += 1

arr.append(None)  # Increase the size of the array by 1

for i in range(n-1, pos-1, -1):
    arr[i] = arr[i - 1]
arr[pos - 1] = x

print("Array elements after insertion")
for i in range(n):
    print(arr[i], end=" ")
print()
