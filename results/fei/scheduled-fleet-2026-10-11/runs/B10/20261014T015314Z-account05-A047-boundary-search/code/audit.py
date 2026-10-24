from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
import importlib.util,json,time,sys
R=Path(__file__).resolve().parents[1]
OLD=R/'code/exact_logs_base.py'
sp=importlib.util.spec_from_file_location('exact_logs',OLD); E=importlib.util.module_from_spec(sp);sp.loader.exec_module(E)
@lru_cache(None)
def exact_factors(n):
    from sympy import factorint
    d={int(p):int(k) for p,k in factorint(n).items()}
    product=1
    for p,k in d.items():
        # Equality of integer-log coefficient vectors is sufficient regardless
        # of primality. Only the exact integer product identity is needed.
        assert p>=2 and k>=1
        product*=p**k
    assert product==n
    return d
E.factors=exact_factors
ent,add,mul,hb=E.ent,E.add,E.mul,E.hb
start=time.perf_counter(); checks=0; pilot='--pilot' in sys.argv
def ck(x):
    global checks
    assert x;checks+=1
    assert time.perf_counter()-start<(55 if pilot else 300)
def save(name,obj): (R/'out'/name).write_text(json.dumps(obj,indent=2),encoding='utf8')
@lru_cache(None)
def weights(ps):
    return tuple(__import__('functools').reduce(lambda a,ip:a*(ip[1] if x>>ip[0]&1 else 1-ip[1]),enumerate(ps),F(1)) for x in range(1<<len(ps)))
@lru_cache(None)
def st(t,ps):
    n=len(ps);ws=weights(ps); masses=[]
    # Direct centered moments; independent of A050's transform and our old fast transform.
    for s in range(1<<n):
        z=F(0);norm=F(1)
        for i,p in enumerate(ps):
            if s>>i&1:norm*=p*(1-p)
        for x,(w,v) in enumerate(zip(ws,t)):
            term=w*v
            for i,p in enumerate(ps):
                if s>>i&1:term*=((x>>i)&1)-p
            z+=term
        masses.append(z*z/norm)
    ds=[]
    for i,p in enumerate(ps):
        ds.append(sum((w for x,w in enumerate(ws) if t[x]!=t[x^(1<<i)]),F(0)))
        ck(sum(v for s,v in enumerate(masses) if s>>i&1)==4*p*(1-p)*ds[-1])
    ck(sum(masses)==1)
    neg=sum((w for w,v in zip(ws,t) if v<0),F(0))
    return tuple(masses),tuple(ds),neg
def restrict(t,i,b):
    return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
