# DELETE EKSİK!!!!!!!
class TreeNode:
    left_child = None
    right_child = None
    parent = None
    value: int

    def __init__(self, value: int):
        self.value = value

    def set_left_child(self, left_child):
        self.left_child = left_child

    def set_right_child(self, right_child):
        self.right_child = right_child

    def tree_insert(self, value: int):
        if value <= self.value:
            if self.left_child is None:
                self.left_child = TreeNode(value)
                self.left_child.parent = self
            else:
                self.left_child.tree_insert(value)

        else:
            if self.right_child is None:
                self.right_child = TreeNode(value)
                self.right_child.parent = self
            else:
                self.right_child.tree_insert(value)

    def inorder_tree_walk(self, node):

        if node.left_child is not None:
            node.left_child.inorder_tree_walk(node.left_child)
        print(str(self.value), end=" ")

        if node.right_child is not None:
            node.right_child.inorder_tree_walk(node.right_child)

    def tree_search(self, value: int):
        if value == self.value:
            return self

        if value < self.value:
            if self.left_child is not None:
                return self.left_child.tree_search(value)

        elif value > self.value:
            if self.right_child is not None:
                return self.right_child.tree_search(value)

        return None

    def tree_minimum(self):
        if self.left_child is None:
            return self

        else:
            return self.left_child.tree_minimum()

    def tree_maximum(self):
        if self.right_child is None:
            return self

        else:
            return self.right_child.tree_maximum()

    def tree_successor(self, node):
        if node.right_child is not None:
            return self.right_child.tree_minimum()

        parent = node.parent
        while parent is not None:
            if node is not parent.right_child:
                break
            node = parent
            parent = parent.parent
        return parent

    def tree_predecessor(self, node):
        if node.left_child is not None:
            return self.left_child.tree_maximum()

        parent = node.parent
        while parent is not None:
            if node is not parent.left_child:
                break
            node = parent
            parent = parent.parent
        return parent

    def tree_max_path_length(self, node):
        if node is None:
            return 0

        left_depth = self.tree_max_path_length(node.left_child)
        right_depth = self.tree_max_path_length(node.right_child)

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

    def tree_min_path_length(self, node):
        if node is None:
            return 0

        left_depth = self.tree_max_path_length(node.left_child)
        right_depth = self.tree_max_path_length(node.right_child)

        if left_depth < right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

    # def tree_delete(self, root):
    #     # Case 1
    #     curr = self
    #     if self.left_child is None and self.right_child is None:
    #         if self is not root:
    #             if self.parent.left_child is self:
    #                 self.parent.left_child = None
    #             else:
    #                 self.parent.right_child = None
    #
    #     # Case 2
    #     elif self.left_child and self.right_child:
    #         successor = self.tree_delete(self.tree_successor(self.right_child))
    #         self.right_child.parent = successor
    #
    #     # Case 3
    #     else:
    #         if self.left_child:
    #             child = self.left_child
    #
    #         else:
    #             child = self.right_child
    #
    #         if self is not root:
    #             if self is self.parent.left_child:
    #                 self.parent.left_child = child
    #             else:
    #                 self.parent.right_child = child
    #     return curr

    def tree_delete(self, root):
        if root is None:
            return root

        if root.left_child is None:
            temp = root.right_child
            return temp

        elif root.right_child is None:
            temp = root.left_child
            return temp

        temp = self.tree_successor(self)
        root.value = temp.value

        root.right_child = self.tree_delete(root.right_child)

        if root is None:
            return
        return root


