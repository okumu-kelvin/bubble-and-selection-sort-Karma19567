def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
      
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
                
    return arr

unsorted_list = [76, 65, 12, 22, 11, 90, 34]
sorted_list = selection_sort(unsorted_list)
print("Sorted list:", sorted_list)
