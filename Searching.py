def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  

    mid = (low + high) // 2 

    if arr[mid] == target:
        print("target found at", mid)
        return mid

    if arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1) 
    else:
        return binary_search_recursive(arr, target, mid + 1, high)
    
    
    
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
           return i
    return -1



def search_rotated_array(arr, target, left=0, right=None): # we cannot check on just one half, first identify the sorted half and then perform binary search on that
    
    if right is None: # for the first recurrsion node
        right  = len(arr)-1
        
    mid = (left+right)//2
    print(left, mid, right)
    print(arr)
  
    if arr[mid]==target:
        print("found the target at", mid)
        return mid
    
    if arr[left]==arr[mid]==arr[right]: ## if there are duplicates  - TC (worst case) - O(n/2)
        left+=1
        right-=1
    
    if left>=mid:
        return -1
    
    elif (arr[left]<=arr[mid]):  # left half is sorted
        if (arr[left] <= target <=arr[mid]):  # target is there in the left sorted half
            return binary_search_recursive(arr, target, left, mid)  # TC - O(log2n)
        else:
            return search_rotated_array(arr, target, mid, right)
        
    elif (arr[mid]<=arr[right]): # right half is sorted
        if (arr[mid] <= target <= arr[right]): # taregt is there in the right sorted half
            return binary_search_recursive(arr, target, mid, right)
        else:  
            return search_rotated_array(arr, target, left, mid)
         
    else:
        print("target not found")
        return -1
        

def search_minimum_sorted_array(arr):  # finding the point of rotation - will be in unsorted half 
    
    left = 0 
    right = len(arr)-1
    
    
    while left<right:
        
        mid= (left+right)//2
        
        if arr[left] == arr[mid] == arr[right]:
            left+=1
            right-=1
   
        if arr[left]<arr[mid]:
            left = mid
            
        else:
            right = mid

    print("minimum element is", arr[left+1], "at", left+1, "index")
    print("array has been rotated", left+1, "times")
    return arr[left+1]  # TC  - O(lgo2n)

        
        
    
(search_minimum_sorted_array([7, 8, 1, 2, 3, 4, 5, 6]))
    
    
    
    
