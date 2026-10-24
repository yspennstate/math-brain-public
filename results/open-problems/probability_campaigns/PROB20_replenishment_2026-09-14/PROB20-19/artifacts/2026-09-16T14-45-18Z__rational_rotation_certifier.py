#!/usr/bin/env python3
"""PROB20-19: interval certificate for rational two-block rotations.

This is a self-check/certificate for one finite search family, not a proof of the
full Mallat-Zeitouni conjecture.

Family:
  Sigma = diag(a,a,1,1), a in {4,9,16}; p=4, d=3.
  U(c,s) simultaneously rotates (1,3) and (2,4), with rational
  Pythagorean (c,s).

For d=3, retained energy = tr(Sigma) - E[min_i X_i^2].  Splitting the
four Gaussian coordinates into two independent 2D blocks and integrating the
chi_2^2 radii exactly reduces the minimum expectation to a 2D angular integral
of the harmonic mean H(x,y)=2xy/(x+y).  Angular cells are enclosed with
mpmath.iv outward interval trigonometry.  No Gaussian radial tail is truncated.
"""
from fractions import Fraction
import math
import numpy as np
import mpmath as mp

mp.iv.dps = 80
N = 2048
ROUND_PAD = 1e-6  # conservative final widening of each J bound
TRIPLES = [(3,4,5),(5,12,13),(8,15,17),(7,24,25),(20,21,29),(12,35,37)]
AS = [4,9,16]


def frac_matmul(A,B):
    m=len(A); n=len(B); k=len(B[0])
    return [[sum(A[i][r]*B[r][j] for r in range(n)) for j in range(k)] for i in range(m)]

def frac_transpose(A):
    return [list(row) for row in zip(*A)]

def rotation_fraction(x,y,z):
    c=Fraction(x,z); s=Fraction(y,z)
    return [
        [c,0,s,0],
        [0,c,0,s],
        [-s,0,c,0],
        [0,-s,0,c],
    ]

def diag_fraction(vals):
    n=len(vals)
    return [[Fraction(vals[i],1) if i==j else Fraction(0,1) for j in range(n)] for i in range(n)]

def exact_checks(a,x,y,z):
    U=rotation_fraction(x,y,z)
    UT=frac_transpose(U)
    I=frac_matmul(U,UT)
    assert I==diag_fraction([1,1,1,1])
    S=diag_fraction([a,a,1,1])
    C=frac_matmul(frac_matmul(U,S),UT)
    assert sum(C[i][i] for i in range(4)) == Fraction(2*(a+1),1)
    return C


def down(ivx):
    # ivx.a is an outward lower endpoint; converting to double then stepping
    # down once preserves an outer bound.
    return np.nextafter(float(ivx.a), -np.inf)

def up(ivx):
    return np.nextafter(float(ivx.b), np.inf)


def m_cell_bounds(a, cnum, cden, snum, sden):
    """Bounds m(phi)=min(q1(phi),q2(phi)) on each equal phi-cell in [0,pi]."""
    aa=mp.iv.mpf(a)
    cc=mp.iv.mpf(cnum)/cden
    ss=mp.iv.mpf(snum)/sden
    sa=mp.iv.sqrt(aa)
    # b=1, so sqrt(b)=1 exactly.
    L=np.empty(N,dtype=float)
    U=np.empty(N,dtype=float)
    for i in range(N):
        phi=mp.iv.pi * mp.iv.mpf([i,i+1]) / N
        co=mp.iv.cos(phi); si=mp.iv.sin(phi)
        ell1=cc*sa*co + ss*si
        ell2=-ss*sa*co + cc*si
        q1=ell1**2; q2=ell2**2
        # If q1 in [l1,u1], q2 in [l2,u2], then min(q1,q2)
        # lies in [min(l1,l2), min(u1,u2)].
        L[i]=max(0.0, min(down(q1),down(q2)))
        U[i]=max(0.0, min(up(q1),up(q2)))
        assert L[i] <= U[i]
    return L,U


def harmonic(x,y):
    den=x+y
    return np.divide(2*x*y, den, out=np.zeros(np.broadcast_shapes(x.shape,y.shape)), where=den>0)


