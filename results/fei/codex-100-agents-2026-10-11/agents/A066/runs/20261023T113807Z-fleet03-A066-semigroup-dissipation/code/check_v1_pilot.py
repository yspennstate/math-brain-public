from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from math import lcm
import sys,time,json
run=Path(__file__).resolve().parents[1];mode=sys.argv[1];start=time.perf_counter();checks=0
def ck(v):
    global checks
    checks+=1;assert v
    assert time.perf_counter()-start<55,'FROZEN_RUNTIME'
def E(*xs):
    a={}
    for x in xs:
        for b,c in x.items():a[b]=a.get(b,Q(0))+c
    return {b:c for b,c in a.items() if c and b!=1}
def M(x,c):return E({b:a*c for b,a in x.items()})
def B(c):return E({Q(2):Q(c)})
def CE(p,q):
    a={}
    for x,y in zip(p,q):
        if x:
            assert y>0;a[y]=a.get(y,Q(0))-x
    return E(a)
@lru_cache(None)
def power(t):
    den=lcm(*(c.denominator for b,c in t)) if t else 1
    p=Q(1)
    for b,c in t:p*=b**int(c*den)
    return p,den
def sign(x):
    p,_=power(tuple(sorted(x.items())));return (p>1)-(p<1)
def eq(x,y):return sign(E(x,M(y,-1)))==0
def show(x):
    p,d=power(tuple(sorted(x.items())))
    return {'terms':{str(b):str(c) for b,c in x.items()},'power_ratio':str(p),'power_denominator':d,'sign':(p>1)-(p<1)}
@lru_cache(None)
def walsh(v):
    a=list(v);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):x,y=a[k],a[k+h];a[k]=x+y;a[k+h]=x-y
        h*=2
    return tuple(Q(x,len(v)) for x in a)
