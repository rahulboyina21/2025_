class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        ans=[]
        for i in range(len(nums)):
            if hm.get(target-nums[i])!=None:
                ans.append(i)
                ans.append(hm.get(target-nums[i]))
                return ans
            else:
                hm[nums[i]]=i
        return ans