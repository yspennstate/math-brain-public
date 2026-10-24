#!/usr/bin/env python3
"""Exact finite-core self-check for the strengthened PROB10-09 semidirect example.

The matrix M has trace 3, hence is hyperbolic/infinite order.  The finite checks
certify the semidirect lift relation, generation of the full Z^2 kernel by one
relator value and its M-orbit, noncentrality, the quantitative gap, and a
counterexample showing that horizontal generation is not automatic.
"""

def mv(A, x):
    return (A[0][0]*x[0] + A[0][1]*x[1],
            A[1][0]*x[0] + A[1][1]*x[1])

def mm(A, B):
    return ((A[0][0]*B[0][0] + A[0][1]*B[1][0],
             A[0][0]*B[0][1] + A[0][1]*B[1][1]),
            (A[1][0]*B[0][0] + A[1][1]*B[1][0],
             A[1][0]*B[0][1] + A[1][1]*B[1][1]))

def subm(A, B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(2)) for i in range(2))

def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def basis_det(x,y):
    return x[0]*y[1]-x[1]*y[0]

I=((1,0),(0,1))
# Hyperbolic matrix: det=1, trace=3>2, so infinite order.
M=((0,-1),(1,3))
v=(-2,1)
e1=(1,0)
e2=(0,1)

assert det(M)==1
assert M[0][0]+M[1][1]==3
w=mv(subm(M,I),v)
assert w==e1
Mw=mv(M,w)
assert Mw==e2
assert basis_det(w,Mw)==1
assert Mw!=w

# Inverse and surface-action relation: [M,I][I,I]=I.
Minv=((3,1),(-1,0))
assert mm(M,Minv)==I and mm(Minv,M)==I
assert mm(mm(M,I),mm(Minv,I))==I

# beta_8(4 sqrt 2)=1+2 sqrt 2 < 5 because sqrt2<2.
# Exact gap: (10 sqrt2-12)/35 > 61/1000
# iff 10000 sqrt2 > 14135; square both positive sides.
gap_square_margin=2*10000**2-14135**2
assert gap_square_margin==201775 and gap_square_margin>0

# p_u lower floor >261/1000:
# 1/(1+2sqrt2)>261/1000 iff 739>522sqrt2.
pu_square_margin=739**2-2*522**2
assert pu_square_margin==1153 and pu_square_margin>0

# Negation test: a different lift/action spans an index-two sublattice.
Mbad=((0,-1),(1,0))
vbad=(1,0)
wbad=mv(subm(Mbad,I),vbad)
Mwbad=mv(Mbad,wbad)
bad_index_det=abs(basis_det(wbad,Mwbad))
assert bad_index_det==2

print('PROB10-09 NONCENTRAL HYPERBOLIC-ACTION EXACT CHECK')
print(f'det_M={det(M)}')
print(f'trace_M={M[0][0]+M[1][1]}')
print(f'w=(M-I)v={w}')
print(f'Mw={Mw}')
print(f'kernel_orbit_basis_det={basis_det(w,Mw)}')
print(f'noncentral_test_Me1_ne_e1={mv(M,e1)!=e1}')
print('infinite_order_reason=trace_M_gt_2_for_SL2Z')
print(f'gap_gt_61_over_1000_square_margin={gap_square_margin}')
print(f'pu_gt_261_over_1000_square_margin={pu_square_margin}')
print(f'negation_index_det={bad_index_det}')
print('ALL_EXACT_CHECKS_PASS')
