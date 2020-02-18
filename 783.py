# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    NUM = 0
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root.left and root.left) is not None or (root.right and root.right) is not None:
            diff = self.helper(root)
        elif (root.left) is not None:
            diff = abs(root.val - root.left.val)
        elif root.right is not None:
            diff = abs(root.val - root.right.val)
        else:
            return


        if root.left is not None:
            if diff >= abs(root.left.val - root.val):
                #diff = abs(root.left.val - root.val)
                diff = self.minDiffInBST(root.left)
            else:
                self.minDiffInBST(root.left)

        if root.right is not None:
            if diff >= abs(root.right.val - root.val):
                #diff = abs(root.right.val - root.val)
                diff = self.minDiffInBST(root.right)
            else:
                self.minDiffInBST(root.right)

        return diff

    def helper(self, root):
        """
        :param root:
        :return:
        """
        if root.left is not None:
            return abs(root.left.val-root.val)
        elif root.right is not None:
            return abs(root.right.val-root.val)
        else:
            return 0

    def main(self):
        #[4,2,6,1,3,null,null]

        node1 = TreeNode(4)
        node2 = TreeNode(2)
        node3 = TreeNode(6)
        node4 = TreeNode(1)
        node5 = TreeNode(3)

        node1.left = node2
        node1.right = node3

        node2.left = node4
        node2.right = node5

        node3.left = None
        node3.right = None

        node4.left = None
        node4.right = None

        node5.left = None
        node5.right = None

        num = self.minDiffInBST(self, node1)
        print(num)

if __name__ == '__main__':

    res = Solution()
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(6)
    node4 = TreeNode(1)
    node5 = TreeNode(3)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = None
    node3.right = None

    node4.left = None
    node4.right = None

    node5.left = None
    node5.right = None

    num = res.minDiffInBST(node1)
    print(num)