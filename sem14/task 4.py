def hackers_func(hackers: list, security_level: int, increase: int) -> int:
    count = 0
    for i in hackers:
        if i > security_level:
            count += 1
        elif i <= security_level:
            security_level += increase
    
    return count

print(hackers_func([1, 2, 3, 4, 5], 3, 1))