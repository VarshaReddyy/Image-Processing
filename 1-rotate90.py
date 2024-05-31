matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
temp_matrix =[]
for c in range(len(matrix)):
    temp=[]
    for r in range(len(matrix)-1,-1,-1):
        temp.append(matrix[r][c])
    temp_matrix.append(temp)
print(temp_matrix)