def spectrum(v):return tuple(x*x for x in walsh(v))
def edge(v,i):return Q(sum(x!=v[k^(1<<i)] for k,x in enumerate(v)),len(v))
def child(v,i,s):return tuple(x for k,x in enumerate(v) if (k>>i)&1==s)
def erase(p,i):
    out=[]
    for k in range(len(p)//2):
        ix=(k&((1<<i)-1))+((k>>i)<<(i+1));out.append(p[ix]+p[ix+(1<<i)])
    return tuple(out)
def A(j):return (2 if j&1 else 0)^(4 if j&2 else 0)^(7 if j&4 else 0)
maj=tuple(1 if y.bit_count()<=1 else -1 for y in range(8));pm=spectrum(maj)
ck(tuple(i for i,p in enumerate(pm) if p)==(1,2,4,7));ck(all(pm[i]==Q(1,4) for i in [1,2,4,7]))
ck(sum(edge(maj,i) for i in range(3))==Q(3,2));ck(len({A(j) for j in range(8)})==8)
ck([A(j) for j in [1,2,4,7]]==[2,4,7,1])
for j in range(8):ck(A(A(A(A(j))))==j);ck(pm[A(j)]==pm[j])
rows=[];cores=cases=supplied=rejected=0
for d in range(2 if mode=='pilot' else 4):
    N=1<<d
    for mask in range(1<<N):
        cores+=1;g=tuple(1 if mask>>z&1 else -1 for z in range(N));pg=spectrum(g);Ig=sum(edge(g,i) for i in range(d))
        root=tuple((1-2*t)*(1-2*x)*maj[y]*g[z] for z in range(N) for y in range(8) for x in range(2) for t in range(2))
        p=spectrum(root);ft=[child(root,0,s) for s in [0,1]];pft=[spectrum(v) for v in ft]
        leaves=[child(v,0,s) for v in ft for s in [0,1]];pl=[spectrum(v) for v in leaves]
        ck(all(pp==pl[0] for pp in pl));ck(pft[0]==pft[1]);ck(pft[0]==erase(p,0));ck(pl[0]==erase(pft[0],0))
        ck(edge(root,0)==1);ck(all(edge(v,0)==1 for v in ft))
        ck(sum(edge(root,i) for i in range(d+5))==Ig+Q(7,2))
        ck(sum(edge(leaves[0],i) for i in range(d+3))==Ig+Q(3,2))
        ck(p[0]==pft[0][0]==pl[0][0]==0)
        for v in [root]+ft:
            a=walsh(v);ck(a[1]==0);ck(all(a[k]*a[k+1]==0 for k in range(0,len(a),2)))
        # Complete actual spectrum and physical orbit invariance, arbitrary core.
        for z in range(N):
            for j in range(8):
                ck(pl[0][j+8*z]==pm[j]*pg[z]);ck(pl[0][j+8*z]==pl[0][A(j)+8*z])
        for ref in ['actual','half_uniform']:
            qg=pg if ref=='actual' else tuple((x+Q(1,N))/2 for x in pg)
            cg=CE(pg,qg)
            for K in ([4] if mode=='pilot' else [4,5,8,16]):
                cases+=1;Bh=E(B(K*Ig),M(cg,-1))
                if sign(Bh)<0:rejected+=1;continue
                supplied+=1;eps=Q(1,1<<(3*K));qm=tuple(1-3*eps if j==1 else eps if pm[j] else Q(0) for j in range(8))
                ck(sum(qm)==1);c=CE(pm,qm);ck(eq(c,E(B(Q(9*K,4)),{1-3*eps:-Q(1,4)})))
                ck(sign(E(c,B(-Q(9*K,4))))>0);ck(sign(E(B(Q(9*K+1,4)),M(c,-1)))>0)
                qroot=[Q(0)]*(32*N)
                for z in range(N):
                    for j in range(8):qroot[3+4*j+32*z]=qm[j]*qg[z]
                qroot=tuple(qroot);qt=erase(qroot,0);qr=erase(qt,0)
                ck(sum(qroot)==sum(qt)==sum(qr)==1)
                for pp in [p]:ck(all(not x or y>0 for x,y in zip(pp,qroot)))
                parentCE=CE(p,qroot);ck(eq(parentCE,E(c,cg)))
                ck(eq(CE(pft[0],qt),parentCE));ck(eq(CE(pl[0],qr),parentCE))
                # FOUR source copies under the actual invariant physical orbit.
                mix=[Q(0)]*(8*N)
                for z in range(N):
                    for j in range(8):
                        jj=j
                        for u in range(4):mix[A(jj)+8*z]+=qr[j+8*z]/4;jj=A(jj)
                mix=tuple(mix);ck(sum(mix)==1)
                for z in range(N):
                    for j in range(8):ck(mix[j+8*z]==pm[j]*qg[z])
                after=CE(pl[0],mix);ck(eq(after,E(B(2),cg)));ck(sign(E(parentCE,M(after,-1),B(-7)))>0 if K==4 else sign(E(parentCE,M(after,-1)))>0)
                tau=E(Bh,B(Q(1,4)));ck(sign(tau)>0)
                quota=K*(Ig+Q(7,2))
                # Prefix t queried once on every path; keep BOTH x-query children.
                old=E(B(quota-K),M(parentCE,-1),M(tau,-1));ck(eq(old,E(B(Q(5*K,2)-Q(1,4)),M(c,-1))));ck(sign(old)>0)
                raw=E(B(quota-2*K),M(parentCE,-1),M(tau,-1));ck(sign(raw)<0)
                final=E(B(quota-2*K),M(after,-1),M(tau,-1));ck(eq(final,B(Q(3*K,2)-Q(9,4))));ck(sign(final)>0)
                bill=E(B(K),after,M(parentCE,-1));ck(sign(E(B(2-Q(5*K,4)),M(bill,-1)))>0)
                # Exact same-owner conservation, no renewed child quota.
                ck(eq(E(old,M(bill,-1)),final))
                if d==0 and mask==0 and ref=='actual':rows.append({'K':K,'old_bank_after_prefix':show(old),'raw_bank_after_next_query':show(raw),'final_bank_same_original_owner':show(final),'conversion_refund':show(E(parentCE,M(after,-1))),'old_debit':show(tau)})
out={'status':'PASS','mode':mode,'cores':cores,'source_rate_cases':cases,'supplied_cases':supplied,'supplier_rejected':rejected,'exact_assertions':checks,'seconds':time.perf_counter()-start,'max_physical_dimension':6 if mode=='pilot' else 8,'rows':rows,'scope':'All admitted supplied-core cases: genuine paid prefix, mandatory next nonempty repair, actual C4 orbit refund, SAME original source/old debit/both complete terminals. No arbitrary core supplier asserted.'}
(run/'out'/('CHECK_'+mode.upper()+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
