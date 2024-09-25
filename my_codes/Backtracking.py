# N Queens

class NQueens:
    
    def __init__(self, N):
        self.N = N
        self.matrix =  [[0] * N for _ in range(N)]
          
            
    def is_safe(self, row, col):
        c= col
        r = row
        #upper diagonal
        while(row>=0 and col>=0):
            if (self.matrix[row][col]=='Q'):
                return False
            row-=1
            col-=1
            
        col = c
        row = r
        #same row
        while(col>=0):
            if  self.matrix[row][col]=='Q':
                return False
            
            col-=1
            
        col = c
        row = r
        #lower diagonal
        while(row<self.N and col>=0):
            if self.matrix[row][col]=="Q":
                return False
            
            col-=1
            row+=1
            
        return True
    
    
    
    def solve(self, col=0):
        
        if col==self.N:
            print(self.matrix)
            return 
        
        for row in range(self.N):
            if self.is_safe(row, col):
                self.matrix[row][col]="Q"
   
                self.solve(col+1)
                self.matrix[row][col]=0
    

            
# nq = NQueens(5)

# nq.solve()
# [['Q', 0, 0, 0, 0], [0, 0, 0, 'Q', 0], [0, 'Q', 0, 0, 0], [0, 0, 0, 0, 'Q'], [0, 0, 'Q', 0, 0]]
# [['Q', 0, 0, 0, 0], [0, 0, 'Q', 0, 0], [0, 0, 0, 0, 'Q'], [0, 'Q', 0, 0, 0], [0, 0, 0, 'Q', 0]]
# [[0, 0, 'Q', 0, 0], ['Q', 0, 0, 0, 0], [0, 0, 0, 'Q', 0], [0, 'Q', 0, 0, 0], [0, 0, 0, 0, 'Q']]
# [[0, 0, 0, 'Q', 0], ['Q', 0, 0, 0, 0], [0, 0, 'Q', 0, 0], [0, 0, 0, 0, 'Q'], [0, 'Q', 0, 0, 0]]
# [[0, 'Q', 0, 0, 0], [0, 0, 0, 'Q', 0], ['Q', 0, 0, 0, 0], [0, 0, 'Q', 0, 0], [0, 0, 0, 0, 'Q']]
# [[0, 0, 0, 0, 'Q'], [0, 0, 'Q', 0, 0], ['Q', 0, 0, 0, 0], [0, 0, 0, 'Q', 0], [0, 'Q', 0, 0, 0]]
# [[0, 'Q', 0, 0, 0], [0, 0, 0, 0, 'Q'], [0, 0, 'Q', 0, 0], ['Q', 0, 0, 0, 0], [0, 0, 0, 'Q', 0]]
# [[0, 0, 0, 0, 'Q'], [0, 'Q', 0, 0, 0], [0, 0, 0, 'Q', 0], ['Q', 0, 0, 0, 0], [0, 0, 'Q', 0, 0]]
# [[0, 0, 0, 'Q', 0], [0, 'Q', 0, 0, 0], [0, 0, 0, 0, 'Q'], [0, 0, 'Q', 0, 0], ['Q', 0, 0, 0, 0]]
# [[0, 0, 'Q', 0, 0], [0, 0, 0, 0, 'Q'], [0, 'Q', 0, 0, 0], [0, 0, 0, 'Q', 0], ['Q', 0, 0, 0, 0]]
    
      
class Suduko:
    def __init__(self, matrix):
        self.matrix = matrix
 
    def is_valid(self, row, col, c):
    
        for y in range(9):
          
            if c==self.matrix[y][col]:
                return False
                
  
            elif c== self.matrix[row][y]:
                return False
                
            elif self.matrix[3*(row//3)+(y//3)][3 * (col // 3) +( y % 3)]==c: #***
                return False
        
        return True
    
    def solve(self):
        for x in range(9):
            for y in range(9):
                if self.matrix[x][y]==".":
                    for c in "123456789":
                        if self.is_valid(x,y,c):
                            self.matrix[x][y]=c
                            if self.solve():
                                return True
                            else:
                                self.matrix[x][y]="."
                    return False
      
        return True
    
    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(row))

board = [
        ["9", "5", "7", ".", "1", "3", ".", "8", "4"],
        ["4", "8", "3", ".", "5", "7", "1", ".", "6"],
        [".", "1", "2", ".", "4", "9", "5", "3", "7"],
        ["1", "7", ".", "3", ".", "4", "9", ".", "2"],
        ["5", ".", "4", "9", "7", ".", "3", "6", "."],
        ["3", ".", "9", "5", ".", "8", "7", ".", "1"],
        ["8", "4", "5", "7", "9", ".", "6", "1", "3"],
        [".", "9", "1", ".", "3", "6", ".", "7", "5"],
        ["7", ".", "6", "1", "8", "5", "4", ".", "9"],
    ]

sudo = Suduko(board)
sudo.print_matrix()
if sudo.solve():
    sudo.print_matrix()
else:
    print("No solution exists")
    
# 9 5 7 . 1 3 . 8 4
# 4 8 3 . 5 7 1 . 6
# . 1 2 . 4 9 5 3 7
# 1 7 . 3 . 4 9 . 2
# 5 . 4 9 7 . 3 6 .
# 3 . 9 5 . 8 7 . 1
# 8 4 5 7 9 . 6 1 3
# . 9 1 . 3 6 . 7 5
# 7 . 6 1 8 5 4 . 9

# 9 5 7 6 1 3 2 8 4
# 4 8 3 2 5 7 1 9 6
# 6 1 2 8 4 9 5 3 7
# 1 7 8 3 6 4 9 5 2
# 5 2 4 9 7 1 3 6 8
# 3 6 9 5 2 8 7 4 1
# 8 4 5 7 9 2 6 1 3
# 2 9 1 4 3 6 8 7 5
# 7 3 6 1 8 5 4 2 9

