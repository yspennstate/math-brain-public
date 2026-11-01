import argparse, itertools, json, time
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--pilot',action='store_true')
args=parser.parse_args()
START=time.monotonic()
counts={}

def check(ok,label):
    assert ok,label
    counts[label]=counts.get(label,0)+1
    if time.monotonic()-START>59:
        raise RuntimeError('Frozen 60-second cap reached; no escalation')

@lru_cache(None)
def walsh(values):
    a=list(values); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                x,y=a[k],a[k+h]
                a[k],a[k+h]=x+y,x-y
        h*=2
    return tuple(Q(x,len(a)) for x in a)

def law(values):
    return tuple(x*x for x in walsh(values))

@lru_cache(None)
def inf(values,i):
    return Q(sum(values[x]!=values[x^(1<<i)] for x in range(len(values))),len(values))

@lru_cache(None)
def total_inf(values):
    return sum((inf(values,i) for i in range(len(values).bit_length()-1)),Q(0))

def minority(values):
    return Q(sum(x==-1 for x in values),len(values))

def ln_bounds(y):
    z=(y-1)/(y+1); z2=z*z; power=z; lo=Q(0)
    for j in range(22):
        lo+=2*power/(2*j+1); power*=z2
    return lo,lo+2*power/(45*(1-z2))

LN2=ln_bounds(Q(2))

@lru_cache(None)
def loginv(prob):
    x=1/prob; k=0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    lo,hi=ln_bounds(x)
    return Q(k)+lo/LN2[1],Q(k)+hi/LN2[0]

# Formal sums of rational multiples of log2(1/q) retain exact cancellation.
def combine(*parts):
    out={}
    for factor,form in parts:
        for key,c in form.items():
            out[key]=out.get(key,Q(0))+factor*c
    return {key:c for key,c in out.items() if c}

def bounds(form):
    lo=hi=Q(0)
    for key,c in form.items():
        a,b=loginv(key)
        if c>=0: lo+=c*a; hi+=c*b
        else: lo+=c*b; hi+=c*a
    return lo,hi

@lru_cache(None)
def H(values):
    form={}
    for p in law(values):
        if p and p!=1: form[p]=form.get(p,Q(0))+p
    return form

def E(a):
    p=a*a
    return {p:p} if p and p!=1 else {}

def G(p,r,d):
    # Constants represented as a coefficient of log2(1/(1/2))=1.
    const={Q(1,2):8*r*p*d*(1-p*d)}
    return combine((1,const),(p*(1-p),E(2*d)),(1,E(1-2*p*d)),(-p,E(1-2*d)))

