def is_isomorphic(a, b):
    # mapping of each character in a to b
    m = {}
    # mapping of each character in b to a
    r = {}
    for i, c in enumerate(a):
        if c in m:
            if b[i] != m[c]:
                return False
        else:
            m[c] = b[i]
        if b[i] in r:
            if c != r[b[i]]:
                return False
        else:
            r[b[i]] = c
    return True


# Running the Question:

print(is_isomorphic('egg', 'add'))
print(is_isomorphic('foo', 'bar'))
print(is_isomorphic('paper', 'title'))
print(is_isomorphic('paper', 'tttle'))
