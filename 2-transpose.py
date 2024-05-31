
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
def transpose(matrix):
    temp_matrix =[]
    for i in range(len(matrix)):
        temp=[]
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        temp_matrix.append(temp)
    return temp_matrix
print(transpose(matrix))