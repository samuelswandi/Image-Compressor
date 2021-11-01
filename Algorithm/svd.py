import numpy as np
import sympy as sym
# from sympy import symbols, Matrix, Symbol, Poly

def eigenValues(m):
    # KAMUS LOKAL
    eigenSymbol = sym.Symbol('l')
    n = m.shape[0]
    
    # ALGORITMA
    # Create the eigenIdentity Matrix with 'l' as variable
    eigenIdentity = np.array([[eigenSymbol for j in range(n)] for i in range(n)])

    for i in range(n):
        for j in range(n):
            if (i != j):
                eigenIdentity[i][j] = 0

    # Find the determinant of the matrix
    eigenSubstract = eigenIdentity - m
    eigenSubstract = sym.Matrix(eigenSubstract)
    eigenDet = eigenSubstract.det()

    #Find the coeffs
    eigenCoeff = sym.Poly(eigenDet, eigenSymbol)
    eigenCoeff = eigenCoeff.all_coeffs()

    #Find the root
    eigenRoot = np.roots(eigenCoeff)
    eigenRoot.sort()
    eigenRoot = eigenRoot[::-1]

    # print(eigenDet)
    # print(eigenCoeff)
    print(eigenRoot)

    return eigenRoot


def matrixU(m):
    # KAMUS LOKAL
    # Find the eigen values of M x M^T
    matrT = m.transpose()
    matrMult = np.dot(m, matrT)
    eigenVal = eigenValues(matrMult)

    #Create Matrix U
    n = matrMult.shape[0]
    matrU = [[0 for j in range(n)] for i in range(n)]

    #Create Matrix l x I for substitute with eigen values
    eigenSymbol = sym.Symbol('l')
    matrEigen = [[eigenSymbol for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i != j):
                matrEigen[i][j] = 0

    #Create Matrix (l x I) - (M x M^T)
    matrSubstract = matrEigen - matrMult

    # Create Matrix B for solving linalg Ax = B
    matrB = np.array([0 for i in range(n)], dtype='float')
    
    #ALGORITMA
    # Subs matrSubstract with eigenVal
    for i in range(eigenVal.shape[0]):
        matrTemp = sym.Matrix(matrSubstract)
        matrTemp = matrTemp.subs(eigenSymbol, eigenVal[i])
        matrTemp = np.array(matrTemp, dtype='float')
        
        # solve Ax = B
        a = matrTemp
        b = matrB
        num_equations, num_variables = a.shape
        x = sym.symarray('x', num_variables)
        solution = sym.solve([sym.Eq(ax-b, 0) for ax, b in zip(np.dot(a, x), b)])
        
        # for key in solution:
        #     if (type(k)
        print(solution)

    
# arr = np.array([1,2,3])
matr = np.array([[3,1,1], [-1,3,1]])
# print(arr.shape[0])
matrixU(matr)