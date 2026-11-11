class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1   # target is in the right half
            else:
                r = mid - 1   # target is in the left half

        return -1