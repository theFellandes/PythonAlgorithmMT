import time


class TreeNode:
    left_child = None
    right_child = None
    parent = None
    value: int

    def __init__(self, value: int):
        self.value = value

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

    def tree_delete(self):
        if self.left_child is None or self.right_child is None:
            y = self
        else:
            y = self.tree_successor(self)

        if y.left_child is not None:
            x = y.left_child
        else:
            x = y.right_child

        if x is not None:
            x.parent = y.parent

        elif y is y.parent.left_child:
            y.parent.left_child = x

        else:
            y.parent.right_child = x

        if y is not self:
            self.value = y.value

        return y


class Tree:
    root = None

    def tree_insert(self, value: int):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.tree_insert(value)

    def tree_delete(self, node: TreeNode):
        if node is self.root:
            old_root = TreeNode(self.root.value)
            old_root.right_child = self.root.right_child
            old_root.left_child = self.root.left_child
            self.__delete(node)
            return old_root
        else:
            return node.tree_delete()

    def __delete(self, node: TreeNode):
        if node.left_child is None or node.right_child is None:
            y = node
        else:
            y = node.tree_successor(node)

        if y.left_child is not None:
            x = y.left_child
        else:
            x = y.right_child

        if x is not None:
            x.parent = y.parent

        if y.parent is None:
            self.root = x

        elif y is y.parent.left_child:
            y.parent.left_child = x

        else:
            y.parent.right_child = x

        if y is not node:
            node.value = y.value

        return y

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
    int_tree2 = Tree()
    int_tree3 = Tree()

    print("---------------int_tree1------------------------------------")
    print()

    print("Insert")
    tic = time.perf_counter_ns()
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
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("tree_search")
    tic = time.perf_counter_ns()
    root = int_tree.tree_search(15)
    print("Result: " + str(root.value))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("inorder_tree_walk")
    tic = time.perf_counter_ns()
    int_tree.inorder_tree_walk(root)
    toc = time.perf_counter_ns()
    print()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Successor: ")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree.tree_successor(root).value))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Predecessor:")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree.tree_predecessor(root).value))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Maximum: ")
    tic = time.perf_counter_ns()
    print(int_tree.tree_maximum(root).value)
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Minimum: ")
    tic = time.perf_counter_ns()
    print(int_tree.tree_minimum(root).value)
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Maximum Path: ")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree.tree_max_path_length(root)))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Minimum Path: ")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree.tree_min_path_length(root)))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Ratio: ")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree.tree_ratio_length(root)))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Delete: ")
    tic = time.perf_counter_ns()
    print("Result : " + str(int_tree.tree_delete(root).value))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("############################################################")
    print("---------------int_tree2------------------------------------")

    print("Insert")
    tic = time.perf_counter_ns()
    int_tree2.tree_insert(5)
    int_tree2.tree_insert(3)
    int_tree2.tree_insert(7)
    int_tree2.tree_insert(2)
    int_tree2.tree_insert(5)
    int_tree2.tree_insert(9)
    int_tree2.tree_insert(8)
    int_tree2.tree_insert(8)
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("tree_search")
    tic = time.perf_counter_ns()
    root = int_tree2.tree_search(5)
    print("Result: " + str(root.value))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("inorder_tree_walk")
    tic = time.perf_counter_ns()
    int_tree2.inorder_tree_walk(root)
    toc = time.perf_counter_ns()
    print()
    print(str((toc - tic) / 1000) + " microseconds")

    root = int_tree2.tree_search(7)
    print("Successor: ")
    tic = time.perf_counter_ns()
    print(str(root.value))
    print("Result: " + str(int_tree2.tree_successor(int_tree2.tree_search(5)).value))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Predecessor:")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree2.tree_predecessor(root).value))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Maximum: ")
    tic = time.perf_counter_ns()
    print(int_tree2.tree_maximum(root).value)
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Minimum: ")
    tic = time.perf_counter_ns()
    print(int_tree2.tree_minimum(root).value)
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Maximum Path: ")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree2.tree_max_path_length(root)))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Minimum Path: ")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree2.tree_min_path_length(root)))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Ratio: ")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree2.tree_ratio_length(root)))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    root = int_tree2.tree_search(9)
    print("Delete: ")
    tic = time.perf_counter_ns()
    print("Result : " + str(int_tree2.tree_delete(root).value))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("#######################################################")
    print("--------------------int_tree3-------------------------------")

    print("Insert")
    tic = time.perf_counter_ns()
    int_tree3.tree_insert(9)
    int_tree3.tree_insert(4)
    int_tree3.tree_insert(8)
    int_tree3.tree_insert(1)
    int_tree3.tree_insert(3)
    int_tree3.tree_insert(10)
    int_tree3.tree_insert(12)
    int_tree3.tree_insert(11)
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("tree_search")
    tic = time.perf_counter_ns()
    root = int_tree3.tree_search(9)
    print("Result: " + str(root.value))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("inorder_tree_walk")
    tic = time.perf_counter_ns()
    int_tree3.inorder_tree_walk(root)
    toc = time.perf_counter_ns()
    print()
    print(str((toc - tic) / 1000) + " microseconds")

    root = int_tree3.tree_search(10)
    print("Successor: ")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree3.tree_successor(root).value))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Predecessor:")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree3.tree_predecessor(root).value))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Maximum: ")
    tic = time.perf_counter_ns()
    print(int_tree3.tree_maximum(root).value)
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Minimum: ")
    tic = time.perf_counter_ns()
    print(int_tree3.tree_minimum(root).value)
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Maximum Path: ")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree3.tree_max_path_length(root)))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Minimum Path: ")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree3.tree_min_path_length(root)))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Ratio: ")
    tic = time.perf_counter_ns()
    print("Result: " + str(int_tree3.tree_ratio_length(root)))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")

    print("Delete: ")
    tic = time.perf_counter_ns()
    print("Result : " + str(int_tree3.tree_delete(root).value))
    toc = time.perf_counter_ns()
    print(str((toc - tic) / 1000) + " microseconds")


def main2():
    #Testing successor and predecessor's correctness
    int_tree2 = Tree()
    int_tree2.tree_insert(15)
    int_tree2.tree_insert(6)
    int_tree2.tree_insert(18)
    int_tree2.tree_insert(3)
    int_tree2.tree_insert(7)
    int_tree2.tree_insert(17)
    int_tree2.tree_insert(20)
    int_tree2.tree_insert(2)
    int_tree2.tree_insert(4)
    int_tree2.tree_insert(13)
    int_tree2.tree_insert(9)

    print(int_tree2.tree_successor(int_tree2.tree_search(15)).value)
    print(int_tree2.tree_successor(int_tree2.tree_search(13)).value)
    print(int_tree2.tree_successor(int_tree2.tree_search(9)).value)
    print()
    print(int_tree2.tree_predecessor(int_tree2.tree_search(15)).value)
    print(int_tree2.tree_predecessor(int_tree2.tree_search(9)).value)
    print(int_tree2.tree_predecessor(int_tree2.tree_search(7)).value)


if __name__ == '__main__':
    main()
    # main2()
