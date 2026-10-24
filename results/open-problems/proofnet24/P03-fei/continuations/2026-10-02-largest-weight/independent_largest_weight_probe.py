"""Stress checks for a proposed LTF split argument, not a theorem certificate."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import log, log2, sqrt, floor
from pathlib import Path
import random
import json


def walsh(v):
    out=list(v);width=1
    while width<len(out):
        for left in range(0,len(out),2*width):
            for i in range(left,left+width):
                u,z=out[i],out[i+width]
                out[i],out[i+width]=u+z,u-z
        width*=2
    return out


def entropy(masses):
    return -sum(x*log2(x) for x in masses if x)


def binary(q):
    return entropy([q,1-q])


report={'status':'PASS (finite checks only)','cases':0,'worst':{},
        'scope':'Checks proposed route inequalities numerically; no novelty or general proof claim'}
def record(name,value,weights,threshold):
    old=report['worst'].get(name)
    if old is None or value>old['value']:
        report['worst'][name]={'value':value,'weights':weights,'threshold':threshold}


def check(weights,t):
    weights=tuple(sorted(weights))
    d=len(weights)-1;N=1<<d;w=weights[-1]
    if not w:return
    scores=[sum(v*(2*((x>>i)&1)-1)for i,v in enumerate(weights[:-1]))for x in range(N)]
    fm=[1 if s-w>t else -1 for s in scores]
    fp=[1 if s+w>t else -1 for s in scores]
    B=[(u-v)//2 for u,v in zip(fp,fm)]
    A=[(u+v)//2 for u,v in zip(fp,fm)]
    alpha=F(sum(B),N)
    positive=sum(x==1 for x in fp)+sum(x==1 for x in fm)
    if positive in(0,2*N):return
    assert alpha>0
    p=F(min(positive,2*N-positive),2*N)
    assert alpha<=2*p
    ah,bh=walsh(A),walsh(B)
    P=[F(a*a+b*b,N*N)for a,b in zip(ah,bh)]
    Q=[F(b*b,N*N*alpha)for b in bh]
    assert sum(P)==sum(Q)==1
    assert Q[0]==alpha
    assert all(px>=alpha*qx for px,qx in zip(P,Q))
    K=len(weights)
    L=log(1/float(p));kap=float(F(sum(v*v for v in weights[:-1]),w*w))
    M=max(1,kap,L)
    Pdeg=[sum(v for s,v in enumerate(P)if s.bit_count()==k)for k in range(d+1)]
    Qdeg=[sum(v for s,v in enumerate(Q)if s.bit_count()==k)for k in range(d+1)]
    for k in range(1,d+1):
        low=float(sum(Qdeg[:k+1]))
        record('Q_low_mass_over_sqrt_k_M',low/sqrt(k/M),list(weights),t)
        tail=float(sum(Pdeg[k:]))
        record('P_tail_over_alpha_sqrt_M_k',tail/(float(alpha)*sqrt(M/k)),list(weights),t)
    D=sum(float(q)*log2(float(q/px))for q,px in zip(Q,P)if q)
    Pb,Qb={0:Pdeg[0]},{0:Qdeg[0]}
    for k in range(1,d+1):
        label=('j',floor(log2(k/M)))
        Pb[label]=Pb.get(label,F(0))+Pdeg[k]
        Qb[label]=Qb.get(label,F(0))+Qdeg[k]
    Db=sum(float(q)*log2(float(q/Pb[k]))for k,q in Qb.items()if q)
    assert Db<=D+1e-10
    cond=sum(float(px)*binary(float(alpha*qx/px))for px,qx in zip(P,Q)if px)
    full_entropy=entropy([float(F(a*a,N*N))for a in ah]+[float(F(b*b,N*N))for b in bh])
    avg_branch_entropy=(entropy([float(F(z*z,N*N))for z in walsh(fm)])+
                        entropy([float(F(z*z,N*N))for z in walsh(fp)]))/2
    delta=full_entropy-avg_branch_entropy
    assert cond-1e-10<=delta<=2*cond+1e-10
    assert cond<=binary(float(alpha))-float(alpha)*D+1e-10
    record('full_KL_deficit_bits',log2(1/float(alpha))-D,list(weights),t)
    record('binned_KL_deficit_bits',log2(1/float(alpha))-Db,list(weights),t)
    record('conditional_bit_entropy_over_alpha',cond/float(alpha),list(weights),t)
    record('entropy_split_increment_over_alpha',delta/float(alpha),list(weights),t)
    record('negative_bin_absolute_mean',sum(float(q)*abs(k[1])for k,q in Qb.items()
                                        if isinstance(k,tuple)and k[1]<0),list(weights),t)
    report['cases']+=1


for n in range(1,7):
    for weights in combinations_with_replacement(range(4),n):
        if not any(weights):continue
        scores=sorted(set(sum(v*(2*((x>>i)&1)-1)for i,v in enumerate(weights))for x in range(1<<n)))
        for t in scores:check(weights,t)

rng=random.Random(271828)
for n in(7,8,10,12,14):
    families=[tuple([1]*n),tuple(range(1,n+1)),tuple(1<<i for i in range(n)),
              tuple([1]*(n-1)+[1000]),tuple([0]*(n//2)+[1]*(n-n//2)),
              tuple(rng.randrange(0,30)for _ in range(n)),
              tuple([1]*(n//2)+[3]*(n-n//2))]
    for weights in families:
        scores=sorted(set(sum(v*(2*((x>>i)&1)-1)for i,v in enumerate(weights))for x in range(1<<n)))
        chosen={0,1,len(scores)//2,len(scores)-2,len(scores)-1}
        chosen.update(rng.randrange(len(scores))for _ in range(13))
        for j in chosen:
            if 0<=j<len(scores):check(weights,scores[j])

out=Path(__file__).with_name('independent_largest_weight_probe_checks.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
