from tree import BinarySearchTree


BST = BinarySearchTree(15)
BST.insert(9)
BST.insert(6)
BST.insert(12)
BST.insert(4)
BST.insert(2)
BST.insert(5)
BST.insert(8)
BST.insert(10)
BST.insert(14)
BST.insert(30)
BST.insert(19)
BST.insert(17)
BST.insert(18)
BST.insert(20)
BST.insert(35)
BST.insert(32)
BST.insert(36)

print("===Preorder===")
BST.preorder()
print("\n\n---------remove30-----------\n\n")

BST.remove(30)
BST.remove(17)
print("===Preorder===")
BST.preorder()

print("\n===size, depth===\n")
print("size : {}".format(BST.size()))
print("depth : {}".format(BST.depth()))