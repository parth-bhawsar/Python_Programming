matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

i = 0

while i < 3:
    j = 0

    while j < 3:
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        j += 1

    i += 1



i = 0

while i < 3:
    j = 0

    while j < 3:
        print(matrix[i][j], end=" ")
        j += 1

    print()
    i += 1