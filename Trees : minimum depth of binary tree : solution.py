# Promblem - minimum depth of binary tree 
# Approach - recursion
# Time and space complexity - 0(n) & 0(h) 
# Leetcode and diffculty level - 111 & easy 
class Solution {
public:
    int minDepth(TreeNode* root) {
        
        if(root == NULL) {
            return 0;
        }

        int left = minDepth(root->left);
        int right = minDepth(root->right);

        if(root->left == NULL) {
            return 1 + right;
        }

        if(root->right == NULL) {
            return 1 + left;
        }

        return 1 + min(left, right);
    }
};
