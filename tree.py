
class Node :
    def __init__(self,data):
        self.tree = None
        self.left =None
        self.right = None
        self.data = data
        self.parent = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l+r+1

    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return l +1 if l > r else r + 1

    def inorder(self):
        if self.left :
            self.left.inorder()
        print(self.data)
        if self.right :
            self.right.inorder()

    def preorder(self):
        print(self.data)
        if self.left :
            self.left.preorder()
        if self.right :
            self.right.preorder()

    def postorder(self):
        if self.left :
            self.left.postorder()
        if self.right :
            self.right.postorder()
        print(self.data)

class BinaryTree:
    def __init__(self,r):
        self.root = r

    def size(self):
        return self.root.size() if self.root else 0

    def depth(self):
        return self.root.depth() if self.root else 0

    def inorder(self):
        self.root.inorder()

    def preorder(self):
        self.root.preorder()

    def postorder(self):
        self.root.postorder()

class BSTNode(Node):

    def __init__(self,data,tree):

        self.tree = None
        self.left =None
        self.right = None
        self.data = data
        self.parent = None
        self.tree = tree

    def childCount(self):
        count = 0
        if self.left:
            count +=1
        if self.right :
            count+=1
        return count

    def insert(self,k,tree):

        if self.data :
            if self.data > k: # left
                if self.left :
                    self.left.insert(k,tree)
                else :
                    self.left = BSTNode(k,tree)
                    self.left.parent = self
            else :
                if self.right:
                    self.right.insert(k,tree)
                else:
                    self.right = BSTNode(k, tree)
                    self.right.parent = self


    def search(self,k):
        if self.data == k :
            return self

        elif self.data > k :
            return self.left.search(k)

        else :
            return self.right.search(k)


    def subtree_left(self,subtree_node):
        if subtree_node.left:
            self.tree.for_remove_lis.append(subtree_node.left.data)
            self.subtree_left(subtree_node.left)
        if subtree_node.right:
            self.tree.for_remove_lis.append(subtree_node.right.data)
            self.subtree_left(subtree_node.right)



    def remove(self, k):
        target = self.search(k)
        if target == False:
            print("존재하지 않습니다.")
            return 0
        childCount = target.childCount()

        if childCount == 0: # 말단 노드인 경우 나만 지워지면 됌. parent 기준 left라면 parent.left = None.
            if target.parent.left == target:
                target.parent.left = None
            if target.parent.right == target:
                target.parent.right = None
        elif childCount == 1: # 자식이 하나만 있는 경우.
            if target.parent.left == target:
                if target.left :
                    target.parent.left = target.left
                if target.right :
                    target.parent.left = target.right

            if target.parent.right == target:
                if target.left :
                    target.parent.right = target.left
                if target.right :
                    target.parent.right = target.right

        else :
            if target.parent.left == target : # 좌가 올라오든 우가 올라오든 상관 없는듯 싶다. 좌측 노드가 올라가자.
                self.subtree_left(target.left) # 노드의 tree 객체의 remove list를 이용해서 target.left의 하단 노드들을 그냥 다 가져오
                subtrees = BSTNode(target.left.data, target.tree)
                rightsubtree = target.right
                subtrees.right = rightsubtree
                target.parent.left = subtrees


                for data in self.tree.for_remove_lis: # 위에셔 가져온 하단 노드들을 그냥 insert 시켜주자 순서에 맞게
                    target.parent.insert(data)


            if target.parent.right == target :
                self.subtree_left(target.left)
                subtrees = BSTNode(target.left.data, target.tree)
                rightsubtree = target.right
                subtrees.right = rightsubtree
                target.parent.right = subtrees

                for data in self.tree.for_remove_lis:
                    target.parent.insert(data,target.tree)

            self.tree.initialize_remove_lis()


class BinarySearchTree(BinaryTree):
    def __init__(self, k):
        self.root = BSTNode(k,self)
        self.for_remove_lis = []

    def initialize_remove_lis(self):
        self.for_remove_lis = None

    def insert(self, k):
        self.root.insert(k,self)

    def search(self, k):
        return self.root.search(k)

    def remove(self, k):
        self.root.remove(k)
