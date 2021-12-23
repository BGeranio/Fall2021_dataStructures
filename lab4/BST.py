"""
Brendan Geranio
lab 4 for CIS22

This lab is about implementing a BST node and BST class through a main file. BST stands
for Binary Search Tree. A type of tree where all nodes have a left and right child
with the left being less than their value and the right being greater than their value.
It handles a complicated traversal print out with the Queue() class from lab 3.
"""
from Queue import Queue

class BSTNode:
    """
    This is my BST Node class.
    Its different than a linked list node in that it has a left/right element vs just next.
    General getter/setters for all 3
    """
    def __init__(self, value) -> None:
        self.data = value
        self.left = None
        self.right = None

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data

    def setData(self, value):
        self.data = value

class BST:
    """
    This is my Binary Search Tree class
    It has all the general functions, creaters/destroyers, and traversals. 
    """
    def __init__(self, node = None) -> None:
        self.root = node

    def insert(self, currency):
        """
        This function inserts a value into the tree.
        pre: currency object
        post: 
        Return: None
        PSEUDOCODE
            newNode = BSTNode(currency)
            if root is empty:
                root = newNode
            prev = None, cur = root
            while cur exists:
                if cur data > passed data:
                    prev = cur
                    cur = cur.left
                if cur data < passed data:
                    prev = cur
                    cur = cur.right
            
            if prev data > passed data:
                prev.left = newNode
            else:
                prev.right = newNode
        """
        newNode = BSTNode(currency)
        if self.root == None:
            self.root = newNode
            return
        prev = None
        cur = self.root
        while cur:
            if cur.getData().getTotal() > currency.getTotal():
                prev = cur
                cur = cur.getLeft()
            elif cur.getData().getTotal() < currency.getTotal():
                prev = cur
                cur = cur.getRight()

        if prev.getData().getTotal() > currency.getTotal():
            prev.setLeft(newNode)
        else:
            prev.setRight(newNode)

    def search(self, value):
        """
        This function searches the tree for a value. It uses a helper function.
        pre: value (int/float)
        post: 
        Return: node if found, else: error
        PSEUDOCODE
            if root is none call error
            if root data is equal to value:
                print (found currency)
                print root data
            
            if root data < value:
                return _search(root.right, value)
            return _search(root.left, value)
        """
        if self.root == None:
            return ValueError('Currency was not found!')

        if self.root.getData().getTotal() == value:
            print('Currency was found!', end = ' ')
            self.root.getData().print()
            return 

        if self.root.getData().getTotal() < value:
            return self._search(self.root.getRight(), value)
        
        return self._search(self.root.getLeft(), value)

    def _search(self, node, value):
        """
        This function is a helper function for search.
        pre: node, value
        post: 
        Return: value if found else None
        PSEUDOCODE
            if node is None:
                return currency not found
            if node data equals value:
                return currency found + node data
            if node data < value:
                return _search(node.right, value)
            return _search(node.left, value)
        """
        if node is None:
            return 'Currency was not Found!'
        if node.getData().getTotal() == value:
            return 'Currency was found! ' + '{:.2f}'.format(node.getData().getTotal())
        if node.getData().getTotal() < value:
            return self._search(node.getRight(), value)
        return self._search(node.getLeft(), value)

    def delete(self, value):
        """
        This function deletes the node with the value specified.
        pre: value (int/float)
        post: 
        Return: deleted value or None if its not found
        PSEUDOCODE
            if root is empty:
                error
            prev = None
            cur = root
            while cur exists and cur data is not value:
                prev = cur
                if value < cur data:
                    cur = cur.left
                else:
                    cur = cur.right
            if cur is None:
                return root
            if cur.left is None and cur.right is None:
                if cur is not root:
                    if prev.left equals cur:
                        prev.left = None
                    else:
                        prev.right = None
                else:
                    root = None
            if cur.left and cur.right exist:
                succ = getMin(cur.right)
                temp = succ data

                delete(succ data)
                cur.setData(temp)
            else:
                if cur.left:
                    next = cur.left
                else:
                    next = cur.right
                
                if cur is not root:
                    if cur is prev.left:
                        prev.left = next
                    else:
                        prev.right = next
                else:
                    root = next
            return root
        """
        if self.root == None:
            return ValueError('Its an empty tree!')
        prev = None
        cur = self.root
        while cur and cur.getData().getTotal() != value:
            prev = cur
            if value < cur.getData().getTotal():
                cur = cur.getLeft()
            else:
                cur = cur.getRight()

        if cur is None:
            return self.root
        
        # No Children
        if cur.getLeft() is None and cur.getRight() is None:
            if cur != self.root:
                if prev.getLeft() == cur:
                    prev.setLeft(None)
                else:
                    prev.setRight(None)
            else:
                self.root = None
        # 2 children
        elif cur.getLeft() and cur.getRight():
            succ = self.getMin(cur.getRight())
            x = succ.getData()

            self.delete(succ.getData().getTotal())
            cur.setData(x)

        else:
            # left child
            if cur.getLeft():
                next = cur.getLeft()
            else:
                #right child
                next = cur.getRight()

            if cur != self.root:
                if cur == prev.getLeft():
                    prev.setLeft(next)
                else:
                    prev.setRight(next)
            else:
                self.root = next
        return self.root
            
    def inorder(self):
        """
        This function does an inorder traversal of the BST with a helper function and 
        returns the Queue of the BST traversal.
        pre: None
        post: 
        Return: Queue()
        PSEUDOCODE
            if root is empty:
                error
            q = new queue
            _inorder(root, q)
            return q
        """
        if self.root == None:
            return ValueError('Its an empty tree!')
        inQ = Queue()
        self._inorder(self.root, inQ)
        return inQ

    def _inorder(self, node, inQ):
        """
        Helper traversal function
        pre: node, q
        post: q changed
        Return: if node becomes none
        PSEUDOCODE
            if node is None:
                return
            _inorder(node.left, q)
            q.enqueue(node)
            _inorder(node.right, q)
        """
        if node is None:
            return
        self._inorder(node.getLeft(), inQ)
        inQ.enqueue(node)
        self._inorder(node.getRight(), inQ)

    def postorder(self):
        """
        This function does an postorder traversal of the BST with a helper function and 
        returns the Queue of the BST traversal.
        pre: None
        post: 
        Return: Queue()
        PSEUDOCODE
            if root is empty:
                error
            q = new queue
            _postorder(root, q)
            return q
        """
        if self.root == None:
            return ValueError('Its an empty tree!')
        pstQ = Queue()
        self._postorder(self.root, pstQ)
        return pstQ

    def _postorder(self, node, pstQ):
        """
        Helper traversal function
        pre: node, q
        post: updated queue
        Return: if node is None
        PSEUDOCODE
            if node is None:
                return
            _postorder(node.left, q)
            _postorder(node.right, q)
            q.enqueue(node)
        """
        if node is None:
            return
        self._postorder(node.getLeft(), pstQ)
        self._postorder(node.getRight(), pstQ)
        pstQ.enqueue(node)

    def preorder(self):
        """
        This function does an preorder traversal of the BST with a helper function and 
        returns the Queue of the BST traversal.
        pre: None
        post: 
        Return: Queue()
        PSEUDOCODE
            if root is empty:
                error
            q = new queue
            _preorder(root, q)
            return q
        """
        if self.root == None:
            return ValueError('Its an empty tree!')
        preQ = Queue()
        self._preorder(self.root, preQ)
        return preQ

    def _preorder(self, root, preQ):
        """
        Helper traversal function
        pre: node, q
        post: updated queue
        Return: if node is None
        PSEUDOCODE
            if node is None:
                return
            q.enqueue(node)
            _preorder(node.left, q)
            _preorder(node.right, q)
        """
        if root is None:
            return
        preQ.enqueue(root)
        self._preorder(root.getLeft(), preQ)
        self._preorder(root.getRight(), preQ)
        
    def BFS(self):
        """
        This function does a Breadth First Search traversal of the BST and 
        returns the Queue of the BST traversal.
        pre: None
        post: 
        Return: Queue()
        PSEUDOCODE
            if root is None:
                error
            q = new Queue()
            copy = new Queue()

            q.enqueue(root)
            copy.enqueue(root)

            while q.count > 0:
                cur = q.dequeue()
                
                if cur.left exists:
                    q.enqueue(cur.left)
                    copy.enqueue(cur.left)
                if cur.right exists:
                    q.enqueue(cur.right)
                    copy.enqueue(cur.right)

            return copy
        """
        if self.root == None:
            return ValueError('Its an empty tree!')
        que = Queue()
        prntQue = Queue()
        que.enqueue(self.root)
        prntQue.enqueue(self.root)

        while que.countCurrency() > 0:
            cur = que.dequeue()
         
            if cur.getLeft() is not None:
                que.enqueue(cur.getLeft())
                prntQue.enqueue(cur.getLeft())

            if cur.getRight() is not None:
                que.enqueue(cur.getRight())
                prntQue.enqueue(cur.getRight())
        return prntQue       

    def getCount(self):
        """
        This function gets a count of the nodes in the tree with a helper function.
        pre: None
        post: 
        Return: return 1 + _count(root.left) + _count(root.right) 
        PSEUDOCODE
            if root is None:
                error
            print(count: )
            return 1 + _count(root.left) + _count(root.right)
        """
        if self.root is None:
            return ValueError('This tree is Empty!')
        print('Count of nodes in BST:', end = ' ')
        return 1 + self._getCount(self.root.getLeft()) + self._getCount(self.root.getRight())
    
    def _getCount(self, node):
        """
        This function helps the count function count all nodes in tree by adding 1 recursively
        pre: node
        post: int
        Return: return 1 + _count(node.left) + _count(node.right) or 0 if node is None
        PSEUDOCODE
            if node is None:
                return 0
            return 1 + _count(node.left) + _count(node.right)
        """
        if node is None:
            return 0
        return 1 + self._getCount(node.getLeft()) + self._getCount(node.getRight())
        
    def getMin(self, node):
        """
        This function gets the minimum node from this node.
        pre: node
        post: minimum node
        Return: minimum node
        PSEUDOCODE
            while node.left:
                node = node.left
            return node
        """
        while node.getLeft():
            node = node.getLeft()
        return node

    def printBST(self):
        return ['\n',
        "Breadth First Search of BST: ", self.BFS().printQueue(), '\n',
        "Inorder traversal of BST: ",  self.inorder().printQueue(), '\n',
        "Preorder traversal of BST: ", self.preorder().printQueue(), '\n',
        "Postorder traversal of BST: ", self.postorder().printQueue(), '\n']
    
    def isEmpty(self):
        return self.root == None

    def emptyTree(self):
        self.root = None
        
arr = BST()

arr.insert('Bob')
arr.insert('Tim')
arr.insert('Fred')
arr.insert('Peter')
arr.insert('Jane')
arr.delete('Tim')
arr.insert('Laura')
arr.insert('Nancy')
arr.insert('Hank')
arr.delete('Peter')
arr.insert('Rhea')
arr.insert('David')
arr.delete('Rhea')
arr.delete('Nancy')

for i in range(6):
 print(arr.printBST()[i])