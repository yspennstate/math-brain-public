#!/usr/bin/env python3
"""Finite corroboration of the all-dimensional rowwise-minimum GU cut."""
import math, random

LN2=math.log(2.0)
C0=2.0/LN2
C9=9.0/LN2

def fwht(v):
    v=list(map(float,v)); N=len(v); h=1
    while h<N:
        for a in range(0,N,2*h):
            for b in range(a,a+h):
                x,y=v[b],v[b+h]; v[b],v[b+h]=x+y,x-y
        h*=2
    return [x/N for x in v]

def dbern(q,r):
    out=0.0
    if q>0.0:
        if r<=0.0: return float('inf')
        out+=q*math.log2(q/r)
    if q<1.0:
        if r>=1.0: return float('inf')
        out+=(1-q)*math.log2((1-q)/(1-r))
    return out

def analyze(vals):
    N=len(vals); n=N.bit_length()-1; hat=fwht(vals); p=[z*z for z in hat]
    pi=p[:]
    for bit in range(n):
        for A in range(N):
            if not (A>>bit)&1: pi[A]+=pi[A|(1<<bit)]
    M1=sum(min(p[0],p[1<<i]) for i in range(n))
    K0=0.0; Krow=[0.0]*n
    for i in range(n):
        ib=1<<i
        for A in range(N):
            if A&ib or A.bit_count()>1: continue
            a,b=hat[A],hat[A|ib]; m=a*a+b*b
            if m<1e-300: continue
            M=pi[A]; free=((N-1)^A^ib)&(N-1); sub=free; C=0.0
            while True:
                T=A|sub; C+=hat[T]*hat[T|ib]
                if sub==0: break
                sub=(sub-1)&free
            alpha=max(-1.0,min(1.0,2*a*b/m))
            beta=max(-1.0,min(1.0,2*C/M))
            K=m*dbern((1+alpha)/2,(1+beta)/2)
            if A==0: K0+=K
            else: Krow[A.bit_length()-1]+=K
    minsum=0.0; oldsum=0.0; ternsum=0.0
    min_row_slack=1e300
    for j in range(n):
        jb=1<<j; r=s=vj=0.0
        for i in range(n):
            if i==j: continue
            ij=jb|(1<<i); r+=p[ij]
            m=p[jb]+p[ij]
            if m>1e-300: vj+=m*math.log2(pi[jb]/m)
        for S in range(N):
            if (S&jb) and S.bit_count()>=3: s+=p[S]
        old=.5*vj+r/LN2
        tern=C9*(2*r+s)
        assert Krow[j] <= old+3e-9
        assert Krow[j] <= tern+3e-9
        min_row_slack=min(min_row_slack,min(old,tern)-Krow[j])
        minsum+=min(old,tern); oldsum+=old; ternsum+=tern
    assert sum(Krow) <= minsum+3e-9
    assert K0 <= C0*M1+3e-9
    W2=sum(p[S] for S in range(N) if S.bit_count()==2)
    H3=sum(S.bit_count()*p[S] for S in range(N) if S.bit_count()>=3)
    assert sum(Krow) <= (36*W2+9*H3)/LN2+3e-9
    return min_row_slack, oldsum-minsum, ternsum-minsum, sum(Krow), minsum

def surgery(d):
    n=d+2; N=1<<n; out=[]
    for x in range(N):
        u=(x>>0)&1; v=(x>>1)&1
        z=x>>2
        g=-1 if (u==1 and v==0) else 1
        out.append(-1 if x==0 else g)
    return out

def surgery_global_bounds(d):
    """Closed-form bounds from the signed spectrum of the B11 family."""
    n=d+2; eps=2.0**(-d-1)
    A=(.5-eps)**2; B=(.5+eps)**2; C=eps**2
    mm=A+C; mp=B+C
    v1_lower=d*(mm*math.log2((.5-eps)/mm)+mp*math.log2((.5+eps)/mp))
    W2=A+(math.comb(n,2)-1)*C
    H3=C*(n*2.0**(n-1)-n-2*math.comb(n,2))
    old_lower=.5*v1_lower+C0*W2
    ternary=(36*W2+9*H3)/LN2
    return old_lower,ternary

def main():
    cases=assertions=0; minslack=1e300; strict_old=0; strict_tern=0
    for n in range(1,5):
        N=1<<n
        for mask in range(1<<(N-1)):
            vals=[1.0]+[1.0 if (mask>>(x-1))&1 else -1.0 for x in range(1,N)]
            s,so,st,_,_=analyze(vals); cases+=1; assertions+=2*n+3
            minslack=min(minslack,s); strict_old+=so>1e-10; strict_tern+=st>1e-10
    rng=random.Random(202610141220)
    random_cases=0
    for n,count in ((5,1200),(6,300)):
        N=1<<n
        for _ in range(count):
            vals=[1.0]+[rng.choice((-1.0,1.0)) for _ in range(1,N)]
            s,so,st,_,_=analyze(vals); random_cases+=1; assertions+=2*n+3
            minslack=min(minslack,s); strict_old+=so>1e-10; strict_tern+=st>1e-10
    surgery_rows=[]
    for d in range(1,9):
        s,so,st,k,m=analyze(surgery(d))
        surgery_rows.append((d,k,m,so,st))
    crossover=None
    for d in range(1,201):
        old_lower,ternary=surgery_global_bounds(d)
        if old_lower>ternary:
            crossover=(d,old_lower,ternary); break
    print('claim=B20-A097-ROWWISE-MIN-SINGLETON-CUT-v1')
    print('boolean_functions_mod_output',cases)
    print('seeded_larger_controls',random_cases)
    print('row_and_root_assertions',assertions)
    print('minimum_rowwise_slack',format(minslack,'.12e'))
    print('cases_where_rowwise_min_strictly_beats_global_old',strict_old)
    print('cases_where_rowwise_min_strictly_beats_global_ternary',strict_tern)
    print('near_tensor_d_K1_minbudget_oldgap_terngap')
    for row in surgery_rows: print(row)
    print('near_tensor_global_bound_crossover',crossover)
    print('universal_GU=OPEN')
    print('status=PASS')

if __name__=='__main__': main()
