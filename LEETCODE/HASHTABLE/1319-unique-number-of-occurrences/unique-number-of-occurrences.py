from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dc = defaultdict(int)
        for i in arr:
            dc[i]+=1
        st=set()
        for k,v in dc.items():
            if v in st:
                return False
            st.add(v)
        return True 