class Tree:
    root = None

    def tree_insert(self, value: int):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.tree_insert(value)

    # def tree_delete(self, node: TreeNode):
    #     self.root = self.delete(self.root, node)
    #
    # def delete(self, subtree_root: TreeNode, node: TreeNode):
    #
    #     if subtree_root is None:
    #         return subtree_root
    #
    #     if node.value < subtree_root.value:
    #         subtree_root.set_left_child(self.delete(subtree_root.left_child, node))
    #
    #     elif node.value > subtree_root.value:
    #         subtree_root.set_right_child(self.delete(subtree_root.right_child, node))
    #
    #     else:
    #         # Case 1 and 2
    #         # Handling node has 0 or 1 child
    #         if subtree_root.left_child is None:
    #             return subtree_root.right_child
    #
    #         if subtree_root.right_child is None:
    #             return subtree_root.left_child
    #
    #         # Case 3
    #         # subtree_root.

    # def tree_delete(self, node: TreeNode):
    #     if node.left_child is None or node.right_child is None:
    #         y = node
    #     else:
    #         y = node.tree_successor(node)
    #
    #     if y.left_child is not None:
    #         x = y.left_child
    #     else:
    #         x = y.right_child
    #
    #     if x is not None:
    #         x.parent = y.parent
    #
    #     if y.parent is None:
    #         self.root = x
    #     elif y == y.parent.left_child:
    #         y.parent.left_child = x
    #     else:
    #         y.parent.right_child = x
    #     if y is not node:
    #         node.tree_delete(y)
    #     return y

    # def tree_delete(self, node: TreeNode):
    #     curr = node
    #     if node is not self.root:
    #         return node.tree_delete(self.root)
    #     # Case 2
    #     if node.left_child and node.right_child:
    #         successor = self.tree_delete(node.tree_successor(node.right_child))
    #         self.root.value = successor.value
    #
    #     # Case 3
    #     else:
    #         if node.left_child:
    #             child = node.left_child
    #
    #         else:
    #             child = node.right_child
    #
    #         if node is not self.root:
    #             if node is node.parent.left_child:
    #                 node.parent.left_child = child
    #             else:
    #                 node.parent.right_child = child
    #         else:
    #             self.root = child
    #     return curr

    def tree_delete(self, node: TreeNode):
        self.root = node.tree_delete(self.root)

    @staticmethod
    def inorder_tree_walk(node: TreeNode):
        if node is not None:
            node.inorder_tree_walk(node)

    def tree_search(self, value: int):
        if self.root is not None:
            return self.root.tree_search(value)
        return None

    def tree_minimum(self, node: TreeNode):
        if self.root is None:
            print(Exception("Tree is empty"))

        else:
            return node.tree_minimum()

    def tree_maximum(self, node: TreeNode):
        if self.root is None:
            print(Exception("Tree is empty"))

        else:
            return node.tree_maximum()

    def tree_successor(self, node: TreeNode):
        return self.root.tree_successor(node)

    def tree_predecessor(self, node: TreeNode):
        return self.root.tree_predecessor(node)

    @staticmethod
    def tree_max_path_length(node: TreeNode):
        return node.tree_max_path_length(node)

    @staticmethod
    def tree_min_path_length(node: TreeNode):
        return node.tree_min_path_length(node)

    @staticmethod
    def tree_ratio_length(node: TreeNode):
        return node.tree_min_path_length(node) / node.tree_max_path_length(node)


def main():
    int_tree = Tree()
    int_tree.tree_insert(15)
    int_tree.tree_insert(5)
    int_tree.tree_insert(16)
    int_tree.tree_insert(3)
    int_tree.tree_insert(12)
    int_tree.tree_insert(20)
    int_tree.tree_insert(10)
    int_tree.tree_insert(13)
    int_tree.tree_insert(18)
    int_tree.tree_insert(23)
    int_tree.tree_insert(6)
    int_tree.tree_insert(7)

    # int_tree.tree_insert(5)
    # int_tree.tree_insert(3)
    # int_tree.tree_insert(7)
    # int_tree.tree_insert(2)
    # int_tree.tree_insert(5)
    # int_tree.tree_insert(9)
    # int_tree.tree_insert(8)
    # int_tree.tree_insert(8)

    # print(int_tree.tree_maximum().value)
    # print("---------------------")
    # print(int_tree.tree_predecessor(int_tree.tree_search(7)).value)
    # print(int_tree.tree_min_path_length(int_tree.tree_search(5)))
    # print(int_tree.tree_max_path_length(int_tree.tree_search(5)))
    # print(int_tree.tree_ratio_length(int_tree.tree_search(5)))
    # print(int_tree.tree_delete(int_tree.tree_search(8)).value)
    # print(int_tree.tree_delete(int_tree.tree_search(8)).value)
    # print(int_tree.tree_delete(int_tree.tree_search(7)).value)
    print(int_tree.tree_delete(int_tree.tree_search(5)))
    print(int_tree.inorder_tree_walk(int_tree.tree_search(6)))


if __name__ == '__main__':
    main()
