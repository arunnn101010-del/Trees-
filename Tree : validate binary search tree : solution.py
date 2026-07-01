# Problem - validate binary search tree 
# Approach - dfs 
# Time and space complexity - 0(n) & 0(h) 
# Leetcode and diffculty level - 98 & medium 
class Solution {
public:

    bool check(TreeNode* root, long minVal, long maxVal) {

        if(root == NULL) {
            return true;
        }

        if(root->val <= minVal || root->val >= maxVal) {
            return false;
        }

        return check(root->left, minVal, root->val) && 
            check(root->right, root->val, maxVal);
    }
    bool isValidBST(TreeNode* root) {
        return check(root, LONG_MIN, LONG_MAX);
    }
};
