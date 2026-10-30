from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from math import isqrt
import time,json

ROOT=Path(__file__).resolve().parents[1]
started=time.perf_counter(); checks=0
def check(ok):
    global checks
    checks+=1
    assert ok
    if time.perf_counter()-started>58:raise RuntimeError('58-second pilot guard')
@lru_cache(None)
def factors(n):
    out={};p=2
    while p*p<=n and p<=1000:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p=3 if p==2 else p+2
    if n>1:
        s=isqrt(n)
        if s*s==n:
            for p,e in factors(s).items():out[p]=out.get(p,0)+2*e
        else:out[n]=out.get(n,0)+1
    return out
def addlog(z,x,c):
    if not c:return
    for n,sgn in [(x.numerator,1),(x.denominator,-1)]:
        for p,e in factors(n).items():z[p]=z.get(p,F(0))+sgn*c*e
def clean(z):return {p:c for p,c in z.items() if c}
def linear(*terms):
    z={}
    for coeff,vec in terms:
        for p,c in vec.items():z[p]=z.get(p,F(0))+coeff*c
    return clean(z)
def constant(x):return {2:F(x)} if x else {}
def entropy_weights(rows):
    z={}
    for count,p in rows:
        if p:addlog(z,p,-count*p)
    return clean(z)
def entropy(law):return entropy_weights([(1,p) for p in law])
def h(x):return entropy([x,1-x])
def phi(x):return linear((1,h(x)),(-F(1,2),h(2*x)))
def walsh(table):
    a=list(table);step=1
    while step<len(a):
        for b in range(0,len(a),2*step):
            for j in range(b,b+step):
                x,y=a[j],a[j+step];a[j],a[j+step]=x+y,x-y
        step*=2
    return a
def law(table):
    N=len(table)
    return [F(x*x,N*N) for x in walsh(table)]
