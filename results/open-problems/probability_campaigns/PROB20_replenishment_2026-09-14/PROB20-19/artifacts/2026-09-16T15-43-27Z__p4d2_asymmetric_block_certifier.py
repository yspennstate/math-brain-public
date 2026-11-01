#!/usr/bin/env python3
"""PROB20-19 finite exact/interval certificate, p=4,d=2 asymmetric two-block family.

This is a reproducible self-check/certificate for a finite counterexample search,
not a proof of the full Mallat-Zeitouni conjecture.

Family:
  six four-distinct integer spectra;
  all three disjoint pairings of the four eigendirections into two 2D blocks;
  each block is actively rotated by one of three rational Pythagorean rotations.
This gives 6*3*3*3 = 162 exact rational covariances.

For d=2, retained top-two energy = tr(Sigma) minus the expected sum of the two
smallest squared coordinates. Conditional on the two block angles, the two
chi-square_2 radial variables can be integrated exactly. The resulting kernel
is then enclosed on a compact two-angle square by outward interval arithmetic.
No Gaussian tail is truncated.
"""
from fractions import Fraction
import math
import numpy as np
import mpmath as mp
import sympy as sp

mp.iv.dps = 80
N = 1024
ROUND_PAD = 1e-6

SPECTRA = [
    (3,4,6,9),
    (2,3,6,9),
    (2,3,9,16),
    (1,2,9,16),
    (3,4,9,16),
    (2,3,4,6),
]
PAIRINGS = [
    ((0,1),(2,3)),
    ((0,2),(1,3)),
    ((0,3),(1,2)),
]
TRIPLES = [(3,4,5),(8,15,17),(20,21,29)]


def frac_transpose(A):
    return [list(row) for row in zip(*A)]


def frac_matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def diag_fraction(vals):
    n=len(vals)
    return [[Fraction(vals[i],1) if i==j else Fraction(0,1)
             for j in range(n)] for i in range(n)]


def block_rotation(pairing, r1, r2):
    U=diag_fraction([1,1,1,1])
    for (i,j),(x,y,z) in zip(pairing,(r1,r2)):
        c=Fraction(x,z); s=Fraction(y,z)
        U[i][i]=c; U[i][j]=s
        U[j][i]=-s; U[j][j]=c
    return U


def exact_covariance(spec,pairing,r1,r2):
    U=block_rotation(pairing,r1,r2)
    UT=frac_transpose(U)
    I=frac_matmul(U,UT)
    assert I==diag_fraction([1,1,1,1])
    S=diag_fraction(spec)
    C=frac_matmul(frac_matmul(U,S),UT)
    assert sum(C[i][i] for i in range(4)) == Fraction(sum(spec),1)
    # Every selected pair mixes unequal eigenvalues and both rotations are nontrivial.
    for pair,r in zip(pairing,(r1,r2)):
        i,j=pair
        assert spec[i] != spec[j]
        assert r[0] != 0 and r[1] != 0
        assert C[i][j] != 0
    return C


def symbolic_radial_identity_check():
    # l<=u and m<=v.  With x,y iid chi2_2 and t=y/x, the lower envelope is
    # Bt on [0,l/v], l+mt on [l/v,u/m], and A on [u/m,infinity].
    t=sp.symbols('t', positive=True)
    l,u,m,v=sp.symbols('l u m v', positive=True)
    A=l+u; B=m+v
    expr=4*(
        sp.integrate(B*t/(1+t)**3,(t,0,l/v))
        + sp.integrate((l+m*t)/(1+t)**3,(t,l/v,u/m))
        + sp.integrate(A/(1+t)**3,(t,u/m,sp.oo))
    )
    closed=2*(l*m*u+l*m*v+l*u*v+m*u*v)/(l*m+l*u+m*v+u*v)
    assert sp.simplify(expr-closed)==0
    # The breakpoint order follows from l*m <= u*v under l<=u,m<=v.
    return sp.factor(sp.together(expr-closed))


def down(ivx):
    return np.nextafter(float(ivx.a), -np.inf)


def up(ivx):
    return np.nextafter(float(ivx.b), np.inf)