@lru_cache(None)
def activate(core,r):
    N=len(core)
    return tuple(core[x&(N-1)] if x//N==0 else 1 for x in range(N*(1<<r)))

@lru_cache(None)
def restrict(values,fixed):
    m=len(values).bit_length()-1
    fixed=dict(fixed)
    free=[i for i in range(m) if i not in fixed]
    offset=sum(b<<i for i,b in fixed.items())
    return tuple(values[offset+sum(((x>>j)&1)<<i for j,i in enumerate(free))] for x in range(1<<len(free)))

def overlap(form1,form2):
    a,b=bounds(form1); c,d=bounds(form2)
    return max(a,c)<=min(b,d)

def monotone_order(values,order):
    n=len(values).bit_length()-1
    for i in range(n):
        for x in range(len(values)):
            if not (x>>i)&1 and values[x]>values[x|(1<<i)]: return False
    for pos,i in enumerate(order):
        for j in order[pos+1:]:
            for x in range(len(values)):
                if not ((x>>i)&1 or (x>>j)&1):
                    if values[x|(1<<i)]<values[x|(1<<j)]: return False
    return True

@lru_cache(None)
def negative_regular_certificate(core):
    n=len(core).bit_length()-1
    neg=tuple((1-x)//2 for x in core)
    for flip in range(1<<n):
        oriented=tuple(neg[x^flip] for x in range(1<<n))
        for order in itertools.permutations(range(n)):
            if monotone_order(oriented,order): return flip,order
    return None

@lru_cache(None)
def verify_regular_lift(core,r):
    cert=negative_regular_certificate(core)
    if cert is None: return False
    flip,order=cert; n=len(core).bit_length()-1
    F=activate(core,r)
    flip|=((1<<r)-1)<<n
    q=tuple((1-F[x^flip])//2 for x in range(len(F)))
    check(monotone_order(q,tuple(range(n,n+r))+order),'regular terminal order certificate')
    # Bound 9 is a rational relaxation of the independently audited C_reg<8.937.
    check(bounds(H(F))[1]<=9*total_inf(F),'regular terminal entropy certificate')
    return True

@lru_cache(None)
def verify_activation(core,r):
    p=Q(1,1<<r); F=activate(core,r); d=minority(core)
    check(sum(law(F))==1,'activation Parseval')
    check(overlap(H(F),combine((p,H(core)),(1,G(p,r,d)))),'exact arbitrary-bias entropy correction enclosure')
    n=len(core).bit_length()-1
    check(total_inf(F)==p*total_inf(core)+2*r*p*d,'full activation physical influence')
    verify_regular_lift(core,r)
    return True

def evaluate(core,r,leaves,query_cost,label):
    p=Q(1,1<<r); F=activate(core,r); root_d=minority(core)
    verify_activation(core,r)
    core_leafH={}; act_leafH={}; mean=Q(0); leafI=Q(0); actleafI=Q(0)
    variation=Q(0); correction=G(p,r,root_d)
    check(sum(w for fixed,w in leaves)==1,'physical leaf weights')
    for fixed,w in leaves:
        child=restrict(core,fixed); actchild=restrict(F,fixed)
        check(actchild==activate(child,r),'actual lifted physical restriction')
        verify_activation(child,r)
        d=minority(child); mean+=w*d; variation+=w*abs(d-root_d)
        leafI+=w*total_inf(child); actleafI+=w*total_inf(actchild)
        core_leafH=combine((1,core_leafH),(w,H(child)))
        act_leafH=combine((1,act_leafH),(w,H(actchild)))
        correction=combine((1,correction),(-w,G(p,r,d)))
    check(mean==root_d,'minority leaf martingale')
    check(total_inf(core)-leafI==query_cost,'core query budget versus leaf telescope')
    check(total_inf(F)-actleafI==p*query_cost,'lifted query budget versus leaf telescope')
    check(actleafI==p*leafI+2*r*p*root_d,'unspent terminal control reserve')
    check(variation<=query_cost/2,'actual mean-bias variation payment')
    Pi_core=combine((1,H(core)),(-1,core_leafH))
    Pi_act=combine((1,H(F)),(-1,act_leafH))
    error=combine((1,Pi_act),(-p,Pi_core))
    check(overlap(error,correction),'exact partial-core correction enclosure')
    lo,hi=bounds(error)
    check(max(abs(lo),abs(hi))<=24*p*query_cost,'complete entropy transport certified')
    counts[label]=counts.get(label,0)+1
    return F

fixed_cases=adaptive_cases=0
for m in ((2,) if args.pilot else (2,3)):
    N=1<<m
    for table in range(1<<N):
        core=tuple(1 if (table>>x)&1 else -1 for x in range(N))
        for r in (1,2,3):
            for mask in range(1,(1<<m)-1):
                W=[i for i in range(m) if (mask>>i)&1]
                leaves=[(tuple((i,(b>>j)&1) for j,i in enumerate(W)),Q(1,1<<len(W))) for b in range(1<<len(W))]
                cost=sum((inf(core,i) for i in W),Q(0))
                F=evaluate(core,r,leaves,cost,'fixed proper-core partition')
                # Original spectrum -> outside marginal -> full conditional block entropy.
                outside=[i for i in range(m+r) if i not in W]
                rows={}
                for s,mass in enumerate(law(F)):
                    key=sum(((s>>i)&1)<<j for j,i in enumerate(outside))
                    rows.setdefault(key,[]).append(mass)
                marginal=tuple(sum(row) for row in rows.values())
                marginalform={}
                for q in marginal:
                    if q and q!=1: marginalform[q]=marginalform.get(q,Q(0))+q
                B=combine((1,H(F)),(-1,marginalform))
                check(bounds(B)[0]>=0,'proper-block full conditional entropy nonnegative')
                fixed_cases+=1
            if m==3:
                for left,right in itertools.product((None,1,2),repeat=2):
                    leaves=[]; cost=inf(core,0)
                    for bit,nextvar in enumerate((left,right)):
                        base=((0,bit),)
                        if nextvar is None:
                            leaves.append((base,Q(1,2)))
                        else:
                            child=restrict(core,base)
                            cost+=inf(child,nextvar-1)/2
                            for value in (0,1): leaves.append((base+((nextvar,value),),Q(1,4)))
                    evaluate(core,r,leaves,cost,'adaptive proper-core partition')
                    adaptive_cases+=1

def pointdefect_H(q,s):
    return combine((1,E(1-2*q)),(1,{4*q*q:(1/q-1)*4*q*q}) if 4*q*q!=1 else (1,{}))

symbolic_cases=0
if not args.pilot:
    for t,s,r in itertools.product((1,2,3),(1,2,4,8,16,32),(1,2,4,8,16)):
        q=Q(1,1<<s); p=Q(1,1<<r)
        Hg=pointdefect_H(q,s)
        full=combine((p,Hg),(1,G(p,r,Q(1,2))))
        plus=combine((p,Hg),(1,G(p,r,q)))
        minus=combine((p,Hg),(1,G(p,r,1-q)))
        Pi=combine((1,full),(-Q(1,2),plus),(-Q(1,2),minus))
        check(bounds(Pi)[1]<=24*p,'low-density character-block charge certified')
        check(overlap(plus,pointdefect_H(p*q,r+s)),'positive leaf point-defect identity')
        check(bounds(minus)[1]<=9*(p*2*s*q+2*r*p*(1-q)),'negative regular leaf payment certified')
        check(bounds(full)[1]<=24*p*(t+2*s*q+r),'low-density full stopping payment certified')
        symbolic_cases+=1

check(fixed_cases==(96 if args.pilot else 4704),'frozen fixed case count')
check(adaptive_cases==(0 if args.pilot else 6912),'frozen adaptive case count')
check(symbolic_cases==(0 if args.pilot else 90),'frozen symbolic case count')
result={'status':'PASS','helper_version':'A027-partial-core-transport-v2','pilot':args.pilot,'fixed_partitions':fixed_cases,'adaptive_partitions':adaptive_cases,'symbolic_low_density_cases':symbolic_cases,'assertions':sum(counts.values()),'checks':counts,'elapsed_seconds':time.monotonic()-START,'log_series_terms':22,'arithmetic':'Exact rational spectra, physical counts, formal log sums with rational enclosure','independent_review':'PENDING'}
(ROOT/'out'/('pilot.json' if args.pilot else 'validation.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
