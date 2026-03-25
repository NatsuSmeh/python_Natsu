spl = input().split(",")
res = [int(spl([i])) for i in range(len(spl))]
    
def solve(nums: list) -> int:
    if not validate(nums):
        return "invalid input"
    for i in range(len(nums)):
        if nums[i] + 1 != nums[i+1]:
            return "unexpected error"

def validate(nums: list) -> bool:
    if len(nums) != 3:
        return False
    for i in nums:
        if not isinstance(i, int):
            return False
        
    return sum(nums)

print(solve())