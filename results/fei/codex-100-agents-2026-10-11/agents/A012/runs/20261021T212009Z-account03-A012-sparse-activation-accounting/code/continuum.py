"""Exact tangent certificates; no float arithmetic in certification."""
from pathlib import Path
from functools import lru_cache
from itertools import product
import json,time,sys
ROOT=Path(__file__).resolve().parents[1];(ROOT/'out').mkdir(exist_ok=True)
S=1<<80
def ceildiv(a,b):return -(-a//b)
@lru_cache(None)
def lnsmall(n,d,N=24):
    # 1<=n/d<=2, t=(n-d)/(n+d)<=1/3.
    assert d<=n<=2*d
    tl=(n-d)*S//(n+d);th=ceildiv((n-d)*S,n+d)
    lo=hi=0;pl,ph=tl,th
    t2l=tl*tl//S;t2h=ceildiv(th*th,S)
    for j in range(N):
        lo+=2*pl//(2*j+1);hi+=ceildiv(2*ph,2*j+1)
        pl=pl*t2l//S;ph=ceildiv(ph*t2h,S)
    # uniform tail 2*(1/3)^(2N+1)/((2N+1)*(1-1/9))
    hi+=ceildiv(18*S,8*(2*N+1)*3**(2*N+1))
    return lo,hi
L2,H2=lnsmall(2,1)
@lru_cache(None)
def logupper(n,d):
    assert n>=d>0
    k=0
    while n>=2*d:d*=2;k+=1
    _,h=lnsmall(n,d)
    return k*S+ceildiv(h*S,L2)
def phase(mask):return [1-2*((mask>>s)&1) for s in range(8)]
def chars(s,t):return 1-2*((s&t).bit_count()%2)
def profile(mask):
    c=phase(mask)
    return [(sum(c[s]*chars(s,t) for s in range(8)),tuple(c[j]*chars(j,t) for j in (0,1,2))) for t in range(8)]
def canonical(mask):
    c=phase(mask);o=[]
    for t in range(8):
        for sign in (-1,1):
            o.append(sum((c[s]*chars(s,t)*sign<0)<<s for s in range(8)))
    return min(o)
REPS=sorted({canonical(m) for m in range(256)})
def certificate(P,idx,dep):
    den=1<<dep;mid=[2*j+1 for j in idx];md=2*den
    slopes=[]
    for a,v in P:
        if not a:continue # Phi(b^2,b^2)-2b^2=0 exactly.
        k=sum(v[j]*mid[j] for j in range(3));x=(a*md-k)**2;y=k*k
        if not y:nu,de=1,1024
        elif not x:nu,de=1023,1024
        else:nu,de=y,x+y
        lam=logupper(de,de-nu);mu=logupper(de,nu)
        assert lam+mu>=2*S
        slopes.append((a,v,lam,mu))
    worst=None
    for bits in product((0,1),repeat=3):
        q=[idx[j]+bits[j] for j in range(3)]
        val=-16*den*S*sum(q)
        for a,v,lam,mu in slopes:
            k=sum(v[j]*q[j] for j in range(3))
            val+=lam*(a*den-k)**2+(mu-2*S)*k*k
        worst=val if worst is None else max(worst,val)
    # -worst/(64 den^2 S) lower bounds 4d-B throughout this box.
    return -worst
def run(job):
    t0=time.perf_counter();mask=REPS[job];P=profile(mask)
    stack=[(tuple(i),2) for i in product(range(4),repeat=3)]
    leaves=[];pruned=[];unresolved=[];visited=0
    while stack:
        idx,dep=stack.pop();visited+=1;den=1<<dep
        if sum(idx)+3<=den//4 if dep>=2 else False:
            pruned.append([list(idx),dep,'rare']);continue
        if 3*sum(idx)>=4*den:
            pruned.append([list(idx),dep,'moderate']);continue
        bound=certificate(P,idx,dep)
        if bound>0:leaves.append([list(idx),dep,str(bound)]);continue
        if dep>=9:unresolved.append([list(idx),dep]);continue
        if time.perf_counter()-t0>50 or visited>=100000:
            unresolved.append([list(idx),dep]);unresolved += [[list(i),d] for i,d in stack];stack=[];break
        stack.extend((tuple(2*idx[j]+bits[j] for j in range(3)),dep+1) for bits in product((0,1),repeat=3))
    out={'job':job,'mask':mask,'status':'PASS' if not unresolved else 'UNRESOLVED','visited':visited,'leaves':leaves,'pruned':pruned,'unresolved':unresolved,'seconds':time.perf_counter()-t0,'log_arithmetic':'80-bit outward fixed point,24-term atanh,uniform proved tail','minimum_unscaled_numerator':str(min((int(x[2]) for x in leaves),default=0))}
    (ROOT/'out'/f'CONTINUUM_{job}.json').write_text(json.dumps(out,separators=(',',':'))+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('leaves','pruned','unresolved')}), 'counts',len(leaves),len(pruned),len(unresolved))
if __name__=='__main__':
    if sys.argv[1]=='classify':
        out={'representatives':REPS,'mapping':{str(m):canonical(m) for m in range(256)},'profiles':{str(m):profile(m) for m in REPS}}
        (ROOT/'out'/'CLASSIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(REPS)
    else:run(int(sys.argv[1]))
