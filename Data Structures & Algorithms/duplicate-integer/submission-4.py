class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st = []
        for i in nums:
            if i in st:
                return True
            st.append(i)
        return False