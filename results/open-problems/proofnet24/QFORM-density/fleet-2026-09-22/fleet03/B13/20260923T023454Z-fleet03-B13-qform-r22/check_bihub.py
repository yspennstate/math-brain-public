from fractions import Fraction
from itertools import combinations
from math import e, sqrt


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def volume_stats(M):
    nr, nc = len(M), len(M[0])
    rows = list(combinations(range(nr),3))
    cols = list(combinations(range(nc),3))
    Z = Fraction(0)
    row_inc = [Fraction(0) for _ in range(nr)]
    col_inc = [Fraction(0) for _ in range(nc)]
    joint = [[Fraction(0) for _ in range(nc)] for _ in range(nr)]
    for S in rows:
        for T in cols:
            a = [[Fraction(M[i][j]) for j in T] for i in S]
            w = det3(a)**2
            Z += w
            for i in S:
                row_inc[i] += w
            for j in T:
                col_inc[j] += w
            for i in S:
                for j in T:
                    joint[i][j] += w
    assert Z > 0
    alpha = [x/Z for x in row_inc]
    beta = [x/Z for x in col_inc]
    return Z, alpha, beta, joint


def delete_row(M,h):
    return [r[:] for i,r in enumerate(M) if i!=h]


def delete_col(M,k):
    return [[x for j,x in enumerate(r) if j!=k] for r in M]


# Diffuse row-side test: duplicated coordinate frame. Every row inclusion marginal is 1/2.
Md = [[1,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1],[0,0,1]]
Zd, ad, bd, jd = volume_stats(Md)
assert Zd == 8
assert all(x == Fraction(1,2) for x in ad)
assert all(x == 1 for x in bd)

# Hub test: one dominant row/column. Both row and column volume marginals exceed 2/3.
Mh = [[10,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
Zh, ah, bh, jh = volume_stats(Mh)
assert Zh == 301
h = max(range(4), key=lambda i: ah[i])
k = max(range(4), key=lambda j: bh[j])
assert h == k == 0
assert ah[h] == Fraction(300,301) and bh[k] == Fraction(300,301)
Zrow = volume_stats(delete_row(Mh,h))[0]
Zcol = volume_stats(delete_col(Mh,k))[0]
assert Zrow == (1-ah[h])*Zh == 1
assert Zcol == (1-bh[k])*Zh == 1
assert jh[h][k] >= (ah[h] + bh[k] - 1)*Zh
assert jh[h][k] == 300

q = Fraction(4,3)
C = 9*sqrt(3)*e/2
Rstar = 30 + 12*sqrt(6)
a_star = sqrt(3/Rstar)
q_star = (1+a_star)**2
assert abs(q_star - 1.5) < 1e-12
R43 = 9*(2+sqrt(3))**2
a43 = sqrt(3/R43)
q43 = (1+a43)**2
assert abs(q43 - 4/3) < 1e-12
q225 = (1+sqrt(3/225))**2
C225 = 3*e/((3-2*q225)*(1+sqrt(3/225)))

print('QFORM_B13_R22_BIHUB_STABLERANK_CHECK_PASS')
print('diffuse_Z=', Zd, 'diffuse_alpha=', [str(x) for x in ad])
print('hub_Z=', Zh, 'hub_alpha0=', ah[0], 'hub_beta0=', bh[0], 'joint00=', jh[0][0])
print('row_residual=', Zrow, 'col_residual=', Zcol)
print('q=', q, 'C_q=', format(C,'.15f'))
print('stable_rank_threshold=', format(Rstar,'.15f'))
print('q43_threshold_R=', format(R43,'.15f'), 'q=', format(q43,'.15f'))
print('R225_q=',format(q225,'.15f'),'R225_C=',format(C225,'.15f'))
