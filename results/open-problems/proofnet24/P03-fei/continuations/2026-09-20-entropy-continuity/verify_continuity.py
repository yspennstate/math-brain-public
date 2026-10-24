#!/usr/bin/env python3
"""Exact finite checks for the entropy-continuity continuation.

Only Python standard library. Walsh transforms, Fourier-coset identities and
finite-field operations are exact. All entropy inequalities use outward rational
logarithm enclosures. Infinite-dimensional conclusions are proved in REPORT.md.
"""
from __future__ import annotations
from collections import Counter
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, isqrt
from pathlib import Path
import argparse, json, random

BITS=100
SCALE=1<<BITS
SEED=202609200120


def require(x, message):
    if not x: raise AssertionError(message)


def ln_unit(x: F, terms: int=48):
    require(1 <= x <= 2, 'log range')
    z=(x-1)/(x+1); zz=z*z; p=z; total=F(0)
    for j in range(terms):
        total += p/(2*j+1); p*=zz
    lo=2*total
    return lo,lo+2*p/((2*terms+1)*(1-zz))


LN2=ln_unit(F(2))
e_lo=sum((F(1,factorial(j)) for j in range(49)),F(0))
e_hi=e_lo+F(50,49*factorial(49))
C0=(16/(e_hi*LN2[1]),16/(e_lo*LN2[0]))
require(C0[1] < F(17,2), '8.5 constant certificate')


def exp_bounds(x:F, terms:int=96):
    require(x>=0,'nonnegative exponential argument')
    term=F(1);lo=term
    for j in range(1,terms+1):
        term*=x/j;lo+=term
    nxt=term*x/(terms+1)
    require(x<terms+2,'geometric exponential tail')
    return lo,lo+nxt/(1-x/(terms+2))


# Enclose the unique positive solution of u*tanh(u)=1.
UROOT=(F(11996786402577338,10**16),F(11996786402577340,10**16))
a,b=UROOT
x,y=exp_bounds(2*a),exp_bounds(2*b)
require((a-1)*x[1]-(a+1)<0,'lower root endpoint')
require((b-1)*y[0]-(b+1)>0,'upper root endpoint')
ea,eb=exp_bounds(a),exp_bounds(b)
KAPPA=(a/(eb[1]+1/ea[0]),b/(ea[0]+1/eb[1]))
CSTAR=(16*KAPPA[0]/LN2[1],16*KAPPA[1]/LN2[0])
require(CSTAR[1]<F(153,20),'7.65 constant certificate')


@lru_cache(maxsize=None)
def log_int(n:int):
    require(n>0,'positive log input')
    e=n.bit_length()-1
    if n==1<<e:return e*SCALE,e*SCALE
    a,b=ln_unit(F(n,1<<e))
    a=(e+a/LN2[1])*SCALE; b=(e+b/LN2[0])*SCALE
    return a.numerator//a.denominator,-((-b.numerator)//b.denominator)


@lru_cache(maxsize=None)
def entropy_hist(n:int,hist:tuple):
    N=1<<n; low=high=0
    require(sum(c*a*a for a,c in hist)==N*N,'spectral histogram Parseval')
    for a,c in hist:
        if not a:continue
        lo,hi=log_int(a); low+=c*a*a*lo; high+=c*a*a*hi
    return F(2*n)-F(2*high,N*N*SCALE),F(2*n)-F(2*low,N*N*SCALE)


def entropy(a):
    return entropy_hist(len(a).bit_length()-1,tuple(sorted(Counter(abs(x) for x in a).items())))


def walsh(f):
    a=list(f); h=1
    require(len(a)>0 and len(a)&(len(a)-1)==0,'table size')
    while h<len(a):
        for b in range(0,len(a),2*h):
            for i in range(b,b+h):
                a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
        h*=2
    return tuple(a)


