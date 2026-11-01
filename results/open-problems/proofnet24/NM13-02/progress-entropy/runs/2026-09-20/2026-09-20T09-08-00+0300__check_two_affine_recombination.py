#!/usr/bin/env python3
import itertools, math, random, json, time
from functools import lru_cache

TOL=1e-9
C8=8.0*(-(1/8)*math.log2(1/8)-(7/8)*math.log2(7/8))
K3=4.0*(-0.25*math.log2(0.25)-0.75*math.log2(0.75))
TARGET=24.0

def h2(p):
    if p<=0.0 or p>=1.0:
        return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

def fwht(a):
    a=list(map(float,a)); n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return [x/n for x in a]

def entropy_truth(truth):
    H=0.0
    for x in fwht(truth):
        p=x*x
        if p>0: H-=p*math.log2(p)
    return H

def influences_truth(truth,n):
    N=1<<n
    return [sum(1 for x in range(N) if truth[x]!=truth[x^(1<<i)])/N for i in range(n)]

def B_i_truth(truth,n,i):
    hats=fwht(truth); N=1<<n
    B=0.0
    for s in range(N):
        if (s>>i)&1: continue
        p0=hats[s]*hats[s]
        p1=hats[s|(1<<i)]*hats[s|(1<<i)]
        q=p0+p1
        if q>0:
            B += q*h2(p1/q)
    return B

def all_affine_flats(n, include_empty=True):
    N=1<<n
    linear=[]
    for mask in range(1<<(N-1)):
        V={0}
        for x in range(1,N):
            if (mask>>(x-1))&1: V.add(x)
        ok=True
        for a in V:
            for b in V:
                if (a^b) not in V:
                    ok=False; break
            if not ok: break
        if ok: linear.append(frozenset(V))
    flats=set()
    for V in linear:
        for x in range(N):
            flats.add(frozenset(y^x for y in V))
    if include_empty: flats.add(frozenset())
    return sorted(flats,key=lambda S:(len(S),tuple(sorted(S))))

def codim(A,n):
    if not A: return None
    return n-(len(A).bit_length()-1)

def all_quadratics(n):
    mons=[()] + [(i,) for i in range(n)] + [(i,j) for i in range(n) for j in range(i+1,n)]
    out=[]
    for mask in range(1<<len(mons)):
        vals=[]
        for x in range(1<<n):
            v=0
            for k,m in enumerate(mons):
                if (mask>>k)&1:
                    z=1
                    for i in m: z &= (x>>i)&1
                    v ^= z
            vals.append(v)
        out.append(tuple(vals))
    return out

def truth_state(q,A,B,n):
    return tuple(-1 if (q[x] ^ (x in A) ^ (x in B)) else 1 for x in range(1<<n))

def compress_set(A,n,i,b):
    if not A: return frozenset()
    out=[]
    lowmask=(1<<i)-1
    for x in A:
        if ((x>>i)&1)!=b: continue
        lo=x&lowmask
        hi=x>>(i+1)
        out.append(lo|(hi<<i))
    return frozenset(out)

def restrict_q(q,n,i,b):
    lowmask=(1<<i)-1
    vals=[]
    for y in range(1<<(n-1)):
        lo=y&lowmask; hi=y>>i
        x=lo|(b<<i)|(hi<<(i+1))
        vals.append(q[x])
    return tuple(vals)

def polar_row(q,n):
    q0=q[0]
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if q0 ^ q[1<<i] ^ q[1<<j] ^ q[(1<<i)|(1<<j)]:
                return i
    return None

def nonconstant_derivative_coordinate(truth,n):
    N=1<<n
    for i in range(n):
        vals={truth[x]*truth[x^(1<<i)] for x in range(N)}
        if len(vals)>1: return i
    return None

def restrict_truth(truth,n,i,b):
    lowmask=(1<<i)-1; out=[]
    for y in range(1<<(n-1)):
        lo=y&lowmask; hi=y>>i
        x=lo|(b<<i)|(hi<<(i+1))
        out.append(truth[x])
    return tuple(out)

def allocation_degree3(truth,n):
    if n==0: return 0.0
    i=nonconstant_derivative_coordinate(truth,n)
    if i is None: return 0.0
    B=B_i_truth(truth,n,i)
    return B+0.5*(allocation_degree3(restrict_truth(truth,n,i,0),n-1)+allocation_degree3(restrict_truth(truth,n,i,1),n-1))

