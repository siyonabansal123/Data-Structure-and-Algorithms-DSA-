# Single Linked List 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def transverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def search(self, val):
        current = self.head
        while current:
            if current.data==val:
                print("val is present in the linked list")
                return True
            current = current.next
        print("val is not present in the linked list")
        return False
    
    def deleteHead(self):
        
        if self.head is None:
            print("Linked list is empty.")
            return 
        self.head = self.head.next
        self.transverse()
        return

    def delete_tail(self):
        
        if self.head is None:
            print("Linked list is empty.")
            return 
        
        if self.head.next is None:
            print("Linked list had only 1 element.")
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        self.transverse()
        return
    
    def del_kth(self, k):
		 
        if self.head is None:
            return None

        if k==1:
            self.head = self.head.next
            
        if k>self.length():
            self.transverse()
            return
                 
        cnt = 0
        current = self.head
        while current and cnt<=k:
            cnt+=1
            if cnt == (k-1):
                current.next = current.next.next
                break 
            current = current.next
        self.transverse()
        return
    
    def del_val(self, val):
        
        if self.head is None:
            return None
        
        if self.head.data==val:
            return self.deleteHead()
        
        current = self.head
        prev = None
        while current:
            if current.data == val:
                prev.next = prev.next.next
                self.transverse()
                return
                
            prev = current
            current = current.next
        
        print("Not in Linked List")
        return 
    
    def insertHead(self, val):
        
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        self.transverse()
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def insert_at_kth(self, val, k):
        
        if k==1:
            self.insertHead(val)
            
        current = self.head
        cnt = 0
        while current and cnt<k+1:
            cnt+=1
            if cnt == (k-1):
                connect = current.next 
                current.next = Node(val)
                current.next.next = connect
                return self.transverse()
            current = current.next
            
        print("beyong the length of the list")
        return 
    
    def reverse_recursive(self):
        def _reverse_recursive(current, prev):
            if not current:
                return prev
            next_node = current.next
            current.next = prev
            return _reverse_recursive(next_node, current)
        
        self.head = _reverse_recursive(self.head, None)
        
    def find_middle(self):
        
        fast= self.head
        slow = self.head
        
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            
        print(slow.data)
        return slow.data
         

def array_to_linked_list(arr):
    linked_list = LinkedList()
    for element in arr:
        linked_list.insert_at_end(element)
    linked_list.transverse()
    return linked_list


# Doubly Linked List

class doubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    
    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
        
    def insert_at_end(self, data):
        new_node = doubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev=self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def insert_at_beginning(self, data):
        new_node = doubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def insert_kth(self, k, value):
        if self.head is None:
            return None
        
        if k==1:
            self.insert_at_beginning()
            return self.traverse_forward()
        
        new_node = doubleNode(value)
        
        cnt =0 
        current = self.head
        while current:
            cnt+=1
            if cnt==k:
                current.prev.next = new_node
                new_node.prev = current.prev
                new_node.next = current
                current.prev = new_node
                return self.traverse_forward()
            current = current.next
        
        print("k is beoynd list length")
            
    def delete_head(self):
        if self.head is None:
            print("None")
            
        else:
            self.head = self.head.next
            self.head.prev = None
        self.traverse_forward()
        
    def del_tail(self):
        if self.head is None:
            print("None")
        elif self.head.next is None:
            self.head = None
            
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
        self.traverse_forward()
        
    def del_value(self, value):
        if self.head is None:
            return None
        current = self.head
        while current:
            if current.data ==value:
                current.prev.next = current.next
                current.next.prev = current.prev
                return self.traverse_forward()
            current = current.next
            
        print("this value is not present in the doubly linked list")
        return 
    
    def del_kth(self, k):
        if k==1:
            self.delete_head()
            return self.traverse_forward()
        
        cnt =0 
        current = self.head
        while current:
            cnt+=1
            if cnt==k:
                current.prev.next = current.next
                current.next.prev = current.prev
                return self.traverse_forward()
            current = current.next
        
        print("k is beoynd list length")
        
    def reverse(self):
        
        current = self.head
        
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head

        return self.traverse_forward()
            
def array_to_doubly_linked_list(arr):
    linked_list = DoubleLinkedList()
    for element in arr:
        linked_list.insert_at_end(element)
    linked_list.traverse_forward()
    return linked_list 
        
        
class  CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        while True:
            print(current.data, ' -> ', end="")
            current = current.next
            if current == self.head:
                break
        print("None")

    def insert_at_end(self, val):
        new_node = Node(val)
        
        # if there is no head
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_at_beginning(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            self.head = new_node
            current.next = self.head
            
    def del_kth(self, k):
        if k==0:
            self.head = self.head.next
            return
        
        current = self.head
        cnt = 0 
        while current:
            cnt+=1
            if cnt==k-1:
                current.next = current.next.next
                self.traverse()
                return
            current = current.next
            
        print("k is out of length of circular list")
        return

def array_to_circular_linked_list(arr):
    linked_list = CircularLinkedList()
    for element in arr:
        linked_list.insert_at_end(element)
    linked_list.traverse()
    return linked_list


        


print("ll")
arr = [1,3,5,2,7]
ll=array_to_linked_list(arr)
ll.transverse()
ll.length()
ll.search(9)
ll.delete_tail()
ll.del_kth(3)
ll.del_val(1)
ll.insert_at_kth(6, 8)
ll.insert_at_kth(5, 3)
ll.reverse_recursive()
ll.find_middle()

print("dll")
dll = array_to_doubly_linked_list(arr)
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_beginning(0)
dll.traverse_forward()
dll.delete_head()
dll.del_tail()
dll.del_value(3)
dll.del_kth(8)
dll.insert_kth(3,9)
dll.reverse()

print("cll")
cll = array_to_circular_linked_list(arr)
cll.del_kth(3)