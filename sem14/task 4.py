def hackers_func(hackers: list, security_level: int, increase: int) -> int:
    count = 0
    for i in hackers:
        if i > security_level:
            count += 1
        elif i <= security_level:
            security_level += increase
    
    return count

print(hackers_func([4, 15, 1, 6, 28], 3, 1))