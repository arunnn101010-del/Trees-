# Promblem - kth smallest element in a bst 
# Time and space complexity - 0(n) & 0(h) 
# Approach - bst + sorted tree 
# Leetcode and diffculty level - 230 & medium 
class Solution {
public:
    int count = 0;
    int ans = 0;

    void inorder(TreeNode* root, int k) {     
        if(root == NULL) {
            return;
        }  

        inorder(root->left, k);

        count++;

        if(count == k) {
            ans = root->val;
            return;
        }
        inorder(root->right, k);
    }
    int kthSmallest(TreeNode* root, int k) {
        inorder(root, k);
        return ans;
    }
};
