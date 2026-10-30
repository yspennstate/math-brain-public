from fractions import Fraction
from itertools import combinations
from math import sqrt
import numpy as np


def sign_vectors(N):
    assert N % 4 == 0
    s0 = np.ones(N)
    s1 = np.r_[np.ones(N//2), -np.ones(N//2)]
    s2 = np.r_[np.ones(N//4), -np.ones(N//4), np.ones(N//4), -np.ones(N//4)]
    return s0, s1, s2


def matrix_family(N):
    s0,s1,s2 = sign_vectors(N)
    u1 = np.r_[s0/np.sqrt(N), np.zeros(N)]
    u2 = np.r_[s1/np.sqrt(N), np.zeros(N)]
    v  = np.r_[s2/np.sqrt(2*N), s0/np.sqrt(2*N)]
    A = 2*np.outer(u1,u1) - np.outer(u2,u2) - 2*np.outer(v,v)
    return A,u1,u2,v

for N in (4,8,16):
    A,u1,u2,v = matrix_family(N)
    G = np.array([[u1@u1,u1@u2,u1@v],
                  [u2@u1,u2@u2,u2@v],
                  [v@u1,v@u2,v@v]])
    assert np.max(np.abs(G-np.eye(3))) < 1e-12
    ev = np.linalg.eigvalsh(A)
    nz = ev[np.abs(ev)>1e-9]
    assert np.max(np.abs(np.sort(nz)-np.array([-2.,-1.,2.]))) < 1e-10
    assert np.max(np.abs(np.diag(A)[:N])) < 1e-12
    assert np.max(np.abs(np.diag(A)[N:] + 1/N)) < 1e-12
    maxdet = 0.0
    # exact exhaustive enumeration is cheap through N=16 (C(32,3)=4960)
    for S in combinations(range(2*N),3):
        d = abs(np.linalg.det(A[np.ix_(S,S)]))
        maxdet=max(maxdet,d)
    assert maxdet <= 125/(2*N**3) + 1e-10
    print(f"N={N}: spectrum={nz.tolist()}, maxdiag={np.max(np.abs(np.diag(A))):.12g}, max3det={maxdet:.12g}, bound3det={125/(2*N**3):.12g}")

C = 16*sqrt(60)*2**(-0.25)
delta = Fraction(47045881,12*10**18)
partner = 3*2**(4/3)*float(delta)**(-1/6)
print(f"banked_constant={C:.15f}")
print(f"partner_incident_constant={partner:.15f}")
assert abs(C-104.21688998922089)<1e-12
assert partner < 602.012
print("ALL_CHECKS_PASS")
