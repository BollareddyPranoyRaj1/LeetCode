class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character,Integer> map = new HashMap<>();
        int ini=0,mble=0;int maxlen=0;
        for (mble = 0; mble < s.length(); mble++){
            char ch = s.charAt(mble);
            map.put(ch,map.getOrDefault(ch,0)+1);
            while(map.get(ch)>1){
                char left = s.charAt(ini);
                map.put(left, map.get(left) - 1);
                ini++;
            }
            maxlen=Math.max(maxlen,mble-ini+1);
        }
        return maxlen;
    }
}