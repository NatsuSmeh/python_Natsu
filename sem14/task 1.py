st = input()
nums = st.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])


def is_positive(num: int) -> int:
    if nums[i] >= 0:
        return True

def count_positive(nums: list) -> int:
    if is_positive(nums[i]):
        count_positive += 1
        return 0

def count_negative(nums: list) -> int:
    if nums[i] < 0:
        count_negative += 1
        return 0

print(f'Кол-во положительных чисел {count_positive(nums)}')
print(f'Кол-во отрицательных чисел {count_negative(nums)}')