def sqrt_bounds(x:F):
    require(x>=0,'nonnegative square root')
    z=isqrt(x.numerator*SCALE*SCALE//x.denominator)
    lo=F(z,SCALE)
    return lo,lo if lo*lo==x else F(z+1,SCALE)


def abs_gap(a,b):
    return max(F(0),a[0]-b[1],b[0]-a[1]),max(a[1]-b[0],b[1]-a[0])


def decimal_interval(ab, places=15):
    out=[]
    for x,rounding in zip(ab,(ROUND_FLOOR,ROUND_CEILING)):
        with localcontext() as c:
            c.prec=max(80,places+30); c.rounding=rounding
            y=Decimal(x.numerator)/Decimal(x.denominator)
            out.append(str(y.quantize(Decimal(1).scaleb(-places),rounding=rounding)))
    return out


def interval_json(ab):
    # Compact the report without losing rigor: round final endpoints outward.
    a,b=ab[0]*SCALE,ab[1]*SCALE
    ab=(F(a.numerator//a.denominator,SCALE),F(-((-b.numerator)//b.denominator),SCALE))
    return {'rational':[str(x) for x in ab],'decimal':decimal_interval(ab)}


def table(mask,n):return tuple(1-2*((mask>>x)&1) for x in range(1<<n))


def span(basis):
    out=[0]
    for b in basis:out += [x^b for x in out]
    return tuple(sorted(out))


def spaces(n):
    # Enumerate all distinct binary linear subspaces, using their exact point sets.
    allspaces={(0,)}; frontier={(0,)}
    while frontier:
        nxt=set()
        for W in frontier:
            for v in range(1,1<<n):
                if v in W:continue
                U=tuple(sorted(W+tuple(w^v for w in W)))
                if U not in allspaces:nxt.add(U)
        allspaces.update(nxt);frontier=nxt
    return sorted(allspaces,key=lambda w:(len(w),w))


def basis_from_span(W):
    basis=[]; U={0}
    for w in W:
        if w not in U:
            basis.append(w);U.update([u^w for u in list(U)])
    return tuple(basis)


def affine_gates(n):
    for W in spaces(n):
        basis=basis_from_span(W);r=len(basis)
        for beta in range(1<<r):
            A=tuple(x for x in range(1<<n) if all(((x&b).bit_count()&1)==((beta>>j)&1) for j,b in enumerate(basis)))
            require(len(A)==1<<(n-r),'affine size')
            yield W,A,r


def influence_numer(a):
    return sum(s.bit_count()*v*v for s,v in enumerate(a))


def verify_gate(f,W,A,r,structural=True):
    N=len(f);n=N.bit_length()-1;M=1<<r
    Aset=set(A);g=tuple(-v if x in Aset else v for x,v in enumerate(f))
    a,b=walsh(f),walsh(g)
    ah,bh=entropy(a),entropy(b)
    gap=abs_gap(ah,bh)
    require(gap[1] <= CSTAR[0]*sqrt_bounds(F(1,M))[0],'affine entropy bound')
    if structural:
        remaining=set(range(N));sum_u2=0;x0=A[0]
        while remaining:
            c=min(remaining);coset=tuple(c^w for w in W)
            remaining.difference_update(coset)
            require(sum(a[s]**2 for s in coset)==sum(b[s]**2 for s in coset),'coset mass')
            u=sum(a[c^w]*(1-2*((w&x0).bit_count()&1)) for w in W)
            sum_u2+=u*u
            for w in W:
                require(M*(b[c^w]-a[c^w]) == -2*(1-2*((w&x0).bit_count()&1))*u,'flat reflection identity')
        require(sum_u2==N*N,'restricted Boolean Parseval')
        active=sum(any(w>>i&1 for w in W) for i in range(n))
        require(abs(influence_numer(a)-influence_numer(b))*M <= 2*active*N*N,'influence-change bound')
    return gap


def field_mul(a,b,mod,n):
    r=0
    while b:
        if b&1:r^=a
        a<<=1
        if a>>n:a^=mod
        b>>=1
    return r


def field_pow(a,k,mod,n):
    out=1
    while k:
        if k&1:out=field_mul(out,a,mod,n)
        a=field_mul(a,a,mod,n);k>>=1
    return out


def poly_mod(a,b):
    while a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
    return a


def poly_gcd(a,b):
    while b:a,b=b,poly_mod(a,b)
    return a


def irreducible(mod,n):
    v=2
    for k in range(1,n+1):
        v=field_mul(v,v,mod,n)
        if k<=n//2 and poly_gcd(v^2,mod)!=1:return False
    return v==2


def field_trace(a,mod,n):
    out=0
    for _ in range(n):out^=a;a=field_mul(a,a,mod,n)
    require(out in (0,1),'field trace');return out


def j4(y,m):
    # On each pair (a,b), J(a,b)=(b,a+b); J^2+J+1=0.
    z=0
    for i in range(0,m,2):
        a=(y>>i)&1;b=(y>>(i+1))&1
        z|=b<<i;z|=(a^b)<<(i+1)
    return z


def triple_spread_function(m):
    require(m%2==0 and m>=2,'even y dimension')
    M=1<<m;U=M//2;pi=[0]*M;label=0
    for y in range(1,M):
        if pi[y]:continue
        a=j4(y,m);b=j4(a,m)
        require(j4(b,m)==y and len({y,a,b})==3 and y^a^b==0,'triple subspace')
        label+=1
        for z in (y,a,b):
            require(pi[z]==0,'disjoint triple');pi[z]=label
    require(label==(M-1)//3 and label<U,'labels fit')
    f=tuple(1-2*((x&pi[y]).bit_count()&1) for x in range(U) for y in range(M))
    return f,label


def histogram_from_fibers(m,k,fibers):
    M=1<<m;U=1<<k;N=M*U
    L=sum(fibers.values())
    require(L+1<=U,'label budget')
    require(sum((q-1)*count for q,count in fibers.items())==M-1,'nonzero point partition')
    hist=Counter({U:M}) # normalized Fourier coefficient 1/M; raw coefficient N/M=U.
    minus=0
    for q,count in fibers.items():
        require(M%q==0,'annihilator size')
        hist[(q-1)*U]+=count*M//q
        minus+=count*M*(q-1)//q
    hist[-U]+=minus
    hist[0]+=(U-L-1)*M
    require(sum(hist.values())==N,'histogram count')
    require(sum(a*a*c for a,c in hist.items())==N*N,'histogram norm')
    require(sum(a*c for a,c in hist.items())==N,'f(0)=1')
    require(all(c>=0 for c in hist.values()),'nonnegative counts')
    return hist


def hist_entropy(n,hist):
    ah=Counter()
    for a,c in hist.items():ah[abs(a)]+=c
    return entropy_hist(n,tuple(sorted(ah.items())))


def hist_flipped(n,hist):
    out=Counter()
    for a,c in hist.items():out[a-2]+=c
    a,b=hist_entropy(n,hist),hist_entropy(n,out)
    diff=(b[0]-a[1],b[1]-a[0]); sq=sqrt_bounds(F(1<<n))
    products=[x*y for x in diff for y in sq]
    scaled=min(products),max(products)
    require(abs_gap(a,b)[1] <= CSTAR[0]*sqrt_bounds(F(1,1<<n))[0],'large-dimensional continuity bound')
    return {'dimension':n,'entropy_change':interval_json(diff),'scaled_by_sqrt_N':interval_json(scaled),
            'signed_raw_walsh_histogram':{str(a):str(c) for a,c in sorted(hist.items())}}


def mixed_spread_hist(m):
    require(m%20==0 and m>=20,'mixed-spread dimension')
    M=1<<m;U=M//16;D=(1<<20)-1;B=(M-1)//D
    a16,a32=D//15,D//31
    A=(U-1-a32*B)//(a16-a32)
    require(0<=A<=B,'mixture count')
    L16=A*a16;L32=(B-A)*a32
    hist=histogram_from_fibers(m,m-4,{16:L16,32:L32})
    return hist,{'y_dimension':m,'outer_blocks':str(B),'sixteen_type_blocks':str(A),
                 'fibers_size_15':str(L16),'fibers_size_31':str(L32),
                 'unused_output_labels':str(U-1-L16-L32)}


def run():
    counts=Counter();out={};rng=random.Random(SEED)
    maxima=[]
    for n in range(1,5):
        N=1<<n;best=(F(0),F(0));witness=None;maximum_upper=F(0)
        for mask in range(0,1<<N,2):
            a=walsh(table(mask,n));b=tuple(x-2 for x in a)
            gap=abs_gap(entropy(a),entropy(b));counts['origin_flip_pairs_exhaustive']+=1
            require(gap[1] <= CSTAR[0]*sqrt_bounds(F(1,N))[0],'exhaustive point inequality')
            maximum_upper=max(maximum_upper,gap[1])
            if gap[0]>best[0]:best=gap;witness=mask
        maxima.append({'dimension':n,'max_gap_interval':interval_json((best[0],maximum_upper)),'witness_negative_mask':str(witness)})
    out['small_dimension_maxima']=maxima
    for n in range(1,4):
        gates=list(affine_gates(n));counts['affine_gate_descriptions']+=len(gates)
        for mask in range(1<<(1<<n)):
            f=table(mask,n)
            for W,A,r in gates:
                verify_gate(f,W,A,r);counts['all_function_affine_gate_cases_n_le_3']+=1
    for n in range(4,11):
        N=1<<n
        for trial in range(120):
            f=tuple(rng.choice((-1,1)) for _ in range(N))
            if trial%4==0:
                f=tuple(1-2*(rng.randrange(100)<3) for _ in range(N))
            r=rng.randrange(n+1);basis=[];V={0}
            while len(basis)<r:
                v=rng.randrange(1,N)
                if v not in V:basis.append(v);V.update([x^v for x in list(V)])
            x0=rng.randrange(N);W=tuple(sorted(V))
            A=tuple(x for x in range(N) if all(((x^x0)&b).bit_count()%2==0 for b in basis))
            verify_gate(f,W,A,r);counts['sampled_affine_gate_cases']+=1
    triples=[]
    for m in (2,4,6,8):
        f,L=triple_spread_function(m);n=2*m-1;M=1<<m
        predicted=histogram_from_fibers(m,m-1,{4:L});actual=Counter(walsh(f))
        require(actual==+predicted,'explicit triple-spread Fourier histogram')
        triples.append(hist_flipped(n,predicted));counts['explicit_triple_spread_truth_tables']+=1
    out['triple_spread_examples']=triples
    nihos=[]
    for n,mod in ((4,0b10011),(8,0b100011011),(12,(1<<12)|(1<<3)|1)):
        require(irreducible(mod,n),'irreducible field modulus')
        N=1<<n;s=1<<(n//2);r=2*s-1
        f=tuple(1-2*field_trace(field_pow(x,r,mod,n),mod,n) for x in range(N))
        actual=Counter(walsh(f))
        predicted=Counter({-s:(N-s)//3,0:(N-s)//2,s:s,2*s:(N-s)//6})
        require(actual==predicted,'Niho benchmark table')
        nihos.append(hist_flipped(n,actual));counts['niho_benchmark_truth_tables']+=1
    out['published_niho_benchmarks']=nihos
    mixtures=[]
    for m in (20,40,60):
        hist,metadata=mixed_spread_hist(m)
        example=hist_flipped(2*m-4,hist);example['construction']=metadata
        if m>=40:require(example['scaled_by_sqrt_N']['rational'] and F(example['scaled_by_sqrt_N']['rational'][0])>F(7467,1000),'improved asymptotic lower certificate')
        mixtures.append(example);counts['symbolic_mixed_spread_certificates']+=1
    out['mixed_spread_examples']=mixtures
    # The limiting lower constant, as a rational linear form in log_2 integers.
    l15,l31=log_int(15),log_int(31)
    limit=(F(225,128)*F(l15[0],SCALE)+F(31,256)*F(l31[0],SCALE),
           F(225,128)*F(l15[1],SCALE)+F(31,256)*F(l31[1],SCALE))
    out['mixed_spread_limit']=interval_json(limit)
    out.update({'status':'PASS','seed':SEED,'counts':dict(counts),'coarse_universal_constant':interval_json(C0),'refined_universal_constant':interval_json(CSTAR),'maximizer_root_interval':interval_json(UROOT),
      'arithmetic':'Integer Walsh and finite-field operations; 48-term positive atanh logarithm intervals, outward dyadic rounding at 2^-100; rational comparisons. Printed decimal intervals are outward-rounded.',
      'coverage':'Origin flips exhaust all Boolean tables through dimension four, modulo exchanging the pair. Affine gates exhaust all functions and affine subspaces through dimension three. Higher dimensions are samples or the explicitly proved structured families. Large mixed-spread truth tables were NOT enumerated.',
      'scope':'Tests support REPORT.md, not a proof of unrestricted FEI or independent verification. The mixed-spread asymptotic proof is separate from the finite certificates.'})
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=Path('verification.json'));args=p.parse_args()
    result=run();args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'counts':result['counts'],'mixed_spread_limit':result['mixed_spread_limit']['decimal']},indent=2))

if __name__=='__main__':main()
