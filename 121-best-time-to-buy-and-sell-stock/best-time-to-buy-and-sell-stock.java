class Solution {
    public int maxProfit(int[] prices) {
        int low=prices[0],profit=-1;
        for(int i=0;i<prices.length;++i)
        {
            int temp=prices[i]-low;
            if(temp<0)
            {
                low=prices[i];
            }
            else if(temp>profit)
            {
                profit=temp;
            }
        }
        return profit;
    }
}