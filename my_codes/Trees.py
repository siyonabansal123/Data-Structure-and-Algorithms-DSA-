
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

from my_codes.Stack_Queue import Queue, Stack

class Tree:
    def __init__(self):
        self.root = None
        
        
    def insert(self, value):
        
        if self.root is None:
            self.root = Node(value)
            
        else:
            self._insert_(self.root, value)
            
    def _insert_(self, current_node, value):
        
        if value<=current_node.data:
            
            if current_node.left_child is None:
               current_node.left_child = Node(value)
               
            else:
                self._insert_(current_node.left_child, value) 
                
        else:
            
            if current_node.right_child is None:
               current_node.right_child = Node(value)
               
            else:
                self._insert_(current_node.right_child, value) 
    
    def preorder(self, node):
        
        if node is None:
            return
        
        print(node.data)
        self.preorder(node.left_child)
        self.preorder(node.right_child)
        
    def preorder_iterative(self):
        
        preorder=[]
        
        if self.root is None:
            return preorder
        
        stack = Stack()
        
        stack.push(self.root)
        
        while not stack.is_empty():
            current = stack.top()
            stack.pop()
            
            preorder.append(current.data)
            
            if current.right_child is not None:
                stack.push(current.right_child)
                
            if current.left_child is not None:
                stack.push(current.left_child)
                
        return preorder
        
    def postorder(self,node):
        
        if node is None :
            return
        
        self.postorder(node.left_child)
        self.postorder(node.right_child)
        print(node.data)
        
    def postorder_iterative_2_stacks(self):
        
        postorder=[]
        
        if self.root is None:
            return postorder
        
        s1= Stack()
        s2= Stack()
        s1.push(self.root)
        
        while not s1.is_empty():
            current = s1.top()
            s1.pop()
            s2.push(current)
            if current.left_child is not None:
                s1.push(current.left_child)
                
            if current.right_child is not None:
                s1.push(current.right_child)
                
        while not s2.is_empty():
            postorder.push(s2.top().data)
            s2.pop()
            
        return postorder
    
    def postorder_iterative_1_stack(self):
        
        postorder=[]
        
        if self.root is None:
            return postorder
        
        s1= Stack()
        
        s1.push(self.root)
        current = s1.top()
        
        while (current is not None) and (not s1.is_empty()):
            
            if current is not None:
                s1.push(current)
                current=current.left_child
                
            else:
                temp = s1.top().right_child
                if temp is None:
                    
                    temp = s1.top()
                    s1.pop()
                    postorder.append(temp)
                    while s1 is not None and temp==s1.top().right_child:
                        tmep = s1.top()
                        s1.pop()
                        postorder.append(temp.data)
                        
                else:
                    current = temp
               
                
      
            
        return postorder
        
    def inorder(self, node):
        
        if node is None:
            return
        
        self.inorder(node.left_child)
        print(node.data)
        self.inorder(node.right_child)
        
    def inorder_iterative(self):
        
        inorder=[]
        
        stack = Stack()
        current = self.root
        while True:
            if current is not None:
                stack.push(current)
                current = current.left_child
                
            else:
                
                if stack.is_empty():
                    break
                
                current = stack.pop()
                inorder.append(current.data)
                current = current.right_child
                
        return inorder
        
    
    def level_order(self, q = Queue(), ans=[], levels=[]): # uses more space as compared to recurrsion
        
        if self.root is None:
            return ans
        
        q.push(self.root)
         
        while not q.is_empty():
            
            level_size = q.size()  # Number of nodes at the current level
            current_level = []  

            for _ in range(level_size):
                current_node = q.top()
                q.pop()
                
                current_level.append(current_node.data)
                
                if current_node.left_child is not None:
                    q.push(current_node.left_child)
                if current_node.right_child is not None:
                    q.push(current_node.right_child)

            ans.append(current_level)

        return ans
                
                
    def single_flow(self):
        
        st = Stack()
        
        preorder= []
        inorder=[]
        postorder=[]
        
        st.push([self.root,1])
        
        if self.root is None:
            return 
        
        while not st.is_empty():
            temp = st.top()
            
            st.pop()
            
            if temp[-1]==1:
                preorder.append(temp[0].data)
                temp[-1]+=1
                st.push(temp)
                
                if temp[0].left_child is not None:
                    st.push([temp[0].left_child,1])
                    
            elif temp[-1]==2:
                inorder.append(temp[0].data)
                temp[-1]+=1
                st.push(temp)
                
                if temp[0].right_child is not None:
                    st.push([temp[0].right_child,1])
            
            else:
                postorder.append(temp[0].data)
        
    
        print(preorder)
        print(inorder)
        print(postorder)
        
        
    def max_depth(self):  # finding height of tree
        return self._max_depth(self.root)  
    def _max_depth(self, curr=None):
        if curr is None:
            return 0
        
        l = curr.left_child
        r = curr.right_child   
        
        return 1+ max(self._max_depth(l),self._max_depth(r))
       
        
    def is_balance(self):
        if self.root is None:
            return False
        return self._is_balance(self.root)   
    def _is_balance(self, curr=None): # TC = O(n^2)
        if curr is None:
            return True
        
        if abs(self._max_depth(curr.left_child) - self._max_depth(curr.right_child)) > 1:
            return False
        
        lb = self._is_balance(curr.left_child)
        rb = self._is_balance(curr.right_child)
        
        if (not lb) or (not rb):
            return False
        
        return True
    
    
    def diameter(self):
        #** Initialize maxi as a list to allow its value to be modified within the helper function
        maxi = [0]
        self._diameter(self.root, maxi)
        print(maxi)
        return maxi[0]
    def _diameter(self, curr, maxi):
        if curr is None:
            return 0
        
        lh = self._diameter(curr.left_child, maxi)
        rh = self._diameter(curr.right_child, maxi)
        
        maxi[0] = max(maxi[0], lh + rh)
        
        return 1 + max(lh, rh)
    
    
    def max_path_sum(self):
        maxi= [float("-inf")]
        self._max_path_sum(self.root, maxi)
        return maxi[0]
    def _max_path_sum(self, curr=None, maxi=0):
        
        if curr is None:
            return 0
        left_sum = self._max_path_sum(curr.left_child, maxi)
        right_sum = self._max_path_sum(curr.right_child, maxi)
        
        maxi[0] = max(left_sum+right_sum+curr.data, maxi[0])
        return curr.data + max(left_sum, right_sum)
    
    
    def zig_zag_traversal(self):
        ans =[]
        
        if self.root is None:
            return ans 
        
        q = Queue()
        q.push(self.root)
        ltr = True
        
        while not q.is_empty():
            
            level_size = q.size()
            curr_ans = [None]*level_size
            
            for i in range(0,level_size):
                curr_node = q.top()
                q.pop()
                
                if ltr:
                    curr_ans[i]=(curr_node.data) ###
                
                else:
                    curr_ans[level_size-1-i]=(curr_node.data)  ###
                    
                if curr_node.left_child is not None:
                    q.push(curr_node.left_child)
                        
                if curr_node.right_child is not None:
                    q.push(curr_node.right_child)
                             
            ltr = not ltr       
            ans.append(curr_ans)

        return ans
        
        
    def boundary_trvarsel(self): # anticlockwise - left boundary + leaf nodes + right boundary
        
        ans = [self.root.data]
        
        def left_boundary():
            left_bound = []
            curr=self.root
            while curr:
                if curr.left_child and (curr.left_child.left_child or curr.left_child.right_child ) :
                    left_bound.append(curr.left_child)
                    if curr.right_child.right_child:
                        curr = curr.left_child
                    else:
                        curr = curr.right_child
                elif curr.right_child and (curr.right_child.left_child or curr.right_child.right_child):
                    left_bound.append(curr.right_child)
                    if curr.right_child.right_child:
                        curr = curr.left_child
                    else:
                        curr = curr.right_child
                        
            return left_bound
                
        
        def right_bound():
            right_bound = []
            curr = self.root
            while curr.left_child or curr.right_child:
                if curr.right_child and (curr.right_child.left_child or curr.right_child.right_child ) :
                    right_bound.append(curr.left_child)
                    if curr.right_child.right_child:
                        curr = curr.right_child
                    else:
                        curr = curr.left_child
                elif curr.left_child and (curr.left_child.left_child or curr.left_child.right_child):
                    right_bound.append(curr.right_child)
                    if curr.right_child.right_child:
                        curr = curr.right_child
                    else:
                        curr = curr.left_child
            return right_bound
        
        def leaf_nodes(lb,rb):
            
            ln =[]
            
            if lb[-1].left_child:
                ln.append(lb[-1].left_child)
                
            elif lb[-1].right_child:
                ln.append(lb[-1].left_child)
                
            if rb[-1].left_child:
                ln.append(lb[-1].left_child)
                
            elif rb[-1].right_child:
                ln.append(lb[-1].left_child)
                
            
            return ln
            
        lb = left_boundary()
        rb = right_bound()
        ln = leaf_nodes(lb,rb)
        
        print([lb,ln,rb])
        return [lb,ln,rb]
        
        
    def vertical_traversal(self):
        
        return
        
        
    
    
