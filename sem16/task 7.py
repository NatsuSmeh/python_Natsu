def proverka(st: list):
    for i in st:
        if i < 0:
            st.remove(i)
    return st

print(proverka([17, 45, -69, 7, 3]))