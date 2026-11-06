# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def insert(root,key):
            if root is None:
                return(TreeNode(key))

            if root.val<key:
                root.right=insert(root.right,key)
                
            elif root.val>key:
                root.left=insert(root.left,key)
            return root
        root=None
        
        for i in preorder:
            root=insert(root,i)
        return root
