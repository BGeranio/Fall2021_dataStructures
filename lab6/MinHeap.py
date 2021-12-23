"""
Brendan Geranio
lab 4 for CIS22

This lab is about implementing a BST node and BST class through a main file. BST stands
for Binary Search Tree. A type of tree where all nodes have a left and right child
with the left being less than their value and the right being greater than their value.
It handles a complicated traversal print out with the Queue() class from lab 3.
"""
"""
Brendan Geranio
lab 6 for CIS22

This is an Extra Credit lab. It is a MinHeap derived from my BST class created in lab4. It adds a simple minHeapify function
that maintains the order of the tree on deletion/insertion. Plus it edits insert, delete, and search to accomodate the new function.
"""
from Queue import Queue

class MinHeapNode:
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

class MinHeap:
    """
    This is my Binary Search Tree class
    It has all the general functions, creaters/destroyers, and traversals. 
    """
    def __init__(self, node = None) -> None:
        self.root = node

    def minHeapify(self, node):
        """
        This function heapifies a node passed, meaning it compares the node to its children and swaps its value with the smaller of the two.
        pre: node
        post: 
        Return: None
        PSEUDOCODE
            check if node has two children or one
            if two children:
                node.left or node.right < node
                    if node.left > node.right
                        node, node.right = node.right, node
                    else
                        node, node.left = node.left, node
            if 1 child: 
                if child.data < node.data:
                    node, child = child, node
        """
        if node.getLeft() and node.getRight():
            if (node.getData().getTotal() > node.getLeft().getData().getTotal()) or (node.getData().getTotal() > node.getRight().getData().getTotal()):
                if node.getLeft().getData().getTotal() < node.getRight().getData().getTotal():
                    temp = node.getLeft().getData()
                    node.getLeft().setData(node.getData())
                    node.setData(temp)
                    self.minHeapify(node.getLeft())
                else:
                    temp = node.getRight().getData()
                    node.getRight().setData(node.getData())
                    node.setData(temp)
                    self.minHeapify(node.getRight())


        if node.getLeft() and (node.getRight() == None):
            if (node.getData().getTotal() > node.getLeft().getData().getTotal()):
                temp = node.getLeft().getData()
                node.getLeft().setData(node.getData())
                node.setData(temp)
                self.minHeapify(node.getLeft())

        if node.getRight() and (node.getLeft() == None):
            if node.getData().getTotal() > node.getRight().getData().getTotal():
                temp = node.getRight().getData()
                node.setRight(node.getData())
                node.setData(temp)
                self.minHeapify(node.getRight())

    def heapify(self):
        """
        This function heapifies each node in the tree
        pre: none
        post: 
        Return: None
        PSEUDOCODE
            new queue
            queue.append(root):
            while queue:
                temp = q.pop()
                if temp:
                    self.minHeapify(temp)
                if temp.left:
                    q.append left
                if tempright:
                    q.append right
        """
        q = []
        q.append(self.root)
        while q:
            temp = q[0]
            q.pop(0)
            if temp:
                self.minHeapify(temp)
            if temp.getLeft():
                q.append(temp.getLeft())
            if temp.getRight():
                q.append(temp.getRight())

    def getParent(self, node):
        """
        This function gets the parent node of the passed node.
        pre: node
        post: 
        Return: parent node if found
        PSEUDOCODE
            sought = node data
            new queue
            queue.append(root):
            while queue:
                temp = q.pop()
                if node.left or node.right == sought:
                    current = temp
                    break
                if temp.left:
                    q.append left
                if tempright:
                    q.append right
            return current
        """
        sought = node.getData().getTotal()
        q = []
        q.append(self.root)
        while q:
            temp = q[0]
            q.pop(0)
            if temp.getLeft().getData().getTotal() or temp.getRight().getData().getTotal() == sought:
                cur = temp
                break
            if temp.getLeft():
                q.append(temp.getLeft())
            if temp.getRight():
                q.append(temp.getRight())
            
        return cur

    def isHeap(self):
        """
        This function checks if the tree is a heap. 
        pre: none
        post: 
        Return: boolean
        PSEUDOCODE
            heap = true
            new queue
            queue.append(root):
            while queue:
                temp = q.pop()
                if temp.left:
                    q.append left
                    if temp.left < temp:
                        heap = false
                if tempright:
                    q.append right
                    if temp.right < temp:
                        heap = false
            return heap
        """
        q = []
        q.append(self.root)
        heap = True

        while q:
            temp = q[0]
            q.pop(0)
            if temp.getLeft():
                q.append(temp.getLeft())
                if temp.getLeft().getData().getTotal() < temp.getData().getTotal():
                    heap = False
                    break
            if temp.getRight():
                q.append(temp.getRight())
                if temp.getRight().getData().getTotal() < temp.getData().getTotal():
                    heap = False
                    break
            
        return heap

    def insert(self, currency):
        """
        This function inserts a value into the tree.
        pre: currency object
        post: 
        Return: None
        PSEUDOCODE
            newNode = MinHeapNode(currency)
            if root is empty:
                root = newNode
 
            new queue
            queue.append(root):
            while queue:
                temp = q.pop()
                
                if not temp.left:
                    temp.left = newNode
                    checker = temp.left
                    while checker.parent and checker.parent > checker:
                        checker.parent, checker = checker, checker.parent
                    minheapify()
                else:
                    q.append(temp.left)
                if  temp.right:
                      temp.right = newNode
                    checker =  temp.right
                    while checker.parent and checker.parent > checker:
                        checker.parent, checker = checker, checker.parent
                    minheapify()
                else:
                    q.append(temp.right)
            heapify()
            
        """
        newNode = MinHeapNode(currency)
        if self.root == None:
            self.root = newNode
            return
        # major changes from lab 5
        # uses a q to get to next available spot in a complete binary tree
        q = []
        q.append(self.root)
        while q:
            temp = q[0]
            q.pop(0)

            # if no left child you insert
            if not temp.getLeft():
                temp.setLeft(newNode)
                # this while loop moves up the tree to the root to compare the values and swap if necessary
                checker = temp.getLeft()
                while self.getParent(checker) and self.getParent(checker).getData().getTotal() > checker.getData().getTotal():
                    newTemp = self.getParent(checker).getData()
                    self.getParent(checker).setData(checker.getData())
                    checker.setData(newTemp)
                    checker = self.getParent(checker)
                self.minHeapify(temp)
                                  
                break
            else:
                # there is a left child so we append
                q.append(temp.getLeft())

            # if no right child we set it to the new value
            if not temp.getRight():
                temp.setRight(newNode)
                checker = temp.getRight()
                while self.getParent(checker) and self.getParent(checker).getData().getTotal() > checker.getData().getTotal():
                    newTemp = self.getParent(checker).getData()
                    self.getParent(checker).setData(checker.getData())
                    checker.setData(newTemp)
                    checker = self.getParent(checker)    
                self.minHeapify(temp)
                break
            else:
                q.append(temp.getRight())

        # call the heapify function to straighten everything out
        self.heapify()

    def search(self, value):
        """
        This function searches the tree for a value. I got rid of the helper function by using a q instead.
        pre: value (int/float)
        post: 
        Return: node if found, else: error
        PSEUDOCODE
            if root is none call error
            if root data is equal to value:
                print (found currency)
                print root data
            
            new queue
            queue.append(root):
            while queue:
                temp = q.pop()
                if node.left or node.right == value:
                    current = node.left or node.right
                    break
                if temp.left:
                    q.append left
                if tempright:
                    q.append right

            print not found if current == None
            else print value
        """
        if self.root == None:
            return ValueError('Currency was not found!')

        if self.root.getData().getTotal() == value:
            print('Currency was found!', end = ' ')
            self.root.getData().print()
            return 

        q = []
        q.append(self.root)
        while q:
            temp = q[0]
            q.pop(0)
            if temp.getLeft().getData().getTotal()  == value:
                cur = temp.getLeft()
                break
            if temp.getRight().getData().getTotal() == value:
                cur = temp.getRight()
                break
            if temp.getLeft():
                q.append(temp.getLeft())
            if temp.getRight():
                q.append(temp.getRight())
    
        if cur is None:
            return 'Currency was not Found!'
        if cur.getData().getTotal() == value:
            return 'Currency was found! ' + '{:.2f}'.format(cur.getData().getTotal())

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

        # call the heapify function to straighten everything out
        self.heapify()
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

    def printMinHeap(self):
        return ['\n',
        "Breadth First Search of BST: ", self.BFS().printQueue(), '\n',
        "Inorder traversal of BST: ",  self.inorder().printQueue(), '\n',
        "Preorder traversal of BST: ", self.preorder().printQueue(), '\n',
        "Postorder traversal of BST: ", self.postorder().printQueue(), '\n']
    
    def isEmpty(self):
        return self.root == None

    def emptyTree(self):
        self.root = None
        
