class Solution {
    public int maxSubArray(int[] nums) {
        
        int sum=nums[0],maxsum=nums[0];

        // Taking the sum and compare the with the new sum(which exist from the point of getting low)

        for(int i=1;i<nums.length;++i)
        {
            if(nums[i]>sum && sum<0)
            {
                sum=nums[i];    
            }
            else
            {
                sum+=nums[i];
            }
            maxsum=Math.max(maxsum,sum);
            if(sum<0) sum=0;
        }

        return maxsum;
    }
}