class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> mp = new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;++i)
        {
            int rem = target - nums[i];
            if(mp.containsKey(rem))
            {
                return new int[]{mp.get(rem),i};
            }
            else
            {
                mp.put(nums[i],i);
            }
        }
        return new int[]{};
    }
}