def project(s,ids): return sum(((s>>i)&1)<<j for j,i in enumerate(ids))
def ambient(s,ids): return sum(((s>>j)&1)<<i for j,i in enumerate(ids))
def tree(t,ps,policy):
    n=len(ps); P,ds,neg=st(t,ps); A=set(range(min(3,n))) if policy=='controllers' else set(range(n))
    a=[sum(v for s,v in enumerate(P) if s>>i&1) if i in A else F(0) for i in range(n)]
    deletion=[F(0)]*n; Rphys=F(0);leafphys=F(0);leaffourier={};leafout={};J={};M={};dbar={};joint=[]
    def visit(t,ps,ids,law,path):
        nonlocal Rphys,leafphys,leaffourier,leafout,J,M,dbar
        spec,inf,np=st(t,ps);w=sum(law.values());ck(w>0)
        pm=defaultdict(F)
        for s,v in law.items():pm[project(s,ids)]+=v
        ck(all(pm[k]==w*v for k,v in enumerate(spec)))
        active=[j for j,i in enumerate(ids) if inf[j] and i in A]
        stop=not active or (policy=='prefix' and len(path)==1) or (policy=='adaptive' and len(path)>=2)
        if stop:
            for s,v in law.items():joint.append((s,path,s&~sum(1<<i for i,b in path),v))
            leafphys+=w*sum(inf);leaffourier=add(leaffourier,mul(ent(spec),w));leafout=add(leafout,mul(hb(np),w))
            return
        i=active[-1] if policy=='adaptive' and path and path[0][1] else active[0]
        g=ids[i];p=ps[i];newids=ids[:i]+ids[i+1:];newps=ps[:i]+ps[i+1:]
        kids=[restrict(t,i,b) for b in (0,1)];K=[st(k,newps)[0] for k in kids];q=[(1-p)*u+p*v for u,v in zip(*K)]
        J=add(J,mul(add(ent(q),mul(ent(K[0]),-(1-p)),mul(ent(K[1]),-p)),w))
        localM=add(ent(spec),mul(ent(q),-1));M=add(M,mul(localM,w))
        localJ=add(ent(q),mul(ent(K[0]),-(1-p)),mul(ent(K[1]),-p))
        dbar=add(dbar,mul(add(mul(hb(p),F(1,2)),localM,mul(localJ,-1)),w))
        Rphys+=w*inf[i];deletion[g]+=w*4*p*(1-p)*inf[i]
        for b,prob in ((0,1-p),(1,p)):
            child={}
            for s,v in law.items():
                u=project(s,newids);ck(q[u]>0);c=v*prob*K[b][u]/q[u]
                if c:child[s]=c
            ck(sum(child.values())==w*prob)
            visit(kids[b],newps,newids,child,path+((g,b),))
    visit(t,ps,tuple(range(n)),{s:v for s,v in enumerate(P) if v},())
    S=defaultdict(F);W=defaultdict(F);Pi=defaultdict(F);SW=defaultdict(F);SP=defaultdict(F);WP=defaultdict(F)
    terminal=[F(0)]*n
    for s,p,w,v in joint:
        S[s]+=v;W[w]+=v;Pi[p]+=v;SW[s,w]+=v;SP[s,p]+=v;WP[w,p]+=v
        ck(w&s==w)
        for i in range(n):
            if w>>i&1:terminal[i]+=v
    ck(tuple(S.get(s,F(0)) for s in range(1<<n))==P)
    ck(sum(ds)==Rphys+leafphys)
    ck(all(a[i]==deletion[i]+terminal[i] for i in A))
    e=add(ent(SW.values()),mul(ent(P),-1))
    HP=ent(Pi.values());j=add(ent(P),HP,mul(ent(SP.values()),-1));jw=add(ent(W.values()),HP,mul(ent(WP.values()),-1))
    ck(j==J);ck(add(leaffourier,M,J)==ent(P))
    ck(add(ent(W.values()),mul(leaffourier,-1))==jw)
    bank=add(ent(WP.values()),mul(ent(W.values()),-1))
    ck(add(leaffourier,mul(M,2),mul(bank,F(1,2)),mul(jw,F(1,2)),mul(dbar,-1))==ent(P))
    # Exact coordinate deletion code and conditional KL, reconstructed row by row.
    theta=[deletion[i]/a[i] if a[i] else F(0) for i in range(n)]
    cap={}
    for ai,th in zip(a,theta):cap=add(cap,mul(hb(th),ai))
    kl={};normchecks=0
    for s,sv in S.items():
        labels=[i for i in A if s>>i&1];rho={}
        for mask in range(1<<len(labels)):
            d=sum(1<<i for j,i in enumerate(labels) if mask>>j&1);v=F(1)
            for i in labels:v*=theta[i] if d>>i&1 else 1-theta[i]
            rho[d]=v
        ck(sum(rho.values())==1);normchecks+=1
        dist={s^w:v/sv for (ss,w),v in SW.items() if ss==s}
        cross={}
        for d,pd in dist.items():
            ck(rho[d]>0)
            # -pd log rho[d], using entropy contribution divided by rho[d].
            for i in labels:
                v=theta[i] if d>>i&1 else 1-theta[i]
                cross=add(cross,mul(ent((v,)),pd/v))
        kl=add(kl,mul(add(cross,mul(ent(dist.values()),-1)),sv))
    ck(add(e,kl)==cap)
    at=sum(a);rt=sum(deletion);aggregate=mul(hb(rt/at),at) if at else {}
    ck(rt<=Rphys)
    # No floating sign decisions: exact identities plus universal KL nonnegativity proof.
    if not rt or rt==at:ck(not e)
    if all(p==F(1,2) for p in ps):ck(rt==Rphys)
    return {'injection':e,'capacity':cap,'aggregate_capacity':aggregate,'R_physical':str(Rphys),'R_spectral':str(rt),'a_spectral':str(at),'terminal_fourier_entropy':leaffourier,'KL':kl,'coordinate_a':list(map(str,a)),'coordinate_R':list(map(str,deletion))}
def serialize(row): return {k:E.expr(v) if isinstance(v,dict) else v for k,v in row.items()}
def main():
    laws=[(F(1,2),)*3,(F(1,8),)*3,(F(1,8),F(1,4),F(3,8)),(F(3,4),F(7,8),F(1,2))];count=0;zero=0
    for n in range(3 if pilot else 4):
        for ps in laws:
            for m in range(1<<(1<<n)):
                t=tuple(1-2*((m>>x)&1) for x in range(1<<n))
                for policy in ('complete','prefix','adaptive','controllers'):
                    row=tree(t,ps[:n],policy);count+=1;zero+=not row['injection']
        save('PILOT.json' if pilot else 'CHECK.json',{'cases':count,'assertions':checks,'last_n':n,'status':'CHECKPOINT'})
    shared=0
    if not pilot:
        for ps in [(F(1,2),)*5,(F(1,8),F(3,4),F(7,8),F(1,4),F(3,8))]:
            for g in range(16):
                for h in range(16):
                    t=tuple((1-2*((g>>(x>>3))&1)) if (x&3)==3 else ((1-2*((h>>(x>>3))&1)) if (x&5)==5 else 1) for x in range(32))
                    for policy in ('controllers','adaptive'):
                        row=tree(t,ps,policy);count+=1;shared+=1
                        if policy=='controllers':ck(not row['injection'])
            save('SHARED_PROGRESS.json',{'cases':shared,'assertions':checks})
    witnesses=[]
    for ps in [(F(1,2),)*3,(F(1,8),F(1,4),F(3,8)),(F(1,256),F(1,65536),F(3,4))]:
        t=tuple((-1)**x.bit_count() for x in range(8));row=tree(t,ps,'adaptive');count+=1
        b=[4*p*(1-p) for p in ps]
        exact=mul(hb(ps[0]),b[1]+b[2]-b[1]*b[2]);cap=mul(hb(ps[0]),b[1]+b[2])
        ck(row['injection']==exact);ck(row['capacity']==cap);ck(row['KL']==mul(hb(ps[0]),b[1]*b[2]))
        witnesses.append({'biases':list(map(str,ps)),**serialize(row)})
    save('PARITY_BOUNDARY.json',witnesses)
    result={'status':'PASS','cases':count,'shared_cases':shared,'assertions':checks,'zero_injection_census':zero,'runtime_seconds':time.perf_counter()-start}
    save('PILOT.json' if pilot else 'CHECK.json',result);print(json.dumps(result))
if __name__=='__main__':main()
