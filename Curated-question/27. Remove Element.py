'''
### question:
Given an integer array 'nums' and an integer 'val', remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''
'''
# 解題說明
* 目標：給定 nums 整數 array，val 整數，移除所有目標值，回傳剩下多少個元素。
* 處理策略：double pointer (slow & fast)
'''
# 答案
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow]=nums[fast]
                slow += 1
        return slow

'''
迴圈流程說明：
[0,1,3,4,3], val= 3
round 1：fast=0, nums[fast]=0, slow=0, nums[slow]=0
滿足if nums[fast] != val(0!=3)，所以nums[slow]=nums[fast]，因此nums[slow]=0（有被覆蓋，但和原本一樣）
結果：第一個數確認非val，slow += 1，slow=1
[0,1,3,4,3]

round 2：fast=1, nums[fast]=1, slow=1, nums[slow]=1
滿足if nums[fast] != val(1!=3)，所以nums[slow]=nums[fast]，因此nums[slow]=1（有被覆蓋，但和原本一樣）
結果：第二個數確認非val，slow += 1，slow=2
[0,1,3,4,3]

round 3：fast=2, nums[fast]=3, slow=2, nums[slow]=3
不符合if nums[fast] != val(3=3)，所以slow 不會 +1
結果：第三個數查找完畢，目前slow仍為2
[0,1,3,4,3]

round 4：fast=3, nums[fast]=4, slow=2, nums[slow]=3
滿足if nums[fast] != val(4!=3)，所以nums[slow]=nums[fast]，因此nums[slow]=4(原本為3，現在被覆蓋成4)
結果：第四個數確認非val，slow += 1，slow=3
[0,1,4,4,3]

round 5：fast=4, nums[fast]=3, slow=3, nums[slow]=4
不符合if nums[fast] != val(3=3)，所以slow 不會 +1
結果：第五個數查找完畢，本回合slow未+1，目前slow為3

[0,1,4,4,3]
       ↑
slow = 3
         ↑
    fast = 4
結果，因爲我們只是要找出[0,1,3,4,3]裡面有幾個非3的數字，所以有三個，且是「前面三個數字」，也就是[[0,1,4,4,3]的[0,1,4]，後面4,3是用不到的，就不用管了。

'''


