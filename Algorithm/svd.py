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

        # if iterations == 20:
        if abs(np.dot(currentV, lastV)) > 1 - epsilon:
#             print("converged in {} iterations!".format(iterations))
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



# def simultaneous_power_iteration(A, k):
#     n, m = A.shape
#     Q = np.random.rand(n, k)
#     Q, _ = np.linalg.qr(Q)
#     Q_prev = Q
 
#     for i in range(1000):
#         Z = A.dot(Q)
#         Q, R = np.linalg.qr(Z)

#         # can use other stopping criteria as well 
#         err = ((Q - Q_prev) ** 2).sum()
#         if i % 10 == 0:
#             print(i, err)

#         Q_prev = Q
#         if err < 1e-3:
#             break

#     return np.diag(R), Q

# def svd_test(A, k):
#     V = np.dot(A.T, A)
#     eigenVal, eigenVec = simultaneous_power_iteration(V, k)

#     singularVal = 

