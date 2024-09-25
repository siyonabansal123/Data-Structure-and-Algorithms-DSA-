
def print_name_N_times(name, N, cnt=0):
    if cnt==N:
        return 
    
    print(cnt+1, name)
    print_name_N_times(name, N, cnt+1)

def print_1_to_N(N,cnt=1):
    if cnt == N+1:
        return
    
    print(cnt)
    print_1_to_N(N, cnt+1)

def print_N_to_1(N):
    
    if N==0:
        return 
    
    print(N)
    print_N_to_1(N-1)

def print_1_to_N_backtrace(N):
    if N<1: 
        return

    print_1_to_N_backtrace(N-1)
    print(N)
    return N
    
def print_N_to_1_backtrace(N, cnt=1):
    if cnt==N+1:
        return 
    
    print_N_to_1_backtrace(N,cnt+1)
    print(cnt)
    return cnt

def sum_N_numbers(N, cnt=1, sum=0):
    
    if cnt == N+1:
        print(sum)
        return

    sum_N_numbers(N, cnt+1, sum+cnt)
    
def sum_of_N_nos(N):
    
    if N==0:
        return 0

    return N + sum_of_N_nos(N-1, sum)

def factorial(N):
    
    if N==1:
        return 1
    
    return N*factorial(N-1)

def revese_array(arr, l=0):
    
    n=len(arr)
    
    if l>=n/2:
        return arr
    
    arr[l], arr[n-l-1] = arr[n-l-1], arr[l]
    arr = revese_array(arr, l+1)
   
    return arr

def is_palindrome(s, l=0):
  
    if (l>len(s)/2):
        return True
    
    if (s[l] != s[len(s)-l-1]):
        return False

    return is_palindrome(s,l+1)
    
def Nth_fibonacci(N): #TC - O(2**n)
    
    if (N<=1) :
        return N
    
    return Nth_fibonacci(N-1)+Nth_fibonacci(N-2)
    
 
# *** SUBSETS
def all_subsequence(s, idx= 0 , ans=[]):  # TC - O(2**n), SC - O(n)
        
        if idx >=len(s):
            print(ans, "=", sum(ans))
            return
        
        ans.append(s[idx])
        
        all_subsequence(s, idx+1, ans)

        ans.pop()
        
        all_subsequence(s, idx+1, ans)
        
# OUTPUT ->
# [3, 1, 2, 3]
# [3, 1, 2]
# [3, 1, 3]
# [3, 1]
# [3, 2, 3]
# [3, 2]
# [3, 3]
# [3]
# [1, 2, 3]
# [1, 2]
# [1, 3]
# [1]
# [2, 3]
# [2]
# [3]
# []


def subsequce_sum_K(s, K,idx=0, ans=[] ):
        
        if sum(ans)==K:
            print(ans)
            return True
        
        if idx >=len(s):
            return 
        
        ans.append(s[idx]) # pick case
        
        if (subsequce_sum_K(s, K, idx+1, ans)):  # only one answer **
            return True

        ans.pop() # not pick case
        
        if (subsequce_sum_K(s, K, idx+1, ans)):
            return True
        
        return False
    
# OUTPUT - subsequce_sum_K([3,1,2,3], 6)
# [3, 1, 2]
# [3, 3]
# [1, 2, 3]


def subset_sum(arr, idx=0, ans=[], sum_arr=[]): # all subsets - sum them - sort the sum array
    
    if idx>=len(arr):
        sum_arr.append(sum(ans))
        print(ans,"->", sorted(sum_arr))
        return
    
    ans.append(arr[idx])

    subset_sum(arr, idx+1, ans, sum_arr)
    
    ans.pop()
    
    subset_sum(arr, idx+1, ans, sum_arr)
    
    return 

# OUTPUT - subset_sum([3,1,2])
# [3, 1, 2] -> [6]
# [3, 1] -> [4, 6]
# [3, 2] -> [4, 5, 6]
# [3] -> [3, 4, 5, 6]
# [1, 2] -> [3, 3, 4, 5, 6]
# [1] -> [1, 3, 3, 4, 5, 6]
# [2] -> [1, 2, 3, 3, 4, 5, 6]
# [] -> [0, 1, 2, 3, 3, 4, 5, 6]


def subset_sum_with_duplicates(arr, idx=0, ans=[], sum_arr=[]): # NOT GENERATING DUPLICATES SUBSETS
    
    ## arr is assumed to be sorted, so that duplicate elements are together
    
    if idx > len(arr)-1:
        sum_arr.append(sum(ans))
        print(ans, sum_arr)
        return
    
    ans.append(arr[idx])
    
    subset_sum_with_duplicates(arr, idx+1, ans, sum_arr)
    
    ans.pop()
    
    # Skip over duplicate elements**
    
    while idx + 1 < len(arr) and arr[idx] == arr[idx + 1]:
        idx += 1
    subset_sum_with_duplicates(arr, idx + 1, ans, sum_arr)

# OUTPUT -  subset_sum_with_duplicates([1,2,2,3])
# [1, 2, 2, 3] [8]
# [1, 2, 2] [8, 5]
# [1, 2, 3] [8, 5, 6]
# [1, 2] [8, 5, 6, 3]
# [1, 3] [8, 5, 6, 3, 4]
# [1] [8, 5, 6, 3, 4, 1]
# [2, 2, 3] [8, 5, 6, 3, 4, 1, 7]
# [2, 2] [8, 5, 6, 3, 4, 1, 7, 4]
# [2, 3] [8, 5, 6, 3, 4, 1, 7, 4, 5]
# [2] [8, 5, 6, 3, 4, 1, 7, 4, 5, 2]
# [3] [8, 5, 6, 3, 4, 1, 7, 4, 5, 2, 3]
# [] [8, 5, 6, 3, 4, 1, 7, 4, 5, 2, 3, 0]





def myAtoi(s: str) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    s = s.lstrip()
    
    if not s:
        return 0
    i = 0
    sign = 1
    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1
    
    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
    
    result *= sign
    
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX
    
    return result


def myPow(self, x: float, n: int) -> float:
        
        ans = 1.0

        nn = n

        if nn<0:
            nn*=-1

        while nn:
            if nn%2:
                ans = ans*x
                nn = nn-1

            else:
                x= x*x
                nn = nn/2

        if n<0:
            ans = 1/ans
            
        return ans
    

