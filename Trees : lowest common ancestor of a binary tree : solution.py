# Promblem - lowest common ancestor of a binary tree 
# Approach - bfs 
# Time and space complexity - 0(n) & 0(h) 
# Leetcode and diffculty level - 236 & medium 
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
        if(root == NULL) {
            return NULL;
        }

        if(root == p || root == q) {
            return root;
        }

        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);

        if(left != NULL && right != NULL) {
            return root;
        }

        if(left != NULL) {
            return left;
        }
        return right;
    }
};
