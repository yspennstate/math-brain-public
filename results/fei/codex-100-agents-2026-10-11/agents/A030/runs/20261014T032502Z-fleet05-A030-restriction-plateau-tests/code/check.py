from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib,sys
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parents[1]/'runs/20261013T212321Z-fleet05-A030-restriction-plateau-tests/code/check.py'
ns={'__file__':str(OLD)}
exec(OLD.read_text(encoding='utf-8').split('for n in (1,2,3):')[0],ns)
expr,add,const,stats,child,reserve,positive=[ns[k] for k in ('expr','add','const','stats','child','reserve','positive')]
ZERO=(); START=time.perf_counter(); LIMIT=55 if '--pilot' in sys.argv else 595
checks=0;counts=dict(roots=0,control_faces=0,trees=0,interleaved_nodes=0)
def ck(ok):
    global checks
    checks+=1;assert ok,checks
    assert time.perf_counter()-START<LIMIT,'frozen runtime guard'
def phi(s):
    if not s:return ZERO
    d={}
    for p,e in ns['factors'](s.denominator).items():d[p]=s*e
    for p,e in ns['factors'](s.numerator).items():d[p]=d.get(p,F(0))-s*e
    return expr(d)
def mean(t):return F(sum(t),len(t))
def dim(t):return len(t).bit_length()-1
def mix(h,u,v):
    nh,nu=dim(h),dim(u)
    return tuple((u[(x>>nh)&(len(u)-1)] if h[x&(len(h)-1)]==1 else v[x>>(nh+nu)]) for x in range(len(h)*len(u)*len(v)))
def correction(b,m,n):
    q=(1+b)/2;p=1-q;a=(m+n)/2;c=(m-n)/2;delta=(1-m*n)/2;vu=1-m*m;vv=1-n*n
    return add((1,phi((a+c*b)**2)),(-delta,phi(b*b)),(1-b*b,phi(c*c)),(1,const((vu+vv)*(1-b*b)/2)),(vu,phi(q*q)),(vv,phi(p*p)),(-q,phi(m*m)),(-p,phi(n*n)))
@lru_cache(None)
def potential(h,u,v,Cd,Ch):
    b,m,n=mean(h),mean(u),mean(v);q=(1+b)/2;p=1-q;delta=(1-m*n)/2
    rh=reserve(h,tuple(range(dim(h))),Ch);ru=reserve(u,tuple(range(dim(u))),Cd);rv=reserve(v,tuple(range(dim(v))),Cd)
    rarity=add((1-m*m,phi(q)),(1-n*n,phi(p)))
    return add((q,ru),(p,rv),(1,rarity),(delta,rh)),add((delta,rh)),rarity
def tree(h,u,v,order,Cd,Ch):
    f=mix(h,u,v);R,owned,rarity=potential(h,u,v,Cd,Ch)
    if not order:ck(R==ZERO);ck(stats(f)[0]==ZERO);return ZERO
    label=order[0]; nh,nu=dim(h),dim(u)
    index={'h':0,'u':nh,'v':nh+nu}[label]
    kids=[];Rs=[];owns=[];banks=[];Hs=[]
    for sign in (0,1):
        parts=[h,u,v];j={'h':0,'u':1,'v':2}[label];parts[j]=child(parts[j],0,sign)
        hh,uu,vv=parts
        rr,oo,bb=potential(hh,uu,vv,Cd,Ch);Rs.append(rr);owns.append(oo);banks.append(bb)
        Hs.append(stats(mix(hh,uu,vv))[0]);kids.append(tree(hh,uu,vv,order[1:],Cd,Ch))
    H,di=stats(f);D=add((1,H),(-F(1,2),Hs[0]),(-F(1,2),Hs[1]));alpha=max(F(Cd)+F(11,2),F(Ch)+22)
    debt=add((1,D),(-1,const(alpha*di[index])),(-1,R),(F(1,2),Rs[0]),(F(1,2),Rs[1]))
    ck(positive(debt)==ZERO)
    if label!='h':ck(owned==add((F(1,2),owns[0]),(F(1,2),owns[1])))
    else:ck(positive(add((-1,rarity),(F(1,2),banks[0]),(F(1,2),banks[1])))==ZERO)
    Q=positive(add((1,D),(-1,const(alpha*di[index])),(F(1,2),kids[0]),(F(1,2),kids[1])))
    ck(positive(add((1,Q),(-1,R)))==ZERO)
    counts['interleaved_nodes']+=1
    return Q
cores=[(1,1,1,1),(-1,-1,-1,-1),(1,-1,1,-1),(-1,-1,-1,1),(1,-1,-1,1)]
pilot='--pilot' in sys.argv
for nh in (1,2):
    tables=range(1<<(1<<nh)) if not pilot else range(2)
    for mask in tables:
        h=tuple(-1 if mask>>x&1 else 1 for x in range(1<<nh))
        domain=cores if not pilot else [cores[2],cores[3]]
        for u in domain:
            for v in domain:
                f=mix(h,u,v);b,m,n=mean(h),mean(u),mean(v);q=(1+b)/2;delta=(1-m*n)/2
                H,di=stats(f);hh,dih=stats(h)
                B=correction(b,m,n)
                ck(H==add((delta,hh),(q,stats(u)[0]),(1-q,stats(v)[0]),(1,B)))
                ck(positive(add((1,B),(-1,const(22*delta*(1-abs(b))))))==ZERO)
                ck(positive(add((-1,B),(-1,const(22*delta*(1-abs(b))))))==ZERO)
                for i in range(nh):
                    hs=[child(h,i,s) for s in (0,1)]
                    DF=add((1,H),(-F(1,2),stats(mix(hs[0],u,v))[0]),(-F(1,2),stats(mix(hs[1],u,v))[0]))
                    DH=add((1,hh),(-F(1,2),stats(hs[0])[0]),(-F(1,2),stats(hs[1])[0]))
                    DB=add((1,B),(-F(1,2),correction(mean(hs[0]),m,n)),(-F(1,2),correction(mean(hs[1]),m,n)))
                    ck(DF==add((delta,DH),(1,DB)));ck(di[i]==delta*dih[i])
                    ck(positive(add((1,DB),(-1,const(22*di[i]))))==ZERO)
                    counts['control_faces']+=1
                for Cd,Ch in ((0,0),(4,1)):
                    R=potential(h,u,v,Cd,Ch)[0]
                    inherited=add((q,reserve(u,(0,1),Cd)),(1-q,reserve(v,(0,1),Cd)),(delta,reserve(h,tuple(range(nh)),Ch)))
                    ck(positive(add((1,R),(-1,inherited),(-1,const(2*sum(di[:nh])))))==ZERO)
                    orders=[('h',)*nh+('u','u','v','v'),('u','h','v')+('h',)*(nh-1)+('u','v')]
                    for order in orders:tree(h,u,v,order,Cd,Ch);counts['trees']+=1
                counts['roots']+=1
        stats.cache_clear();reserve.cache_clear();potential.cache_clear()
result=dict(status='PASS',pilot=pilot,helper_version='A030-nonpoint-two-core-v1',checks=checks,counts=counts,certified_nonzero_signs=ns['signs'],exact_zero_signs=ns['zeros'],elapsed_seconds=time.perf_counter()-START,memory_estimate_mb=240,arithmetic='integer Walsh; Fraction prime-log expressions; rational atanh intervals',code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),helper_sha256=hashlib.sha256(OLD.read_bytes()).hexdigest())
(ROOT/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
