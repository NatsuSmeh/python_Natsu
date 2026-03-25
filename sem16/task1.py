s = input().split()
numb = [int(s[i]) for i in range(len(s))]

def is_zero(num: int) -> bool:
    if num == 0:
        return True
    else:
        return False
    
def count_zeros(numbers: list) -> int:
    count = 0
    for i in numbers:
        if is_zero(int(i)):
            count += 1
    return count


def count_non_zeros(numbers: list) -> int:
    counter = 0
    for i in numbers:
        if is_zero(int(i)) == False:
            counter += 1
    return counter

print(count_zeros(s))
print(count_non_zeros(s))