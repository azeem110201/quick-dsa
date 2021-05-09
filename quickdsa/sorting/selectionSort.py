from typing import List

def SelectionSort(nums: List, reverse: bool = False) -> List:
    '''
     Functions takes in two arguments that is the array and reverse which indicates ascending or descending sorting.
    '''

    if not isinstance(nums, list):
        raise Exception("Array should be of type list")
        return

    if len(nums) == 0:
        raise Exception("Array of length zero is passed")    

    if reverse == True:
        for i in range(len(nums)):
            j = i
            for k in range(i+1, len(nums)):
                if nums[k] > nums[j]:
                    j = k

            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        return nums
    else:
        for i in range(len(nums)):
            j = i
            for k in range(i+1, len(nums)):
                if nums[k] < nums[j]:
                    j = k

            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        return nums               