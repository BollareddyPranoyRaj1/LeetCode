class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                map.remove(nums[i]); 
            } else {
                map.put(nums[i], 1);  
            }
        }
        for(int key : map.keySet()){
            return key;
        }
        return -1;
    }
}