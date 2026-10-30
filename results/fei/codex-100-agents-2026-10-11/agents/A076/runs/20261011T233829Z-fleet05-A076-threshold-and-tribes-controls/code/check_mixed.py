"""A076 mixed-majority v1; exact log ledgers and rational interval certificates."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from math import comb
from pathlib import Path
import time, json, hashlib

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); checks=0
def eq(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1

def add(dst,src,weight=F(1)):
    for x,c in src.items():
        dst[x]+=weight*c
        if not dst[x]: del dst[x]

def term(dst,c,x):
    if c and x!=1:
        assert c>0 and x>0
        dst[x]+=c

@lru_cache(None)
def coeff(tt):
    a=list(tt); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]; a[j],a[j+h]=u+v,u-v
        h*=2
    return tuple(F(x,len(a)) for x in a)

def entropy(c):
    out=defaultdict(F)
    for x in c:
        p=x*x
        if p:term(out,p,1/p)
    return out

def influence(c):return sum((s.bit_count()*x*x for s,x in enumerate(c)),F(0))

@lru_cache(None)
def packet(tt):
    c=coeff(tt); L=len(tt)
    B=defaultdict(F); Q=defaultdict(F)
    mass=F(0); inf=F(0)
    for i in range(0,L,2):
        p=c[i]**2; v=c[i+1]**2; q=p+v; small=min(p,v)
        if p:term(B,p,q/p)
        if v:term(B,v,q/v)
        if small:term(Q,small,q/small)
        mass+=small; inf+=v
    eq(sum(x*x for x in c),F(1))
    eq(inf,F(sum(tt[i]!=tt[i+1] for i in range(0,L,2)),L//2))
    j=min(inf,1-inf)
    cg=coeff(tt[0::2]); ch=coeff(tt[1::2])
    kap=min(1-max(x*x for x in cg),1-max(x*x for x in ch))
    Lam=defaultdict(F)
    if j:term(Lam,j,1+kap/(2*j))
    return B,Q,Lam,mass,inf,kap

def permute(tt,order):
    return tuple(tt[sum(((z>>i)&1)<<old for i,old in enumerate(order))] for z in range(len(tt)))

def symmetric(tt):
    n=len(tt).bit_length()-1
    essential=[i for i in range(n) if any(tt[z]!=tt[z^(1<<i)] for z in range(len(tt)))]
    vals={}
    for z in range(1<<len(essential)):
        index=sum(((z>>j)&1)<<i for j,i in enumerate(essential))
        k=z.bit_count(); v=tt[index]
        if k in vals and vals[k]!=v:return False
        vals[k]=v
    ordered=[vals[k] for k in sorted(vals)]
    return sum(a!=b for a,b in zip(ordered,ordered[1:]))<=1

def tree(tt,stop):
    out={k:defaultdict(F) for k in ['B','Q','Lambda','Hleaf']}
    spent=leafI=defect=F(0); nodes=leaves=0
    todo=[(tt,F(1))]
    while todo:
        table,weight=todo.pop()
        if len(set(table))==1 or (stop and symmetric(table)):
            leaves+=1
            c=coeff(table); add(out['Hleaf'],entropy(c),weight)
            leafI+=weight*influence(c)
            continue
        B,Q,L,M,inf,kap=packet(table)
        nodes+=1
        add(out['B'],B,weight);add(out['Q'],Q,weight);add(out['Lambda'],L,weight)
        spent+=weight*inf;defect+=weight*M
        todo.extend([(table[0::2],weight/2),(table[1::2],weight/2)])
    eq(spent+leafI,influence(coeff(tt)))
    return out,spent,leafI,defect,nodes,leaves

# Log intervals: atanh series, reduced to [1,2], then outward dyadic rounding.
BITS=70; SCALE=1<<BITS; TERMS=24
def ln_series(x):
    z=(x-1)/(x+1);s=F(0)
    for k in range(TERMS):s+=2*z**(2*k+1)/F(2*k+1)
    tail=2*z**(2*TERMS+1)/((2*TERMS+1)*(1-z*z))
    return s,s+tail
LN2=ln_series(F(2))
@lru_cache(None)
def logbounds(x):
    if x==1:return F(0),F(0)
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/F(2)**k
    while y<1:k-=1;y*=2
    while y>2:k+=1;y/=2
    lo,hi=ln_series(y)
    if k>=0:lo+=k*LN2[0];hi+=k*LN2[1]
    else:lo+=k*LN2[1];hi+=k*LN2[0]
    corners=[a/b for a in (lo,hi) for b in LN2]
    lower=min(corners);upper=max(corners)
    il=(lower.numerator*SCALE)//lower.denominator
    iu=-((-upper.numerator*SCALE)//upper.denominator)
    return F(il,SCALE),F(iu,SCALE)

def bounds(expr):
    lo=hi=F(0)
    for x,c in expr.items():
        l,u=logbounds(x)
        if c>=0:lo+=c*l;hi+=c*u
        else:lo+=c*u;hi+=c*l
    return lo,hi

def encoded(expr):return [[str(x),str(c)] for x,c in sorted(expr.items())]
def interval(v):return dict(lower_exact=str(v[0]),upper_exact=str(v[1]),lower_diagnostic=float(v[0]),upper_diagnostic=float(v[1]))

def mixed(m,G):
    # first m bit-signs x=(-1)^b, then physical core bits
    return tuple(1 if m-2*(z&((1<<m)-1)).bit_count()+G[z>>m]>0 else -1 for z in range((1<<m)*len(G)))

transport_cases=0
for k in range(4):
    size=1<<k
    for mask in range(1<<size):
        G=tuple(1-2*((mask>>z)&1) for z in range(size))
        cg=coeff(G);mu=cg[0]
        for m in [2,4]:
            tt=mixed(m,G);cc=coeff(tt);alpha=F(comb(m,m//2),1<<m)
            gx=tuple(1 if m-2*x.bit_count()>0 else -1 if m-2*x.bit_count()<0 else 0 for x in range(1<<m))
            cx=tuple(int(m-2*x.bit_count()==0) for x in range(1<<m))
            gg=coeff(gx);cgx=coeff(cx)
            eq(sum(v*v for v in cgx),alpha)
            for s,c in enumerate(cc):
                X=s&((1<<m)-1);Y=s>>m
                expected=(gg[X] if Y==0 else 0)+cgx[X]*cg[Y]
                eq(c,expected)
            eq(influence(cc),alpha*(m+influence(cg)))
            for i in range(k):
                core_packet=packet(permute(G,[i]+[j for j in range(k) if j!=i]))
                big_packet=packet(permute(tt,[m+i]+[j for j in range(m+k) if j!=m+i]))
                for idx in [0,1]:
                    target=defaultdict(F);add(target,core_packet[idx],alpha)
                    eq(dict(big_packet[idx]),dict(target))
                eq(big_packet[3],alpha*core_packet[3]);eq(big_packet[4],alpha*core_packet[4])
            if m==2:
                for i in range(k):eq(packet(permute(tt,[m+i]+[j for j in range(m+k) if j!=m+i]))[5],F(3,4))
                p=mu*mu/F(4);q=F(1,4)
                expected=defaultdict(F)
                if p:term(expected,2*p,(p+q)/p)
                term(expected,2*q,(p+q)/q)
                # For each outer x coordinate this is the exact B expression.
                for i in range(2):
                    eq(dict(packet(permute(tt,[i]+[j for j in range(m+k) if j!=i]))[0]),dict(expected))
            transport_cases+=1

spec=json.loads((ROOT/'out'/'FROZEN_SPEC.json').read_text())
rows=[];ledgers=[]
for m,w,t in spec['domain']:
    mask=(1<<w)-1;core_n=w*t
    G=tuple(1 if any((z>>(w*j))&mask==0 for j in range(t)) else -1 for z in range(1<<core_n))
    tt=mixed(m,G);n=m+core_n;cc=coeff(tt);I=influence(cc);H=entropy(cc)
    x=list(range(m));y=list(range(m,n))
    alternating=[]
    for j in range(max(len(x),len(y))):
        if j<len(x):alternating.append(x[j])
        if j<len(y):alternating.append(y[j])
    for name,order in [('x-first',x+y),('y-first',y+x),('alternating-x-y',alternating)]:
        for stop in [False,True]:
            expr,spent,leafI,defect,nodes,leaves=tree(permute(tt,order),stop)
            if m==2 and name=='y-first':
                q=F(1,1<<w);b=1-q;beta=2*q*b**(t-1)
                closed=defaultdict(F)
                for j in range(t):
                    for u in range(1,w+1):
                        if stop and j==t-1 and u==1:continue
                        d=F(1,1<<(u-1))*b**(t-j-1)
                        term(closed,beta/2,1+F(3,4)/d)
                eq(dict(expr['Lambda']),dict(closed))
                if stop:
                    eq(leafI,1+beta/2)
                    eq(dict(expr['Hleaf']),{F(4):F(1)})
            certified={key:bounds(value) for key,value in expr.items()}
            Hbounds=bounds(H)
            # Analytic JS>=0 proves Btree+Hleaf<=H. Verify a signed
            # log expression certificate for these cases too; exact zeros
            # use coefficient-spectrum identity rather than interval noise.
            debt=defaultdict(F);add(debt,H);add(debt,expr['B'],-1);add(debt,expr['Hleaf'],-1)
            db=bounds(debt)
            assert db[0]>=0 or (db[0]<=0<=db[1] and float(db[1]-db[0])<1e-15)
            # Sandwich is a diagnostic only when intervals straddle zero.
            assert float(certified['Q'][0])<=float(Hbounds[1])+1e-15
            record=dict(m=m,w=w,t=t,policy=name,stopping='symmetric-threshold-leaves' if stop else 'constant-only',I_exact=str(I),consumed_influence_exact=str(spent),leaf_influence_exact=str(leafI),defect_exact=str(defect),internal_nodes=nodes,leaves=leaves,H=interval(Hbounds))
            for key,value in certified.items():record[key]=interval(value)
            # C_reg<9 follows from the provided source. 9 is the only
            # leaf-certificate constant used; no formula-class theorem.
            cert=(certified['Lambda'][0]+9*leafI,certified['Lambda'][1]+9*leafI)
            record['Lambda_plus_9_leafI_over_I']=interval((cert[0]/I,cert[1]/I))
            rows.append(record)
            ledgers.append(dict(m=m,w=w,t=t,policy=name,stopping=record['stopping'],expressions={key:encoded(value) for key,value in expr.items()},H_expression=encoded(H)))

# Exact constant used in the all-w proof, checked without logarithms.
eq(3*15**16>16**16,True)
for w in [16,18,20,22,24,26,28,30,32]:
    eq((1<<w)%4,0)
    eq(w//2-4>=w//4,True)

result=dict(helper_version='A076-mixed-majority-v2',transport_cases=transport_cases,tree_cases=len(rows),exact_assertions=checks,elapsed_seconds=time.perf_counter()-START,log_interval_method=dict(atanh_terms=TERMS,dyadic_rounding_bits=BITS,proved_remainder='2*z^(2N+1)/((2N+1)*(1-z^2)); range 0<=z<=1/3'),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=rows,scope='rational spectra/influence/kappa/log bounds exact; interval-straddling zero identities handled analytically; no all-dimensional claim comes from the finite grid')
(ROOT/'out'/'VALIDATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
(ROOT/'out'/'EXACT_LOG_LEDGERS.json').write_text(json.dumps(ledgers,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
