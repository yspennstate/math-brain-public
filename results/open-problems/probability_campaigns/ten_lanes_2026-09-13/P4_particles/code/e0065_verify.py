# Independent verification of the m=2 result, exact rational arithmetic where possible.
from fractions import Fraction as F
import random, math
def H(A,B,C): return 4*A*C-4*B*B+4*B-4*C+3
def fp_and_slope(A,B,C):
    a=A-2*B+C; b=2*B-2*C
    # g(x)=a x^2+(b-1)x+C
    if a==0: p=F(C,1)/(1-b) if isinstance(C,F) else C/(1-b)
    else:
        disc=(b-1)**2-4*a*C
        s=math.sqrt(float(disc))
        cands=[(-(float(b)-1)+s)/(2*float(a)),(-(float(b)-1)-s)/(2*float(a))]
        p=[c for c in cands if -1e-12<=c<=1+1e-12][0]
    return p, 2*float(a)*p+float(b)
# (1) sign(f'(p)+1) == sign(H) on random parameters
random.seed(3)
bad=0
for _ in range(300000):
    A,B,C=random.random(),random.random(),random.random()
    if C<=1e-9 or A>=1-1e-9: continue
    p,s=fp_and_slope(A,B,C)
    h=H(A,B,C)
    if abs(h)<1e-9 or abs(s+1)<1e-9: continue
    if (s+1>0) != (h>0): bad+=1
print("sign mismatches between f'(p)+1 and H over 300k random QSOs:",bad)
# (2) exact minimum of H on the box [lam,1-lam]^3 by exact corner+interior analysis
import itertools
def minH_box(lam, N=400):
    best=None
    for i in range(N+1):
        A=lam+(1-2*lam)*i/N
        for j in range(N+1):
            B=lam+(1-2*lam)*j/N
            for C in (lam,1-lam):
                h=H(A,B,C)
                if best is None or h<best[0]: best=(h,(A,B,C))
    return best
lam=(3-math.sqrt(7))/4
print("lambda* = (3-sqrt7)/4 =",lam)
print("closed form min H on box = -8L^2+12L-1 at L=lambda*:", -8*lam**2+12*lam-1)
print("grid min H on box at lambda*:", minH_box(lam)[0], minH_box(lam)[1])
for L in (0.05,0.08,lam,0.09,0.12,0.1771):
    print(f"  L={L:.6f}  closed-form min H = {-8*L*L+12*L-1:+.6e}   grid min = {minH_box(L,200)[0]:+.6e}")
# (3) exact rational certificate: lam = 88/1000 (< lambda*) -> non regular ; 89/1000 -> regular
for num in (88,89):
    L=F(num,1000); A=B=L; C=1-L
    h=H(A,B,C)
    print(f"  exact: lam={L}  H={h}  ({'NON-REGULAR (H<0)' if h<0 else 'regular (H>0)'})")
# (4) the exact threshold solves 8L^2-12L+1=0
import sympy as sp
L=sp.symbols('L')
print("roots of 8L^2-12L+1:", sp.solve(8*L**2-12*L+1,L))
