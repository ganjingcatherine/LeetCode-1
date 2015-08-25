/*
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
*/


public class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        List<String> path = new ArrayList<>();
        
        dfs(s, result, path, 0, 1);
        return result;
    }
    
    private void dfs(String s, List<List<String>> result, List<String> path, int prev, int start) {
        if(start == s.length()) {
            /*test whether s[prev:start-1] is palindrome*/
            /*if it is true, then must add it to one result*/
            if(isPalindrome(s, prev, start - 1)) {
                path.add(s.substring(prev, start));
                result.add(new ArrayList<>(path));
                path.remove(path.size() - 1);
            }
            return;
        }
        
        /*do dfs, search for the next palindrome*/
        dfs(s, result, path, prev, start + 1);
        if(isPalindrome(s, prev, start - 1)) {
            path.add(s.substring(prev, start));
            dfs(s, result, path, start, start + 1);
            path.remove(path.size() - 1);
        }
    }
    
    private boolean isPalindrome(String s, int start, int end) {
        while (start < end) {
            if(s.charAt(start)!=s.charAt(end)) return false;
            start ++;
            end --;
        }
        return true;
    }
}