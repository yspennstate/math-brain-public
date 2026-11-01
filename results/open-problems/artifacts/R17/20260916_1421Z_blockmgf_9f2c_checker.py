#!/usr/bin/env python3
"""
R17 exact checker, 2026-09-16.

No Monte Carlo.

R17:
  C004: exhaustive small-string check of the exact source-block/target-composition
        LCS decomposition.
  C005: exact pair counts for m=12, b=0..30, using global-complement symmetry;
        rational annealed generating-function certificate at
        s=16, z=119/400; rigorous rational-log enclosure proving
        gamma_2 <= Q < 432877/500000 = 0.865754.
        This is NONCOMPETITIVE with Lueker 0.826280, so it does not move R17's
        certified interval.
        The infinite-b generating function tail is bounded exactly and the
        induced Q truncation error is certified <1e-9.

R18 independent finite-core audit:
  Checks the reported kernel-error rational inequalities using a different
  coarse pi enclosure 333/106 < pi < 355/113, independently verifies the
  three limiting Q inequalities by exact alternating arctan series, and
  checks 125/(585344*pi) and 0.000067<T*<0.000069.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import hashlib

def lcs(x,y):
    d=[0]*(len(y)+1)
    for a in x:
        prev=0
        for j,b in enumerate(y,1):
            old=d[j]
            d[j]=prev+1 if a==b else max(d[j],d[j-1])
            prev=old
    return d[-1]

def compositions(n,r):
    if r==1:
        yield (n,)
        return
    for b in range(n+1):
        for tail in compositions(n-b,r-1):
            yield (b,)+tail

# C004: exact decomposition for small strings:
# split X into equal source blocks of size m; maximize the sum of block LCSs
# over all consecutive target compositions.
c004=0
for m,r in [(1,3),(2,2),(2,3),(3,2)]:
    n=m*r
    for X in product((0,1), repeat=n):
        blocks=[X[j*m:(j+1)*m] for j in range(r)]
        for Y in product((0,1), repeat=n):
            rhs=0
            for bs in compositions(n,r):
                pos=0
                val=0
                for block,b in zip(blocks,bs):
                    chunk=Y[pos:pos+b]
                    pos += b
                    val += lcs(block,chunk)
                rhs=max(rhs,val)
            assert rhs==lcs(X,Y)
            c004 += 1
print(f"C004 exact block/composition identity: PASS ({c004} string pairs)")

def update_row(row,X,y):
    # row[i]=LCS(X[:i],Yprefix), i=0..m
    m=len(X)
    new=[0]*(m+1)
    for i in range(1,m+1):
        if X[i-1]==y:
            new[i]=row[i-1]+1
        else:
            new[i]=max(row[i],new[i-1])
    return tuple(new)

M=12
B=30

# Count # pairs (X,Y), |X|=M, |Y|=b, by their LCS score.
# By simultaneous bit complementation, it is enough to enumerate X_1=0
# and double all counts.
counts=[defaultdict(int) for _ in range(B+1)]
for tail in product((0,1), repeat=M-1):
    X=(0,)+tail
    dist={tuple([0]*(M+1)):1}
    counts[0][0] += 2
    for b in range(1,B+1):
        nd=defaultdict(int)
        for row,cnt in dist.items():
            nd[update_row(row,X,0)] += cnt
            nd[update_row(row,X,1)] += cnt
        dist=nd
        for row,cnt in dist.items():
            counts[b][row[-1]] += 2*cnt

for b in range(B+1):
    assert sum(counts[b].values()) == 2**(M+b)
print("C005 exact LCS pair-count totals: PASS for m=12, b=0..30")

# Annealed generating function:
# Phi(z,s)=sum_{b>=0} z^b E[s^LCS(X_m,Y_b)].
S=16
Z=F(119,400)

partial=F(0)
for b in range(B+1):
    moment_num=sum(cnt*(S**ell) for ell,cnt in counts[b].items())
    moment=F(moment_num, 2**(M+b))
    partial += (Z**b)*moment

# Since LCS<=M, E[S^LCS]<=S^M for every b:
tail_bound = F(S**M) * (Z**(B+1)) / (1-Z)
phi_plus = partial + tail_bound

# Exact-rational log enclosure based on
# log x = k log 2 + 2 sum_{j>=0} u^(2j+1)/(2j+1),
# u=(y-1)/(y+1), y=x/2^k in [1,2).
def log_bounds(x,N=80):
    assert x>0
    y=x
    k=0
    while y>=2:
        y/=2
        k+=1
    while y<1:
        y*=2
        k-=1
    def base(v):
        u=(v-1)/(v+1)
        assert 0<=u<F(1)
        ss=F(0)
        for j in range(N):
            ss += u**(2*j+1)/F(2*j+1)
        lo=2*ss
        rem=2*u**(2*N+1)/(F(2*N+1)*(1-u*u))
        return lo,lo+rem
    ylo,yhi=base(y)
    l2lo,l2hi=base(F(2))
    if k>=0:
        return ylo+k*l2lo, yhi+k*l2hi
    return ylo+k*l2hi, yhi+k*l2lo

lz_lo,lz_hi=log_bounds(Z)
lp_lo,lp_hi=log_bounds(phi_plus)
ls_lo,ls_hi=log_bounds(F(S))
num_lo=-lz_hi+lp_lo/F(M)
num_hi=-lz_lo+lp_hi/F(M)
q_lo=num_lo/ls_hi
q_hi=num_hi/ls_lo

CERT=F(432877,500000) # 0.865754
assert q_hi < CERT

# Difference between using Phi_B and Phi_B+tail:
# log(1+R/P) <= R/P, so
# Q_plus-Q_partial <= R / (M log(S) P).
trunc_q_err = tail_bound/(F(M)*ls_lo*partial)
assert trunc_q_err < F(1,10**9)

# Current published upper bound remains much better.
LUEKER=F(826280,1000000)
assert CERT > LUEKER

print("C005 annealed block-MGF certificate: PASS")
print("  parameters: m=12, B=30, s=16, z=119/400")
print("  rigorous Q interval (decimal display only): "
      f"[{float(q_lo):.15f}, {float(q_hi):.15f}]")
print("  certified Q < 432877/500000 = 0.865754")
print("  certified generating-function truncation contribution to Q < 1e-9")
print("  noncompetitive: 0.865754 > published Lueker upper 0.826280")
print("  exact Phi_plus numerator digits:", len(str(phi_plus.numerator)))
print("  exact Phi_plus denominator digits:", len(str(phi_plus.denominator)))
print("  exact pair-count digest:",
      hashlib.sha256(repr([(b,sorted(d.items())) for b,d in enumerate(counts)]).encode()).hexdigest())

# ----------------------------------------------------------------------
# R18 independent finite-core audit.
# ----------------------------------------------------------------------

# Kernel-error rational core, derived independently from the report:
# B=sin b/b >=1-b^2/6, and the report's C-factor bounds at
# b<=1/320, |v|<=19.
bden=320
B_LO=F(1)-F(1,6*bden*bden)
C_LO=F(2*bden*bden-19*19, 2*bden*bden)
C_HI=F(12*bden*bden, 12*bden*bden-1)
assert F(1)-B_LO*C_LO < F(3,1600)
assert C_HI-F(1) < F(3,1600)

# Independent coarse pi enclosure, classical convergents.
PI_LO=F(333,106)
PI_HI=F(355,113)

# Exact alternating-series atan enclosure for |x|<=1, with reciprocal
# reduction otherwise.  This is independent code and does not use R18's
# Machin enclosure.
def atan01_bounds(x,n=100):
    assert 0<=x<=1
    ss=F(0)
    for k in range(n):
        ss += (-1)**k*x**(2*k+1)/F(2*k+1)
    nxt=x**(2*n+1)/F(2*n+1)
    if n%2==0:
        return ss,ss+nxt
    return ss-nxt,ss

def atan_bounds(x):
    if x==0:
        return F(0),F(0)
    if x<0:
        lo,hi=atan_bounds(-x)
        return -hi,-lo
    if x<=1:
        return atan01_bounds(x)
    lo,hi=atan01_bounds(F(1)/x)
    return PI_LO/F(2)-hi, PI_HI/F(2)-lo

p=F(3,50)
ell=F(19)
D=F(4573,100000)
eps=F(1,1600)

def Q_bounds(y):
    a_lo,a_hi=atan_bounds(y)
    b_lo,b_hi=atan_bounds(y-ell)
    delta_lo=a_lo-b_hi
    delta_hi=a_hi-b_lo
    const=p/(1+y*y)
    nlo=const+(1-p)/ell*delta_lo
    nhi=const+(1-p)/ell*delta_hi
    return nlo/PI_HI, nhi/PI_LO

for y in [F(1,2),F(2),F(35,4)]:
    lo,hi=Q_bounds(y)
    if y==F(2):
        assert hi<D-eps
    else:
        assert lo>D+eps

# Endpoint algebra and coarse rigorous pi enclosure.
b0=F(1,320)
coef=b0*b0/D
assert coef==F(125,585344)
T_LO=coef/PI_HI
T_HI=coef/PI_LO
assert T_LO>F(67,1_000_000)
assert T_HI<F(69,1_000_000)

print("R18 independent finite-core audit: PASS")
print("  kernel rational error core <1/1600: PASS")
print("  three Q witness inequalities using only 333/106<pi<355/113: PASS")
print("  T*=125/(585344*pi), and 0.000067<T*<0.000069: PASS")
print("  scope: finite core only; source-criterion-to-final-conclusion not audited end-to-end here")
print("PASS")
