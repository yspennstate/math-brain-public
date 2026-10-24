"""A014-interference-v1. Exact finite tests, not a proof of all-q payment."""
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import argparse, hashlib, itertools, json, time

START=time.monotonic()
ASSERTIONS=0
def check(x):
    global ASSERTIONS
    ASSERTIONS+=1
    assert x
    if time.monotonic()-START>60: raise TimeoutError('Frozen 60-second compute budget')

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]; a[j],a[j+h]=u+v,u-v
        h*=2
    return a

@lru_cache(None)
def ln_interval(x):
    x=F(x); k=0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    def reduced(y):
        z=(y-1)/(y+1)
        lo=2*sum((z**(2*t+1)/F(2*t+1) for t in range(28)),F(0))
        err=2*z**57/(57*(1-z*z))
        return lo,lo+err
    lo,hi=reduced(x); l2,h2=reduced(F(2))
    return (lo+k*l2,hi+k*h2) if k>=0 else (lo+k*h2,hi+k*l2)

@lru_cache(None)
def log_interval(x):
    lo,hi=ln_interval(F(x)); l2,h2=ln_interval(F(2))
    vals=[lo/l2,lo/h2,hi/l2,hi/h2]
    return min(vals),max(vals)

def interval_expect(weights, ratios, scale=F(1)):
    lo=hi=F(0)
    for w,r in zip(weights,ratios):
        if w:
            l,h=log_interval(r); lo+=w*l*scale; hi+=w*h*scale
    return [str(lo),str(hi)]

def norm(v,q):
    t=next(x for x in v if x); inv=pow(t,-1,q)
    return tuple(x*inv%q for x in v)

def plane(q):
    pts=sorted({norm(v,q) for v in itertools.product(range(q),repeat=3) if any(v)})
    lines=[]
    for normal in pts:
        line=[i for i,p in enumerate(pts) if sum(x*y for x,y in zip(p,normal))%q==0]
        check(len(line)==q+1); lines.append(line)
    n=len(pts); check(n==q*q+q+1)
    check(all(sum(j in l for l in lines)==q+1 for j in range(n)))
    check(all(len(set(a)&set(b))==1 for a,b in itertools.combinations(lines,2)))
    return pts,lines

def analyse(name,n,gates, supports, rank_test=False):
    size=1<<n
    truth=[1 if any(g(x) for g in gates) else -1 for x in range(size)]
    full=fwht(truth); check(sum(v*v for v in full)==size*size)
    p=[F(v*v,size*size) for v in full]
    influence=sum(F(t.bit_count())*w for t,w in enumerate(p))
    entlo=enthi=F(0)
    for v in full:
        if v:
            w=F(v*v,size*size); lo,hi=log_interval(1/w)
            entlo+=w*lo; enthi+=w*hi
    rows=[]
    for j in range(n):
        physical=[i for i in range(n) if i!=j]; N=1<<(n-1)
        ids=[l for l,s in enumerate(supports) if j in s]
        arrays={l:[0]*N for l in ids}; deriv=[0]*N
        for z in range(N):
            x=sum(((z>>i)&1)<<physical[i] for i in range(n-1)); xp=x|(1<<j)
            d=(truth[xp]-truth[x])//2; deriv[z]=d
            if d:
                eligible=[l for l in ids if gates[l](x)!=gates[l](xp)]
                check(bool(eligible)); arrays[min(eligible)][z]=d
        transformed=[fwht(arrays[l]) for l in ids]
        total=fwht(deriv); alpha=F(sum(x*x for x in deriv),N)
        check(alpha==sum(w for t,w in enumerate(p) if t&(1<<j)))
        check(all(sum(row[t] for row in transformed)==total[t] for t in range(N)))
        masses=[F(sum(x*x for x in arrays[l]),N) for l in ids]
        check(sum(masses)==alpha)
        if not alpha: continue
        nu=[F(x*x,N*N)/alpha for x in total]
        rho=[F(sum(row[t]**2 for row in transformed),N*N)/alpha for t in range(N)]
        check(sum(nu)==sum(rho)==1)
        kappa=max((nu[t]/rho[t] for t in range(N) if rho[t]),default=F(0))
        check(kappa<=len(ids))
        eps={str(k):sum((max(F(0),v-k*r) for v,r in zip(nu,rho)),F(0)) for k in (1,2)}
        row={'j':j,'piece_ids':ids,'piece_masses':list(map(str,masses)), 'influence':str(alpha),
             'kappa':str(kappa),'kappa_empty':str(nu[0]/rho[0]) if rho[0] else None,
             'epsilon':{k:str(v) for k,v in eps.items()},
             'spectrum_sha256':hashlib.sha256(json.dumps(transformed).encode()).hexdigest()}
        if rank_test:
            ratios=[]
            for t in range(N):
                A={j}|{physical[i] for i in range(n-1) if t&(1<<i)}
                ratios.append(min(F(supports[l].index(j)+1,len(A&set(supports[l][:supports[l].index(j)]))+1) for l in ids))
            row['rank_mean_interval']=interval_expect(nu,ratios,F(6,5))
            row['incoherent_rank_mean_interval']=interval_expect(rho,ratios,F(6,5))
            tails=[]
            for r in sorted(set(ratios)):
                v=sum((w for w,x in zip(nu,ratios) if x>r),F(0))
                z=sum((w for w,x in zip(rho,ratios) if x>r),F(0))
                if z: tails.append([str(r),str(v/z)])
            row['tail_congestion']=tails
        if name.startswith('ADDR'):
            check(kappa<=2)
        rows.append(row)
    result={'family':name,'n':n,'read':max(sum(j in s for s in supports) for j in range(n)),
            'influence':str(influence),'entropy_interval':[str(entlo),str(enthi)],'derivatives':rows}
    if name.startswith('ADDR'):
        a=int(name[4:]); check(influence==1+F(a,2)); check(entlo<=2*a<=enthi)
    return result

def pp(q):
    pts,lines=plane(q)
    masks=[sum(1<<j for j in l) for l in lines]
    gates=[lambda x,m=m: x&m==m for m in masks]
    return analyse('PP'+str(q),len(pts),gates,lines,True)

def addr(a):
    m=1<<a; n=a+m
    gates=[lambda x,u=u: (x&(m-1))==u and bool(x&(1<<(a+u))) for u in range(m)]
    supports=[list(range(a))+[a+u] for u in range(m)]
    return analyse('ADDR'+str(a),n,gates,supports)

parser=argparse.ArgumentParser(); parser.add_argument('--pilot',action='store_true'); parser.add_argument('--out',required=True)
args=parser.parse_args()
results=[pp(2)] if args.pilot else [pp(2),pp(3)]+[addr(a) for a in (1,2,3)]
out={'helper':'A014-interference-v1','assertions':ASSERTIONS,'elapsed_seconds':time.monotonic()-START,'results':results}
Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'assertions':ASSERTIONS,'elapsed_seconds':out['elapsed_seconds'],
 'summaries':[{'family':r['family'],'I':r['influence'],'kappa_max':str(max(F(d['kappa']) for d in r['derivatives'])),'mass_profiles': sorted(set(tuple(d['piece_masses']) for d in r['derivatives']))} for r in results]}))
