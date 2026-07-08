nums = [1, 2, 3, 4, 5]
target = 10

def two_sum(nums, target):
    seen = {}
    for i in range(len(nums) - 1):
        complement = target - nums[i]
        if complement in seen:
            return (complement, nums[i])
        seen[nums[i]] = i
    raise ValueError("No two sum solution found")

print(two_sum(nums, target))
