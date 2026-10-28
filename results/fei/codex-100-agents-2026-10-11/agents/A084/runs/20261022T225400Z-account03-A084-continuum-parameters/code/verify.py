"""Independent exact occupied-mask reconstruction and heterogeneous-query audit."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, time, sys, hashlib
from arithmetic import Q,log2,plus,scale,constant
ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
    global checks
    assert x
    checks+=1
def save(name,x):
    (ROOT/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def add(*ps):
    d={}
    for p in ps:
        for k,v in p.items():d[k]=d.get(k,F(0))+v
    return {k:v for k,v in d.items() if v}
def times(p,r):return {k:v*r for k,v in p.items() if v*r}
def ent(ps):return add(*[{p:-p} for p in ps if p and p!=1])
def ev(p):
    out=(0,0)
    for k,v in p.items():
        a=(Q,Q) if k is None else log2(k)
        out=plus(out,scale(a,v) if v>=0 else tuple(-x for x in scale(a,-v)[::-1]))
    return out
def pack(p):return {'CONST' if k is None else str(k):str(v) for k,v in p.items()}
def show(iv):return [float(F(x,Q)) for x in iv]
def table(kind):
    h=tuple(-1 if x in {0,1,2,4,8,16,32,6,17,40} else 1 for x in range(64))
    return h if kind=='h' else tuple(-h[x^1] for x in range(64))
@lru_cache(None)
def walsh(t):
    N=len(t);a=list(t);step=1
    while step<N:
        for j in range(0,N,step*2):
            for k in range(j,j+step):a[k],a[k+step]=a[k]+a[k+step],a[k]-a[k+step]
        step*=2
    direct=[sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(t)) for s in range(N)]
    ck(a==direct);ck(sum(z*z for z in a)==N*sum(z*z for z in t))
    return tuple(F(z,N) for z in a)
@lru_cache(None)
def core(t):
    ck(all(z in [-1,1] for z in t))
    N=len(t);n=(N-1).bit_length();w=walsh(t);ds=[]
    for i in range(n):
        di=F(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N)
        ck(di==sum(w[s]**2 for s in range(N) if s>>i&1));ds.append(di)
    return dict(mu=sum(t,F(0))/N,H=ent([z*z for z in w]),I=sum(ds),ds=ds)
def child(t,i,b):
    return tuple(t[x] for x in range(len(t)) if x>>i&1==b)
def prod(xs):
    z=F(1)
    for x in xs:z*=x
    return z
@lru_cache(None)
def outer(kind,mus):
    h=table(kind);w=walsh(h);v=[1-x*x for x in mus];P=[]
    for T in range(64):
        a=sum(w[U]*prod(mus[j] for j in range(6) if (U^T)>>j&1) for U in range(64) if U&T==T)
        P.append(a*a*prod(v[j] for j in range(6) if T>>j&1))
    ck(sum(P)==1 and all(x>=0 for x in P))
    qs=[]
    for j in range(6):
        q=sum(prod((1-mus[k])/2 if x>>k&1 else (1+mus[k])/2 for k in range(6) if k!=j) for x in range(64) if not(x>>j&1) and h[x]!=h[x|1<<j])
        ck(sum(P[x] for x in range(64) if x>>j&1)==v[j]*q);qs.append(q)
    C=add(ent(P),*[times(ent([z,1-z]),-q) for z,q in zip(v,qs)])
    direct_mean=sum(F(h[x])*prod((1-mus[j])/2 if x>>j&1 else (1+mus[j])/2 for j in range(6)) for x in range(64))
    ck(P[0]==direct_mean**2)
    return dict(P=P,q=qs,C=C)
def full(kind,ts):
    cs=[core(t) for t in ts];op=outer(kind,tuple(c['mu'] for c in cs))
    H=add(op['C'],*[times(c['H'],q) for c,q in zip(cs,op['q'])]);I=sum(c['I']*q for c,q in zip(cs,op['q']))
    return dict(ts=ts,cs=cs,op=op,H=H,I=I,S=add({None:4*I},times(H,-1)))
def split(kind,p,j,i):
    ps=[]
    for b in (0,1):
        ts=list(p['ts']);ts[j]=child(ts[j],i,b);ps.append(full(kind,tuple(ts)))
    d=p['op']['q'][j]*p['cs'][j]['ds'][i]
    ck(p['I']-sum(z['I'] for z in ps)/2==d)
    for k in range(6):ck(p['op']['q'][k]==sum(z['op']['q'][k] for z in ps)/2)
    dh=add(p['H'],*[times(z['H'],F(-1,2)) for z in ps])
    dc=add(p['op']['C'],*[times(z['op']['C'],F(-1,2)) for z in ps])
    dcore=add(p['cs'][j]['H'],*[times(z['cs'][j]['H'],F(-1,2)) for z in ps])
    ck(dh==add(times(dcore,p['op']['q'][j]),dc))
    e=add(dh,{None:-4*d})
    ck(add(*[times(z['S'],F(1,2)) for z in ps])==add(p['S'],e))
    return ps,d,dc,e
def witness():
    rows=[];exceptions=[]
    for kind in ['h','J']:
        h=table(kind)
        for k in range(6):
            for j in range(6):
                if j==k:continue
                ws=[x for x in range(64) if not(x>>k&1) and not(x>>j&1) and h[x]!=h[x|1<<j]]
                r=min((x.bit_count() for x in ws),default=None)
                if r is None:
                    ck((kind,k,j)==('J',0,4))
                    ws1=[x for x in range(64) if x>>k&1 and not(x>>j&1) and h[x]!=h[x|1<<j]]
                    ck(min(x.bit_count()-1 for x in ws1)==1)
                    exceptions.append(dict(kind=kind,previous=k,target=j,positive_section_independent=True,negative_section_min_weight=1,witnesses=ws1))
                else:
                    ck(r==(1 if kind=='h' or j==0 else 2 if j==4 else 0))
                rows.append(dict(gate=kind,previous=k,target=j,min_weight=r,witnesses=ws))
    ck(len(rows)==60 and len(exceptions)==1)
    save('WITNESSES.json',rows);save('FAILED_UNIFORM_POSITIVE_WITNESS.json',exceptions)
    # Exact endpoint inequalities which prove the real-parameter envelopes.
    p=F(1,16)
    ck((1-2*p)*(1-p)**4>F(2,3))
    ck((1-2*p)*(1-p)**3>F(2,3))
    ck((1-2*p)*(1-p)**2>F(3,4))
    ck((1-p)**4>F(3,4))
    ck((1-p)**3>F(3,4))
    ck(2*p*(4+F(19,4))==F(35,32)<F(5,4))
    return rows
def main():
    start=time.perf_counter();witness();pilot='--pilot' in sys.argv
    G=tuple(-1 if x in {0,1,2} else 1 for x in range(64));rows=[]
    choices=[(kind,k,b,j) for kind in ['h','J'] for k in range(6) for b in (0,1) for j in range(6)]
    if pilot:choices=choices[:4]
    for kind,k,b,j in choices:
        root=full(kind,(G,)*6);parents,_,_,_=split(kind,root,k,2);p=parents[b]
        i=0 if j==k else 2
        cs,d,dc,e=split(kind,p,j,i)
        B=(F(5,4) if kind=='h' else F(3,4) if j in [1,2,3,5] else F(7,4) if j==0 else F(11,4)) if j==k else (F(3,4) if kind=='h' or j==0 else F(35,32) if (k,j)==(0,4) else F(5,4) if j==4 else F(1,8))
        margin=add({None:B*d},times(dc,-1));mi=ev(margin)
        if d:ck(mi[0]>0)
        else:ck(not dc and all(z['H']==p['H'] for z in cs))
        # Full inherited core term remains, and q for every other core averages.
        rows.append(dict(gate=kind,previous_block=k,previous_answer=b,target_block=j,current_coordinate=i,physical_influence=str(d),bound=str(B),delta_C=ev(dc),margin=mi,query_excess=ev(e),full_child_slack=[ev(z['S']) for z in cs],parent_H=ev(p['H']),full_child_H=[ev(z['H']) for z in cs],delta_C_profile=pack(dc)))
        save('PILOT_CASES.json' if pilot else 'PHYSICAL_CASES.json',rows)
        ck(time.perf_counter()-start<55)
    # Exact saturated-source reconstruction uses the actual A072 000 prefix.
    p=full('J',(G,)*6)
    for original,bit in [(2,0),(0,0),(3,0)]:
        labels=[x for x in range(6) if x not in ([2] if original==0 else [2,0] if original==3 else [])]
        cs,_,_,_=split('J',p,0,labels.index(original));p=cs[bit]
    pS=ev(p['S']);ck(pS[0]>0)
    cs,d,dc,e=split('J',p,1,0)
    ck(add(p['S'],e)==add(*[times(c['S'],F(1,2)) for c in cs]))
    ck(all(ev(c['S'])[0]>0 for c in cs))
    audit=dict(parent_slack=pS,child_slacks=[ev(c['S']) for c in cs],query_excess=ev(e),exact_mean_child_slack_profile=pack(add(p['S'],e)),scope='One original saturated A072 parent; exact accounting reconstruction only, not all60 optimizer acceptance')
    save('SATURATION_RECONSTRUCTION.json',audit)
    result=dict(version='A084-heterogeneous-second-query-v1',physical_queries=len(rows),exact_assertions=checks,core_tables=core.cache_info().currsize,outer_profiles=outer.cache_info().currsize,scale_bits=192,ln_terms=80,runtime_seconds=time.perf_counter()-start,full_fei='OPEN',rung='analytic continuum proof with finite exact checks; independent review pending')
    save('PILOT.json' if pilot else 'VALIDATION.json',result);print(json.dumps(result))
if __name__=='__main__':main()
