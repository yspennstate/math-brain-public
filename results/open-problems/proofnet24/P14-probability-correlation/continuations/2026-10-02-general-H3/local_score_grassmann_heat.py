"""Exact conditional marked score for a twin-pair two-boundary gadget.

Tests whether higher score dependence stays inside the first response space.
All Grassmann arithmetic is independent explicit bitmask exterior algebra.
Interior fields come first; two boundary Grassmann pairs come last.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def add(A,B):
    out=dict(A)
    for m,c in B.items():
        out[m]=out.get(m,F(0))+c
        if not out[m]:del out[m]
    return out


def scale(A,c):return {m:c*v for m,v in A.items()if c*v}


def mul(A,B):
    out={}
    for m,a in A.items():
        for n,b in B.items():
            if m&n:continue
            inversions=sum((n&((1<<i)-1)).bit_count()for i in range(8)if m&(1<<i))
            key=m|n;v=a*b*(-1 if inversions%2 else 1)
            out[key]=out.get(key,F(0))+v
            if not out[key]:del out[key]
    return out


def var(i):return {1<<i:F(1)}


def expect_interior(A,derivative=False):
    # Covariance of the two interiors at marked conductance e=1 is
    # [[3/8,1/8],[1/8,3/8]], and its e derivative is -vv^T,
    # v=(1/4,-1/4). Mask order is bar0,psi0,bar1,psi1.
    moments={0:F(1),3:F(3,8),12:F(3,8),9:F(1,8),6:F(-1,8),15:F(1,8)}
    derivatives={0:F(0),3:F(-1,16),12:F(-1,16),9:F(1,16),6:F(-1,16),15:F(-1,16)}
    M=derivatives if derivative else moments
    out={}
    for m,c in A.items():
        v=c*M.get(m&15,F(0))
        key=m>>4
        if v:out[key]=out.get(key,F(0))+v
    return {m:c for m,c in out.items()if c}


def main():
    # Each terminal has unit-conductance spokes to both boundary vertices,
    # giving the common harmonic exit row (1/2,1/2). Mark e joins terminals.
    bars=[add(var(0),scale(add(var(4),var(6)),F(1,2))),
          add(var(2),scale(add(var(4),var(6)),F(1,2))),var(4),var(6)]
    psis=[add(var(1),scale(add(var(5),var(7)),F(1,2))),
          add(var(3),scale(add(var(5),var(7)),F(1,2))),var(5),var(7)]
    q=[mul(b,p)for b,p in zip(bars,psis)]
    Ce=mul(q[0],q[1]);V=add(q[0],q[1])
    for x,y in [(0,1),(0,2),(0,3),(1,2),(1,3)]:V=add(V,scale(mul(q[x],q[y]),F(-1)))
    powers=[{0:F(1)}]
    for k in range(1,5):powers.append(mul(powers[-1],V))
    Fs=[];Ds=[]
    for k in range(5):
        Fs.append(scale(expect_interior(powers[k]),F(1,factorial(k))))
        d=scale(expect_interior(powers[k],True),F(1,factorial(k)))
        if k:d=add(d,scale(expect_interior(mul(Ce,powers[k-1])),F(-1,factorial(k-1))))
        Ds.append(d)
    # Arithmetic after integration uses boundary masks 0..15 only.
    inv=[{0:F(1)}]
    for k in range(1,5):
        v={}
        for i in range(1,k+1):v=add(v,mul(Fs[i],inv[k-i]))
        inv.append(scale(v,F(-1)))
    score=[]
    for k in range(5):
        v={}
        for i in range(k+1):v=add(v,mul(Ds[i],inv[k-i]))
        score.append(v)
    labels={0:'constant',3:'bar_s0 psi_s0',12:'bar_s1 psi_s1',9:'bar_s0 psi_s1',6:'psi_s0 bar_s1',15:'q_s0 q_s1'}
    out={'arithmetic':'Fraction exact exterior algebra',
         'local_graph':'terminal twin pair joined by marked edge e; four unit spokes to two boundary vertices',
         'conditional_covariance':[['3/8','1/8'],['1/8','3/8']],
         'first_response_space':'span of boundary field s0-s1',
         'conditional_partition':[{labels.get(m,str(m)):str(c)for m,c in p.items()}for p in Fs],
         'marked_score':[{labels.get(m,str(m)):str(c)for m,c in p.items()}for p in score]}
    assert score[1].get(15,F(0))==0
    # Whether this assertion holds is the research question; record explicitly.
    out['higher_score_quartic_exists']=any(p.get(15,F(0))for p in score[2:])
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
