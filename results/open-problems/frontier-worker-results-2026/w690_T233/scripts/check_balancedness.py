"""Exact arithmetic audit of balancedness identity and Wishart polynomial witness."""
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import json

def pairings(items):
    if not items:
        yield []
        return
    a=items[0]
    for j in range(1,len(items)):
        for rest in pairings(items[1:j]+items[j+1:]):
            yield [(a,items[j])]+rest

def trace_moment_coeffs(k):
    # tr((G^T G)^k): factors (b_t,a_t),(b_t,a_(t+1)).
    factors=[(t,k+a) for t in range(k) for a in [t,(t+1)%k]]
    count=Counter()
    for pairing in pairings(list(range(2*k))):
        parent=list(range(2*k))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        def union(x,y):
            parent[find(x)]=find(y)
        for i,j in pairing:
            union(factors[i][0],factors[j][0])
            union(factors[i][1],factors[j][1])
        free=len({find(x) for x in range(2*k)})
        assert free<=k+1
        count[free]+=1
    return dict(count)

def trans(a):
    return [list(x) for x in zip(*a)]
def mul(a,b):
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def scale(c,a):
    return [[c*x for x in row] for row in a]
def add(a,b):
    return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def sub(a,b):
    return add(a,scale(-1,b))
def identity(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]
def product(mats):
    out=identity(len(mats[0][0]))
    for mat in mats:
        out=mul(mat,out)
    return out

def check():
    expected=[{2:1},{3:2,2:1},{4:5,3:6,2:4}]
    actual=[trace_moment_coeffs(k) for k in [1,2,3]]
    assert actual==expected
    a=F(1,4);C0,C1,C2,C3=map(F,[1,1,2,5])
    gram=C0-2*a*C1+a*a*C2
    hcost=C1-2*a*C2+a*a*C3
    vcost=(C0-a*C1)**2
    difference=hcost-vcost
    assert (gram,hcost,vcost,difference,difference/gram)==(F(5,8),F(5,16),F(9,16),F(-1,4),F(-2,5))
    # Finite exact example, arbitrary fixed normalization: verifies ALL terms of discrete identity.
    w=[[[F(x)] for x in [1,2,-1,1]],
       [[F((i==j)*2+((i+j)%3==0)) for j in range(4)] for i in range(4)],
       [[F((i==j)-((2*i+j)%4==0)) for j in range(4)] for i in range(4)],
       [[F(x) for x in [-1,1,2,0]]]]
    x=[[F(1),F(2)]];y=[[F(3),F(6)]]
    alpha=F(1,8);eta=F(1,10000)
    prefix=[x]
    for wi in w:
        prefix.append(mul(wi,prefix[-1]))
    residual=sub(scale(alpha,prefix[-1]),y)
    suffix=[None]*(len(w)+1);suffix[-1]=identity(1)
    for i in range(len(w)-1,-1,-1):
        suffix[i]=mul(suffix[i+1],w[i])
    grad=[scale(alpha,mul(mul(trans(suffix[i+1]),residual),trans(prefix[i]))) for i in range(len(w))]
    wp=[sub(wi,scale(eta,gi)) for wi,gi in zip(w,grad)]
    for i in range(len(w)-1):
        di=sub(mul(trans(w[i+1]),w[i+1]),mul(w[i],trans(w[i])))
        dip=sub(mul(trans(wp[i+1]),wp[i+1]),mul(wp[i],trans(wp[i])))
        rhs=scale(eta*eta,sub(mul(trans(grad[i+1]),grad[i+1]),mul(grad[i],trans(grad[i]))))
        assert sub(dip,di)==rhs
    return {"status":"pass","wick_coefficients":actual,"witness":{"gram":str(gram),"H_cost":str(hcost),
            "V_cost":str(vcost),"difference":str(difference),"rayleigh_over_m":str(difference/gram)},
            "discrete_identity":"all three internal boundaries verified by exact rational matrices",
            "scope":"symbolic/arithmetic audit, not a Gaussian training experiment or convergence proof"}

if __name__=="__main__":
    result=check()
    dest=Path(__file__).resolve().parents[1]/"logs"/"balancedness_check.json"
    dest.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result))
