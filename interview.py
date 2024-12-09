
def rotated_min(arr):
    
    min_ele= arr[0]
    
    for i in range(len(arr)-1):
        
        if arr[i]>arr[i+1]:
            min_ele = arr[i+1]
            break
        
    return min_ele


# arr = [0,1,2,3,4]
# print(rotated_min(arr))

def kadane(arr):
    
    max_sum = 0
    sum=0
    
    for i in range(len(arr)):
        sum+=arr[i]
        if sum<0:
            sum=0
            
        elif sum>max_sum:
            max_sum = sum
            
    return max_sum

# ar = [2,3,-8,7,-1,2,3, 4]
# print(kadane(ar))
            
            

            
def sprial_print(matrix):
    
    level = 0
    n = len(matrix)
    m = len(matrix[0])
    
    ans=[]
    
    while level<n:
        print(level)
        
        if level%2==0:
            for i in matrix[level]:
                ans.append(i)
            
        elif level%2==1:
            
            for i in range(len(matrix[level])-1,-1,-1):
                ans.append(matrix[level][i])
                
        level+=1
        
    for i in ans:
        
        print(i, end=" ")

    return            
    
    
    
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    
sprial_print(a)