def allocation_oneflat(q,A,n):
    if n==0: return 0.0
    if not A:
        return allocation_degree3(tuple(-1 if q[x] else 1 for x in range(1<<n)),n)
    r=codim(A,n)
    if r<=2:
        qq=tuple(q[x]^(x in A) for x in range(1<<n))
        return allocation_degree3(tuple(-1 if qq[x] else 1 for x in range(1<<n)),n)
    truth=truth_state(q,A,frozenset(),n)
    row=polar_row(q,n)
    if row is not None:
        i=row
    else:
        inf=influences_truth(truth,n)
        Bs=[B_i_truth(truth,n,i) for i in range(n)]
        cand=[(Bs[i]/inf[i],i) for i in range(n) if inf[i]>TOL]
        if not cand: return 0.0
        _,i=min(cand)
    Bloc=B_i_truth(truth,n,i)
    return Bloc+0.5*(allocation_oneflat(restrict_q(q,n,i,0),compress_set(A,n,i,0),n-1)+allocation_oneflat(restrict_q(q,n,i,1),compress_set(A,n,i,1),n-1))

def allocation_twoflat(q,A,B,n):
    if n==0: return 0.0
    if not A: return allocation_oneflat(q,B,n)
    if not B: return allocation_oneflat(q,A,n)
    if A==B:
        return allocation_degree3(tuple(-1 if q[x] else 1 for x in range(1<<n)),n)
    rA,rB=codim(A,n),codim(B,n)
    if rA<=2:
        qq=tuple(q[x]^(x in A) for x in range(1<<n))
        return allocation_oneflat(qq,B,n)
    if rB<=2:
        qq=tuple(q[x]^(x in B) for x in range(1<<n))
        return allocation_oneflat(qq,A,n)
    truth=truth_state(q,A,B,n)
    if rA==3 and rB==3:
        return allocation_degree3(truth,n)
    row=polar_row(q,n)
    if row is not None:
        i=row
    else:
        inf=influences_truth(truth,n)
        Bs=[B_i_truth(truth,n,i) for i in range(n)]
        cand=[(Bs[i]/inf[i],i) for i in range(n) if inf[i]>TOL]
        if not cand: return 0.0
        _,i=min(cand)
    Bloc=B_i_truth(truth,n,i)
    return Bloc+0.5*(allocation_twoflat(restrict_q(q,n,i,0),compress_set(A,n,i,0),compress_set(B,n,i,0),n-1)+allocation_twoflat(restrict_q(q,n,i,1),compress_set(A,n,i,1),compress_set(B,n,i,1),n-1))

def main():
    t0=time.time()
    out={"status":"PASS","constants":{"C8":C8,"K3":K3,"hereditary_target":TARGET}}
    flats4=all_affine_flats(4)
    high4=[A for A in flats4 if A and codim(A,4)>=3]
    max_terminal=(-1,None); terminal_cases=0; terminal_viol=0
    for ai,A in enumerate(high4):
        for bi,B in enumerate(high4):
            if A==B: continue
            truth=tuple(-1 if ((x in A)^(x in B)) else 1 for x in range(16))
            I=sum(influences_truth(truth,4)); H=entropy_truth(truth)
            ratio=H/I if I>TOL else 0.0
            if ratio>max_terminal[0]: max_terminal=(ratio,[ai,bi,len(A),len(B),len(A&B),I,H])
            if H>TARGET*I+TOL: terminal_viol+=1
            terminal_cases+=1
    if terminal_viol: out["status"]="FAIL"
    out["terminal_two_flat_dim4"]={"cases":terminal_cases,"violations":terminal_viol,"max_H_over_I":max_terminal[0],"witness":max_terminal[1]}
    flats3=all_affine_flats(3); qs3=all_quadratics(3)
    max_rec=(-1,None); rec_cases=0; rec_viol=0
    for qi,q in enumerate(qs3):
        for ai,A in enumerate(flats3):
            for bi,B in enumerate(flats3):
                truth=truth_state(q,A,B,3)
                I=sum(influences_truth(truth,3)); R=allocation_twoflat(q,A,B,3)
                ratio=R/I if I>TOL else 0.0
                if ratio>max_rec[0]: max_rec=(ratio,[qi,ai,bi,len(A),len(B),I,R])
                if R>TARGET*I+TOL: rec_viol+=1
                rec_cases+=1
    if rec_viol: out["status"]="FAIL"
    out["recursive_exhaustive_dim3"]={"cases":rec_cases,"violations":rec_viol,"max_R_over_I":max_rec[0],"witness":max_rec[1]}
    qs4=all_quadratics(4); rng=random.Random(20260920)
    max_samp=(-1,None); samp_viol=0; samples=5000
    for t in range(samples):
        q=qs4[rng.randrange(len(qs4))]
        A=flats4[rng.randrange(len(flats4))]
        B=flats4[rng.randrange(len(flats4))]
        truth=truth_state(q,A,B,4)
        I=sum(influences_truth(truth,4)); R=allocation_twoflat(q,A,B,4)
        ratio=R/I if I>TOL else 0.0
        if ratio>max_samp[0]: max_samp=(ratio,[t,len(A),len(B),I,R])
        if R>TARGET*I+TOL: samp_viol+=1
    if samp_viol: out["status"]="FAIL"
    out["recursive_sample_dim4"]={"samples":samples,"violations":samp_viol,"max_R_over_I":max_samp[0],"witness":max_samp[1]}
    out["elapsed_seconds"]=time.time()-t0
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
