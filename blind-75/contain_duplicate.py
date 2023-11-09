def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty dictionary
        num_dict = {}
        # Check through the array to find if they have occur more than once 
        # { key: value }
        # { 1: 2, 2: 1, 3:1, 4:1}
        for n in nums:
            if n in num_dict:
                num_dict[n] += 1
            else:
                num_dict[n] = 1
        print(num_dict)
        for (key, val) in num_dict.items():
            if val > 1:
                return True
        return False
        print(num_dict)