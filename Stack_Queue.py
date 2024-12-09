# FIFO
class Queue:
    def __init__(self, capacity=50):
        self.front = 0
        self.rear = 0
        self.cnt= 0
        self.capacity = capacity
        self.arr = [None] * self.capacity
    
    def push(self, val):
        if self.cnt<self.capacity:
            self.arr[self.rear % self.capacity] = val
            self.rear+=1
            self.cnt+=1
            return self.arr
        
        else:
            return print("Queue is full.")
            
    def top(self):
        if self.cnt==0:
            return None
        return self.arr[self.front % self.capacity]
    
    def size(self):
        return self.cnt
    
    def pop(self):
        if self.cnt==0:
            return None
        
        self.arr[self.front % self.capacity]=None
        self.front+=1
        self.cnt-=1
        return self.arr
    
    def is_empty(self):
        return self.cnt==0
    
    def traverse(self):
        if self.cnt==0:
            print("Queue is Empty")
            return
        for i in range(self.front, self.rear):
            print(self.arr[i%self.capacity], end='<=')
        print()
        
def arr_to_queue(arr):
    q = Queue()
    for i in arr:
        q.push(i)
    
    q.traverse()
    return q

class StackUsingQueue:
    def __init__(self):
        self.q = Queue()
        
    def push(self, x):
        s = self.q.cnt()
        self.q.push(x)
        for i in range(s):
            self.q.push(self.q.pop()) #Use a for loop of size()-1, remove element from queue and again push back to the queue, hence the most recent element becomes the most former element and vice versa.

        return self.q
    
    
# LIFO

class Stack :
    def __init__(self):
        self.stack = []
        
    def push(self, val):
        return self.stack.append(val)
    
    def pop(self):
        return self.stack.pop() if not self.is_empty() else None
    
    def traverse(self):
        for i in self.stack:
            print(i, end='=>')
        print()
            
    def size(self):
        return len(self.stack)
    
    def top(self):
        return  self.stack[-1] if not self.is_empty() else None
        
    def is_empty(self):
        return len(self.stack) == 0
    
def arr_to_stack(arr):
    s= Stack()
    for i in arr:
        s.push(i)
        
    s.traverse()
    return s
    
    
class QueueUsingStack:
    def __init__(self):  
        self.s1  = Stack()
        self.s2  = Stack()
        
    def push(self,x):    # TC - O(n), SC - O(2n)
        for i in range(self.s1.size()):
            self.s2.push(self.s1.top())
            
        self.s1.push(x)
        
        for i in range(self.s2.size()):
            self.s1.push(self.s2.top())
            
            
    def pop(self):
        return self.s1.pop()
            
    def top(self):
        return self.s1.top() 
        
        
# Questions
def Balanced_brackets(string):
    
    open_stack = Stack()
    for char in string:
        if char in "([{":
            open_stack.push(char)
        else:
            if open_stack.is_empty():
                return False
            top_char = open_stack.top()
            if (char == "]" and top_char == "[") or \
               (char == "}" and top_char == "{") or \
               (char == ")" and top_char == "("):
                open_stack.pop()
            else:
                return False
    return open_stack.is_empty()

  
def next_greater_element(num1):
    
    numstack = Stack()
    
    n1 = len(num1)
    ans = [-1]*n1
    
    for i in range(0,n1):
        
        if numstack.is_empty():
                numstack.push(num1[-1*(i+1)])
     
        else:
            while not numstack.is_empty():
                
                if num1[-1*(i+1)]<numstack.top():
                    ans[-1*(i+1)] = numstack.top()
                    numstack.push(num1[-1*(i+1)])
                    break
                    
                elif num1[-1*(i+1)]>=numstack.top():
                    numstack.pop()

                    
            numstack.push(num1[-1*(i+1)])
            
    return  ans    


class sort_stack_recurrsion:
    
    def __init__(self, arr):
        self.stack = arr_to_stack(arr)
        
    def insert_in_sorted_order(self,stack, element):
        if stack.is_empty() or element > stack.top():
            stack.push(element)
        else:
            # Pop the top element and hold it
            temp = stack.pop()
            # Recur for the remaining elements in the stack
            self.insert_in_sorted_order(stack, element)
            # Push the held element back into the stack
            stack.push(temp)

    def sort_stack(self):
        if not self.stack.is_empty():
            # Hold the top element
            temp = self.stack.pop()
            # Recursively sort the remaining stack
            self.sort_stack()
            # Insert the held element into the sorted stack
            self.insert_in_sorted_order(self.stack, temp)
    
        self.stack.traverse()
        
        return self.stack
   


# s = sort_stack_recurrsion([4,12,5,3,1,2,5,3,1,2,4,6])

# s.sort_stack()