def lu_cell_bounds(a,b,x,y,z):
    """Cellwise bounds for l=min(q1,q2), u=max(q1,q2) on phi in [0,pi]."""
    aa=mp.iv.mpf(a); bb=mp.iv.mpf(b)
    cc=mp.iv.mpf(x)/z; ss=mp.iv.mpf(y)/z
    sa=mp.iv.sqrt(aa); sb=mp.iv.sqrt(bb)
    Ll=np.empty(N,dtype=float); Ul=np.empty(N,dtype=float)
    Lu=np.empty(N,dtype=float); Uu=np.empty(N,dtype=float)
    for k in range(N):
        phi=mp.iv.pi*mp.iv.mpf([k,k+1])/N
        co=mp.iv.cos(phi); si=mp.iv.sin(phi)
        e1=cc*sa*co + ss*sb*si
        e2=-ss*sa*co + cc*sb*si
        q1=e1**2; q2=e2**2
        q1l,q1u=down(q1),up(q1)
        q2l,q2u=down(q2),up(q2)
        Ll[k]=max(0.0,min(q1l,q2l))
        Ul[k]=max(0.0,min(q1u,q2u))
        Lu[k]=max(0.0,max(q1l,q2l))
        Uu[k]=max(0.0,max(q1u,q2u))
        assert Ll[k] <= Ul[k] and Lu[k] <= Uu[k]
    return Ll,Ul,Lu,Uu


def bottom2_kernel(l,u,m,v):
    """Exact radial expectation conditioned on angular coefficients.

    K=2(lmu+lmv+luv+muv)/(lm+lu+mv+uv), continuously 0 at the origin.
    It is coordinatewise nondecreasing because it equals the expectation of
    the sum of the two smallest among {lX,uX,mY,vY}, a pointwise monotone
    function of each nonnegative coefficient.
    """
    den=l*m+l*u+m*v+u*v
    num=l*m*u+l*m*v+l*u*v+m*u*v
    shape=np.broadcast_shapes(l.shape,u.shape,m.shape,v.shape)
    return np.divide(2*num,den,out=np.zeros(shape,dtype=float),where=den>0)


def B2_bounds(B1,B2):
    Ll1,Ul1,Lu1,Uu1=B1
    Ll2,Ul2,Lu2,Uu2=B2
    n=len(Ll1)
    slo=0.0; shi=0.0
    chunk=128
    for i in range(0,n,chunk):
        lo=bottom2_kernel(Ll1[i:i+chunk,None],Lu1[i:i+chunk,None],
                          Ll2[None,:],Lu2[None,:])
        hi=bottom2_kernel(Ul1[i:i+chunk,None],Uu1[i:i+chunk,None],
                          Ul2[None,:],Uu2[None,:])
        lo=np.nextafter(lo,-np.inf)
        hi=np.nextafter(hi,np.inf)
        slo += float(lo.sum(dtype=np.float64))
        shi += float(hi.sum(dtype=np.float64))
    return slo/(n*n)-ROUND_PAD, shi/(n*n)+ROUND_PAD


def fmt_frac(q):
    return str(q.numerator) if q.denominator==1 else f"{q.numerator}/{q.denominator}"


print(f"N={N}, iv_dps={mp.iv.dps}, ROUND_PAD={ROUND_PAD}")
print("MODEL_RUNTIME_METADATA: not available to script; report must state platform metadata separately")
print("SYMBOLIC_RADIAL_IDENTITY_RESIDUAL", symbolic_radial_identity_check())
print("Radial identity: E[sum two smallest | angles] = 2(lmu+lmv+luv+muv)/(lm+lu+mv+uv).")
print("No Gaussian tail truncation: both chi-square_2 radii are integrated exactly.")

# Conservative floating reduction budget.  Each exact conditional bottom-two
# expectation is <= E[16X+16Y]=64 for X,Y~chi2_2, so 64 is a safe term bound.
M=N*N
u=2.0**-53
gamma=(M-1)*u/(1.0-(M-1)*u)
mean_sum_error_bound=gamma*64.0
pointwise_budget=1e-10
assert mean_sum_error_bound+pointwise_budget < ROUND_PAD/10
print(f"IEEE_MEAN_REDUCTION_ERROR_BOUND={mean_sum_error_bound:.3e}; ROUND_PAD={ROUND_PAD:.1e}; margin>10x=PASS")

