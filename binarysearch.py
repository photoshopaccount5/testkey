
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        

class BinaryTree:
    
    def __init__(self,val):
        self.root=Node(val=val)
    def addValue(self,val):
        if self.root is None:
            self.root= Node(val=val)
        else:
            self.addvalueRecursive(val,self.root)
            
    def addvalueRecursive(self,value,node):
        
        if(value<node.val):
            if(node.left is None):
                node.left =Node(val=value)
            else:
                self.addvalueRecursive(value,node.left)
        else:
            if node.right is None:
                node.right=Node(val=value)
            else:
                self.addvalueRecursive(value=value,node=node.right)
                
    def binarySearch(self,value):
        return self.binarySearchRecursive(value,self.root)
        
    def binarySearchRecursive(self,value,node):
        if(node is None):
            return False
        if(value==node.val):
            return True
        elif(value<node.val):
            return self.binarySearchRecursive(value,node.left)
        else:
            return self.binarySearchRecursive(value,node.right)
            

            
        
        
        
 #this is working good       
        
        
tree=BinaryTree(3)
tree.addValue(4)
tree.addValue(6)
tree.addValue(2)

print(tree.binarySearch(6))
        
        



