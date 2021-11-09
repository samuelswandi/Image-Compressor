from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
# from svd import *

img = Image.open("algorithm/image.png")
np_img = np.array(img)
np_img = np_img[:10,:10, 0]

# print(np_img.shape)
# print(eigenValues(np_img[:15, :15, 0]))
# plt.imshow(img)
# plt.show()

# ***************************************************************************************************************************************
import numpy as np
from numpy.linalg import norm

from random import normalvariate
from math import sqrt


def randomUnitVector(n):
    unnormalized = [normalvariate(0, 1) for _ in range(n)]
    theNorm = sqrt(sum(x * x for x in unnormalized))
    return [x / theNorm for x in unnormalized]


def svd_1d(A, epsilon=1e-10):
    ''' The one-dimensional SVD '''

    n, m = A.shape
    x = randomUnitVector(min(n,m))
    lastV = None
    currentV = x

    if n > m:
        B = np.dot(A.T, A)
    else:
        B = np.dot(A, A.T)

    iterations = 0
    while True:
        iterations += 1
        lastV = currentV
        currentV = np.dot(B, lastV)
        currentV = currentV / norm(currentV)

        if abs(np.dot(currentV, lastV)) > 1 - epsilon:
            print("converged in {} iterations!".format(iterations))
            return currentV


def svd(A, k=None, epsilon=1e-10):
    '''
        Compute the singular value decomposition of a matrix A
        using the power method. A is the input matrix, and k
        is the number of singular values you wish to compute.
        If k is None, this computes the full-rank decomposition.
    '''
    A = np.array(A, dtype=float)
    n, m = A.shape
    svdSoFar = []
    if k is None:
        k = min(n, m)

    for i in range(k):
        matrixFor1D = A.copy()

        for singularValue, u, v in svdSoFar[:i]:
            matrixFor1D -= singularValue * np.outer(u, v)

        if n > m:
            v = svd_1d(matrixFor1D, epsilon=epsilon)  # next singular vector
            u_unnormalized = np.dot(A, v)
            sigma = norm(u_unnormalized)  # next singular value
            u = u_unnormalized / sigma
        else:
            u = svd_1d(matrixFor1D, epsilon=epsilon)  # next singular vector
            v_unnormalized = np.dot(A.T, u)
            sigma = norm(v_unnormalized)  # next singular value
            v = v_unnormalized / sigma

        svdSoFar.append((sigma, u, v))

    singularValues, us, vs = [np.array(x) for x in zip(*svdSoFar)]
    return singularValues, us.T, vs


if __name__ == "__main__":
    movieRatings = np.array([
        [2, 5, 3],
        [1, 2, 1],
        [4, 1, 1],
        [3, 5, 2],
        [5, 3, 1],
        [4, 5, 5],
        [2, 4, 2],
        [2, 2, 5],
    ], dtype='float64')

    # v1 = svd_1d(movieRatings)
    # print(v1)

    theSVD = svd(np_img)
    print(theSVD[1])
    print(theSVD[2])


import math
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
    print(eigenSubstract)
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
    # print(eigenRoot)

    for i in eigenRoot:
        print(math.sqrt(i))
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
        # print(solution)

    
# arr = np.array([1,2,3])
matr = np.array([[3,1,1], [-1,3,1]])
# print(arr.shape[0])
matrixU(matr)