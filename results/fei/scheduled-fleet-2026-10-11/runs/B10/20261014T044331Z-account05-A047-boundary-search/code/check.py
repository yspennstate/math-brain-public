from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,sys,importlib.util
R=Path(__file__).resolve().parents[1];ROOT=R.parents[1]
sp=importlib.util.spec_from_file_location('exact_logs',R/'code/exact_logs_base.py');E=importlib.util.module_from_spec(sp);sp.loader.exec_module(E)
@lru_cache(None)
def decomposition(n):
    from sympy import factorint
    d={int(p):int(k) for p,k in factorint(n).items()};prod=1
    for p,k in d.items():assert p>=2 and k>=1;prod*=p**k
    assert prod==n
    return d
E.factors=decomposition
add,mul,ent=E.add,E.mul,E.ent
start=time.perf_counter();checks=0;pilot='--pilot' in sys.argv
def ck(x):
    global checks
    assert x;checks+=1
    assert time.perf_counter()-start<(55 if pilot else 240)
def save(name,x):(R/'out'/name).write_text(json.dumps(x,indent=2),encoding='utf8')
def walsh(t):
    a=list(t);step=1
    while step<len(a):
        for lo in range(0,len(a),2*step):
            for j in range(lo,lo+step):u,v=a[j],a[j+step];a[j],a[j+step]=u+v,u-v
        step*=2
    return tuple(F(x*x,len(t)**2) for x in a)
