class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        // Brain stroming time 

        /* 
            Mighty Algo monstor will mix all the elements as dough in the bakery and remove the items in the dough like i remove star shape from the dough if i am using the star mold as i am going to get the same star there so.

            1. Multiply all the elements while doing keep few things in mind
            a)number of zero's if there is only one zero then it alone get's the only value if there are multiple zero's none get any value.
            b)if there are -ve elements then value doesn't change only sign does 
            op is -ve and current element is -ve(Encountered odd -ve's) make it positive
            op is +ve and current element is -ve(Encountered even -ve's) make it negative 
        */

        Boolean foundZero=false;

        int arraySize=nums.length;

        if(arraySize == 1 ) return nums;

        if(arraySize == 0 ) throw new IllegalArgumentException("Invalid number of args");

        int zeroCounter=0,productAll=1,zeroIndex=-1;
        for(int i=0;i<arraySize;++i)
        {
            int value=nums[i];

            if(value==0) 
            {
                ++zeroCounter;
                zeroIndex=i;
            }
            else
            {
                productAll*=value;
            }
            if(zeroCounter>1) return new int[nums.length];
        }
        if(zeroCounter!=0)
        {
            Arrays.fill(nums,0);
            nums[zeroIndex]=productAll;
            return nums;
        }
        for(int i=0;i<arraySize;++i)
        {
                int updatedValue=productAll/nums[i];
                nums[i]=updatedValue;
        }
        return nums;
    }
}