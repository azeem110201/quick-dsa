from typing import List

def LinearSearch(nums: List, key: (int, float)):
    '''
     Functions takes in two arguments that is the array and key and returns the index and bool value.
     If present the bool is True otherwise False. If the index is present, then functions return index of that
     key and True and if not it returns -1 with False value
    '''

    if not isinstance(nums, list):
        raise Exception("Array should be of type list")
        return

    if not isinstance(key, (int, float)):
        raise Exception("key value passed should be and integer or float")
        return

    if len(nums) == 0:
        raise Exception("Array of length zero is passed") 

    for i in range(len(nums)):
        if nums[i] == key:
            return i, True

    return -1, False