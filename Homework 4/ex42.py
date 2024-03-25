def reverse_range_iterative(L, start, end):
    for i in range((end - start) // 2):
        L[start + i], L[end - i] = L[end - i], L[start + i]


def reverse_range_recursive(L, start, end):
    if start >= end:
        return
    L[start], L[end] = L[end], L[start]
    reverse_range_recursive(L, start + 1, end - 1)

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(L)
reverse_range_iterative(L, 3, 6)
print(L)
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_range_recursive(L, 3, 6)
print(L)
