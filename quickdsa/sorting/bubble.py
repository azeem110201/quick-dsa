from typing import List

def BubbleSort(nums: List, reverse: bool = False) -> List:
    '''
     Functions takes in two arguments that is the array and reverse which indicates ascending or descending sorting.
    '''

    if not isinstance(nums, list):
        raise Exception("Array should be of type list")
        return

    if len(nums) == 0:
        raise Exception("Array of length zero is passed")   

    n = len(nums)     

    if reverse == True:
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] < nums[j+1]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]

        return nums

    else:
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]

        return nums               