#Tạo matrix theo đề
row = int(input())
matrix = []
for i in range(row):
  matrix.append([i for i in input()])
#print(matrix)

#Xem thử cách lấy hàng cột kiểu mới thấy lần đầu :))
row = len(matrix)
col = len(matrix[0])
#print(row,col)

#Các thể loại dictionaries
# left, right, up, down
DIRECTION = {
             'l': (0, -1),
             'r': (0, 1),
             'u': (-1, 0),
             'd': (1, 0)
            }
# Các thể loại ống kết nối : chuyển hướng tương ứng
FLOW = {
    #Phải -> ống 2: hướng Phải, ống 3: hướng Xuống, ống 6: hướng Lên, ống 7: hướng Phải
        'l': {'2': 'l', '3': 'd', '6': 'u', '7': 'l'},
    #Trái -> 
        'r': {'2': 'r', '4': 'd', '5': 'u', '7': 'r'},
    #Xuống ->
        'd': {'1': 'd', '5': 'l', '6': 'r', '7': 'd'},
    #Lên ->
        'u': {'1': 'u', '3': 'r', '4': 'l', '7': 'u'}
       }

# Hàm vô danh -> kiểm tra vị trí x, y tồn tại trong matrix 
_IN_RANGE = lambda x, y, matrix: 0<=x<len(matrix) and 0<=y<len(matrix[0])

def find_starting_points(matrix):
  starts = []
  pos = {}
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if 'a'<=matrix[i][j]<='z':
        starts.append(matrix[i][j])
        #dictionaries chữ thường có trong matrix và input vị trí tương ứng
        pos[matrix[i][j]] = [i,j]
  return starts, pos

#Kiểm tra tính liền mạch của ống nước
def follow_flow(flow, current_path, matrix, end, final_path):
    x, y = [x+y for x,y in zip(current_path[-1], DIRECTION[flow])]
    #print(x, y,current_path[-1], DIRECTION[flow])
    #Trường hợp đến được bể nước tương ứng
    if _IN_RANGE(x, y, matrix) and matrix[x][y] == end:
        final_path.append(current_path + [''])
    #Trường hợp ống phù hợp và dòng chảy tiếp tục
    elif _IN_RANGE(x, y, matrix) and matrix[x][y] in FLOW[flow]:
        return follow_flow(FLOW[flow][matrix[x][y]], current_path + [[x, y]], matrix, end, final_path)
    #Trường hợp ống không phù hợp và dòng chảy bị đứt đoạn
    else:
        final_path.append(current_path + ['leak'])

    return final_path

def sum_water(total_path):
    final_cells = set()
    #Hàm vô danh -> kiểm tra trong total_path có bị rò rỉ ko
    first_leak = list(map(lambda x: len(x), filter(lambda x: 'leak' in x, total_path)))
    first_leak = 0 if len(first_leak) == 0 else min(first_leak) - 1

    for path in total_path:
        path = path[:-1]
        path = list(map(lambda x: str(x[0]) + ' ' + str(x[1]), path))
        idx = min(first_leak, len(path)) if first_leak else len(path)
        final_cells |= set(path[:idx])

    return len(final_cells) * (-1 if first_leak > 0 else 1)

#Main tại đây

#Tìm chữ thường có trong matrix, và vị trí của chữ thường
starts,pos = find_starting_points(matrix)
#print(starts, pos)

total_path = []
for item in starts:
  #Lấy chữ in hoa
  end = item.upper()
  #print(end)
  #Một chữ xét 4 trường hợp l,r,d,u
  for di in DIRECTION:
    #Lấy vị trí của chữ + vị trí hướng l,r,u,d -> vị trí x,y hướng l,r,u,d của chữ
    #print(pos[item], DIRECTION[di])
    x, y = [x+y for x,y in zip(pos[item], DIRECTION[di])]
    #print(di)
    #print(x,y)
    #Kiểm tra nếu vị trí x,y tồn tại trong matrix và loại ống của vị trí x,y phù hợp với dòng chảy:
    if _IN_RANGE(x, y, matrix) and matrix[x][y] in FLOW[di]:
      total_path += follow_flow(FLOW[di][matrix[x][y]], [[x, y]], matrix, end, [])

print(sum_water(total_path))