def mutual(p,k):
    # Coordinate 0 is queried; independently reconstructed from joint entropies.
    d=sum(p[s] for s in range(len(p)) if s&1)
    residual=[p[2*t]+p[2*t+1] for t in range(len(p)//2)]
    return linear((1,h(d)),(1,entropy(residual)),(-1,entropy(p)))

nodes={1:{'d':F(1),'H':{},'M':{},'TC':{},'Gamma':{},'JS':{},'Credit':{},'B':{}}}
for k in range(2,17):
    d=F(1,2**(k-1));q0=(1-d)**2+d*d;beta=2*d*(1-d)
    H=entropy_weights([(1,(1-d)**2),(2**k-1,d*d)])
    M=linear((k,h(d)));TC=linear((1,M),(-1,H))
    Gamma=linear((k-1,phi(d)));JS=phi(beta)
    B=linear((q0,h(d*d/q0)),(1,constant(beta)))
    Credit=linear((1,h(d)),(-1,B))
    check(TC==linear((1,Credit),(-1,JS),(1,Gamma),(F(1,2),nodes[k-1]['TC'])))
    check(H==linear((1,B),(1,JS),(F(1,2),nodes[k-1]['H'])))
    nodes[k]={'d':d,'H':H,'M':M,'TC':TC,'Gamma':Gamma,'JS':JS,'Credit':Credit,'B':B}
    if k<=7:
        table=[-1]+[1]*(2**k-1);p=law(table)
        children=[table[parity::2] for parity in (0,1)]
        childlaws=[law(t) for t in children]
        q=[p[2*t]+p[2*t+1] for t in range(2**(k-1))]
        check(entropy(p)==H)
        check(mutual(p,k)==Credit)
        check(linear((1,entropy(q)),(-F(1,2),entropy(childlaws[0])),(-F(1,2),entropy(childlaws[1])))==JS)
        cd=[[sum(cp[s] for s in range(len(cp)) if s&(1<<j)) for j in range(k-1)] for cp in childlaws]
        direct_gamma={}
        for j in range(k-1):
            direct_gamma=linear((1,direct_gamma),(1,h(d)),(-F(1,2),h(cd[0][j])),(-F(1,2),h(cd[1][j])))
        check(direct_gamma==Gamma)
        edges=sum(table[x]!=table[x^(1<<j)] for x in range(2**k) for j in range(k))
        check(F(edges,2**k)==k*d)

def ln_series(x):
    t=(x-1)/(x+1);power=t;total=F(0)
    for j in range(20):total+=2*power/(2*j+1);power*=t*t
    return total,total+2*power/(41*(1-t*t))
LN2=ln_series(F(2));ell=(1/LN2[1],1/LN2[0])
@lru_cache(None)
def lg(x):
    x=F(x);shift=0
    while x>=2:x/=2;shift+=1
    while x<1:x*=2;shift-=1
    a,b=ln_series(x)
    return shift+a/LN2[1],shift+b/LN2[0]
def interval(vec):
    a=b=F(0)
    for p,c in vec.items():
        lo,hi=lg(p)
        if c<0:lo,hi=hi,lo
        a+=c*lo;b+=c*hi
    return a,b
def scaled(x,c):
    a,b=x
    return (a*c,b*c) if c>=0 else (b*c,a*c)
def out(x):
    scale=10**12;a,b=x
    return [str(F((a*scale).__floor__(),scale)),str(F((b*scale).__ceil__(),scale))]

rows=[];ledgers={}
for n in range(2,17):
    dn=nodes[n]['d'];influence=n*dn
    totals={name:{} for name in ['G','C','J','B','S']}
    for k in range(1,n+1):
        weight=F(2**k,2**n)
        for name,key in [('G','Gamma'),('C','Credit'),('J','JS'),('B','B')]:
            totals[name]=linear((1,totals[name]),(weight,nodes[k][key]))
        totals['S']=linear((1,totals['S']),(weight,h(nodes[k]['d'])))
    check(nodes[n]['TC']==linear((1,totals['G']),(1,totals['C']),(-1,totals['J'])))
    check(nodes[n]['H']==linear((1,totals['B']),(1,totals['J'])))
    check(totals['G']==linear((n,h(dn)),(-1,totals['S'])))
    baseline=F(n*(n-1),2)
    # Equality at n=2 endpoints is checked symbolically; strict signs otherwise
    # use rigorously enclosed logarithms with explicit series tails.
    gi=scaled(interval(totals['G']),1/dn)
    ji=scaled(interval(totals['J']),1/dn)
    check(gi[0]>baseline)
    check(gi[1]<baseline+2*ell[0])
    if n==2:check(totals['J']==constant(2*dn))
    else:
        check(ji[0]>2*(n-1)-1)
        check(ji[1]<2*(n-1)+4*ell[0]-1)
    row={'n':n,'I':str(influence),'Delta_over_I':out(scaled(interval(nodes[n]['TC']),1/influence))}
    for key in ['G','C','J','B','S']:row[key+'_over_I']=out(scaled(interval(totals[key]),1/influence))
    if n>=3:
        ti=interval(nodes[n]['TC']);check(ti[0]>0)
        for key in ['G','C','J']:
            a,b=interval(totals[key]);row[key+'_over_Delta']=out((a/ti[1],b/ti[0]))
    if n==16:
        check(interval(totals['G'])[0]>7*influence)
        check(interval(totals['C'])[0]>6*influence)
    rows.append(row);ledgers[n]=totals

# Replay every coordinate ordering for dimensions <=4 on physical restrictions.
order_count=0
def table_on_labels(n,remaining):
    return [-1]+[1]*(2**len(remaining)-1)
for n in range(2,5):
    for order in permutations(range(n)):
        accum={name:{} for name in ['G','C','J']};remaining=list(range(n));weight=F(1)
        for queried in order:
            k=len(remaining);table=table_on_labels(n,remaining);p=law(table)
            idx=remaining.index(queried)
            # Reindex spectral labels so queried coordinate is bit zero.
            new_order=[idx]+[j for j in range(k) if j!=idx]
            pp=[F(0)]*(2**k)
            for s,mass in enumerate(p):
                t=sum(((s>>j)&1)<<a for a,j in enumerate(new_order));pp[t]=mass
            check(mutual(pp,k)==nodes[k]['Credit'])
            for name,key in [('G','Gamma'),('C','Credit'),('J','JS')]:
                accum[name]=linear((1,accum[name]),(weight,nodes[k][key]))
            remaining.remove(queried);weight/=2
        check(accum=={key:ledgers[n][key] for key in ['G','C','J']});order_count+=1
result={'status':'PASS','assertions':checks,'elapsed_seconds':time.perf_counter()-started,'compressed_dimensions':15,'direct_dimensions':6,'all_order_replays':order_count,'rows':rows}
(ROOT/'out'/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
print('n16',json.dumps(rows[-1]))
