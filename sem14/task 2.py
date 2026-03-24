def solve(st: str) -> str:
    result = ""
    upper = [i for i in range(len(st)) if st[i].isupper()]
    lower = [i for i in range(len(st)) if st[i].islower()]

    if len(upper) > len(lower):
        for i in range(st):
            if i not in upper:
                result += st[i].upper
            else:
                result += st[i]

    elif len(lower) > len(upper):
        for i in range(st):
            if i not in lower:
                result += st[i].lower
            else:
                result += s[i]

    else:
        return st.lower()
    
    return result

print(solve("CODe"))
print(solve("coDE"))
print(solve("codE"))