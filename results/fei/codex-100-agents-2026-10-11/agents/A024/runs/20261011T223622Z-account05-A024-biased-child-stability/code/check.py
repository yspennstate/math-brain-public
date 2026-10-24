from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time,argparse

RUN=Path(__file__).resolve().parents[1]
count=0
def ck(a,b):
    global count
    assert a==b,(a,b)
    count+=1

@lru_cache(None)
def factors(n):
    ans={}; d=2
    while d*d<=n:
        while n%d==0: ans[d]=ans.get(d,0)+1; n//=d
        d+=1
    if n>1: ans[n]=ans.get(n,0)+1
    return ans
def add(*terms):
    out={}
    for z in terms:
        for k,v in z.items(): out[k]=out.get(k,Q(0))+v
    return {k:v for k,v in out.items() if v}
def scale(a,z): return {k:a*v for k,v in z.items() if a*v}
def logterm(a,x):
    if not a: return {}
    assert x>0
    return add({k:a*v for k,v in factors(x.numerator).items()},{k:-a*v for k,v in factors(x.denominator).items()})
def e(x): return logterm(-x,x) if x else {}
def L(a,b): return add(e(a*a),e(b*b),scale(-1,e(a*a+b*b)))
def erasure(tab,i):
    a=walsh(tab)
    return add(*(L(a[s],a[s|1<<i]) for s in range(len(a)) if not s>>i&1))
