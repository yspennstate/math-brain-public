#!/usr/bin/env python3
"""Exact certificates for the sharp one-step FEI continuation.
Standard library only. Complete proofs and scope are in REPORT.md.
No floating-point calculation decides a mathematical assertion.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import argparse,json,random

TERMS=60

def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return plus(a,neg(b))
def mul(a,b):
    c=[x*y for x in a for y in b];return (min(c),max(c))
def div(a,b):
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def scale(a,x):return mul(a,(F(x),F(x)))

def ln_unit(x):
    assert 1<=x<=2
    z=(x-1)/(x+1);z2=z*z;power=z;v=F(0)
    for j in range(TERMS):
        v+=power/(2*j+1);power*=z2
    return 2*v,2*v+2*power/((2*TERMS+1)*(1-z2))

LN2=ln_unit(F(2))
@lru_cache(None)
def ln(x):
    x=F(x);assert x>0
    e=0
    while x<1:x*=2;e-=1
    while x>2:x/=2;e+=1
    return plus(ln_unit(x),scale(LN2,e))

@lru_cache(None)
def log2(x):return div(ln(F(x)),LN2)

def hb(q):
    if q in (0,1):return F(0),F(0)
    return neg(plus(scale(ln(q),q),scale(ln(1-q),1-q)))

def phi(q):return sub(scale(hb(q),2),hb(2*q*(1-q)))
def phi_prime(q):
    r=2*q*(1-q)
    return sub(scale(ln((1-q)/q),2),scale(ln((1-r)/r),2*(1-2*q)))

def scalar_certificate():
    a=F(19943435135686,10**14);b=F(19943435135687,10**14)
    ga=sub(scale(phi_prime(a),a),phi(a));gb=sub(scale(phi_prime(b),b),phi(b))
    assert ga[0]>0 and gb[1]<0
    # phi''<0 from q=1/6 onward, by the monotonicity proved in REPORT.md.
    r=F(5,18)
    curvature=sub(ln((1-r)/r),(1/(1-r),1/(1-r)))
    assert curvature[1]<0 and a>F(1,6)
    lower=2*div(phi_prime(b),LN2)[0]
    upper=2*div(phi_prime(a),LN2)[1]
    assert F(53947539099,10**10)<lower<upper<F(53947539100,10**10)
    assert upper<F(2697377,500000) # 5.394754
    return {'q_star_bracket':[str(a),str(b)],
            'G_at_left_positive':True,'G_at_right_negative':True,
            'two_lambda_star_decimal_bracket':['5.3947539099','5.3947539100'],
            'rational_universal_coefficient':'2697377/500000',
            'all_dimension_claim':'D_cross(f) <= 2 lambda_star M(f) < 5.394754 M(f) for M(f)>0; zero case is D=M=0.'}


def fwht(a):
    a=list(a);h=1
    while h<len(a):
        for s in range(0,len(a),2*h):
            for j in range(s,s+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return tuple(a)

# Logarithmic linear forms use key 2 for log2(2)=1.
def clean(a):return {p:x for p,x in a.items() if x}
def add(a,b,c=F(1)):
    a=a.copy()
    for p,x in b.items():a[p]=a.get(p,F(0))+c*x
    return clean(a)
def times(a,c):return clean({p:x*c for p,x in a.items()})
@lru_cache(None)
def factors(k):
    ans={};p=2
    while p*p<=k:
        while k%p==0:ans[p]=ans.get(p,0)+1;k//=p
        p+=1
    if k>1:ans[k]=ans.get(k,0)+1
    return ans

@lru_cache(None)
def amplitude_entropy(num,N):
    if num==0:return {}
    num=abs(num);v=F(num*num,N*N)
    ans={2:2*(N.bit_length()-1)*v}
    for p,e in factors(num).items():ans[p]=ans.get(p,F(0))-2*e*v
    return clean(ans)

@lru_cache(None)
def entropy_hist(N,hist):
    out={}
    for a,c in hist:out=add(out,amplitude_entropy(a,N),F(c))
    return out

def H(f):
    N=len(f);a=fwht(f)
    assert sum(x*x for x in a)==N*N
    return entropy_hist(N,tuple(sorted(Counter(abs(x) for x in a).items())))

def bounds(a):
    out=(F(0),F(0))
    for p,c in a.items():out=plus(out,scale((F(1),F(1)) if p==2 else log2(F(p)),c))
    return out

def M(f):
    N=len(f);n=N.bit_length()-1
    corr=fwht(tuple(x*x for x in fwht(f)))
    assert all(c%N==0 for c in corr)
    costs=[(N-abs(c//N))//2 for c in corr]
    basis=[0]*n;total=0;rank=0
    for v in sorted(range(1,N),key=lambda v:costs[v]):
        w=v
        while w:
            j=w.bit_length()-1
            if basis[j]:w^=basis[j]
            else:basis[j]=w;rank+=1;total+=costs[v];break
        if rank==n:break
    return F(total,N)

def D(f):
    N=len(f);ans=times(H(f),2)
    for z in range(N):ans=add(ans,H(tuple(f[x]*f[x^z] for x in range(N))),-F(1,N))
    return ans

@lru_cache(None)
def truth_coefficient(N,k):
    # N times the coefficient of psi(N^-1 sum signs) at a fixed k-set.
    ans={}
    for a in range(k+1):
        for b in range(N-k+1):
            w=F(N*((-1)**a)*comb(k,a)*comb(N-k,b),1<<N)
            ans=add(ans,amplitude_entropy(N-2*(a+b),N),w)
    return ans

@lru_cache(None)
def zero_xor_masks(n):
    N=1<<n;ans=[]
    for mask in range(1,1<<N):
        k=mask.bit_count()
        if k<4 or k%2:continue
        xor=0;t=mask
        while t:
            b=t&-t;xor^=b.bit_length()-1;t-=b
        if xor==0:ans.append(mask)
    return tuple(ans)

def translate_mask(mask,z):
    out=0
    while mask:
        b=mask&-mask;out|=1<<((b.bit_length()-1)^z);mask-=b
    return out

@lru_cache(None)
def orbits(n):
    todo=set(zero_xor_masks(n));out=[];N=1<<n
    while todo:
        a=min(todo);orb=tuple(sorted({translate_mask(a,z) for z in range(N)}))
        todo.difference_update(orb);out.append(orb)
    return tuple(out)

def expansion(f,squares=False):
    N=len(f);n=N.bit_length()-1;negmask=sum((v<0)<<x for x,v in enumerate(f));ans={}
    for orb in orbits(n):
        m=F(sum(1-2*((a&negmask).bit_count()%2) for a in orb),len(orb))
        charge=1-m
        if squares:charge*=charge
        ans=add(ans,truth_coefficient(N,orb[0].bit_count()),-len(orb)*charge)
    return ans


def execute():
    scalar=scalar_certificate();counts=Counter();rng=random.Random(20260920)
    for n in range(5):
        N=1<<n
        if n<=3:codes=range(1<<N)
        else:
            chosen={0,(1<<N)-1,1,((1<<N)-1)^1}
            # Include a nondegenerate quadratic phase and its complement.
            bent=sum((((x&1)*((x>>1)&1))^(((x>>2)&1)*((x>>3)&1)))<<x for x in range(N))
            chosen.update([bent,bent^((1<<N)-1)])
            while len(chosen)<64:chosen.add(rng.getrandbits(N))
            codes=sorted(chosen)
        for code in codes:
            f=tuple(1-2*((code>>x)&1) for x in range(N))
            h,d,m=H(f),D(f),M(f)
            assert h==expansion(f),('entropy expansion',n,code)
            assert d==expansion(f,True),('derivative square expansion',n,code)
            lo,hi=bounds(d)
            assert lo>=0
            assert hi<=F(2697377,500000)*m
            # A finite test only, not promoted to a universal result.
            assert hi<=4*m
            counts['exact_Boolean_functions']+=1
            counts['entropy_expansion_identities']+=1
            counts['translated_square_identities']+=1
            counts['one_step_upper_bound_checks']+=1
            counts['candidate_constant_four_finite_checks']+=1
    c6=truth_coefficient(16,6);c6_interval=bounds(c6)
    assert c6_interval[0]>F(4412759895,10**12)
    assert c6_interval[1]<F(4412759896,10**12)
    # The set {0,1,2,4,8,15} is a genuine six-point zero-XOR set.
    chosen=[0,1,2,4,8,15];assert len(set(chosen))==6
    x=0
    for v in chosen:x^=v
    assert x==0
    quartic=[]
    for n in (2,4,6,8):
        N=1<<n;beta=bounds(times(truth_coefficient(N,4),-1))
        assert beta[0]>0
        planes=F(N*N*(N-1),48);assert planes.denominator==1
        debit=scale(beta,4*planes);ratio=scale(debit,F(2,n))
        analytic_lower=div((F(N-1),F(N-1)),scale(LN2,12*n))
        assert ratio[0]>analytic_lower[1]
        quartic.append({'n':n,'N':N,'negative_quadratic_planes':str(planes),
                        'quartic_debit_over_M_rational_lower':str(F((ratio[0]*10**12).numerator//(ratio[0]*10**12).denominator,10**12)),
                        'full_quadratic_D_over_M':'4',
                        'large_truth_table_enumeration':False})
    # A fully specified real, NON-Boolean relaxation example.
    # a0^2=119/120, a1^2=1/120. Product Fourier-output entropy is explicit.
    q=F(1,120);t=4*q*(1-q)
    z0=(1+t)/2;r=t/(1+t)
    dreal=sub(scale(div(hb(q),LN2),2),scale(div(hb(r),LN2),z0))
    gap=sub(dreal,(4*q,4*q));assert gap[0]>0
    counts['exact_real_relaxation_counterexample']=1
    result={'status':'PASS','arithmetic':'Integer Walsh transforms; exact rational linear forms in logarithms of primes; 60-term rational atanh enclosures.',
        'scalar_certificate':scalar,'counts':dict(counts),
        'coverage':'All 278 Boolean tables in dimensions 0 through 3 and 64 distinct selected tables in dimension 4. This does not prove the candidate coefficient 4.',
        'positive_sixth_order_coefficient':{'subset':[0,1,2,4,8,15],
             'exact_log2_prime_coefficients':{str(p):str(c) for p,c in sorted(c6.items())},
             'decimal_bracket':['0.004412759895','0.004412759896']},
        'quartic_unsigned_obstruction':quartic,
        'real_relaxation_counterexample':{'q':str(q),'Dminus4I_rational_lower':str(F((gap[0]*10**12).numerator//(gap[0]*10**12).denominator,10**12)),'is_Boolean':False},
        'full_FEI_status':'UNPROVED in this continuation',
        'novelty':'The entropy truth-table coefficient formula is inherited, not new. No publication priority clearance.'}
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=Path('verification.json'));args=p.parse_args()
    result=execute();text=json.dumps(result,indent=2)+'\n';args.output.write_text(text,encoding='utf-8');print(text)

if __name__=='__main__':main()
