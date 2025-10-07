class Solution {
    public boolean containsDuplicate(int[] nums) {

        int maxValue = nums[0];

        for(int value:nums) maxValue=Math.max(value,maxValue);

        if(maxValue>1_000_000)
        {
            Set<Integer> st = new HashSet<>();

            for(int value:nums)
            {
                if(st.contains(value)) return true;
                st.add(value);
            }
            return false;
        }

        // Light weight data strcuture which can be used to track binary event's extending till INT_MAX

        else
        {

            BitSet bitSetPositive = new BitSet(),bitSetNegative = new BitSet();

            for(int value:nums)
            {
                if(value<0)
                {
                    value = Math.abs(value);
                        if(bitSetNegative.get(value)) return true;
                        bitSetNegative.set(value);
                }
                else
                {
                    if(bitSetPositive.get(value)) return true;
                    bitSetPositive.set(value);
                }
            }
            return false;
        }
    }
}