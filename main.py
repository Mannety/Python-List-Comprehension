'''
List Comprehension
'''
# squares = []
# for x in range(10):
#     squares.append(x ** 2)
# print(squares)

# with list Comprehension
# squares = [ x ** 2 for x in range(10)]
# print(squares)

'''
Conditionals in List Comprehension
'''
# Combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             Combs.append((x,y))
# print(Combs)

#  with list comprehensition
# combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(Combs)

'''
Nested list Comprehension
'''

# matrix = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12],
# ]

# [[1,5,9],[2,6,10], [3,7,11],[4,8,12]]
# res = [[row[i] for row in matrix] for i in range(4)]
# print(res)

# =======================

# matrix = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12],
# ]

# res = []
# for i in range(4):
#   res.append([row[i] for row in matrix])

# [[1,5,9],[2,6,10], [3,7,11],[4,8,12]]
# print(res)

# =====================

# matrix = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12],
# ]

# res = []
# for i in range(4):
#     res_row = []
#     for row in matrix:
#         res_row.append(row[i])
#     res.append(res_row)

# [[1,5,9],[2,6,10], [3,7,11],[4,8,12]]
# print(res)

# =======================

# matrix = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12],
# ]

# res = list(zip(*matrix))
# [[1,5,9],[2,6,10], [3,7,11],[4,8,12]]
# print(res)