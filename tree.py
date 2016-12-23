class Node:
    def __init__(self, val):
        self.left = None # is a Node
        self.right = None # is a Node
        self.value = val

# ABR : 
# left.val <= val <= righ.val
class Tree:
    def __init__(self, node):
        self.root = node
  
    def add(self, val):
        newNode = Node(val)
        if self.root == None:
           self.root = newNode
        else:
            focusNode = self.root
            while(True):
                parent = focusNode

                # left branch
                if val < focusNode.value:
                    focusNode = focusNode.left
                    if focusNode == None:
                        parent.left = newNode
                        return
                # right branch
                else:
                    focusNode = focusNode.right
                    if focusNode == None:
                        parent.right = newNode
                        return

    def run(self, val):
        focusNode = self.root
        while focusNode.value != val:
            if val < focusNode.value:
                focusNode = focusNode.left
            else:
                focusNode = focusNode.right
            if focusNode == None:
                return False
        return True

        
newNod = Node(80)
b = Tree(newNod)
b.add(50)
b.add(60)
b.add(40)
b.add(30)
b.add(70)
x = int(input("Entrez le nombre n :"))
if b.run(x):
    print(" True ")
else:
    print(" False ")
