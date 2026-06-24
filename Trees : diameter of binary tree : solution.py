# Promblem - diameter of a binary tree 
# Time and space complexity - 0(n) & o(h)
# Leetcode and diffculty level - 543 & easy 
class Solution {
public: 
    int ans = 0;

    int height(TreeNode* root) {

        if(root == NULL) 
            return 0;
            
        int left = height(root->left);
        int right = height(root->right);

        ans = max(ans, left + right);

        return 1 + max(left, right);
    }

    int diameterOfBinaryTree(TreeNode* root) {

        height(root);

        return ans;
    }
    
};