def H(p): return add(*(e(x) for x in p))
def E(p,w): return add(*(logterm(x,y/x) for i,(x,y) in enumerate(zip(p,w)) if i and x))
def delta(a,b,c): return add(a,scale(-Q(1,2),b),scale(-Q(1,2),c))
def scalar(x): return {2:Q(x)} if x else {}
def deficit(p): return sum(Q(s.bit_count()-1)*v for s,v in enumerate(p) if s)
def influence(p): return sum(Q(s.bit_count())*v for s,v in enumerate(p))
def walsh(table):
    a=list(table); h=1
    while h<len(a):
        for b in range(0,len(a),2*h):
            for j in range(b,b+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    # Walsh uses (-1)^bit: squared coefficients are insensitive to sign convention.
    return tuple(Q(x,len(a)) for x in a)
def table(n,k): return tuple(1 if k>>x&1 else -1 for x in range(1<<n))
@lru_cache(None)
def spec(tab):
    a=walsh(tab); p=tuple(x*x for x in a)
    return {'m':Q(sum(tab),len(tab)),'p':p,'H':H(p),'E':H(p[1:]),'I':influence(p),'D':deficit(p)}

@lru_cache(None)
def outer(tab,means):
    n=len(means); p=[]; w=[]
    for s in range(1<<n):
        c=Q(0)
        for x,f in enumerate(tab):
            prob=Q(1); sign=1
            for i,m in enumerate(means):
                if s>>i&1:
                    prob/=2; sign*=1 if x>>i&1 else -1
                else: prob*= (1+m)/2 if x>>i&1 else (1-m)/2
            c+=f*prob*sign
        ws=Q(1)
        for i,m in enumerate(means):
            if s>>i&1: ws*=1-m*m
        p.append(ws*c*c); w.append(ws)
    ck(sum(p),1)
    weights=[]
    for i in range(n):
        t=Q(0)
        for x in range(1<<n):
            if x>>i&1: continue
            prob=Q(1)
            for j,m in enumerate(means):
                if j!=i: prob*= (1+m)/2 if x>>j&1 else (1-m)/2
            der=Q(tab[x|1<<i]-tab[x],2)
            t+=prob*der*der
        weights.append(t)
        ck(sum(p[s] for s in range(1<<n) if s>>i&1),(1-means[i]**2)*t)
    return {'m':sum(tab[x]*__import__('functools').reduce(lambda a,i:a*((1+means[i])/2 if x>>i&1 else (1-means[i])/2),range(n),Q(1)) for x in range(1<<n)), 'p':tuple(p),'E':E(p,w),'I':influence(p),'D':deficit(p),'a':tuple(weights)}

def compose(g,f,h):
    return tuple(g[(1 if f[x&3]>0 else 0)+2*(1 if h[x>>2]>0 else 0)] for x in range(16))
def restrict(tab,n,i,bit):
    return tuple(tab[(x&((1<<i)-1))|((x>>i)<<(i+1))|(bit<<i)] for x in range(1<<(n-1)))
def check_composition(g,f,h):
    sf,sh=spec(f),spec(h); F=compose(g,f,h); z=spec(F)
    o=outer(g,(sf['m'],sh['m'])); t=o['a'][0]
    ck(z['E'],add(o['E'],scale(t,sf['E']),scale(o['a'][1],sh['E'])))
    ck(z['I'],t*sf['I']+o['a'][1]*sh['I'])
    ck(z['D'],o['D']+t*sf['D']+o['a'][1]*sh['D'])
    ck(z['m'],o['m'])
    for i in range(2):
        children=[spec(restrict(F,4,i,b)) for b in [0,1]]
        fc=[spec(restrict(f,2,i,b)) for b in [0,1]]
        oc=[outer(g,(s['m'],sh['m'])) for s in fc]
        beta=(fc[1]['m']-fc[0]['m'])/2
        d=sf['I']-(fc[0]['I']+fc[1]['I'])/2
        b=(g[1]-g[0])*(1-sh['m'])/4+(g[3]-g[2])*(1+sh['m'])/4
        ck(o['a'][1],(oc[0]['a'][1]+oc[1]['a'][1])/2)
        ck(t,oc[0]['a'][0]); ck(t,oc[1]['a'][0])
        ck(o['D']-(oc[0]['D']+oc[1]['D'])/2,beta*beta*(t-b*b))
        ck(z['D']-(children[0]['D']+children[1]['D'])/2,t*d-b*b*beta*beta)
        ck(z['I']-(children[0]['I']+children[1]['I'])/2,t*d)
        deouter=delta(o['E'],oc[0]['E'],oc[1]['E'])
        deinner=delta(sf['E'],fc[0]['E'],fc[1]['E'])
        ck(delta(z['E'],children[0]['E'],children[1]['E']),add(deouter,scale(t,deinner)))
        norm=add(delta(e(z['m']**2),e(children[0]['m']**2),e(children[1]['m']**2)),scale(-t,delta(e(sf['m']**2),e(fc[0]['m']**2),e(fc[1]['m']**2))))
        transport=add(deouter,norm)
        ck(delta(z['H'],children[0]['H'],children[1]['H']),add(scale(t,delta(sf['H'],fc[0]['H'],fc[1]['H'])),transport))
        full_delta=add(scalar(8*t*d),scale(-1,delta(z['H'],children[0]['H'],children[1]['H'])))
        inner_delta=add(scalar(8*d),scale(-1,delta(sf['H'],fc[0]['H'],fc[1]['H'])))
        ck(full_delta,add(scale(t,inner_delta),scale(-1,transport)))
        A=tuple(Q(g[0 if h[y]<0 else 2]+g[1 if h[y]<0 else 3],2) for y in range(4))
        B=tuple(Q(g[1 if h[y]<0 else 3]-g[0 if h[y]<0 else 2],2) for y in range(4))
        aa,bb=walsh(A),walsh(B)
        beta_w=-beta
        residual=add(*(L(a+sf['m']*b,beta_w*b) for a,b in zip(aa,bb)),scale(-t,L(sf['m'],beta_w)))
        BF,Bf=erasure(F,i),erasure(f,i)
        ck(BF,add(scale(t,Bf),residual))
        JSF=add(delta(z['H'],children[0]['H'],children[1]['H']),scale(-1,BF))
        JSf=add(delta(sf['H'],fc[0]['H'],fc[1]['H']),scale(-1,Bf))
        ck(transport,add(residual,JSF,scale(-t,JSf)))
        if beta==0: ck(transport,{})
    return 2

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); args=ap.parse_args()
    started=time.perf_counter(); cases=0; splits=0
    gates=range(4) if args.pilot else range(16)
    for kg in gates:
        g=table(2,kg)
        for kf in range(16):
            for kh in (range(4) if args.pilot else range(16)):
                splits+=check_composition(g,table(2,kf),table(2,kh)); cases+=1
    # Near-dictator family f=x h(z), h=1-2*one_point(z); split x.
    endpoint=[]
    if not args.pilot:
        for r in range(2,9):
            h=tuple(-1 if x==0 else 1 for x in range(1<<r))
            f=tuple((1 if x&1 else -1)*h[x>>1] for x in range(1<<(r+1)))
            F=tuple(1-2*int(f[x&((1<<(r+1))-1)]>0 and x>>(r+1)&1) for x in range(1<<(r+2)))
            sf=spec(f); z=spec(F)
            fc=[spec(restrict(f,r+1,0,b)) for b in [0,1]]
            zc=[spec(restrict(F,r+2,0,b)) for b in [0,1]]
            ck(delta(sf['H'],fc[0]['H'],fc[1]['H']),{})
            ck(sf['I']-(fc[0]['I']+fc[1]['I'])/2,1)
            ck(z['I']-(zc[0]['I']+zc[1]['I'])/2,Q(1,2))
            endpoint.append({'r':r,'inner_mismatch':0,'inner_entropy_drop':0,'outer_pivotal': '1/2','transport_prime_log_coefficients':{str(k):str(v) for k,v in delta(z['H'],zc[0]['H'],zc[1]['H']).items()}})
    result={'status':'PASS','compositions':cases,'physical_splits':splits,'exact_assertions':count,'seconds':time.perf_counter()-started,'arithmetic':'integer Walsh, Fraction, exact rational prime-log coefficient identities','near_dictator_cases':endpoint}
    target=RUN/'out'/('PILOT.json' if args.pilot else 'VALIDATION.json')
    target.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='near_dictator_cases'}))
if __name__=='__main__': main()
