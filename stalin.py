
arr = [9, 2, 5, 3, 6, 7, 1][::-1]

i = 0

while i < len(arr)-1:
     print(arr)
     if arr[i] >= arr[i+1]:
       arr.pop(i+1)
     else:
       i += 1