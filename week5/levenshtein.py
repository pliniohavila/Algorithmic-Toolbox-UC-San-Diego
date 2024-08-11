
def printTable(table):
  n = len(table)
  for i in range(0, n):
    print(table[i])


def levenshtein(str1, str2):
  m = len(str1) + 1
  n = len(str2) + 1
  matrix = [[0 for _ in range(0, n)] for _ in range(0, m)]

  for i in range(0, m):
    matrix[i][0] = i
  for j in range(0, n):
    matrix[0][j] = j

  for i in range(1, m):
    for j in range(1, n):
      cost = 0 if str1[i - 1] == str2[j - 1] else 1
      matrix[i][j] = min(
        matrix[i-1][j-1] + cost,  # Substituição
        matrix[i-1][j] + 1,       # Remoção 
        matrix[i][j-1] + 1        # Inserção
      )
  print(matrix[m-1][n-1])


if __name__ == '__main__':
  levenshtein("kitten","sitting")
