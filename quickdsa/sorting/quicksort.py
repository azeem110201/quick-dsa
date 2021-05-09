from typing import List

def partition(nums: List, low, high) -> int:
    pivot = nums[low]
    i = low + 1
    j = high

    while True:
        while i <= j and nums[i] <= pivot:
            i += 1

        while nums[j] >= pivot and i <= j:
            j -= 1

        if i > j:
            break
        else:
            nums[j], nums[i] = nums[i], nums[j]

    nums[j], nums[low] = nums[low], nums[j] 

    return j       

def QuickSortUtil(nums: List, low: int, high: int): 
    if low < high:
        partition_pos = partition(nums, low, high)
        QuickSortUtil(nums, low, partition_pos - 1)
        QuickSortUtil(nums, partition_pos + 1, high)


def QuickSort(nums: List) -> List:
    '''
     Functions takes in two arguments that is the array and reverse which indicates ascending or descending sorting.
    '''

    if not isinstance(nums, list):
        raise Exception("Array should be of type list")
        return

    if len(nums) == 0:
        raise Exception("Array of length zero is passed")
        return

    if len(nums) == 1:
        return nums  

    QuickSortUtil(nums, 0, len(nums) - 1)

    return nums