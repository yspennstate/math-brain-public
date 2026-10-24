#!/usr/bin/env python3
from __future__ import annotations
import itertools, math, random, json, argparse, hashlib
from collections import defaultdict
SEED=20260920
BASE=12.04

def parts(n):
    b=[]
    def rec(i):
        if i==n:
            yield tuple(tuple(x) for x in b); return
        for j in range(len(b)):
            b[j].append(i); yield from rec(i+1); b[j].pop()
        b.append([i]); yield from rec(i+1); b.pop()
    yield from rec(0)

def cnt(mask,P): return tuple(sum((mask>>i)&1 for i in q) for q in P)

def sw(mask,j,k):
    if ((mask>>j)&1)!=((mask>>k)&1): mask^=(1<<j)|(1<<k)
    return mask

def peval(C,x):
    s=0
    for m in C:
        if not (m & ~x): s^=1
    return s

def deriv(C,i): return {m^(1<<i) for m in C if (m>>i)&1}

def inv(C,P,V,nonlin=False):
    V=set(V); vm=sum(1<<i for i in V); groups=defaultdict(list)
    for m in range(1<<(max(V,default=-1)+1)):
        if m & ~vm: continue
        if nonlin and m.bit_count()<2: continue
        groups[cnt(m,P)].append(m)
    return all(len({m in C for m in ms})==1 for ms in groups.values())

def bad(C,P,n):
    B=[]; W={}
    for i in range(n):
        D=deriv(C,i); V=[j for j in range(n) if j!=i]
        if inv(D,P,V): continue
        B.append(i)
        for q in P:
            a=[j for j in q if j!=i]
            done=False
            for j,k in itertools.combinations(a,2):
                if {sw(m,j,k) for m in D}!=D:
                    W[i]=(j,k); done=True; break
            if done: break
        assert i in W
    return B,W

def restrict(C,fixed):
    fm=sum(1<<i for i in fixed); zm=sum(1<<i for i,v in fixed.items() if not v); out=set()
    for m in C:
        if m&zm: continue
        q=m&~fm
        if q in out: out.remove(q)
        else: out.add(q)
    return out

def walsh(v):
    a=list(v); h=1
    while h<len(a):
        for s in range(0,len(a),2*h):
            for j in range(s,s+h):
                u,w=a[j],a[j+h]; a[j],a[j+h]=u+w,u-w
        h*=2
    return a

def measure(v):
    N=len(v); n=N.bit_length()-1
    inf=[]
    for i in range(n): inf.append(sum(v[x]!=v[x^(1<<i)] for x in range(N))/N)
    J=sum(min(x,1-x) for x in inf)
    H=0.0
    for z in walsh(v):
        if z:
            p=(z/N)**2; H-=p*math.log2(p)
    return H,J,inf

def hvals(n,P,rng):
    keys=list(itertools.product(*[range(len(q)+1) for q in P])); tab={k:rng.choice((-1,1)) for k in keys}
    return [tab[cnt(x,P)] for x in range(1<<n)]

def randpoly(n,r,rng): return {m for m in range(1<<n) if m.bit_count()<=r and rng.getrandbits(1)}

def check_case(n,P,r,C,h):
    B,W=bad(C,P,n); F=[h[x]*(1 if peval(C,x)==0 else -1) for x in range(1<<n)]
    H,J,inf=measure(F); q=2**(-r); phi=(-q*math.log2(q)-(1-q)*math.log2(1-q))/q; CC=max(BASE+math.log2(max(1,len(P))),phi+2/math.log(2)); assert H<=CC*J+1e-10
    for i in B:
        assert min(inf[i],1-inf[i])+1e-12>=2**(-r)
        j,k=W[i]; D=deriv(C,i); Q=D.symmetric_difference({sw(m,j,k) for m in D})
        diff=sum(peval(Q,x) for x in range(1<<n))/(1<<n); assert diff+1e-12>=2**(-(r-1))
    R=[i for i in range(n) if i not in B]
    for z in range(1<<len(B)):
        Q=restrict(C,{i:(z>>t)&1 for t,i in enumerate(B)})
        assert inv(Q,P,R,True)
    return len(B),H,J

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output'); a=ap.parse_args(); rng=random.Random(SEED)
    out={'status':'PASS','seed':SEED,'sample_cases':0,'bad_coordinate_checks':0,'leaf_structure_checks':0,'max_H_over_J':0.0,'monomial_deletion_obstruction':[]}
    for n in range(2,7):
        ps=list(parts(n))
        for _ in range(300):
            P=rng.choice(ps); r=rng.randint(2,min(5,n)); C=randpoly(n,r,rng); h=hvals(n,P,rng)
            b,H,J=check_case(n,P,r,C,h); out['sample_cases']+=1; out['bad_coordinate_checks']+=b; out['leaf_structure_checks']+=2**b
            if J: out['max_H_over_J']=max(out['max_H_over_J'],H/J)
    for r in range(2,11):
        n=r+1; P=(tuple(range(n)),); C={(1<<r)-1}; h=[1]*(1<<n); B,_=bad(C,P,n); F=[1 if peval(C,x)==0 else -1 for x in range(1<<n)]; H,J,inf=measure(F)
        assert set(B)==set(range(r)); je=min(inf[0],1-inf[0]); assert abs(je-2**(1-r))<1e-12
        req=2*len(B)/sum(min(inf[i],1-inf[i]) for i in B); assert abs(req-2**r)<1e-9
        out['monomial_deletion_obstruction'].append({'degree':r,'dimension':n,'bad_coordinates':len(B),'j_each':je,'required_C_for_2bit_deletion':req,'H_over_J':H/J})
    out['hereditary_internal_constants']=[]
    for rr in range(2,13):
        q=2**(-rr); hh=-q*math.log2(q)-(1-q)*math.log2(1-q); ph=hh/q
        out['hereditary_internal_constants'].append({'degree':rr,'phi':ph,'phi_plus_recombination':ph+2/math.log(2)})
    out['scope']='Exact ANF/influence/leaf-structure assertions with floating entropy sanity checks; all-dimensional proof is in report.'
    txt=json.dumps(out,indent=2,sort_keys=True)
    if a.output: open(a.output,'w').write(txt+'\n')
    else: print(txt)
if __name__=='__main__': main()
