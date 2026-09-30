class Solution {
  public String largestNumber(int[] nums) {
    final String s = Arrays.stream(nums)
                         .mapToObj(String::valueOf)
                        
