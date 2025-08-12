
# 213. House Robber II
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def helperRob(subNum):
            prev = 0
            prevnot = 0
            for num in subNum:
                temp = max(prev, num + prevnot)
                prevnot = prev
                prev = temp
            return prev

        return max(helperRob(nums[1:]), helperRob(nums[:-1]) )

if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,2]
    print("rob II is:", sol.rob2(nums))
