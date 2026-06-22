# Promblem - maximum depth of binary tree 
# Approach - recursion 
# Time and space complexity - 0(n) & 0(h) 
# Leetcode and diffculty level - 104 & easy 
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == NULL) {
            return 0;
        }

        int left = maxDepth(root->left);
        int right = maxDepth(root->right);

        return 1 + max(left, right);
    }
};
