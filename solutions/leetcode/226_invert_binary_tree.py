# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1.1 DFS readable
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

        # 1.2 DFS flex
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left)) if root else None

        # 2 BFS
        q = deque([root])
        while q:
            if cur := q.popleft():
                cur.right, cur.left = cur.left, cur.right
                q.extend([cur.left, cur.right])
        return root

        # 2 Let's change task a little...
        # We'll be working only with a list of values of a given binary tree!
        # from math import log

        tree = [4, 2, 7, 1, 3, 6, 9, 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        print(f'{len(tree)=}')

        max_depth = int(log(len(tree) + 1, 2))
        print(f'{max_depth=}')

        print()

        for i in range(2, max_depth + 1):
            print(f'depth={i}')

            for j in range(2 ** (i - 2)):
                print(j + 1)
                print(f'{tree[2 ** (i - 1) - 1 + j]=}')
                print(f'{tree[2 ** (i - 1) - 1 + 2 ** (i - 1) - j - 1]=}')

                tree[2 ** (i - 1) - 1 + j], tree[2 ** (i - 1) - 1 + 2 ** (i - 1) - j - 1] = tree[2 ** (
                            i - 1) - 1 + 2 ** (i - 1) - j - 1], tree[2 ** (i - 1) - 1 + j]

            print()

        print(f'{tree=}')
