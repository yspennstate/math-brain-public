"""A005 stage2: signed child-slack conservation, exact entropy arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parents[0]/'20261011T225209Z-fleet05-A005-noncircular-endpoint-referee/code/check.py'
# Source reuse without imports/bytecode or executing the old run's main/writers.
scope={'__name__':'a005_exact_arithmetic','__file__':str(BASE)}
exec(compile(BASE.read_text(),str(BASE),'exec'),scope)
add,scale,phi,L,fwht,entropy,influence,total,seed=(scope[k] for k in ['add','scale','phi','L','fwht','entropy','influence','total','seed'])
def roundup(a):
    D=1<<48
    return Q((a[0]*D).__floor__(),D),Q((a[1]*D).__ceil__(),D)
def lnunit(x):
    z=(x-1)/(x+1); N=40
    s=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
    e=2*z**(2*N+1)/(Q(2*N+1)*(1-z*z))
    return s,s+e
LN2=lnunit(Q(2))
@lru_cache(None)
def log2(x):
    x=Q(x);q=x.numerator.bit_length()-x.denominator.bit_length();r=x/(Q(2)**q)
    if r<1:q-=1;r*=2
    lo,hi=lnunit(r)
    return roundup((Q(q)+lo/LN2[1],Q(q)+hi/LN2[0]))
def evaluate(v):
    lo=hi=Q(0)
    for p,c in v.items():
        l,h=log2(p)
        lo+=c*(l if c>=0 else h);hi+=c*(h if c>=0 else l)
    return roundup((lo,hi))
def sign(v):
    if not v:return 0
    lo,hi=evaluate(v)
    assert lo>0 or hi<0,(v,lo,hi)
    return 1 if lo>0 else -1
def const(q):return {2:Q(q)} if q else {}
def restricted(v,n,i,b):
    return [v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(1<<(n-1))]
def physical_i(v,n,i):
    return Q(sum(v[x]!=v[x^(1<<i)] for x in range(1<<n)),1<<n)
def packet_js(a,i):
    out={}
    for s,u in enumerate(a):
        if s>>i&1:continue
        v=a[s|(1<<i)]
        out=add(out,phi(u*u+v*v),scale(phi((u+v)**2),-Q(1,2)),scale(phi((u-v)**2),-Q(1,2)))
    return out
def marginal_entropy(a,i):
    return add(*(phi(u*u+a[s|(1<<i)]**2) for s,u in enumerate(a) if not s>>i&1))
def tensor_values(v,m):
    n=(len(v)-1).bit_length();result=[]
    for x in range(1<<(n*m)):
        z=1
        for j in range(m):z*=v[(x>>(n*j))&((1<<n)-1)]
        result.append(z)
    return result

def run(mode):
    nmax=2 if mode=='pilot' else 3;ms=[1,2] if mode=='pilot' else [1,2,3,4]
    Cs=[Q(0),Q(5,2),Q(8,3),Q(3)]; start=time.perf_counter();assertions=0;cases=0;minimal=0;averaged=0
    def eq(x,y):
        nonlocal assertions
        assertions+=1;assert x==y,(x,y)
    def checked(v,n,C):
        nonlocal cases,minimal,averaged,assertions
        cases+=1;a=fwht(v);H=entropy(a);I=total(a,n)
        relevant=[i for i in range(n) if influence(a,i)]
        delta=add(H,const(-C*I));sigmas=[];JS=[];individual=[];overlap=Q(0)
        D=add(*(marginal_entropy(a,i) for i in relevant),scale(H,1-len(relevant)))
        eq(sign(D)>=0,True)
        for i in relevant:
            di=influence(a,i);eq(di,physical_i(v,n,i))
            children=[fwht(restricted(v,n,i,b)) for b in [0,1]]
            child_slacks=[add(const(C*total(ch,n-1)),scale(entropy(ch),-1)) for ch in children]
            sigma=scale(add(*child_slacks),Q(1,2));sigmas.append(sigma)
            individual.extend(sign(s)>=0 for s in child_slacks)
            js=packet_js(a,i);JS.append(js)
            eq(add(scope['erasure'](a,i),js),add(H,scale(add(*(entropy(ch) for ch in children)),-Q(1,2))))
            eq(add(const(C*di),delta,sigma),add(H,scale(add(*(entropy(ch) for ch in children)),-Q(1,2))))
            eq(sum(total(ch,n-1) for ch in children)/2,I-di)
            overlap+=sum((min(u*u,a[s|(1<<i)]**2) for s,u in enumerate(a) if not s>>i&1),Q(0))
        eq(add(D,scale(delta,len(relevant)-1),*sigmas),add(*JS))
        if sign(delta)>0 and all(sign(s)>=0 for s in sigmas):
            averaged+=1
            eq(len(relevant)>=2,True)
            # Prove the bound with a rational upper enclosure, not a float.
            a_hi=2/LN2[0]
            margin=add(const(a_hi*overlap),scale(delta,-(len(relevant)-1)),scale(D,-1),*(scale(s,-1) for s in sigmas))
            eq(sign(margin)>=0,True)
            if all(individual):minimal+=1
        return {'H':H,'I':I,'delta':delta,'sigmas':sigmas,'n':len(relevant),'all_individual_children_certified':all(individual)}
    for n in range(nmax+1):
        for b in range(1<<(1<<n)):
            for C in Cs:checked(seed(n,b),n,C)
    base=seed(3,254);seedstats=checked(base,3,Q(8,3))
    tensor_records=[]
    for m in ms:
        for C in Cs:
            stats=checked(tensor_values(base,m),3*m,C)
            origH=entropy(fwht(base));origI=total(fwht(base),3)
            originaldelta=add(origH,const(-C*origI));originalsig=add(const(C*Q(1,2)),const(-Q(1)))
            eq(stats['delta'],scale(originaldelta,m))
            for s in stats['sigmas']:eq(s,add(originalsig,scale(originaldelta,-(m-1))))
            if C==Q(8,3):
                tensor_records.append({'m':m,'relevant_dimension':3*m,'average_child_slack_signs':[sign(s) for s in stats['sigmas']],
                                       'all_individual_children_certified':stats['all_individual_children_certified'],
                                       'delta_interval':[str(x) for x in evaluate(stats['delta'])]})
    R=scale(seedstats['H'],Q(4,3));gap=add(R,const(-Q(8,3)))
    gaplo,gaphi=evaluate(gap);a_hi=2/LN2[0]
    eq(gaplo>a_hi/10,True)
    eq(sign(add(seedstats['delta'],const(-Q(1,6))))>0,True)
    eq(sign(add(const(Q(1,3)),scale(seedstats['delta'],-1)))>0,True)
    elapsed=time.perf_counter()-start
    assert elapsed<60,'Frozen 60-second job cap exceeded'
    result={'helper_version':'A005-stage2-v1','mode':mode,'cases':cases,'assertions':assertions,'failures':0,
            'all_individual_child_certified_violators':minimal,'all_average_child_certified_violators':averaged,
            'maximum_dimension':12 if mode=='full' else 6,'elapsed_seconds':elapsed,
            'tensor_seed_records':tensor_records,'seed_ratio_interval':[str(x) for x in evaluate(R)],
            'gap_over_a_div10_margin_lower':str(roundup((gaplo-a_hi/10,gaphi-a_hi/10))[0]),
            'dimension_obstruction':'At C=8/3, no n>=11 relevant-variable Boolean function of ratio >= that of the three-bit point defect can have all average children certified.',
            'arithmetic':'integer Walsh, direct physical edge count, exact log-prime vectors; rational atanh intervals with outward dyadic rounding'}
    (ROOT/'out'/f'{mode.upper()}_VALIDATION.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:result[k] for k in ['mode','cases','assertions','failures','elapsed_seconds','all_individual_child_certified_violators','all_average_child_certified_violators']}))
if __name__=='__main__':run(sys.argv[1])
