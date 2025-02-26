#The following function is inefficient. Optimize it for better performance.

'''
def find_duplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and nums[i] not in duplicates:
                duplicates.append(nums[i])
    return duplicates

print(find_duplicates("564654433"))

'''

# Optimized version of code
# Time Complexity of the code is now O(n) which was O(n^2)

from collections import Counter
def find_duplicates(nums):
    data = dict(Counter(nums))
    return [key for key, value in data.items() if value > 1]


print(find_duplicates("65431354.035"))