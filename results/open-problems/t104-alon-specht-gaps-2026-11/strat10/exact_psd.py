"""PROVED: rational symmetric elimination for positive semidefiniteness."""
import sympy as S

def psd(matrix):
    m=S.MutableDenseMatrix(matrix)
    assert m==m.T
    while m.rows:
        pivot=m[0,0]
        if pivot<0:return False
        if pivot==0:
            if any(m[0,j]!=0 for j in range(1,m.cols)):return False
            m=m[1:,1:]
        else:m=m[1:,1:]-(m[1:,0]*m[0,1:])/pivot
    return True
