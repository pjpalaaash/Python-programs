def insertion_sort(arr):
    
    
    for i in range(1,len(arr)):
        j = i
        while arr[j-1] < arr[j] and j>=0:
            arr[j-1] ,arr[j] = arr[j] ,arr[j-1]
            j-=1
    
    print(arr)


arr = [5,7,2,9,3,10,4]

insertion_sort(arr)



