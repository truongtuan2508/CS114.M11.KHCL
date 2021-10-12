arr_color = [i for i in input().split()]
while True:
  lst = [i for i in input().split()]
  if lst[0] == '.':
    break
  else:
    list_act = lst

matrix = []
for i in arr_color:
  lst_temp = []
  for j in range(0,9):
    lst_temp.append(i)
  matrix.append(lst_temp)


def switch_1U(matrix,i):
  temp = matrix[0][0]
  matrix[0][0] = matrix[3][8]
  matrix[3][8] = matrix[2][4]
  matrix[2][4] = temp



for i in list_act[::-1]:
  if i == "U":
    temp = matrix[0][0]
    matrix[0][0] = matrix[3][8]
    matrix[3][8] = matrix[2][4]
    matrix[2][4] = temp
  elif i == "U'":
    temp = matrix[0][0]
    matrix[0][0] = matrix[2][4]
    matrix[2][4] = matrix[3][8]
    matrix[3][8] = temp
  elif i == "u":
    temp_0 = matrix[0][0]
    matrix[0][0] = matrix[3][8]
    matrix[3][8] = matrix[2][4]
    matrix[2][4] = temp_0

    temp_1 = matrix[0][1]
    matrix[0][1] = matrix[3][3]
    matrix[3][3] = matrix[2][6]
    matrix[2][6] = temp_1

    temp_2 = matrix[0][2]
    matrix[0][2] = matrix[3][7]
    matrix[3][7] = matrix[2][5]
    matrix[2][5] = temp_2

    temp_3 = matrix[0][3]
    matrix[0][3] = matrix[3][6]
    matrix[3][6] = matrix[2][1]
    matrix[2][1] = temp_3
  elif i == "u'":
    temp_0 = matrix[0][0]
    matrix[0][0] = matrix[2][4]
    matrix[2][4] = matrix[3][8]
    matrix[3][8] = temp_0

    temp_1 = matrix[0][1]
    matrix[0][1] = matrix[2][6]
    matrix[2][6] = matrix[3][3]
    matrix[3][3] = temp_1

    temp_2 = matrix[0][2]
    matrix[0][2] = matrix[2][5]
    matrix[2][5] = matrix[3][7]
    matrix[3][7] = temp_2

    temp_3 = matrix[0][3]
    matrix[0][3] = matrix[2][1]
    matrix[2][1] = matrix[3][6]
    matrix[3][6] = temp_3
  elif i == "B":
    temp = matrix[1][0]
    matrix[1][0] = matrix[2][8]
    matrix[2][8] = matrix[3][4]
    matrix[3][4] = temp
  elif i == "B'":
    temp = matrix[1][0]
    matrix[1][0] = matrix[3][4]
    matrix[3][4] = matrix[2][8]
    matrix[2][8] = temp
  elif i == "b":
    temp_0 = matrix[1][0]
    matrix[1][0] = matrix[2][8]
    matrix[2][8] = matrix[3][4]
    matrix[3][4] = temp_0

    temp_1 = matrix[1][1]
    matrix[1][1] = matrix[2][3]
    matrix[2][3] = matrix[3][6]
    matrix[3][6] = temp_1

    temp_2 = matrix[1][2]
    matrix[1][2] = matrix[2][7]
    matrix[2][7] = matrix[3][5]
    matrix[3][5] = temp_2

    temp_3 = matrix[1][3]
    matrix[1][3] = matrix[2][6]
    matrix[2][6] = matrix[3][1]
    matrix[3][1] = temp_3
  elif i == "b'":
    temp_0 = matrix[1][0]
    matrix[1][0] = matrix[3][4]
    matrix[3][4] = matrix[2][8]
    matrix[2][8] = temp_0

    temp_1 = matrix[1][1]
    matrix[1][1] = matrix[3][6]
    matrix[3][6] = matrix[2][3]
    matrix[2][3] = temp_1

    temp_2 = matrix[1][2]
    matrix[1][2] = matrix[3][5]
    matrix[3][5] = matrix[2][7]
    matrix[2][7] = temp_2

    temp_3 = matrix[1][3]
    matrix[1][3] = matrix[3][1]
    matrix[3][1] = matrix[2][6]
    matrix[2][6] = temp_3
  elif i == "L":
    temp = matrix[2][0]
    matrix[2][0] = matrix[1][8]
    matrix[1][8] = matrix[0][4]
    matrix[0][4] = temp
  elif i == "L'":
    temp = matrix[2][0]
    matrix[2][0] = matrix[0][4]
    matrix[0][4] = matrix[1][8]
    matrix[1][8] = temp
  elif i == "l":
    temp_0 = matrix[2][0]
    matrix[2][0] = matrix[1][8]
    matrix[1][8] = matrix[0][4]
    matrix[0][4] = temp_0

    temp_1 = matrix[2][1]
    matrix[2][1] = matrix[1][3]
    matrix[1][3] = matrix[0][6]
    matrix[0][6] = temp_1

    temp_2 = matrix[2][2]
    matrix[2][2] = matrix[1][7]
    matrix[1][7] = matrix[0][5]
    matrix[0][5] = temp_2

    temp_3 = matrix[2][3]
    matrix[2][3] = matrix[1][6]
    matrix[1][6] = matrix[0][1]
    matrix[0][1] = temp_3
  elif i == "l'":
    temp_0 = matrix[2][0]
    matrix[2][0] = matrix[0][4]
    matrix[0][4] = matrix[1][8]
    matrix[1][8] = temp_0

    temp_1 = matrix[2][1]
    matrix[2][1] = matrix[0][6]
    matrix[0][6] = matrix[1][3]
    matrix[1][3] = temp_1

    temp_2 = matrix[2][2]
    matrix[2][2] = matrix[0][5]
    matrix[0][5] = matrix[1][7]
    matrix[1][7] = temp_2

    temp_3 = matrix[2][3]
    matrix[2][3] = matrix[0][1]
    matrix[0][1] = matrix[1][6]
    matrix[1][6] = temp_3
  elif i == "R":
    temp = matrix[3][0]
    matrix[3][0] = matrix[0][8]
    matrix[0][8] = matrix[1][4]
    matrix[1][4] = temp
  elif i == "R'":
    temp = matrix[3][0]
    matrix[3][0] = matrix[1][4]
    matrix[1][4] = matrix[0][8]
    matrix[0][8] = temp
  elif i == "r":
    temp_0 = matrix[3][0]
    matrix[3][0] = matrix[0][8]
    matrix[0][8] = matrix[1][4]
    matrix[1][4] = temp_0

    temp_1 = matrix[3][1]
    matrix[3][1] = matrix[0][3]
    matrix[0][3] = matrix[1][6]
    matrix[1][6] = temp_1

    temp_2 = matrix[3][2]
    matrix[3][2] = matrix[0][7]
    matrix[0][7] = matrix[1][5]
    matrix[1][5] = temp_2

    temp_3 = matrix[3][3]
    matrix[3][3] = matrix[0][6]
    matrix[0][6] = matrix[1][1]
    matrix[1][1] = temp_3
  elif i == "r'":
    temp_0 = matrix[3][0]
    matrix[3][0] = matrix[1][4]
    matrix[1][4] = matrix[0][8]
    matrix[0][8] = temp_0

    temp_1 = matrix[3][1]
    matrix[3][1] = matrix[1][6]
    matrix[1][6] = matrix[0][3]
    matrix[0][3] = temp_1

    temp_2 = matrix[3][2]
    matrix[3][2] = matrix[1][5]
    matrix[1][5] = matrix[0][7]
    matrix[0][7] = temp_2

    temp_3 = matrix[3][3]
    matrix[3][3] = matrix[1][1]
    matrix[1][1] = matrix[0][6]
    matrix[0][6] = temp_3
  else:
    break

for i in range(0,4):
  for j in range(0,9):
    print(matrix[i][j], end =" ")
  print()