"""Exact three-label full-profile Markov reference test; actual Boolean selector."""
from pathlib import Path
from fractions import Fraction as F
import json,time
import base as m
e=m.e;R=Path(__file__).resolve().parents[1];START=time.monotonic();nodes=leaves=positive=0

def state(L,gs,rs):
    global positive
    M=len(L);N=len(gs[0]);pi=tuple(F(L.count(j),M) for j in range(len(gs)))
    f=tuple(gs[label][x] for x in range(N) for label in L);pf=m.spectrum(f)
    ps=[m.spectrum(g) for g in gs];Q=[];W=e.add(*(e.scale(m.kl(p,r),weight) for p,r,weight in zip(ps,rs,pi)))
    residual={};C={};Ddata={};rows=[]
    for t in range(N):
        q=sum(pi[j]*ps[j][t] for j in range(len(gs)));r=sum(pi[j]*rs[j][t] for j in range(len(gs)))
        actual=pf[t*M:(t+1)*M];m.ck(sum(actual)==q)
        if not q:Q.extend((r,)+(F(0),)*(M-1));continue
        alpha=tuple(pi[j]*ps[j][t]/q for j in range(len(gs)));rho=tuple(pi[j]*rs[j][t]/r for j in range(len(gs)))
        k=tuple(x/q for x in actual)
        # Quantile interval intersections construct a rational coupling h(label,U).
        abounds=[F(0)];kbounds=[F(0)]
        for x in alpha:abounds.append(abounds[-1]+x)
        for x in k:kbounds.append(kbounds[-1]+x)
        K=[]
        for j,x in enumerate(alpha):
            row=tuple(max(F(0),min(abounds[j+1],kbounds[u+1])-max(abounds[j],kbounds[u]))/x for u in range(M)) if x else k
            m.ck(sum(row)==1 and min(row)>=0);K.append(row)
        ell=tuple(sum(rho[j]*K[j][u] for j in range(len(gs))) for u in range(M))
        m.ck(sum(ell)==1)
        for u in range(M):m.ck(sum(alpha[j]*K[j][u] for j in range(len(gs)))==k[u])
        d=m.kl(k,ell);post={}
        for u,ku in enumerate(k):
            if ku:
                true=tuple(alpha[j]*K[j][u]/ku for j in range(len(gs)))
                ref=tuple(rho[j]*K[j][u]/ell[u] for j in range(len(gs)))
                post=e.add(post,e.scale(m.kl(true,ref),ku))
        m.eq(m.kl(alpha,rho),e.add(d,post));m.nn(d);m.nn(post)
        C=e.add(C,e.scale(d,q));residual=e.add(residual,e.scale(post,q));Q.extend(r*x for x in ell)
        if e.enclosure(d)[0]>0:positive+=1
        rows.append(dict(t=t,k=[str(x) for x in k],ell=[str(x) for x in ell]))
    Q=tuple(Q);D=m.kl(pf,Q);m.eq(e.add(D,residual),W)
    return dict(W=W,S=residual,D=D,H=e.entropy(pf),Q=Q,f=f,pi=pi,C=C,rows=rows)

def walk(L,gs,rs,labels,order):
    global nodes,leaves
    nodes+=1;s=state(L,gs,rs)
    if not order:
        leaves+=1;return dict(sig={},A={},Sleaf=s['S'],path={},ce=e.add(s['H'],s['D']))
    label=order[0];i=labels.index(label);nc=len(L).bit_length()-1
    inh,Ef,Of,rho=m.physical(s['f'],s['Q'],i)
    if i<nc:
        children=[(m.restrict(L,i,b),gs,rs) for b in (0,1)];expected={}
    else:
        j=i-nc;trans=[m.physical(g,r,j) for g,r in zip(gs,rs)]
        children=[(L,tuple(m.restrict(g,j,b) for g in gs),tuple(x[0][b] for x in trans)) for b in (0,1)]
        expected=e.add(*(e.scale(e.add(x[1],x[2]),w) for x,w in zip(trans,s['pi'])))
    kids=[state(*args) for args in children];A=e.add(s['W'],m.neg(m.avg(*(z['W'] for z in kids))))
    m.eq(A,expected);m.nn(A)
    sigma=e.add(m.avg(*(z['D'] for z in kids)),m.neg(s['D']))
    raw=e.add(m.avg(*(z['D'] for z in kids)),m.neg(m.avg(*(m.kl(m.spectrum(m.restrict(s['f'],i,b)),inh[b]) for b in (0,1)))))
    m.eq(raw,e.add(sigma,Ef,Of));m.eq(sigma,e.add(s['S'],m.neg(m.avg(*(z['S'] for z in kids))),m.neg(A)))
    rest=labels[:i]+labels[i+1:];rr=[walk(*args,rest,order[1:]) for args in children]
    out={k:m.avg(*(z[k] for z in rr)) for k in rr[0]};out['sig']=e.add(sigma,out['sig']);out['A']=e.add(A,out['A'])
    out['path']=e.add(s['H'],m.neg(m.avg(*(z['H'] for z in kids))),out['path'])
    m.eq(e.add(out['sig'],out['A'],out['Sleaf']),s['S']);m.eq(e.add(out['path'],out['ce'],out['A'],out['Sleaf']),e.add(s['H'],s['W']))
    return out

L=(0,1,2,0);gs=((1,-1,1,-1),(1,1,-1,-1),(-1,1,1,1));rs=((F(1,4),)*4,)*3
ans=walk(L,gs,rs,('C0','C1','D0','D1'),('D0','C0','D1','C1'))
assert nodes==31 and leaves==16 and positive>0
out=dict(status='PASS',nodes=nodes,leaves=leaves,positive_full_profile_row_visits=positive,assertions=m.checks,seconds=time.monotonic()-START,ledger={k:m.encoded(z) for k,z in ans.items()})
(R/'out/finite_label.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='');print(json.dumps({k:v for k,v in out.items() if k!='ledger'}))
