class Solution {
  public List<String> addOperators(String num, int target) {
    List<String> ans = new ArrayList<>();
    dfs(num, target, 0, 0, 0, new StringBuilder(), ans);
    return ans;
  }

  private void dfs(String num, int target, int s, long prev, long eval, StringBuilder sb,
                   List<String> ans) {
    if (s == num.length()) {
  
