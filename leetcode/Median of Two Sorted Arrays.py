'''num1 = [1,3]
num2 = [2,7]
cumbined = num1 + num2
sorted_num = sorted(cumbined)
sum_num = 0
for j in sorted_num:
    sum_num = sum_num + j
    avg = sum_num / len(sorted_num)
print(sorted_num)
print(sum_num)
print(len(sorted_num))
print(avg)
'''


'''a = [1,2,3,4]
sum_num = 0
for i in a :
    sum_num = sum_num + i
    avg = sum_num/len(a)
print(sum_num)
print(avg)
'''
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        cumbined = nums1 + nums2 
        sum_num = 0
        sorted_num = sorted(cumbined)
        for j in sorted_num:
            sum_num = sum_num + j
            avg = sum_num / len(sorted_num)
        return avg'''

"""4. Median of Two Sorted Arrays
Hard
24.3K
2.7K
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5."""
'''num1 = [1, 3]
num2 = [2, 7]
combined_nums = num1 + num2
sorted_nums = sorted(combined_nums)
sum_nums = sum(sorted_nums)
avg = sum_nums / len(sorted_nums)

print("Sorted list:", sorted_nums)
print("Sum:", sum_nums)
print("Length:", len(sorted_nums))
print("Average:", avg)'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = nums1 + nums2
        sorted_nums = sorted(combined)
        length = len(sorted_nums)

        if length % 2 == 0:
            mid1 = sorted_nums[length // 2 - 1]
            mid2 = sorted_nums[length // 2]
            median = (mid1 + mid2) / 2
        else:
            median = sorted_nums[length // 2]

        return median