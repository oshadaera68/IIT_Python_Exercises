n = 5
magic_square = [[0 for _ in range(n)] for _ in range(n)]

num = 1
i, j = 0, n // 2

while num <= n * n:
    magic_square[i][j] = num
    num += 1
    i -= 1
    j += 1
    if i == -1 and j == n:
        i, j = 1, n - 1
    elif i == -1:
        i = n - 1
    elif j == n:
        j = 0
    elif magic_square[i][j] != 0:
        i += 2
        j -= 1

print("Magic Square of size 5x5:")
for row in magic_square:
    for num in row:
        print(num, end="\t")
    print()
