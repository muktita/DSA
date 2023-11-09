def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary
        prevMap = {} 

        # Check if the answer is in the set
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return