# System of Linear Equations

    General form or represetation of System of Linear Equations:
         _                                                  _
        | (a11)x1 + (a12)x2 + (a13)x3 + .......... + (a1n)xn |
        | (a21)x1 + (a22)x2 + (a23)x3 + .......... + (a2n)xn |
        |  |     |     |         |                      |    |                   
        |  |     |     |         |                      |    |            = b
        |  |     |     |         |                      |    |
        | (am1)x1 + (am2)x2 + (am3)x3 + .......... + (amn)xn |
        |_                                                  _|  

        where,
            (a11, a21, ..... amn)  -> coefficients,
            (x1, x2, x3, .... xn)  -> independent variables,
            b -> constant or scalar.



    Augemented Matrix (Ax = B):

    System of Linear Equations can be represented in a matrix form. This matrix is called Augmented Matrix.
                        A                  x          B
         _                            _   _  _       _  _
        | a11  a12  a13 .......... a1n | | x1 |     | b1 |
        | a21  a22  a22 .......... a2n | | x2 |     | b2 |
        |  |    |    |                 | | .  |     | .  |
        |  |    |    |                 | | .  |  =  | .  |
        |  |    |    |                 | | .  |     | .  |
        | am1  am2  am3 .......... amn | | xn |     | bn |
        |_                            _| |_  _|     |_  _|

        where,
            A  -> coefficient matrix,
            x  -> independent variable matrix,
            b -> constant or scalar matrix.



    There are two types of System of Linear Equations:
        1. Consistent System of Linear Equations: Having 0 or one or more solutions. (No, Unique, Infinite)
        2. Inconsistent System of Linear Equations: Having no solution.

    Note:
    1. If the determinant(Det) of the coefficient matrix is non-zero, then the system of linear equations is consistent.
    2. A system of linear equations is said to be homogeneous if the constant matrix is zero (B = 0).
    3. If the determinant(Det) of the coefficient matrix is zero, then the system of linear equations is inconsistent.
    4. A system of linear equations is said to be non-homogeneous if the constant matrix is non-zero (B != 0).
    4. If the system of linear equations is consistent, then it may have unique, infinite or no solution.
    5. If the system of linear equations is inconsistent, then it has no solution.



    Methods to solve System of Linear Equations:
    The followinf methods are used to solve the system of linear equations and only applicable for 
    consistent system of linear equations and coefficient matrix has to be non-singular |A| != 0 :
        1. Cramer's Rule.
        2. Matrix Inversion Method.
        3. Gauss Elimination Method (Row-Echelon Form).
        4. Gauss-Jordan Elimination Method.
        5. LU Decomposition Method (or) Method of Triangularisation.



Trace of a Matrix Tr(A) :
    The trace of a square matrix A is the sum of the elements on the main diagonal of the matrix.
    
    Tr(A) = a11 + a22 + a33 + ....... + ann.
    Properties of Trace:
        - Tr(A + B) = Tr(A) + Tr(B)
        - Tr(A - B) = Tr(A) - Tr(B)
        - Tr(AB) = Tr(BA)
        - Tr(ABC) = Tr(BCA) = Tr(CAB)
        - Tr(k x A) = k x Tr(A)
        - Tr(AB) != Tr(BA)

- Program for [Tr(A)](Trace-Of-Matrix.py).



Matrices:

    - Determinants are only calculated for Square Matrices.
    - For nXn matrix, the max no of terms after expansion is n!.

Different types of Matrices:

        1. Principal Diagonal Matrix: Let A[aij]m/n and aij = 0 for all i != j.
        2. Upper Triangular Matrix: Let A[aij]m/n where aij = 0 for all i > j.  (or) aij = aji = 0 where i > j.
        3. Lower Triangular Matrix: Let A[aij]m/n where aij = 0 for all i < j.  (or) aij = aji = 0 where i < j.
        4. Scalar Matrix : Let A[aij] where for all i > j and i < j aij = 0 and for all i = j, aij = k.
        5. Unit Matrix (or) Identity Matrix (I): Let A[aij] where aij = 0 for all i > j and i < j and for all i = j, aij = 1.
        6. Transpose of Matrix: Let A[aij] where for aij = aji.
          Properties of Transpose of a Matrix:
                - (A^T)^T = A
                - (A + || - B)^T = (A^T) + || - (B^T)
                - (AB)^T = (B^T)(A^T)
        7. Symmetric Matrix: Let A[aij] where aij == aji (or) { (A^T) = A }. 

    Minors, Cofactors and Adjoint of a Matrix:
        Minor of Matrix (Mij):
            - Let A[aij] where Determinent of aij or (|aij|) = Mij.
        Cofactor of a matrix (Aij): 
            - Let A[aij] where (-1)^(i+j) * Mij = Aij.
        Adjoint of a Matrix (adj(A)):
            - Let A[aij] where Transpose of Cofactor matric (Aij)^T = adj(A).



Inverse of a Matrix (A^(-1)):
   
    Let A[aij] where { A^(-1) } = adj(A) / |A|.

System of Linear equations in one variable (ax = b):

    To find solutions for x:
    X = A^(-1) * B