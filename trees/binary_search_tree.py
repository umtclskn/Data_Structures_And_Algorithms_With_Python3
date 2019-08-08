class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None  
        
class BinaryTree:
    def __init__(self,root=None):
        if root != None:
            self.root = Node(root)
        else: 
            self.root = None
    
    def setRoot(self, value):
        if self.root == None:
            self.root = value
    
    def addNode(self, root, value):
        if root == None:
            return
        if root.value > value:
            if root.left == None:
                root.left = Node(value)
            else:
                root = root.left
                self.addNode(root, value)
        elif root.value < value:
            if root.right == None:
                root.right = Node(value)
            else:
                root = root.right
                self.addNode(root, value)