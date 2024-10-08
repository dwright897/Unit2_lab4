# There is no need to import SAMPLE_MATRICES
# Dalton Wright
# 10/07/24
# Matrix Arithmetic


def mat_sum(m1, m2):
  if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
    height = len(m1)
    width = len(m1[0])
    results = [[0]*width for _ in range(height)]

    for row in range(height):
      for column in range(width):
        results[row][column] = m1[row][column] + m2[row][column]
    
  else:
    results = ("no solution")
  return results


def mat_mul(m1, m2):
  if len(m1[0]) == len(m2):
    height = len(m1)
    width = len(m2[0])
    width2 = len(m2)

    results = [[0]*width for _ in range(height)]

    for row in range(height):
      for column in range(width):
        for item in range(width2):
          results[row][column] += m1[row][item] * m2[item][column]
  else: 
    results = ("no solution")
    
  return results


