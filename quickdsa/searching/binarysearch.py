from typing import List

def checkSorted(nums: List) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return False

    return True        

def BinarySearch(nums: List, key: (int, float)):
    '''
     Functions takes in two arguments that is the array and key and returns bool value.
     If present the bool is True otherwise False. 
    '''

    if not isinstance(nums, list):
        raise Exception("Array should be of type list")
        return

    if not isinstance(key, (int, float)):
        raise Exception("key value passed should be and integer or float")
        return    

    if len(nums) == 0:
        raise Exception("Array of length zero is passed")

    flag = checkSorted(nums)     

    if flag == False:
        nums.sort()

    print(nums)    

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low)//2

        if nums[mid] == key:
            return True
        elif nums[mid] > key:
            high = mid - 1
        else:
            low = mid + 1     

    return False  