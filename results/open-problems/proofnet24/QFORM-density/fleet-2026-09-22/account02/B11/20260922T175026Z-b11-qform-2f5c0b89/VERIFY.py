#!/usr/bin/env python3
from math import pi, sin, cos, sqrt
from itertools import combinations

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def algebra_check():
    tests = [
        (2.0, 3.0, -1.5, 4.0, 5.0),
        (-1.0, 0.7, 2.0, -1.3, 3.1),
        (4.2, -2.2, 0.3, 1.1, -0.8),
    ]
    for p,a,b,c,r in tests:
        detB = -a*a*r + 2*a*b*c - c*c*p
        gamma = (a*a*r - 2*a*b*c + c*c*p)/(4*a*a*c*c)
        assert abs(gamma + detB/(4*a*a*c*c)) < 1e-12
    print("algebra_gamma_identity=PASS")

def circular_frame_check(m):
    R=[]
    for i in range(m):
        th=2*pi*i/m
        R.append([sqrt(2/m)*cos(th), sqrt(2/m)*sin(th), 1/sqrt(m)])
    G=[[sum(R[i][j]*R[i][k] for i in range(m)) for k in range(3)] for j in range(3)]
    orth_err=max(abs(G[j][k]-(1.0 if j==k else 0.0)) for j in range(3) for k in range(3))
    lam=(1.0,1.0,-2.0)
    A=[[sum(R[i][k]*lam[k]*R[j][k] for k in range(3)) for j in range(m)] for i in range(m)]
    diag_err=max(abs(A[i][i]) for i in range(m))
    maxdet=0.0
    argmax=None
    for I in combinations(range(m),3):
        B=[[A[i][j] for j in I] for i in I]
        d=abs(det3(B))
        if d > maxdet:
            maxdet=d
            argmax=I
    target=54.0/(m**3)
    assert orth_err < 1e-12
    assert diag_err < 1e-12
    assert abs(maxdet-target) < 1e-12
    print(f"m={m} orth_err={orth_err:.3e} diag_err={diag_err:.3e} "
          f"max_abs_principal_det={maxdet:.15g} target_54_over_m3={target:.15g} argmax={argmax}")

def constants():
    Cdet=3*2**(2/3)
    Cabc=3*2**(1/3)
    print(f"C_det={Cdet:.15f}")
    print(f"C_abc={Cabc:.15f}")
    assert 4.7622 < Cdet < 4.7623
    assert 3.7797 < Cabc < 3.7798

if __name__ == "__main__":
    algebra_check()
    for m in (6,12,24,48):
        circular_frame_check(m)
    constants()
    print("QFORM_ZERO_PIVOT_TRIPLE_CHECK_PASS")
