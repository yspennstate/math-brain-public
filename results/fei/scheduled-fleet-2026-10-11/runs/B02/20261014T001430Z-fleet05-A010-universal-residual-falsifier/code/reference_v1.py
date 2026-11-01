"""A010 PI-J v1: integer Boolean census and certified residual intervals."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations, product
from functools import lru_cache
import json, math, time, hashlib, sys
RUN=Path(__file__).resolve().parents[1]
OUT=RUN/'out'; OUT.mkdir(exist_ok=True)

def dyadic_bounds(a,b,bits=64):
    scale=1<<bits
    return Q((a*scale).__floor__(),scale),Q((b*scale).__ceil__(),scale)

def walsh(t,n):
    a=[1 if t>>x&1 else -1 for x in range(1<<n)]
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    assert sum(x*x for x in a)==(1<<n)**2
    edge=sum(((t>>x)^(t>>(x^(1<<j))))&1 for x in range(1<<n) for j in range(n))
    assert sum(s.bit_count()*a[s]**2 for s in range(1<<n))==edge*(1<<n)
    return a

def primes(t,n):
    full=(1<<(1<<n))-1; gates=[]
    for mask in range(1,1<<n):
        for val in range(1<<n):
            if val&~mask: continue
            cells=sum(1<<x for x in range(1<<n) if x&mask==val)
            if cells&t!=cells: continue
            if any(all(t>>x&1 for x in range(1<<n) if x&(mask^(1<<j))==val&(mask^(1<<j))) for j in range(n) if mask>>j&1): continue
            gates.append((mask,val))
    if t not in (0,full):
        cover=0
        for mask,val in gates:
            cover|=sum(1<<x for x in range(1<<n) if x&mask==val)
        assert cover==t
    return gates

def reps(n):
    size=1<<n; full=(1<<size)-1; seen=bytearray(1<<size); result=[]
    maps=[]
    for perm in permutations(range(n)):
        for flip in range(size):
            maps.append([sum(((x>>j&1)^(flip>>j&1))<<perm[j] for j in range(n)) for x in range(size)])
    for t in range(1<<size):
        if seen[t]: continue
        orbit=set()
        ones=[x for x in range(size) if t>>x&1]
        for mapping in maps:
            v=sum(1<<mapping[x] for x in ones); orbit.add(v); orbit.add(v^full)
        for v in orbit: seen[v]=1
        result.append((t,len(orbit)))
    assert sum(c for _,c in result)==1<<size
    return result

def fifthfloor(a):
    if not a: return 0
    lo=0; hi=1<<((a.bit_length()+4)//5)
    while hi-lo>1:
        mid=(hi+lo)//2
        if mid**5<=a: lo=mid
        else: hi=mid
    return lo

@lru_cache(None)
def power_interval(d):
    # d^(6/5), dyadic enclosure verified by integer fifth powers.
    scale=1<<72; a=d.numerator**6*scale**5; b=d.denominator**6
    k=fifthfloor(a//b)
    assert k**5*b<=a<(k+1)**5*b
    return Q(k,scale),Q(k+1,scale)

@lru_cache(None)
def ln_interval(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/(Q(2)**k)
    if y<1: k-=1; y*=2
    assert 1<=y<2
    def series(y):
        z=(y-1)/(y+1); zl,zh=dyadic_bounds(z,z,80)
        z2l,z2h=dyadic_bounds(zl*zl,zh*zh,80)
        tl,th=zl,zh; sl,sh=Q(0),Q(0)
        for j in range(40):
            sl,sh=dyadic_bounds(sl+tl/(2*j+1),sh+th/(2*j+1),80)
            tl,th=dyadic_bounds(tl*z2l,th*z2h,80)
        tail=2*th/(81*(1-z2h))
        return 2*sl,2*sh+tail
    a,b=series(y); c,d=series(Q(2))
    lo,hi=(a+k*c,b+k*d) if k>=0 else (a+k*d,b+k*c)
    return dyadic_bounds(lo,hi)

@lru_cache(None)
def log_interval(x):
    a,b=ln_interval(x); c,d=ln_interval(Q(2))
    vals=[a/c,a/d,b/c,b/d]
    return dyadic_bounds(min(vals),max(vals))

def graph_roots(used,parts,supports):
    reach={l:{l}|{k for k in used if k!=l and parts[l]&supports[k]} for l in used}
    for mid in used:
        for l in used:
            if mid in reach[l]: reach[l]|=reach[mid]
    comps=[]; done=set()
    for l in used:
        if l in done: continue
        c={k for k in used if k in reach[l] and l in reach[k]}; done|=c; comps.append(c)
    return [c for c in comps if not any(l not in c and any(k in reach[l] for k in c) for l in used)]

def mass(A,gates,lam,n):
    supports=[g[0] for g in gates]; js=[j for j in range(n) if A>>j&1]
    choices=[[l for l,m in enumerate(supports) if m>>j&1] for j in js]
    low=Q(0); high=Q(0); count=0
    for assignment in product(*choices):
        parts={}
        for j,l in zip(js,assignment): parts[l]=parts.get(l,0)|(1<<j)
        used=tuple(parts); sources=graph_roots(used,parts,supports)
        base=Q(1); d=Q(1)
        for l in used:
            base*=lam
            s=parts[l].bit_count(); kap=(A&supports[l]).bit_count()
            d*=Q(s,kap)**s
            order=[j for j in range(n) if supports[l]>>j&1]
            for j in js:
                if parts[l]>>j&1:
                    rank=order.index(j)+1; pred=sum(A>>i&1 for i in order[:rank-1])
                    d*=Q(pred+1,rank)
        pl,ph=power_interval(d)
        parents=[[None]+[l for l in used if l!=k and parts[l]&supports[k]] for k in used]
        for pp in product(*parents):
            pd=dict(zip(used,pp)); roots={k for k in used if pd[k] is None}
            if len(roots)!=len(sources) or any(len(roots&c)!=1 for c in sources): continue
            valid=True
            for k in used:
                path=set(); v=k
                while v is not None:
                    if v in path: valid=False; break
                    path.add(v); v=pd[v]
                if not valid: break
            if not valid: continue
            edges=[(pd[k],k) for k in used if pd[k] is not None]
            attachment_options=[[j for j in js if (parts[p]&supports[k])>>j&1] for p,k in edges]
            mult=0
            for attach in product(*attachment_options):
                counts={}
                for (p,k),j in zip(edges,attach): counts[p,j]=counts.get((p,j),0)+1
                mult+=math.prod(math.factorial(v) for v in counts.values())
            factor=base*Q(mult)*math.prod(Q(1,1<<supports[l].bit_count()) for l in roots)
            low+=factor*pl; high+=factor*ph; count+=mult
    assert low>0 and high>=low
    return low,high,count

def evaluate(t,n):
    a=walsh(t,n); den=(1<<n)**2
    I=Q(sum(s.bit_count()*a[s]**2 for s in range(1<<n)),den)
    if not I: return None
    gates=primes(t,n); read=max(sum(mask>>j&1 for mask,val in gates) for j in range(n)); lam=Q(1,read)
    T=math.prod(1+lam*Q(1,1<<mask.bit_count()) for mask,val in gates)-1
    lo=Q(0); hi=Q(0); hlow=Q(0); hhigh=Q(0); runs=0
    for A,coeff in enumerate(a):
        if not coeff: continue
        p=Q(coeff*coeff,den); x,y=log_interval(1/p); hlow+=p*x; hhigh+=p*y
        if not A: continue
        wlo,whi,c=mass(A,gates,lam,n); runs+=c
        x,_=log_interval(T/whi); _,y=log_interval(T/wlo); lo+=p*x; hi+=p*y
    return {'truth':t,'n':n,'gates':gates,'read':read,'I':str(I),'ratio_lo':str(lo/I),'ratio_hi':str(hi/I),'ratio':float((lo+hi)/(2*I)),'H_I_lo':str(hlow/I),'H_I_hi':str(hhigh/I),'distinct_runs':runs}

def main():
    start=time.monotonic(); limit=int(sys.argv[1]) if len(sys.argv)>1 else 4
    census=[]; rows=[]
    for n in range(1,limit+1):
        rr=reps(n); census.append({'n':n,'classes':len(rr),'truth_tables':sum(c for _,c in rr)})
        for i,(t,c) in enumerate(rr):
            if time.monotonic()-start>1500: raise RuntimeError('frozen runtime cap')
            full=(1<<(1<<n))-1
            records=[evaluate(t,n),evaluate(t^full,n)]
            records=[r for r in records if r is not None]
            if records:
                r=min(records,key=lambda x:x['ratio']); r['orbit_size']=c; r['representative']=t
                r['both_orientations']=[{'truth':x['truth'],'ratio_lo':x['ratio_lo'],'ratio_hi':x['ratio_hi'],'ratio':x['ratio']} for x in records]
                rows.append(r)
            if i%25==0:
                (OUT/'checkpoint.json').write_text(json.dumps({'n':n,'completed':i+1,'elapsed':time.monotonic()-start}))
        print('n',n,'classes',len(rr),'elapsed',time.monotonic()-start,flush=True)
    rows.sort(key=lambda x:x['ratio'],reverse=True)
    result={'helper_version':'PI-J-v1','census':census,'elapsed_seconds':time.monotonic()-start,'rows':rows,'max_interval_width':max(float(Q(x['ratio_hi'])-Q(x['ratio_lo'])) for x in rows)}
    (OUT/'results.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({'census':census,'top':[{'n':r['n'],'truth':r['truth'],'ratio':r['ratio'],'read':r['read']} for r in rows[:10]],'elapsed':result['elapsed_seconds']},indent=2),flush=True)

if __name__=='__main__': main()