def are_identical(t1, t2): 
    
    if t1 is None or t2 is None:
        return t1==t2
    
    return (t1.data == t2.data) and are_identical(t1.left_child, t2.left_child) and are_identical(t1.right_child, t2.right_child)
    
      
 #Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    
    res = []
    l=0
    
    def ans(root, res, l):
        
        if root is None:
            return 

        if len(res)==l:
            res.append(root.data)
            
        l+=1
        ans(root.left_child, res, l)
    
        ans(root.right_child, res, l)
        l-=1
    ans(root, res,l)
    return res


def bottomView(root):
        
        hd = 0
        res = {}
       
        def bottom_View(root, hd, res):
            if root is None:
                return
                
            hd-=1
            bottom_View(root.left_child, hd, res)
            
            hd+=1
            if hd not in res:
                res[hd]=root.data
            hd+=1
            
            bottom_View(root.right_child, hd, res)
            hd-=1
            
        bottom_View(root, hd, res)
        ans = [value for value in res.values()]
      
        return ans
        



        
t = Tree()

t.insert(10)
t.insert(8)
t.insert(12)
t.insert(9)
t.insert(7)
t.insert(11)
t.insert(13)
t.insert(15)
t.insert(18)
t.insert(50)
t.insert(14)

# t.preorder(t.root)
# print(t.preorder_iterative())
# print(t.inorder_iterative())
# t.postorder(t.root)
print(t.level_order())
# t.single_flow()
# print(t.max_depth())
# print(t._is_balance(t.root))
# t.diameter()
# print(t.max_path_sum())
# print(t.root.data)
# print(bottomView(t.root))
# print(t.zig_zag_traversal())
t.boundary_trvarsel()