# Promblem - same tree 
# Approach - recursion
# Time and space complexity - 0(n) & 0(h) 
# Leetcode and diffculty level - 100 & easy 
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        
        if(p == NULL && q == NULL) {
            return true;
        }
        if(p == NULL || q == NULL) {
            return false;
        }
        if(p->val != q->val) {
            return false;
        }

        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
