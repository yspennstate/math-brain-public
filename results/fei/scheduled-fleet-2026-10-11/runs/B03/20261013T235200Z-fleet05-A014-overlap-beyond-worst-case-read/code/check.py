"""A014-bounded-intersection-v1.2: exact fixed-domain verification."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import argparse, hashlib, itertools, json, time

START=time.monotonic(); ASSERTIONS=0; BUDGET=60
def ck(x):
    global ASSERTIONS
    ASSERTIONS+=1
    assert x
    if time.monotonic()-START>BUDGET: raise TimeoutError('Frozen runtime budget')

def walsh(values):
    values=list(values); step=1
    while step<len(values):
        for i in range(0,len(values),step*2):
            for j in range(step):
                a,b=values[i+j],values[i+j+step]
                values[i+j],values[i+j+step]=a+b,a-b
        step*=2
    return values

def small_ln(x):
    z=(x-1)/(x+1)
    low=2*sum((z**(2*i+1)/F(2*i+1) for i in range(28)),F(0))
    return low,low+2*z**57/(57*(1-z*z))
LN2=small_ln(F(2))
@lru_cache(None)
def lg(x):
    x=F(x); exponent=0
    while x>=2: x/=2; exponent+=1
    while x<1: x*=2; exponent-=1
    lo,hi=small_ln(x)
    return lo/LN2[1]+exponent,hi/LN2[0]+exponent

@lru_cache(None)
def entropy(n,hist):
    low=high=F(0); denominator=1<<(2*n)
    for v,count in hist:
        if v:
            p=F(v*v,denominator); lo,hi=lg(1/p)
            low+=count*p*lo; high+=count*p*hi
    return low,high

def owner_score(A,L):
    w=L.bit_count(); pred=0; ratio=F(1)
    rank=0
    for j in range(L.bit_length()):
        if L&(1<<j):
            rank+=1
            if A&(1<<j): ratio*=F(rank,(A&pred).bit_count()+1)
            pred|=1<<j
    rarity=w*A.bit_count() if 120*A.bit_count()<11*w else 0
    return ratio**6 * (1<<(5*rarity))

def analyse(n,edges):
    N=len(edges); widths=[x.bit_count() for x in edges]; W=max(widths)
    t=max([1]+[(a&b).bit_count() for a,b in itertools.combinations(edges,2)])
    mu=sum((F(1,1<<w) for w in widths),F(0)); theta=(1<<t)*mu
    Q=2*sum((w*F(1,1<<w) for w in widths),F(0))
    truth=[int(any(x&e==e for e in edges)) for x in range(1<<n)]
    full=walsh([2*x-1 for x in truth]); denom=1<<(2*n)
    ck(sum(x*x for x in full)==denom)
    I=sum((F(A.bit_count()*x*x,denom) for A,x in enumerate(full)),F(0))
    lo,hi=entropy(n,tuple(sorted(Counter(abs(x) for x in full).items())))
    ck(hi<=4*I)
    good=[any(A&e==A for e in edges) for A in range(1<<n)]
    owner_checks=0
    for A in range(1,1<<n):
        if good[A] and full[A]:
            candidates=[e for e in edges if A&e==A]
            selected=min(candidates,key=lambda e:(owner_score(A,e),e))
            ck(all(owner_score(A,selected)<=owner_score(A,e) for e in candidates)); owner_checks+=1
    residual_norms=[]; crosses=[]; alpha_sum=F(0); bad_energy=F(0)
    for j in range(n):
        incident=[e for e in edges if e&(1<<j)]
        if not incident: continue
        others=[k for k in range(n) if k!=j]; size=1<<(n-1)
        ideal=[]; residual=[]; derivative=[]; blocking=[]
        for z in range(size):
            x=sum(((z>>k)&1)<<others[k] for k in range(n-1)); xp=x|(1<<j)
            us=[int(x&(e^(1<<j))==e^(1<<j)) for e in incident]
            s=sum(us); d=truth[xp]-truth[x]
            b=int(any(x&e==e for e in edges if not e&(1<<j)))
            ck(d==int(s>0)*(1-b)); ck((s-d)**2<=s*(s-1)+s*b)
            ideal.append(us); derivative.append(d); residual.append(d-s); blocking.append(s*b)
        a=sum((F(2,1<<e.bit_count()) for e in incident),F(0))
        alpha=F(sum(derivative),size); alpha_sum+=alpha
        r2=F(sum(x*x for x in residual),size)
        C=F(sum(sum(us)*(sum(us)-1) for us in ideal),size)
        bmean=F(sum(blocking),size); mu_non=mu-a/2
        ck(C<=F(1<<(t-1))*a*a)
        ck(bmean<=F(1<<t)*a*mu_non)
        ck(r2<=theta*a); ck(alpha>=(1-theta)*a)
        ck(alpha>=a-C/2-bmean)
        transforms=[walsh([us[k] for us in ideal]) for k in range(len(incident))]
        rh=walsh(residual); dh=walsh(derivative)
        spectral_cross=0
        for T in range(size):
            vals=[row[T] for row in transforms]
            # Integer FWHT uses (-1)^bit, whereas a positive conjunction
            # uses coordinates 2*bit-1. All amplitudes at T share this sign.
            ck(all(((-1)**T.bit_count())*x>=0 for x in vals))
            ck(dh[T]==sum(vals)+rh[T])
            cross=sum(vals)**2-sum(x*x for x in vals)
            ck(cross>=0); spectral_cross+=cross
            ck(dh[T]**2<=2*(sum(x*x for x in vals)+cross)+2*rh[T]**2)
            A=(1<<j)|sum(1<<others[k] for k in range(n-1) if T&(1<<k))
            if not good[A]:
                ck(sum(vals)==0); ck(dh[T]==rh[T]); bad_energy+=F(dh[T]**2,size*size)
        ck(F(spectral_cross,size*size)==C)
        residual_norms.append(r2); crosses.append(C)
    ck(alpha_sum==I); ck(I>=(1-theta)*Q)
    ck(sum(residual_norms)<=theta*Q); ck(sum(crosses)<=theta*Q)
    ck(bad_energy<=sum(residual_norms))
    if mu<1:
        ck(N<=1<<W)
        for j in range(n):
            total=sum((F(1,1<<e.bit_count()) for e in edges if e&(1<<j)),F(0))
            for e in edges:
                if e&(1<<j): ck(total<=1)
    scale=10**6
    low_rounded=F((lo/I*scale).__floor__(),scale)
    high_rounded=F((hi/I*scale).__ceil__(),scale)
    return {'n':n,'edges':edges,'t':t,'W':W,'mu':str(mu),'theta_W':str(theta*W),
            'I':str(I),'H_over_I_interval':[str(low_rounded),str(high_rounded)],
            'sparse_hypothesis':theta*W<=F(1,16),'owner_checks':owner_checks}

def antichains4():
    masks=list(range(1,16))
    for bits in range(1,1<<15):
        edges=[e for k,e in enumerate(masks) if bits&(1<<k)]
        if all((a&b)!=a and (a&b)!=b for a,b in itertools.combinations(edges,2)): yield edges

def uniform5():
    for w in range(1,6):
        masks=[e for e in range(1,32) if e.bit_count()==w]
        for bits in range(1,1<<len(masks)):
            yield [e for k,e in enumerate(masks) if bits&(1<<k)]

def affine(q):
    ck(all(q%d for d in range(2,int(q**.5)+1)))
    lines=[frozenset(x*q+(a*x+b)%q for x in range(q)) for a in range(q) for b in range(q)]
    ck(len(lines)==q*q); ck(all(len(L)==q for L in lines))
    ck(all(len(L&M)<=1 for L,M in itertools.combinations(lines,2)))
    ck(all(sum(i in L for L in lines)==q for i in range(q*q)))
    pressure=F(2*q**3,1<<q); ck(pressure<=F(1,16))
    return {'q':q,'points':q*q,'gates':q*q,'read':q,'theta_W':str(pressure),
            'incidence_sha256':hashlib.sha256(json.dumps([sorted(L) for L in lines]).encode()).hexdigest()}

parser=argparse.ArgumentParser(); parser.add_argument('--pilot',action='store_true'); parser.add_argument('--out',required=True)
args=parser.parse_args(); BUDGET=60 if args.pilot else 1200
rows=[]
for e in antichains4(): rows.append(analyse(4,e))
ck(len(rows)==166)
if not args.pilot:
    for i,e in enumerate(uniform5(),1):
        rows.append(analyse(5,e))
        if i%100==0: print(json.dumps({'completed_n5':i,'elapsed_seconds':time.monotonic()-START}),flush=True)
    ck(len(rows)==2275)
affines=[] if args.pilot else [affine(q) for q in (19,23)]
constant=24+(F(216,5)+F(11,16)+F(3,32))*F(16,15)
ck(constant==F(10637,150)); ck(constant<71)
ck(F(2*18**3,2**18)<F(1,16)); ck(19**3<2*18**3)
summary={'helper':'A014-bounded-intersection-v1.2','assertions':ASSERTIONS,
         'elapsed_seconds':time.monotonic()-START,'cases':len(rows),
         'linear_covers':sum(r['t']==1 for r in rows),'sparse_covers':sum(r['sparse_hypothesis'] for r in rows),
         'finite_H_le_4I':'CERTIFIED_BY_RATIONAL_INTERVALS','constant':str(constant),'affines':affines}
Path(args.out).parent.mkdir(parents=True,exist_ok=True)
Path(args.out).write_text(json.dumps({'summary':summary,'cases':rows},indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary))
