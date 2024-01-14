class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1
            while right > left:
                if nums[i]+nums[left]+nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left+1 < right and nums[left] == nums[left+1]:
                        left += 1
                    while right-1 > left and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i]+nums[left]+nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return ans