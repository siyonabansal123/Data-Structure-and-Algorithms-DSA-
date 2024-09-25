class merge_sort:  # TC = O(nlogn)
    def __init__(self, arr):
        self.arr = arr
        self.l = 0
        self.r = len(self.arr)-1
        
    def merge(self, arr, l, m , r):
        left_half = arr[l:m+1]
        il=0
        right_hlaf = arr[m+1:r+1]
        ir=0
        
        im = l
        
        while il<len(left_half) and ir<len(right_hlaf):
            
            if left_half[il] <= right_hlaf[ir]:
                arr[im] = left_half[il]
                il+=1
            
            else:
                arr[im]=right_hlaf[ir]
                ir+=1
             
            im+=1
        
        while il <len(left_half):
            arr[im] = left_half[il]
            il+=1
            im+=1
        while ir <len(right_hlaf):
            arr[im] = right_hlaf[ir]
            ir+=1
            im+=1
        
        return
    
    def merge_sort(self, arr, l, r):
        if l<r:
            m = (l+r)//2
            
            self.merge_sort(arr, l , m)
            self.merge_sort(arr, m+1, r)
            self.merge(arr, l , m, r)
            
        return arr
        
class quickSort: # TC = O(nlogn)
        
    def quick_sort(self, arr, low, high):
    
        if low<high:
            
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi-1)
            self.quick_sort(arr, pi+1, high)
            
        return arr
    
    def partition(self,arr, low, high):
        
        pivot = arr[high]
        i=low-1
     
        
        for j in range(low, high):
            if arr[j] <= pivot: 
                i+=1
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
            
        return i+1
        
def selection_sort(arr): # minium at first index - TC = O(n^2)
    
    for i in range(len(arr)-1):
        min_idx = i+1
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def bubble_sort(arr): # maximum at last index - TC = O(n^2)
    
    i = len(arr)
    while i>0:
        for j in range(0, i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        i-=1
    return arr
                  

# arr = [4, 9, 2, 5, 1, 7]
# qs = quickSort()
# print(qs.quick_sort(arr, 0, len(arr)-1))