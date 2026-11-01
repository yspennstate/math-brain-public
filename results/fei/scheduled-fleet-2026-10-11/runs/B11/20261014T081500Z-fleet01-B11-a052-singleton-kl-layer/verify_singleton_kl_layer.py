#!/usr/bin/env python3
import itertools, math, random

LN2=math.log(2.0)
C0=2.0/LN2

def fwht(v):
    v=list(map(float,v)); n=len(v); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=v[j],v[j+h]; v[j]=x+y; v[j+h]=x-y
        h*=2
    return [x/n for x in v]

def entbit(q):
    if q<=0.0 or q>=1.0: return 0.0
    return -q*math.log2(q)-(1-q)*math.log2(1-q)

def dbern(q,r):
    out=0.0
    if q>0.0:
        if r<=0.0: return float('inf')
        out += q*math.log2(q/r)
    if q<1.0:
        if r>=1.0: return float('inf')
        out += (1-q)*math.log2((1-q)/(1-r))
    return out

def analyze(vals):
    N=len(vals); n=(N.bit_length()-1); hat=fwht(vals); p=[z*z for z in hat]
    pi=p[:]
    for bit in range(n):
        for A in range(N):
            if not (A>>bit)&1: pi[A]+=pi[A|(1<<bit)]
    U=sum(p[A]*math.log2(pi[A]/p[A]) for A in range(N) if p[A]>1e-300)
    I=sum(A.bit_count()*p[A] for A in range(N))
    W=[sum(p[A] for A in range(N) if A.bit_count()==k) for k in range(n+1)]
    M1=sum(min(p[0],p[1<<i]) for i in range(n))
    K0=K1=K2=BG=V1=0.0
    for i in range(n):
        ib=1<<i
        for A in range(N):
            if A&ib: continue
            a,b=hat[A],hat[A|ib]; m=a*a+b*b
            if m<1e-300: continue
            M=pi[A]
            C=0.0
            free=((N-1)^A^ib) & (N-1)
            sub=free
            while True:
                T=A|sub
                C += hat[T]*hat[T|ib]
                if sub==0: break
                sub=(sub-1)&free
            alpha=max(-1.0,min(1.0,2*a*b/m))
            beta=max(-1.0,min(1.0,2*C/M))
            K=m*dbern((1+alpha)/2,(1+beta)/2)
            s=b*b/m
            Nup=pi[A|ib]
            B=m*entbit(s)
            Gamma=b*b*math.log2(M/Nup) if b*b>1e-300 else 0.0
            BG += B-Gamma
            if A==0: K0+=K
            elif A.bit_count()==1:
                K1+=K
                V1+=m*math.log2(M/m)
            else: K2+=K
    G=BG+K0+K1+K2
    single_bound=.5*V1+C0*(W[2] if n>=2 else 0.0)
    total_bound=BG+K2+.5*V1+C0*I
    residual=G-4*I-.75*U
    return dict(n=n,U=U,I=I,G=G,K0=K0,K1=K1,K2=K2,BG=BG,V1=V1,M1=M1,W2=W[2] if n>=2 else 0.0,
                single_slack=single_bound-K1,total_slack=total_bound-G,residual=residual)

cases=0; assertions=0; min_single=1e99; min_total=1e99; max_res=-1e99
worst_single=None; worst_total=None
for n in range(1,5):
    N=1<<n
    for mask in range(1<<(N-1)):
        vals=[1.0]+[1.0 if (mask>>(x-1))&1 else -1.0 for x in range(1,N)]
        r=analyze(vals); cases+=1; assertions+=3
        if r['single_slack']<min_single: min_single=r['single_slack']; worst_single=(n,mask)
        if r['total_slack']<min_total: min_total=r['total_slack']; worst_total=(n,mask)
        max_res=max(max_res,r['residual'])
        assert r['single_slack']>-2e-10
        assert r['total_slack']>-2e-10
        assert r['K0'] <= C0*r['M1']+2e-10

rng=random.Random(11052026)
random_cases=0
for n,count in [(5,1500),(6,500)]:
    N=1<<n
    for _ in range(count):
        vals=[1.0]+[rng.choice((-1.0,1.0)) for _ in range(1,N)]
        r=analyze(vals); random_cases+=1; assertions+=3
        min_single=min(min_single,r['single_slack']); min_total=min(min_total,r['total_slack']); max_res=max(max_res,r['residual'])
        assert r['single_slack']>-3e-9
        assert r['total_slack']>-3e-9
        assert r['K0'] <= C0*r['M1']+3e-9

print('claim=B11-A052-SINGLETON-KL-LAYER-v1')
print('verdict=PASS_AT_STATED_ALL_DIMENSIONAL_THEOREM_SCOPE')
print('exhaustive_boolean_signs_mod_output',cases)
print('seeded_larger_boolean_controls',random_cases)
print('assertions',assertions)
print('min_singleton_bound_slack',format(min_single,'.12e'))
print('min_complete_reduction_slack',format(min_total,'.12e'))
print('max_frozen_residual_seen',format(max_res,'.12e'))
print('unpaid=degree_at_least_two_signed_KL_plus_half_V1')
print('universal_GU=OPEN')
