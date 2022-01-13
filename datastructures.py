from collections import deque


class Node:
    "This node class only points in one direction"

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def get_val(self):
        return self.val

    def get_next(self):
        return self.next

    def set_val(self, new_val):
        self.val = new_val

    def set_next(self, new_next):
        self.next = new_next


class dsNode:
    "This Node class points to the previous node and the next one"

    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def get_val(self):
        return self.val

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_val(self, new_val):
        self.val = new_val

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev


class tNode:
    """This Node class is used for the Binary tree data structure. Similar to the dsNode class except that the children 
    are refered to as left and right as opposed to prev and next."""

    def __init__(self, val=None, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    def get_val(self):
        return self.val

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_val(self, new_val):
        self.val = new_val

    def set_left(self, new_left):
        self.left = new_left

    def set_right(self, new_right):
        self.right = new_right


class LinkedList:
    "This LinkedList class uses the first Node class. This class takes in a Node"

    def __init__(self, head=None):
        self.head = head

    def get_head(self):
        return self.head

    def set_head(self, node):
        node.set_next(self.head)
        self.head = node

    def __repr__(self):
        curr = self.get_head()
        lst = []
        while curr is not None:
            lst.append(str(curr.get_val()))
            curr = curr.get_next()
        return ' -> '.join(lst)+' -> None'


class dLinkedList:
    """This dLinkedList class uses the dsNode class. Like a linked list 
    just that it has a prev pointer. This class takes in two
    dsNodes"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def get_head(self):
        return self.head

    def set_head(self, node):
        node.set_next(self.head)
        self.head = node

    def get_tail(self):
        return self.tail

    def set_tail(self, node):
        node.set_prev(self.tail)
        self.tail.set_next(node)
        self.tail = node

    def __repr__(self):
        curr = self.get_head()
        lst = []
        while curr is not None:
            lst.append(str(curr.get_val()))
            curr = curr.get_next()
        return ' <-> '.join(lst)+' -> None'

# a = dsNode(1)
# b = dsNode(2)
# c = dsNode(3)
# d = dsNode(4)
# e = dsNode(5)
# a.set_next(b)
# b.set_next(c)
# c.set_next(d)
# d.set_next(e)
# llst = dLinkedList(a, e)
# llst.set_head(dsNode(0))
# llst.set_tail(dsNode(6))
# print(llst)


class BinaryTree:
    """This BinaryTree class uses the tNode class. It takes in a tNode 
    to create a tree. If no node is specified it is set to None"""

    def __init__(self, root=None):
        if root is not None:
            self.root = root
            if root.left is not None:
                self.left = BinaryTree(root.left)
            else:
                self.left = None
            if root.right is not None:
                self.right = BinaryTree(root.right)
            else:
                self.right = None
        else:
            self.root = None
            self.right = None
            self.left = None


def preorder(t):
    """visit the root first then traverse the left subtree, and finally traverse the right subtree"""
    if t is None:
        return []
    if t.left is None and t.right is None:
        return [t.root.val]
    if t.left != None:
        return [t.root.val]+preorder(t.left)+preorder(t.right)
    if t.right != None:
        return [t.root.val]+preorder(t.left)+preorder(t.right)


def inorder(t):
    """traverse the left subtree first, then visit the root, finally traverse the right subtree"""
    if t is None:
        return []
    if t.left is None and t.right is None:
        return [t.root.val]
    if t.left != None:
        return inorder(t.left)+[t.root.val]+inorder(t.right)
    if t.right != None:
        return inorder(t.left)+[t.root.val]+inorder(t.right)


def postorder(t):
    """traverse the the left subtree, then traverse the right subtree, finally visit the root"""
    if t is None:
        return []
    if t.left is None and t.right is None:
        return [t.root.val]
    if t.left != None:
        return postorder(t.left)+postorder(t.right)+[t.root.val]
    if t.right != None:
        return postorder(t.left)+postorder(t.right)+[t.root.val]


def levelorder(t):
    """visit the root first, then visit the neighbors of the node"""
    if t is None:
        return []
    q = deque()
    q.append(t)
    lst = []
    while len(q) != 0:
        curr = q.popleft()
        lst.append(curr.root.val)
        if curr.left != None:
            q.append(curr.left)
        if curr.right != None:
            q.append(curr.right)
    return lst


# def ipreorder(t):
#     if t is None:
#         return []
#     q = deque()
#     q.append(t)
#     lst = []
#     while len(q) != 0:
#         curr = q.popleft()
#         lst.append(curr.root.val)
#         if curr.left == None:
#     return lst


def max_depth(t):
    "checks for the depth of the tree"
    if t is None:
        return 0
    if t.left == None and t.right == None:
        return 1
    if t.left != None:
        return 1 + max(max_depth(t.left), max_depth(t.right))
    if t.right != None:
        return 1 + max(max_depth(t.left), max_depth(t.right))


def max_depth2(t, n):
    "checks for the depth of the tree"
    if t is None:
        return 0
    if t.left == None and t.right == None:
        return n+1
    if t.left != None:
        return max(max_depth2(t.left, n+1), max_depth2(t.right, n+1))
    if t.right != None:
        return max(max_depth2(t.left, n+1), max_depth2(t.right, n+1))


# def isOpp(xs, ys):
#     for i in range(len(xs)):
#         if xs[i] == 0 and ys[i] == 0:
#             return False
#         if xs[i] == 1 and ys[i] == 1:
#             return False
#     return True
# def issymmetric(t):
#     if t is None:
#         return False
#     if t.left is None and t.right is None:
#         return True
#     if t.left is not None:
#         left = ['L']+issymmetric(t.left)
#         right = ['R']+issymmetric(t.right)
#         return (left, right)
#     if t.right is not None:
#         left = ['L']+issymmetric(t.left)
#         right = ['R']+issymmetric(t.right)
#         return (left, right)
# print(issymmetric(tree4))
# print(issymmetric(tree5, []))
# print(max_depth(tree, 0))
# print(max_depth(tree, 1))
# print(max_depth(tree2, 0))
# print(max_depth(tree2, 1))
# print(max_depth(tree3, 0))
# print(max_depth(tree3, 1))
# print(max_depth2(tree))
# print(max_depth2(tree2))
# print(max_depth2(tree3))
"Here I built 5 trees"
root = tNode(4, tNode(5), tNode(3))
root2 = tNode("F", tNode("B", tNode("A"), tNode("D", tNode("C"),
              tNode("E"))), tNode("G", None, tNode("I", tNode("H"), None)))
root4 = tNode(1, tNode(2, tNode(3), tNode(4)), tNode(2, tNode(4), tNode(3)))
root5 = tNode(1, tNode(2, None, tNode(3)), tNode(2, None, tNode(3)))
tree = BinaryTree(root)
tree2 = BinaryTree(root2)
tree3 = BinaryTree()
tree4 = BinaryTree(root4)
tree5 = BinaryTree(root5)
"Testing the traversal methods"
assert preorder(tree2) == ["F", "B", "A", "D", "C", "E", "G", 'I', 'H']
assert inorder(tree2) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
assert postorder(tree2) == ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']
assert levelorder(tree2) == ["F", "B", "G", "A", "D", "I", "C", 'E', 'H']
assert max_depth(tree2) == 4
assert max_depth2(tree2, 0) == 4
