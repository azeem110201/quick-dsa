from typing import List

def merge_sort(nums: List, low: int, mid: int, high: int):
    n1 = mid - low + 1
    n2 = high - mid 

    L = [-1 for i in range(n1)]      
    R = [-1 for i in range(n2)]

    for i in range(n1):
        L[i] = nums[low+i]

    for i in range(n2):
        R[i] = nums[mid + 1 + i]    

    i = 0
    j = 0
    k = low

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            nums[k] = L[i];
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        nums[k] = L[i]
        i += 1
        k += 1 
    
    while j < n2:
        nums[k] = L[j]
        j += 1
        k += 1 


def MergeSortUtil(nums: List, low: int, high: int): 
    if low < high:
        mid = low + (high - low)//2
        MergeSortUtil(nums, low, mid)
        MergeSortUtil(nums, mid+1, high)
        merge_sort(nums, low, mid, high)


def MergeSort(nums: List) -> List:
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

    MergeSortUtil(nums, 0, len(nums) - 1)

    return nums

print(MergeSort([5,4,3,2,1]))