# Promblem - pascal's triangle 
# Time and space complexity - o(n^2) & 0(n)
# Leetcode and diffculty level - 119 & medium 
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row(rowIndex+1,0);
        row[0] = 1;

        for(int i=1; i<=rowIndex; i++) {
            for(int j=i; j>=1; j--) {
                row[j] = row[j] + row[j-1];
            }
        }
        return row;
    }
};
