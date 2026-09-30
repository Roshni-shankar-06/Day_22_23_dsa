class Solution {
 public:
  vector<int> maxDepthAfterSplit(string seq) {
    vector<int> ans;
    int depth = 1;

    // Put all odd-depth parentheses in one group and even-depth parentheses in
    // the other group.