def J_bounds(L,U):
    """Enclose E[H(m(Phi),m(Psi))] for independent uniform angles.

    H is coordinatewise increasing for x,y>=0, so cellwise lower/upper m
    bounds immediately give cellwise H bounds. Equal angular cells mean the
    integral average is the arithmetic mean over cells.
    """
    n=len(L)
    slo=0.0; shi=0.0
    chunk=128
    for i in range(0,n,chunk):
        xl=L[i:i+chunk,None]; xu=U[i:i+chunk,None]
        yl=L[None,:]; yu=U[None,:]
        hlo=harmonic(xl,yl)
        hhi=harmonic(xu,yu)
        # Widen each floating evaluation one ulp, then add a much larger
        # final ROUND_PAD below. All terms are nonnegative and <= a <= 16.
        hlo=np.nextafter(hlo,-np.inf)
        hhi=np.nextafter(hhi,np.inf)
        slo += float(hlo.sum(dtype=np.float64))
        shi += float(hhi.sum(dtype=np.float64))
    lo=slo/(n*n)-ROUND_PAD
    hi=shi/(n*n)+ROUND_PAD
    return lo,hi


def fmt_frac(q):
    return str(q.numerator) if q.denominator==1 else f"{q.numerator}/{q.denominator}"

print(f"N={N}, iv_dps={mp.iv.dps}, ROUND_PAD={ROUND_PAD}")
print("Exact identity used: E[min(R1^2 m1,R2^2 m2)|m1,m2] = 2 m1 m2/(m1+m2), R_i^2~chi2_2.")
print("No radial Gaussian tail truncation: radial integral is exact.")

# Conservative IEEE-754 reduction-error check. For M positive terms bounded by 16,
# sequential floating summation has standard absolute mean-error bound
# gamma_{M-1}*16, gamma_n=n*u/(1-n*u), u=2^-53.  Harmonic-mean
# pointwise arithmetic is separately negligible at this scale; we budget 1e-12.
M = N*N
u = 2.0**-53
gamma = (M-1)*u/(1.0-(M-1)*u)
mean_sum_error_bound = gamma*16.0
pointwise_budget = 1e-12
assert mean_sum_error_bound + pointwise_budget < ROUND_PAD/10
print(f"IEEE_MEAN_REDUCTION_ERROR_BOUND={mean_sum_error_bound:.3e}; ROUND_PAD={ROUND_PAD:.1e}; margin>10x=PASS")

records=[]
base_cache={}
for a in AS:
    exact_checks(a,1,0,1)
    L0,U0=m_cell_bounds(a,1,1,0,1)
    B0=J_bounds(L0,U0)
    base_cache[a]=B0
    for x,y,z in TRIPLES:
        assert x*x+y*y==z*z
        C=exact_checks(a,x,y,z)
        L,U=m_cell_bounds(a,x,z,y,z)
        Br=J_bounds(L,U)
        tr=2*(a+1)
        # F_rot-F_KL = J_KL-J_rot for d=3.
        exlo=(B0[0]-Br[1])/tr
        exhi=(B0[1]-Br[0])/tr
        assert exhi < 0.0, (a,(x,y,z),exlo,exhi)
        records.append((exlo,exhi,a,x,y,z,B0,Br,C))

records.sort(key=lambda r:r[1], reverse=True)
best=records[0]
# Prove the identity of the largest signed excess among this finite certified set:
# even the lower endpoint of the best interval exceeds every other upper endpoint.
assert best[0] > max(r[1] for r in records[1:])

print("CERTIFIED_EXAMPLES", len(records))
for r in records:
    exlo,exhi,a,x,y,z,B0,Br,C=r
    print(f"a={a:2d} c={x}/{z} s={y}/{z} J_KL=[{B0[0]:.15g},{B0[1]:.15g}] J_rot=[{Br[0]:.15g},{Br[1]:.15g}] excess_over_trace=[{exlo:.15g},{exhi:.15g}]")

exlo,exhi,a,x,y,z,B0,Br,C=best
print("BEST_CERTIFIED_SIGNED_EXCESS")
print(f"a={a}, c={x}/{z}, s={y}/{z}, interval=[{exlo:.15g},{exhi:.15g}]")
print("BEST_ROTATED_COVARIANCE_EXACT")
for row in C:
    print("["+", ".join(fmt_frac(q) for q in row)+"]")
print("ALL_18_STRICTLY_NEGATIVE=PASS")
print("UNIQUE_FINITE_SET_MAXIMUM=PASS")
