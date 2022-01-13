from collections import deque
# class Node:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next

#     def get_val(self):
#         return self.val

#     def get_next(self):
#         return self.next

#     def set_val(self, new_val):
#         self.val = new_val

#     def set_next(self, new_next):
#         self.next = new_next


# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

#     def get_head(self):
#         return self.head

#     def set_head(self, node):
#         node.set_next(self.head)
#         self.head = node

#     def __repr__(self):
#         curr = self.get_head()
#         lst = []
#         while curr is not None:
#             lst.append(str(curr.get_val()))
#             curr = curr.get_next()
#         return ' -> '.join(lst)+' -> None'

# class dsNode:
#     def __init__(self, val=None, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

#     def get_val(self):
#         return self.val

#     def get_next(self):
#         return self.next

#     def get_prev(self):
#         return self.prev

#     def set_val(self, new_val):
#         self.val = new_val

#     def set_next(self, new_next):
#         self.next = new_next

#     def set_prev(self, new_prev):
#         self.prev = new_prev

# class dLinkedList:
#     def __init__(self, head=None, tail=None):
#         self.head = head
#         self.tail = tail

#     def get_head(self):
#         return self.head

#     def set_head(self, node):
#         node.set_next(self.head)
#         self.head = node

#     def get_tail(self):
#         return self.tail

#     def set_tail(self, node):
#         node.set_prev(self.tail)
#         self.tail.set_next(node)
#         self.tail = node

#     def __repr__(self):
#         curr = self.get_head()
#         lst = []
#         while curr is not None:
#             lst.append(str(curr.get_val()))
#             curr = curr.get_next()
#         return ' <-> '.join(lst)+' -> None'

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

class tNode:
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


class BinaryTree:
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
    if t is None:
        return []
    if t.left is None and t.right is None:
        return [t.root.val]
    if t.left is not None:
        return [t.root.val]+preorder(t.left)+preorder(t.right)
    if t.right is not None:
        return [t.root.val]+preorder(t.right)


def inorder(t):
    if t is None:
        return []
    if t.left is not None:
        return inorder(t.left)+[t.root.val]+inorder(t.right)
    if t.left is None and t.right is None:
        return [t.root.val]
    if t.right is not None:
        return [t.root.val]+inorder(t.left)+inorder(t.right)


def postorder(t):
    if t is None:
        return []
    if t.left is not None:
        return postorder(t.left)+postorder(t.right)+[t.root.val]
    if t.left is None and t.right is None:
        return [t.root.val]
    if t.right is not None:
        return postorder(t.left)+postorder(t.right)+[t.root.val]


def max_depth(t, n):
    if t is None:
        return n
    if t.left is None and t.right is None:
        return n
    if t.left is not None:
        return max(max_depth(t.left, n+1), max_depth(t.right, n+1))
    if t.right is not None:
        return max(max_depth(t.left, n+1), max_depth(t.right, n+1))


def max_depth2(t):
    if t is None:
        return 0
    if t.left is None and t.right is None:
        return 1
    if t.left is not None:
        return max(max_depth2(t.left), max_depth2(t.right))+1
    if t.right is not None:
        return max(max_depth2(t.left), max_depth2(t.right))+1


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


def isOpp(xs, ys):
    for i in range(len(xs)):
        if xs[i] == 0 and ys[i] == 0:
            return False
        if xs[i] == 1 and ys[i] == 1:
            return False
    return True


def issymmetric(t):
    if t is None:
        return False
    if t.left is None and t.right is None:
        return True
    if t.left is not None:
        left = ['L']+issymmetric(t.left)
        right = ['R']+issymmetric(t.right)
        return (left, right)
    if t.right is not None:
        left = ['L']+issymmetric(t.left)
        right = ['R']+issymmetric(t.right)
        return (left, right)


print(issymmetric(tree4))
# print(issymmetric(tree5, []))

# print(preorder(tree2))
# print(inorder(tree2))
# print(postorder(tree2))
# print(max_depth(tree, 0))
# print(max_depth(tree, 1))
# print(max_depth(tree2, 0))
# print(max_depth(tree2, 1))
# print(max_depth(tree3, 0))
# print(max_depth(tree3, 1))
# print(max_depth2(tree))
# print(max_depth2(tree2))
# print(max_depth2(tree3))
