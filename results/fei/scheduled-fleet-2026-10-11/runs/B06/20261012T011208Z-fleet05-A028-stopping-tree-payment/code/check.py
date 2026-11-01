"""Frozen arbitrary-controller certificate; all entropy signs use rational intervals."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import prod
import json, time, sys

ROOT=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
assert MODE in ('pilot','full')
START=time.monotonic()
checks=0

def check(condition):
    global checks
    assert condition
    checks+=1

@lru_cache(None)
def factors(n):
    out={}
    q=2
    while q*q<=n:
        while n%q==0:
            out[q]=out.get(q,0)+1
            n//=q
        q+=1
    if n>1: out[n]=out.get(n,0)+1
    return tuple(out.items())

def add(*terms):
    out={}
    for term in terms:
        for k,v in term.items(): out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}

def scale(term,q):
    return {k:v*q for k,v in term.items() if v*q}

def lg(q):
    q=F(q)
    assert q>0
    return add(dict((k,F(v)) for k,v in factors(q.numerator)),
               dict((k,F(-v)) for k,v in factors(q.denominator)))

def eta(q): return scale(lg(q),-q) if q else {}
def phi(t): return eta((1-2*t)**2)
def entropy(ps): return add(*(eta(q) for q in ps))

def ln_unit(q):
    # q in [1,2]; z<=1/3. Positive atanh series, rigorous tail.
    z=(q-1)/(q+1)
    total=F(0)
    power=z
    for j in range(24):
        total+=2*power/(2*j+1)
        power*=z*z
    tail=2*power/(49*(1-z*z))
    return total,total+tail

L2=ln_unit(F(2))
@lru_cache(None)
def log_prime(k):
    if k==2: return F(1),F(1)
    exponent=k.bit_length()-1
    lo,hi=ln_unit(F(k,1<<exponent))
    lower,upper=F(exponent)+lo/L2[1], F(exponent)+hi/L2[0]
    denominator=1<<48
    lower_scaled,upper_scaled=lower*denominator,upper*denominator
    low=lower_scaled.numerator//lower_scaled.denominator
    high=-((-upper_scaled.numerator)//upper_scaled.denominator)
    return F(low,denominator),F(high,denominator)

@lru_cache(None)
def cached_enclosure(items):
    lo=hi=F(0)
    for k,c in items:
        a,b=log_prime(k)
        lo+=c*(a if c>=0 else b)
        hi+=c*(b if c>=0 else a)
    return lo,hi

def enclosure(term): return cached_enclosure(tuple(sorted(term.items())))

@lru_cache(None)
def walsh(table):
    a=list(table)
    step=1
    while step<len(a):
        for base in range(0,len(a),2*step):
            for j in range(base,base+step):
                x,y=a[j],a[j+step]
                a[j],a[j+step]=x+y,x-y
        step*=2
    return tuple(a)

@lru_cache(None)
def stats(table):
    N=len(table)
    ps=tuple(F(a*a,N*N) for a in walsh(table))
    Hp=entropy(ps[1:])
    return ps,Hp,add(Hp,eta(ps[0])),sum((s.bit_count()*q for s,q in enumerate(ps)),F(0))

def edges(table,indices):
    return sum((F(sum(table[x]!=table[x^(1<<i)] for x in range(len(table))),len(table))
                for i in indices),F(0))

def tables(maxdim):
    for n in range(maxdim+1):
        for code in range(1<<(1<<n)):
            yield n,code,tuple(-1 if code>>x&1 else 1 for x in range(1<<n))

@lru_cache(None)
def tree(table,controls):
    if controls==0: return {},F(0)
    half=len(table)//2
    left,right=table[:half],table[half:]
    H=stats(table)[2]
    D=add(H,scale(add(stats(left)[2],stats(right)[2]),F(-1,2)))
    d=F(sum(x!=y for x,y in zip(left,right)),half)
    A,ai=tree(left,controls-1)
    B,bi=tree(right,controls-1)
    return add(D,scale(add(A,B),F(1,2))),d+(ai+bi)/2

count=0
slack_min=None
for na,ca,a in tables(2):
    pa,Ha_plus,Ha,Ia=stats(a)
    p=F(a.count(-1),len(a))
    va=4*p*(1-p)
    check(Ia==edges(a,range(na)))
    for nu,cu,u in tables(2 if MODE=='pilot' else 3):
        pu,Hu_plus,Hu,Iu=stats(u)
        delta=F(u.count(-1),len(u))
        vu=4*delta*(1-delta)
        table=tuple(val if sign==-1 else 1 for sign in a for val in u)
        ps,Hplus,H,I=stats(table)
        check(Iu==edges(u,range(nu)))
        check(I==edges(table,range(na+nu))==delta*Ia+p*Iu)
        check(edges(table,range(nu,nu+na))==delta*Ia)
        G=add(scale(eta(p*p),vu),{2:vu*va/2},
              scale(lg(1/(delta*delta)),delta*delta*va) if delta else {})
        check(Hplus==add(scale(Ha_plus,delta),scale(Hu_plus,p),G))
        PiH=add(H,scale(Hu,-p))
        check(PiH==add(scale(Ha_plus,delta),G,phi(p*delta),scale(phi(delta),-p)))
        debt,paid=tree(table,na)
        check(debt==PiH and paid==delta*Ia)
        S=add(PiH,scale(Ha_plus,-delta))
        margin=add({2:6*delta*va},scale(S,-1))
        if margin:
            lower,_=enclosure(margin)
            check(lower>=0)
            if lower and (slack_min is None or lower<slack_min): slack_min=lower
        else: check(True)
        D=4*p*delta*(1-p)*(1-delta)
        check(I-4*p*delta*(1-p*delta)==delta*(Ia-va)+p*(Iu-vu)+D)
        gate_margin=add({2:8*D},scale(G,-1))
        check(not gate_margin or enclosure(gate_margin)[0]>=0)
        count+=1
        if time.monotonic()-START>(60 if MODE=='pilot' else 600):
            raise RuntimeError('frozen runtime cap exceeded')

# Exact countercertificate to coefficient four, even with dictator control.
a=(1,-1)
u=(-1,1,1,1)
table=u+(1,)*4
Pi=add(stats(table)[2],scale(stats(u)[2],F(-1,2)))
ratio=scale(Pi,F(4))
check(ratio=={2:F(12),3:F(-9,2)})
check(3**9<2**16) # ratio>4 iff log2(3)<16/9
certificate={'control_sign':list(a),'core_sign':list(u),'p':'1/2','delta':'1/4',
             'PiH_prime_log':{str(k):str(v) for k,v in Pi.items()},'Q':'1/4',
             'ratio_prime_log':{str(k):str(v) for k,v in ratio.items()},
             'ratio_gt_4_integer_certificate':{'left':3**9,'right':2**16,'strict':True}}
out={'helper':'A028-general-control-v2','mode':MODE,'cases':count,'assertions_passed':checks,
     'compute_seconds':time.monotonic()-START,'arithmetic':'integer/Fraction/prime-log/rational-atanh-24',
     'smallest_positive_margin_lower':str(slack_min),'coefficient_four_countercertificate':certificate,
     'max_dimensions':{'control':2,'core':2 if MODE=='pilot' else 3},
     'interval_tail':'2 z^(49)/(49(1-z^2)), z<=1/3; sign-correct division by positive ln2 enclosure, outward floor/ceiling to denominator 2^48',
     'infinite_scope':'Analytic proofs in REPORT.md; finite checks do not certify all dimensions'}
(ROOT/'out'/f'{MODE}_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
