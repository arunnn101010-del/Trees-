# Promblem - symmetric tree
# Approach - recursion
# Time and space complexity - 0(n) & 0(h) 
# Leetcode and diffculty level - 101 & easy 
class Solution {
public:
    bool mirror(TreeNode* left, TreeNode* right) {

        if(left == NULL && right == NULL) {
            return true;
        }
        if(left == NULL || right == NULL) {
            return false;
        }
        if(left->val != right->val) {
            return false;
        }

        return mirror(left->left, right->right) && mirror(left->right, right->left);
    }
    bool isSymmetric(TreeNode* root) { 

        if(root == NULL) {
            return true;
        }
        
        return mirror(root->left, root->right);
    }
};
