"""

def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]
            j=j-1
            arr[j+1]=key
  

arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
"""




























def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return

    else:
        for i in range(1,n) :
            key = arr[i]
            j=i-1

            while j>1 and key < arr[j]:
                arr[j+1] = arr[j]
                j = j-1
                arr[j+1]=key

arr = [1,4,6,23,16,3,2,145,6,2,1]
insertionSort(arr)
print(arr)






