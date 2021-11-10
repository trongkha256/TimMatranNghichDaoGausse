import copy
import math


def in_Put(A, m, n):
    for i in range(0, m):
        for j in range(0, n):
            print("A[", i, "][", j, "]: ")
            A[i][j] = int(input())


def Tao_Ma_Tran_Don_Vi(A):
    C = copy.deepcopy(A)
    n = len(A)
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                C[i][j] = 1
            else:
                C[i][j] = 0
    return C


def Is_Bang(A, B):
    n = len(A)
    for i in range(0, n):
        for j in range(0, n):
            if A[i][j] != B[i][j]:
                return False
    return True


def Mul(A, B):
    n = len(A)
    C = []
    for i in range(0, n):
        C.append([])
        for j in range(0, n):
            C[i].append(0)
    for i in range(0, n):
        for j in range(0, n):
            C[i][j]=0
            for k in range(0, n):
                C[i][j]+=A[i][k]*B[k][j]

    return C



def row_switch(A, x, y):
    for i in range(len(A[0])):
        tmp = A[x][i]
        A[x][i] = A[y][i]
        A[y][i] = tmp


def is_zero(n):
    if n == 0:
        return 1
    return 0


def row_mul(A, x, n):
    for i in range(len(A[0])):
        A[x][i] *= n


def row_add(A, x1, x2, n):
    for i in range(len(A[0])):
        A[x1][i] += A[x2][i] * n


def Tim_Ma_Tran_Nghich_Dao(A):
    R = copy.deepcopy(A)
    C=Tao_Ma_Tran_Don_Vi(A)
    Z = Tao_Ma_Tran_Don_Vi(A)
    m, n = len(R), len(R[0])
    row = col = 0
    while row < m:
        while col < n and all(is_zero(R[i][col]) for i in range(row, m)):
            col += 1
        if col == n: break
        pivot_row = row + [is_zero(R[i][col]) for i in range(row, m)].index(False)
        row_switch(R, row, pivot_row)
        row_switch(Z, row, pivot_row)
        t = 1 / R[row][col]
        row_mul(R, row, 1 / R[row][col])
        row_mul(Z, row, t)
        for i in range(row + 1, m):
            t2 = -R[i][col]
            row_add(R, i, row, -R[i][col])
            row_add(Z, i, row, t2)
        row += 1
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            t3 = -R[i][j]
            row_add(R, i, j, -R[i][j])
            row_add(Z, i, j, t3)
    if Is_Bang(C,Mul(Z,A)) == False:
        return False
    return Z


d = input("Nhap so dong: ")
c = input("Nhap so cot: ")
m = int(d)
n = int(c)
A = []
for i in range(0, m):
    A.append([])
    for j in range(0, n):
        A[i].append(0)
in_Put(A, m, n)
if m==n  and Tim_Ma_Tran_Nghich_Dao(A) is not False:
    print("Ma Tran Nghich dao cua A la: \n",Tim_Ma_Tran_Nghich_Dao(A))
else:
    print("Khong co ma tran nghich dao cua A")