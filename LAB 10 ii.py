matrix=input('Enter Matrix: ')
def sort_matrix(mat):
    evaluation=eval(mat)
    evaluation.sort(key=sum,reverse=True)
    print("Sorted Matrix: ",evaluation)
sort_matrix(matrix)