# Cache angular cell bounds by ordered eigenvalue pair and rational rotation.
cache={}
def get_bounds(a,b,r):
    key=(a,b,r)
    if key not in cache:
        cache[key]=lu_cell_bounds(a,b,*r)
    return cache[key]

ID=(1,0,1)
records=[]
for spec in SPECTRA:
    assert len(set(spec))==4
    for pairing in PAIRINGS:
        (i,j),(k,l)=pairing
        KL=B2_bounds(get_bounds(spec[i],spec[j],ID),
                     get_bounds(spec[k],spec[l],ID))
        for r1 in TRIPLES:
            for r2 in TRIPLES:
                assert r1[0]*r1[0]+r1[1]*r1[1]==r1[2]*r1[2]
                assert r2[0]*r2[0]+r2[1]*r2[1]==r2[2]*r2[2]
                C=exact_covariance(spec,pairing,r1,r2)
                BR=B2_bounds(get_bounds(spec[i],spec[j],r1),
                              get_bounds(spec[k],spec[l],r2))
                tr=sum(spec)
                # top2 excess = bottom2(KL)-bottom2(rotated)
                exlo=(KL[0]-BR[1])/tr
                exhi=(KL[1]-BR[0])/tr
                assert exhi < 0.0, (spec,pairing,r1,r2,exlo,exhi)
                records.append((exlo,exhi,spec,pairing,r1,r2,KL,BR,C))

assert len(records)==162
# Certified bracket for the maximum over this finite set.
max_lower=max(r[0] for r in records)
max_upper=max(r[1] for r in records)
best_lower=max(records,key=lambda r:r[0])
best_upper=max(records,key=lambda r:r[1])

print("CERTIFIED_EXAMPLES",len(records))
print(f"FINITE_SET_MAX_EXCESS_BRACKET=[{max_lower:.15g},{max_upper:.15g}]")
print("MAX_LOWER_WITNESS",best_lower[2],best_lower[3],best_lower[4],best_lower[5],f"[{best_lower[0]:.15g},{best_lower[1]:.15g}]")
print("MAX_UPPER_WITNESS",best_upper[2],best_upper[3],best_upper[4],best_upper[5],f"[{best_upper[0]:.15g},{best_upper[1]:.15g}]")
print("ALL_162_STRICTLY_NEGATIVE=PASS")

# Print the 20 candidates with largest certified upper endpoints.
for r in sorted(records,key=lambda r:r[1],reverse=True)[:20]:
    exlo,exhi,spec,pairing,r1,r2,KL,BR,C=r
    print("TOP",
          "spec="+str(spec),"pairing="+str(pairing),
          "r1="+str(r1),"r2="+str(r2),
          f"B_KL=[{KL[0]:.15g},{KL[1]:.15g}]",
          f"B_rot=[{BR[0]:.15g},{BR[1]:.15g}]",
          f"excess=[{exlo:.15g},{exhi:.15g}]")

# Exact covariance for the witness giving the largest certified lower endpoint.
exlo,exhi,spec,pairing,r1,r2,KL,BR,C=best_lower
print("BEST_LOWER_WITNESS_COVARIANCE_EXACT")
print("spec",spec,"pairing",pairing,"r1",r1,"r2",r2)
for row in C:
    print("["+", ".join(fmt_frac(q) for q in row)+"]")

# Retained prior metric from the immediately preceding verified report.
prior_lo=-0.00435063030941115
prior_hi=-0.00401417468692829
union_lo=max(prior_lo,max_lower)
union_hi=max(prior_hi,max_upper)
assert union_lo > prior_hi
print(f"PRIOR_RETAINED_METRIC=[{prior_lo:.15g},{prior_hi:.15g}]")
print(f"UPDATED_RETAINED_METRIC_BRACKET=[{union_lo:.15g},{union_hi:.15g}]")
print("CERTIFIED_METRIC_MOVEMENT=PASS")
