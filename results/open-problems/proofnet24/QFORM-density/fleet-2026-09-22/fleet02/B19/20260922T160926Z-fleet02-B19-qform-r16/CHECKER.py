from itertools import combinations, product
from fractions import Fraction
import math
import numpy as np

def e2_singular(B):
    s=np.linalg.svd(B,compute_uv=False)
    x=s*s
    return sum(x[i]*x[j] for i in range(len(x)) for j in range(i+1,len(x)))

def minor_energy(H):
    n=H.shape[0]
    total=disjoint=overlap=0.0
    for R in combinations(range(n),2):
        for C in combinations(range(n),2):
            d=float(np.linalg.det(H[np.ix_(R,C)]))
            z=d*d
            total += z
            if set(R).isdisjoint(C):
                disjoint += z
            else:
                overlap += z
    return total,disjoint,overlap

Hs=[]
for raw in [
    [[0,2,-1,0],[2,0,3,1],[-1,3,0,2],[0,1,2,0]],
    [[0,1,2,0,-1],[1,0,0,3,1],[2,0,0,1,2],[0,3,1,0,-2],[-1,1,2,-2,0]],
]:
    Hs.append(np.array(raw,dtype=float))

for idx,H in enumerate(Hs,1):
    total,D,O=minor_energy(H)
    s=np.linalg.svd(H,compute_uv=False)
    spectral=sum(s[i]**2*s[j]**2 for i in range(len(s)) for j in range(i+1,len(s)))
    d=np.sum(H*H,axis=1)
    edge4=sum(H[i,j]**4 for i in range(H.shape[0]) for j in range(i+1,H.shape[0]))
    overlap_formula=float(np.sum(d*d)-edge4)
    assert abs(total-spectral)<1e-8
    assert abs(O-overlap_formula)<1e-8

    vals=[]
    n=H.shape[0]
    for bits in product([0,1], repeat=n):
        I=[i for i,b in enumerate(bits) if b==0]
        J=[i for i,b in enumerate(bits) if b==1]
        B=H[np.ix_(I,J)]
        vals.append(e2_singular(B))
    avg=sum(vals)/(2**n)
    assert abs(avg-D/16)<1e-8
    print(f"H{idx}: wedge={total:.12g} disjoint={D:.12g} overlap={O:.12g} avg_cut={avg:.12g}")

spectra=[
    [1,1],
    [10,1],
    [1,0.4,0.3,0.3],
    [1,0.1]*1 + [0.1]*9,
    [0.7,0.6,0.5,0.4],
]
for xs in spectra:
    xs=sorted(xs,reverse=True)
    T=sum(xs[1:])
    g2=T/4
    theta=sum(x/(g2+x) for x in xs)
    assert theta>=1.6-1e-12
    print(f"ridge: x={xs} T={T:.12g} gamma={math.sqrt(g2):.12g} theta={theta:.12g}")

A=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,-1],[0,0,-1,1]],float)
ev=sorted(np.linalg.eigvalsh(A), reverse=True)
assert np.allclose(ev,[2,1,1,0])
print("target_eigenvalues=",ev)

for a in [Fraction(1,8),Fraction(1,4),Fraction(3,8)]:
    val=Fraction(1,1)/((1-2*a)*(1-a))
    print(f"alpha={a}: exact_negative_moment={val}")
assert Fraction(1,1)/((1-Fraction(1,2))*(1-Fraction(1,4))) == Fraction(8,3)
print("alpha=1/2: DIVERGES logarithmically because integral |x-y|^{-1} dxdy diverges")
print("QFORM_WEDGE_STAR_RIDGE_CHECK_PASS")