def rm(x,i):return (x&((1<<i)-1))|((x>>(i+1))<<i)
def restrict(t,i,b):return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
def marginal(p,i):
    a=[F(0)]*(len(p)//2)
    for s,v in enumerate(p):a[rm(s,i)]+=v
    return tuple(a)
def kl(p,q):
    out=mul(ent(p),-1)
    for a,b in zip(p,q):
        if a:
            ck(b>0);out=add(out,mul(ent((b,)),a/b))
    return out
def query(t,i,tilt=None,alpha=None):
    P=walsh(t);kids=[restrict(t,i,b) for b in (0,1)];B=[walsh(k) for k in kids];pe=marginal(P,i)
    ck(all(pe[z]==(B[0][z]+B[1][z])/2 for z in range(len(pe))))
    inf=F(sum(a!=b for a,b in zip(*kids)),len(kids[0]))
    ck(sum(p for s,p in enumerate(P) if s>>i&1)==inf)
    if alpha is None:
        un=[v*(tilt if z.bit_count()%2 else 1) for z,v in enumerate(pe)];total=sum(un);qe=tuple(v/total for v in un)
    else:
        ck(0<pe[0]<1);qe=tuple(alpha if z==0 else (1-alpha)*p/(1-pe[0]) for z,p in enumerate(pe))
    Q=tuple(qe[rm(s,i)]*p/pe[rm(s,i)] if p else F(0) for s,p in enumerate(P));ck(sum(Q)==1)
    qj=[[F(0)]*len(pe) for _ in (0,1)]
    for z,p in enumerate(pe):
        if p:
            for b in (0,1):qj[b][z]=qe[z]*B[b][z]/(2*p)
    qb=[sum(v) for v in qj];ck(sum(qb)==1 and min(qb)>0)
    bayes=[tuple(v/w for v in a) for a,w in zip(qj,qb)]
    Eroot=kl(P,Q);Cerased=kl(pe,qe);O=kl((F(1,2),F(1,2)),qb);Cchild=mul(add(kl(B[0],bayes[0]),kl(B[1],bayes[1])),F(1,2))
    ck(Eroot==Cerased);ck(Cerased==add(O,Cchild))
    matches=all(p==q for a,b in zip(B,bayes) for p,q in zip(a,b))
    vertices=[z for z,p in enumerate(pe) if p];links={z:set() for z in vertices}
    for b in (0,1):
        support=[z for z in vertices if B[b][z]]
        for z in support:links[z].update(support)
    unseen=set(vertices);components=[]
    while unseen:
        todo=[next(iter(unseen))];comp=set()
        while todo:
            z=todo.pop()
            if z in comp:continue
            comp.add(z);todo.extend(links[z]-comp)
        unseen-=comp;components.append(comp)
    criterion=all(len({pe[z]/qe[z] for z in c})==1 for c in components)
    ck(matches==criterion);ck((not Cchild)==matches)
    full_constant=len({pe[z]/qe[z] for z in vertices})==1
    if full_constant:ck(matches)
    if len(components)==1:ck(matches==full_constant)
    # Actual physical terminal entropy/influence; ordinary telescope retained.
    Hleaf=mul(add(ent(B[0]),ent(B[1])),F(1,2));M=add(ent(P),mul(ent(pe),-1));J=add(ent(pe),mul(Hleaf,-1))
    ck(add(Hleaf,M,J)==ent(P))
    def influence(table):
        n=len(table).bit_length()-1
        return sum((F(sum(v!=table[x^(1<<j)] for x,v in enumerate(table)),len(table)) for j in range(n)),F(0))
    Iroot=influence(t);Ileaf=sum(map(influence,kids))/2;ck(Iroot==inf+Ileaf)
    return {'matches':matches,'components':len(components),'constant_likelihood':full_constant,'source_KL':Eroot,'outcome_KL':O,'child_conditional_KL':Cchild,'query_influence':str(inf),'terminal_entropy':Hleaf,'terminal_influence':str(Ileaf),'root_influence':str(Iroot)}
def enc(row):return {k:E.expr(v) if isinstance(v,dict) else v for k,v in row.items()}
def main():
    count=0;matches=0;weaker=0
    for n in range(1,3 if pilot else 4):
        for m in range(1<<(1<<n)):
            t=tuple(1-2*((m>>x)&1) for x in range(1<<n))
            for i in range(n):
                for tilt in (3,7):
                    row=query(t,i,tilt=tilt);count+=1;matches+=row['matches'];weaker+=row['matches'] and not row['constant_likelihood']
        save('PILOT.json' if pilot else 'CHECK.json',{'status':'CHECKPOINT','cases':count,'assertions':checks,'n':n})
    boundary=[]
    for r in ([2] if pilot else range(2,9)):
        h=tuple(1 if x==1 else (-1)**x.bit_count() for x in range(1<<r));mu=F(sum(h),len(h));ck(mu==F(1,1<<(r-1)));a=mu*mu
        t=tuple(1 if not x&1 else h[x>>1] for x in range(1<<(r+1)))
        for alpha in (F(1,4),1-a*a):
            row=query(t,0,alpha=alpha);count+=1
            beta=alpha*a/(1+a-alpha);formula=mul(kl((a,1-a),(beta,1-beta)),F(1,2));ck(formula==row['child_conditional_KL']);ck(not row['matches'] and row['components']==1)
            if alpha==1-a*a:
                ck(beta==1-a)
                # Equivalent elementary integer-log representation of (1-2a)/2 log((1-a)/a).
                ratio=(1-a)/a;logratio=mul(ent((F(1)/ratio,)),ratio)
                ck(row['child_conditional_KL']==mul(logratio,(1-2*a)/2))
            out={'r':r,'mu':str(mu),'a':str(a),'alpha':str(alpha),'beta':str(beta),**enc(row)};boundary.append(out);save('BOUNDARY.json',boundary)
    # Minimal balanced exception: constant/character children have disjoint supports.
    row=query((1,1,1,-1),0,alpha=F(1,4));ck(row['matches'] and not row['constant_likelihood'] and row['components']==2)
    save('BALANCED_EXCEPTION.json',enc(row))
    result={'status':'PASS','cases':count,'extra_minimal_exception':1,'assertions':checks,'matching_census':matches,'weaker_than_constant_census':weaker,'runtime_seconds':time.perf_counter()-start}
    save('PILOT.json' if pilot else 'CHECK.json',result);print(json.dumps(result))
if __name__=='__main__':main()
