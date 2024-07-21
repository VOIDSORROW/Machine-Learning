def trace(A):
    result = 0
    for i in range(3):
        result += A[i][i]
    return result

if __name__ == '__main__':
    print("_____Trace of a Matrix A_____")
    A = [[1,2,3],[4,5,6],[7,8,9]]
    trace_of_A = trace(A)
    print("Trace of first 9 numbers in a 3x3 matrix is:",trace_of_A)
    print(len(A))
    
__name__

