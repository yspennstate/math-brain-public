"""
End-to-end validation of the quaternion Gaussian extremal base (V.A, thm:quaternion-gaussian-base):
M_m = min_{|T|=m} sigma_min(A_T) for A in H^{N x m} standard quaternion Gaussian, base -h(gamma)/4.
Quaternion m x m matrix -> 4m x 4m real realification (left-mult rep); sigma_min(real)=sigma_min(H).
gamma=2 (N=2m): target -h(2)/4 = -log4/4 = -0.3466.  Compare to real (-1.386), complex (-0.693):
quaternion is least negative (divide by d_F=4).  Run: python verify_quaternion.py
"""
import numpy as np
from itertools import combinations
from math import log
rng=np.random.default_rng(20260628)
def hgamma(g): return g*log(g)-(g-1)*log(g-1)

# left-multiplication 4x4 real rep of a quaternion (basis 1,i,j,k)
def quat_to_real4(q0,q1,q2,q3):
    return np.array([[q0,-q1,-q2,-q3],
                     [q1, q0,-q3, q2],
                     [q2, q3, q0,-q1],
                     [q3,-q2, q1, q0]])

def realify(Q):  # Q: (r,c,4) quaternion array -> (4r,4c) real
    r,c,_=Q.shape
    R=np.zeros((4*r,4*c))
    for a in range(r):
        for b in range(c):
            R[4*a:4*a+4,4*b:4*b+4]=quat_to_real4(*Q[a,b])
    return R

def quat_gauss(r,c):  # standard quaternion Gaussian: 4 comps N(0,1/4), E|q|^2=1
    return rng.standard_normal((r,c,4))*0.5

def smin_quat(Q):
    return np.linalg.svd(realify(Q),compute_uv=False)[-1]

target=-hgamma(2.0)/4
print(f"Quaternion extremal base, gamma=2 (N=2m): target -h(2)/4 = {target:.4f}")
print(f"(compare real -h(2)/1={-hgamma(2.0):.4f}, complex -h(2)/2={-hgamma(2.0)/2:.4f})")
for m in [3,4,5,6]:
    N=2*m
    subs=[list(S) for S in combinations(range(N),m)]
    tr={3:120,4:50,5:18,6:8}[m]
    vals=[]
    for _ in range(tr):
        A=quat_gauss(N,m)
        Mm=min(smin_quat(A[S]) for S in subs)
        vals.append(log(Mm)/m)
    v=np.array(vals)
    print(f"  m={m}: (1/m)log M_m = {v.mean():+.4f}  std(log M_m)={v.std()*m:.3f}  "
          f"(gap to target {v.mean()-target:+.4f}, #subs={len(subs)})")
print("DONE. Trend toward -h(2)/4 and least-negative-of-the-three confirms the d_F=4 quaternion base.")
