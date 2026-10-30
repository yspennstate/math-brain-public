#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product, permutations

# Exact partner datum: fleet01/B08 r12.
U = [
    [F(636,1105), F(-423,1105), F(-12,65), F(-772,1105)],
    [F(3576,5525), F(332,5525), F(-144,325), F(3411,5525)],
    [F(164,425), F(348,425), F(9,25), F(-96,425)],
    [F(27,85), F(-36,85), F(4,5), F(24,85)],
]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):
    return [list(x) for x in zip(*A)]
I = matmul(U,tr(U))
assert all(I[i][j] == (1 if i == j else 0)
           for i in range(4) for j in range(4))

canon=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
basis=[((0,1),1),((2,3),1),((0,2),1),((1,3),-1),((0,3),1),((1,2),1)]
def minor2(i,j,k,l):
    return U[i][k]*U[j][l]-U[i][l]*U[j][k]
C=[[minor2(*rp,*cp) for cp in canon] for rp in canon]
O=[]
for rp,rs in basis:
    rr=canon.index(rp)
    row=[]
    for cp,cs in basis:
        cc=canon.index(cp)
        row.append(rs*cs*C[rr][cc])
    O.append(row)
OO=matmul(O,tr(O))
assert all(OO[i][j] == (1 if i == j else 0)
           for i in range(6) for j in range(6))

# Complex numbers are exact pairs (real,imag).
def cadd(z,w): return (z[0]+w[0], z[1]+w[1])
def csub(z,w): return (z[0]-w[0], z[1]-w[1])
def cmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def det3(A):
    pos = [
        cmul(cmul(A[0][0],A[1][1]),A[2][2]),
        cmul(cmul(A[0][1],A[1][2]),A[2][0]),
        cmul(cmul(A[0][2],A[1][0]),A[2][1]),
    ]
    neg = [
        cmul(cmul(A[0][2],A[1][1]),A[2][0]),
        cmul(cmul(A[0][1],A[1][0]),A[2][2]),
        cmul(cmul(A[0][0],A[1][2]),A[2][1]),
    ]
    z=(F(0),F(0))
    for x in pos: z=cadd(z,x)
    for x in neg: z=csub(z,x)
    return z

M=[[None]*3 for _ in range(3)]
N=[[None]*3 for _ in range(3)]
qp=[[F(0)]*3 for _ in range(3)]
qm=[[F(0)]*3 for _ in range(3)]
for a in range(3):
    for b in range(3):
        x=O[2*a][2*b]; y=O[2*a][2*b+1]
        z=O[2*a+1][2*b]; t=O[2*a+1][2*b+1]
        m=((x+t)/2,(z-y)/2)
        n=((x-t)/2,(z+y)/2)
        M[a][b]=m; N[a][b]=n
        qp[a][b]=m[0]*m[0]+m[1]*m[1]
        qm[a][b]=n[0]*n[0]+n[1]*n[1]

detN=det3(N)
detM=det3(M)
assert detN == (F(0),F(0))
assert detM == (F(404496,1221025),F(0))

# Every parity mask is an anti-linear Frobenius mass after an even
# output/input coordinate-conjugation gauge.
even_bits=[b for b in product((0,1), repeat=3) if sum(b)%2 == 0]
mask_values=[]
for r in even_bits:
    for c in even_bits:
        s=F(0)
        for a in range(3):
            for b in range(3):
                s += qp[a][b] if (r[a]^c[b]) else qm[a][b]
        assert s <= 2
        mask_values.append((s,r,c))
partner_max=max(mask_values)

# Structured coefficient datum from fleet04/B07 r13.
K=[
    [F(245983,5120000),F(5030591,5120000),F(-39077,1024000)],
    [F(-5113569,5120000),F(56671,5120000),F(19643,1024000)],
    [F(-8539,1024000),F(-35819,1024000),F(5009153,5120000)],
]
X=[
    [F(-3609633,1280000),F(111173,51200),F(2385071,1280000)],
    [F(-917133,1280000),F(1431961,1280000),F(525623,256000)],
    [F(-1352967,1280000),F(1061147,1280000),F(948017,1280000)],
]
wp=[[K[a][b]+X[a][b]/2 for b in range(3)] for a in range(3)]
wm=[[-K[a][b]+X[a][b]/2 for b in range(3)] for a in range(3)]

# Exact even-endpoint maximum.
endpoint_scores=[]
for rho in permutations(range(3)):
    for eps in product((0,1),repeat=3):  # 0=plus, 1=minus
        if sum(eps)%2: continue
        score=sum(wm[a][rho[a]] if eps[a] else wp[a][rho[a]]
                  for a in range(3))
        endpoint_scores.append(score)
even_max=max(endpoint_scores)
assert even_max == F(13195057,5120000)

# Exact LP dual certificate for:
# q>=0, row/column totals =1, and all 16 parity-mask sums <=2.
# Equality multipliers may have either sign.
y=[
    F(254881,1024000), F(1268991,5120000), F(-871389,5120000),
    F(-720783,640000), F(670179,2560000), F(0),
]
lam={
    ((0,0,0),(0,1,1)): F(2042727,2560000),
    ((0,1,1),(0,1,1)): F(98951,2560000),
    ((1,1,0),(1,0,1)): F(1845561,2560000),
}
assert all(v >= 0 for v in lam.values())
slacks=[]
for a in range(3):
    for b in range(3):
        for plus in (True,False):
            lhs=y[a]+y[3+b]
            for (r,c),v in lam.items():
                channel_is_in_mask = (r[a]^c[b]) if plus else not (r[a]^c[b])
                if channel_is_in_mask:
                    lhs += v
            rhs=wp[a][b] if plus else wm[a][b]
            slacks.append(lhs-rhs)
assert min(slacks) >= 0
dual_bound=sum(y)+2*sum(lam.values())
assert dual_bound == even_max

print("detN =", detN)
print("detM =", detM)
print("partner_max_parity_mask_sum =", partner_max[0], float(partner_max[0]),
      "r=", partner_max[1], "c=", partner_max[2])
print("partner_mask_slack_to_2 =", 2-partner_max[0], float(2-partner_max[0]))
print("dual_bound =", dual_bound, float(dual_bound))
print("even_endpoint_max =", even_max, float(even_max))
print("dual_equals_even_max =", dual_bound == even_max)
print("min_dual_coefficient_slack =", min(slacks))
print("PASS: rank-2 parity-mask theorem witness and exact structured dual certificate")
