# Independent check of D_2 = 393/64: DP over raw partial assignments of the 9 leaves (no symmetry, no type
# collapsing), plus a brute-force evaluation of the majority formula; and Monte Carlo of the type-DP's
# optimal policy at depth 3 to check 15.064.
import itertools, random
from fractions import Fraction
from functools import lru_cache

def maj3(a,b,c): return 1 if a+b+c>0 else -1
def f2(x):  # x: 9 values in {-1,+1}
    return maj3(maj3(*x[0:3]),maj3(*x[3:6]),maj3(*x[6:9]))

def determined(pa):
    # pa: tuple of 9 entries in {-1,0,+1}; 0 = unknown. Determined iff f constant on all completions.
    unk=[i for i in range(9) if pa[i]==0]
    vals=set()
    for bits in itertools.product((-1,1),repeat=len(unk)):
        x=list(pa)
        for i,b in zip(unk,bits): x[i]=b
        vals.add(f2(x))
        if len(vals)>1: return False
    return True

@lru_cache(maxsize=None)
def W(pa):
    if determined(pa): return Fraction(0)
    best=None
    for i in range(9):
        if pa[i]!=0: continue
        p=list(pa); p[i]=1; q=list(pa); q[i]=-1
        v=1+(W(tuple(p))+W(tuple(q)))/2
        if best is None or v<best: best=v
    return best

D2=W((0,)*9)
print("raw-assignment DP: D_2 =",D2,"=",float(D2), " (type DP gave 393/64 =",393/64,")")

# Monte Carlo of the type-DP optimal policy at depth 3
from dp_exact import V, queries, full, norm
def best_move(t):
    return min(queries(t), key=lambda ab: 1+(V(ab[0])+V(ab[1]))/2)
# To simulate we need to map the abstract move to an actual leaf; instead simulate on the type directly:
# the outcome of a query on a uniform unknown leaf is +/- with prob 1/2 each, and the new type is a or b.
random.seed(12345)
N=200000
tot=0
t0=full(3)
for _ in range(N):
    t=t0; cost=0
    while t not in ('+','-'):
        a,b=best_move(t)
        cost+=1
        t=a if random.random()<0.5 else b
    tot+=cost
m=tot/N
print(f"Monte Carlo of optimal depth-3 policy: mean cost {m:.4f} over {N} runs (exact 15.064288); std err ~ {(m/N)**0.5*1.5:.4f}")
