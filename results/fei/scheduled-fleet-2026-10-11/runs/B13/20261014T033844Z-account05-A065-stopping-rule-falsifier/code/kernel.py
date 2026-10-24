"""A065 v1: exact integer Walsh and outward fixed-point entropy/reserve bounds."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import json, time, sys, hashlib

ROOT=Path(__file__).resolve().parents[1]
SCALE=1<<70
ASSERTIONS=0
def check(c):
    global ASSERTIONS
    assert c
    ASSERTIONS+=1

def ln_bounds(x, terms=28):
    z=(x-1)/(x+1)
    check(0<=z<=F(1,3))
    total=F(0); power=z
    for j in range(terms):
        total+=2*power/(2*j+1)
        power*=z*z
    err=2*power/((2*terms+1)*(1-z*z))
    return total,total+err

L2=ln_bounds(F(2))
def floor(x): return x.numerator//x.denominator
def ceil(x): return -((-x.numerator)//x.denominator)
@lru_cache(None)
def log_bounds(v):
    check(v>=1)
    j=v.bit_length()-1
    if v==1<<j: return j*SCALE,j*SCALE
    lo,hi=ln_bounds(F(v,1<<j))
    return floor((j+lo/L2[1])*SCALE),ceil((j+hi/L2[0])*SCALE)

def walsh(t):
    a=[1-2*x for x in t]; step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):
                u,v=a[k],a[k+step]
                a[k],a[k+step]=u+v,u-v
        step*=2
    check(sum(c*c for c in a)==len(a)**2)
    return a

@lru_cache(None)
def children(t,i):
    b=1<<i; low=bytearray(); high=bytearray()
    for j in range(0,len(t),2*b):
        low.extend(t[j:j+b]); high.extend(t[j+b:j+2*b])
    return bytes(low),bytes(high)

@lru_cache(None)
def stats(t):
    n=len(t).bit_length()-1; N=len(t)
    if t.count(t[0])==N: return (0,0),tuple(0 for _ in range(n))
    w=walsh(t); mult=Counter(abs(v) for v in w if v)
    s_lo=s_hi=0
    for v,c in mult.items():
        a,b=log_bounds(v)
        s_lo+=c*v*v*a; s_hi+=c*v*v*b
    den=N*N
    h=(2*n*SCALE-ceil(F(2*s_hi,den)),2*n*SCALE-floor(F(2*s_lo,den)))
    inf=[]
    for i in range(n):
        a,b=children(t,i)
        count=sum(u!=v for u,v in zip(a,b))
        check(sum(v*v for j,v in enumerate(w) if (j>>i)&1)==2*N*count)
        inf.append(count)
    check(h[0]>=0 and h[1]<=n*SCALE)
    return h,tuple(inf)

def add(a,b): return a[0]+b[0],a[1]+b[1]
def sub(a,b): return a[0]-b[1],a[1]-b[0]
def half(a): return a[0]//2,(a[1]+1)//2
def exact(x): return floor(x*SCALE),ceil(x*SCALE)
def pos(a): return max(0,a[0]),max(0,a[1])

@lru_cache(None)
def factors(v):
    d=2; out={}
    while d*d<=v:
        while v%d==0:
            out[d]=out.get(d,0)+1; v//=d
        d+=1
    if v>1: out[v]=out.get(v,0)+1
    return out

@lru_cache(None)
def symbolic_H(t):
    n=len(t).bit_length()-1; N=len(t); d={2:F(2*n)}
    for v,c in Counter(abs(v) for v in walsh(t) if v).items():
        for p,e in factors(v).items():
            d[p]=d.get(p,F(0))-F(2*c*v*v*e,N*N)
    return {p:c for p,c in d.items() if c}

def symbolic_ratio(t,i,count):
    a,b=children(t,i); d=dict(symbolic_H(t))
    for child in (a,b):
        for p,c in symbolic_H(child).items(): d[p]=d.get(p,F(0))-c/2
    return {p:c/count for p,c in d.items() if c}

RULES=['min-influence','max-influence','greedy-min-D-over-d','control-first','selector-first']
PRICES=[F(4),F(32609,5000),F(8)]

def tree(t,labels,rule,groups,prices=PRICES):
    records=[]; nodes=0; ties=0
    @lru_cache(None)
    def visit(t,labels):
        nonlocal nodes,ties
        nodes+=1
        h,counts=stats(t); relevant=[i for i,c in enumerate(counts) if c]
        if not relevant: return tuple((0,0) for _ in prices)
        if rule=='min-influence': i=min(relevant,key=lambda i:(counts[i],labels[i]))
        elif rule=='max-influence': i=min(relevant,key=lambda i:(-counts[i],labels[i]))
        elif rule=='greedy-min-D-over-d':
            i=relevant[0]; ratio=None
            for j in relevant:
                a,b=children(t,j)
                delta=sub(h,half(add(stats(a)[0],stats(b)[0])))
                rr=(F(delta[0],counts[j]),F(delta[1],counts[j]))
                if ratio is None: ratio=rr; i=j
                elif rr[1]<ratio[0]: ratio=rr; i=j
                elif rr[0]<=ratio[1]:
                    check(symbolic_ratio(t,j,counts[j])==symbolic_ratio(t,i,counts[i]))
                    ties+=1
                    if labels[j]<labels[i]: ratio=rr; i=j
        else:
            order=['control','core','selector','data'] if rule=='control-first' else ['selector','control','core','data']
            i=min(relevant,key=lambda i:(order.index(groups[labels[i]]),labels[i]))
        a,b=children(t,i); new=labels[:i]+labels[i+1:]
        qa,qb=visit(a,new),visit(b,new)
        delta=sub(h,half(add(stats(a)[0],stats(b)[0])))
        d=F(2*counts[i],len(t))
        check(delta[1]>=0)
        check(F(sum(counts)*2,len(t))==d+(F(sum(stats(a)[1])*2,len(a))+F(sum(stats(b)[1])*2,len(b)))/2)
        result=tuple(pos(add(sub(delta,exact(C*d)),half(add(x,y)))) for C,x,y in zip(prices,qa,qb))
        if len(labels)==len(groups):
            records.append({'coordinate':labels[i],'group':groups[labels[i]],'d':str(d),'D_bounds_scaled':delta,'local_ratio_bounds':[float(F(z,SCALE)/d) for z in delta]})
        check(all(q[0]>=0 and q[1]<=h[1]+2*len(labels) for q in result))
        return result
    qs=visit(t,tuple(labels)); I=F(2*sum(stats(t)[1]),len(t))
    check(all(qs[j][0]>=qs[j+1][0] for j in range(len(qs)-1)))
    return {'rule':rule,'I_exact':str(I),'H_scaled':stats(t)[0],'Q_scaled':qs,'Q_over_I_bounds':[[float(F(x,SCALE)/I),float(F(y,SCALE)/I)] for x,y in qs], 'root_query':records,'unique_tree_nodes':nodes,'greedy_exact_ties':ties}

def bent_defect(k,r):
    n=k+r+1; t=bytearray()
    for v in range(1<<n):
        x=v&((1<<k)-1); z=(v>>k)&((1<<r)-1); y=(v>>(k+r))&1
        b=sum(((x>>j)&1)*((x>>(j+1))&1) for j in range(0,k,2))%2
        t.append(0 if z else (b ^ (int(x==0) if y else 0)))
    return bytes(t), ['core']*k+['control']*r+['selector']

def addressing(a):
    n=a+(1<<a)
    return bytes((v>>(a+(v&((1<<a)-1))))&1 for v in range(1<<n)), ['selector']*a+['data']*(1<<a)

def defect(n):
    return bytes(int(v==0) for v in range(1<<n)),['control']*n

def main():
    start=time.monotonic(); pilot='--pilot' in sys.argv
    families=[('B05-k2',*bent_defect(2,4))] if pilot else [
        ('B05-k2',*bent_defect(2,4)),('B05-k4',*bent_defect(4,8)),
        *[(f'splice-k{k}',*bent_defect(k,0)) for k in (2,4,6)],
        *[(f'address-a{a}',*addressing(a)) for a in (1,2,3)],
        *[(f'defect-n{n}',*defect(n)) for n in (2,4,8)]]
    output={'helper_version':'A065 reserve-check v1','scale':str(SCALE),'prices':[str(c) for c in PRICES],'cases':[]}
    for name,t,groups in families:
        for rule in RULES:
            row={'family':name,'dimension':len(groups),**tree(t,list(range(len(groups))),rule,groups)}
            output['cases'].append(row)
            output['assertions']=ASSERTIONS; output['elapsed_seconds']=time.monotonic()-start
            (ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
            print(name,rule,row['Q_over_I_bounds'],flush=True)
        stats.cache_clear();children.cache_clear();symbolic_H.cache_clear()
        check(time.monotonic()-start<(60 if pilot else 1500))
    output['assertions']=ASSERTIONS; output['elapsed_seconds']=time.monotonic()-start
    output['log_cache']=log_bounds.cache_info()._asdict()
    output['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print('PASS',ASSERTIONS,'seconds',output['elapsed_seconds'],flush=True)

if __name__=='__main__':main()
