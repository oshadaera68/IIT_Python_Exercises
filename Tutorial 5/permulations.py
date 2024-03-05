letters = ['A', 'B', 'C']

for i in range(3):
    for j in range(3):
        if i != j:
            for k in range(3):
                if k != i and k != j:
                    permutation = [letters[i], letters[j], letters[k]]
                    print("".join(permutation))
