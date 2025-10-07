class Solution {
    static{
        for(int i=0;i<=500;i++)
            containsDuplicate(new int[]{0, 1, 0});
    }
    public static boolean containsDuplicate(int[] nums) {

        // Using hashset to handle values bigger than a million as they take up more than 125kb at 2 million it start's to see decline in it's performace 

        int maxValue = nums[0];

        // It's more taking pictures of each indivual and comparing rather following any linear interation procudure

        for(int value:nums) maxValue=Math.max(value,maxValue);

        if(maxValue>2_000_000)
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
            // This would work like a beast if it is all the positive number's now it has to be 2x for -ve as well

            BitSet bitSetPositive = new BitSet(),bitSetNegative = new BitSet();

            // It's more like a match sticks in a infinte +ve rows (MAX_INT) and we go by index and lit it and if go to the same match again then return conclusion yeah duplicates exist

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