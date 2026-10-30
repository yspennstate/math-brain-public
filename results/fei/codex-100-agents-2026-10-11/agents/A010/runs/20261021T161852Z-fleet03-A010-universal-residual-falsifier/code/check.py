"""A010 v6. Independent parent-map full-forest coefficients and denominator caps."""
from fractions import Fraction as F
from itertools import product, combinations
from math import factorial, comb, prod
from pathlib import Path
import json, time, sys, hashlib
BASE=Path(__file__).resolve().parents[1]
(BASE/'out').mkdir(exist_ok=True)
checks=0
def ck(p):
    global checks
    checks+=1
    assert p, checks

def full(A,E,n):
    """Sum directed rooted parent maps; count chronological words by slot factorials."""
    vertices=[v for v in range(n) if A>>v&1]
    C={}; count=0
    for assign in product(*[[i for i,e in enumerate(E) if v in e] for v in vertices]):
        blocks={i:tuple(v for v,j in zip(vertices,assign) if j==i) for i in set(assign)}
        U=tuple(sorted(blocks)); reach={(i,j):i==j or bool(set(blocks[i])&set(E[j])) for i in U for j in U}
        for k in U:
            for i in U:
                for j in U:reach[i,j]=reach[i,j] or (reach[i,k] and reach[k,j])
        components={frozenset(j for j in U if reach[i,j] and reach[j,i]) for i in U}
        sources=[S for S in components if not any(set(blocks[i])&set(E[j]) for i in U if i not in S for j in S)]
        for rr in product(*[tuple(sorted(S)) for S in sorted(sources,key=lambda s:min(s))]):
            roots=set(rr); NR=[i for i in U if i not in roots]
            options=[[(i,v) for i in U if i!=j for v in blocks[i] if v in E[j]] for j in NR]
            for pp in product(*options):
                parent=dict(zip(NR,pp)); valid=True
                for j in NR:
                    seen=set(); k=j
                    while k not in roots:
                        if k in seen:valid=False;break
                        seen.add(k); k=parent[k][0]
                    if not valid:break
                if not valid:continue
                slots={(i,v):0 for i in U for v in blocks[i]}
                for iv in pp:slots[iv]+=1
                mult=prod(factorial(c) for c in slots.values())
                c=F(mult,4**len(roots))
                for i in U:
                    s=len(blocks[i]); d=sum(slots[i,v] for v in blocks[i])
                    c/=s*(s+1)*comb(2,s)*(d+1)*(d+2)*comb(s+d-1,d)
                T=sum(1<<i for i in U); C[T]=C.get(T,F(0))+c;count+=mult
    return C,count

def physical(E,n):
    f=[1 if any(all(x>>v&1 for v in e) for e in E) else -1 for x in range(1<<n)]
    w=f[:]; step=1
    while step<len(w):
        for i in range(0,len(w),2*step):
            for j in range(i,i+step):w[j],w[j+step]=w[j]+w[j+step],w[j]-w[j+step]
        step*=2
    P={A:F(z*z,1<<(2*n)) for A,z in enumerate(w) if A and z}
    I=sum(A.bit_count()*p for A,p in P.items())
    ck(sum(F(z*z,1<<(2*n)) for z in w)==1)
    ck(I==F(sum(f[x]!=f[x^(1<<v)] for x in range(1<<n) for v in range(n)),1<<n))
    return P,I

def price(J,n):
    # Exact primal-dual witnesses, not an appeal to half-integrality.
    y=min((y for y in product([F(0),F(1,2),F(1)],repeat=n) if all(y[u]+y[v]>=1 for u,v in J)),key=sum)
    L=sum(y)
    z=next(z for z in product([F(0),F(1,2),F(1)],repeat=len(J)) if sum(z)==L and all(sum(z[i] for i,e in enumerate(J) if v in e)<=1 for v in range(n)))
    ck(sum(z)==sum(y))
    return L,z,y

def cap(k,L):
    return 1/((1+F(4*k,L))**k-F(4*k,L)**k)

def lp(h,u,v):
    left=F(1); p={};threshold=None
    for T in sorted(h,key=lambda T:(h[T],T),reverse=True):
        z=min(left,u[T]);p[T]=z;left-=z
        if not left:threshold=h[T];break
    ck(left==0)
    primal=sum(p[T]*h[T] for T in p)
    dual=threshold+sum(u[T]*max(h[T]-threshold,0) for T in h)
    ck(primal==dual and primal>=v)
    return primal-v,{'threshold':str(threshold),'primal':{str(T):str(z) for T,z in p.items() if z},'value':str(primal),'dual':str(dual)}

def graph(E,n,prior=None):
    deg=[sum(v in e for e in E) for v in range(n)]
    lam=[F(1,2*max(deg))]*len(E); D=prod(1+x/4 for x in lam)-1
    P,I=physical(E,n);v=sum(P.values());C={};Q={};runs=0
    for A in range(1,1<<n):
        if any(A>>j&1 and not deg[j] for j in range(n)):ck(A not in P);continue
        C[A],r=full(A,E,n);runs+=r
        Q[A]=sum(c*prod(lam[i] for i in range(len(E)) if T>>i&1) for T,c in C[A].items())/D
        ck(Q[A]>0)
    ck(sum(Q.values())<=1)
    h={T:sum(P[A]*C[A].get(T,F(0))*4**T.bit_count()/Q[A] for A in P) for T in range(1,1<<len(E))}
    p={T:prod(lam[i]/4 for i in range(len(E)) if T>>i&1)/D for T in h}
    ck(sum(p.values())==1);ck(sum(p[T]*h[T] for T in h)==v)
    old={};new={};duals={};sharp=0
    for T in h:
        J=tuple(e for i,e in enumerate(E) if T>>i&1);k=len(J);L,z,y=price(J,n)
        old[T]=min(F(1),F(4)**(1-k)*L**(k-1)/k**k);new[T]=cap(k,L)
        ck(p[T]<=new[T]<=old[T]);ck(k==1 or new[T]<old[T])
        equal=F(L,k);feasible=all(sum(equal for e in J if v0 in e)<=1 for v0 in range(n))
        if feasible:
            ck(equal**k/(4**k*((1+equal/4)**k-1))==new[T]);sharp+=1
        duals[str(T)]={'L':str(L),'primal':list(map(str,z)),'dual':list(map(str,y)),'cap':str(new[T]),'equal_weight_sharp':feasible}
    go,co=lp(h,old,v);gn,cn=lp(h,new,v);ck(gn<=go)
    if prior is not None:
        ck({str(T):str(z) for T,z in h.items()}==prior['h'])
        ck(str(go)==prior['capped_Gamma'])
        ck(str(I)==prior['I'])
    return {'n':n,'edges':E,'I':str(I),'V':str(v),'runs':runs,'h':{str(T):str(z) for T,z in h.items()},'old_gap':str(go),'new_gap':str(gn),'strict_gap_improvement':gn<go,'sharp_root_subsets':sharp,'old_lp':co,'new_lp':cn,'root_caps':duals}

def stars(top):
    rows=[]
    for m in range(2,top+1):
        D=(1+F(1,4*m))**m-1;delta=F(1,4**m);ph=(1-F(1,2**m))**2;v=1-delta;I=1+F(m-1,2**m)
        a=lambda k:F(factorial(k-1),3*8**k*k*(k+1))
        b=lambda k:F(factorial(k),16*8**k*(k+1)*(k+2))
        h={}
        for t in range(1,m+1):
            h[t]=delta*D*(4*m)**t+delta*D*(4*m)**t*a(t)/(a(t)+b(t)*F(m-t,m))
            h[t]+=4*D*ph if t==1 else t*delta*D*4**t*m**(t-1)*b(t-1)/(a(t-1)+b(t-1)*F(m-t+1,m))
        old={t:comb(m,t)*F(4)**(1-t)/t**t for t in h};new={t:comb(m,t)*cap(t,F(1)) for t in h}
        actual={t:F(comb(m,t),(4*m)**t)/D for t in h}
        ck(sum(actual.values())==1);ck(sum(actual[t]*h[t] for t in h)==v)
        go,_=lp(h,old,v);gn,cert=lp(h,new,v);ck(gn<=go<I/6)
        upper=4*D*(ph+F(2*comb(2*m,m)+comb(2*m,m-1),4**m))-v
        ck(go<=upper<F(91,48))
        if m<=4:
            E=tuple((0,j) for j in range(1,m+1));P,If=physical(E,m+1);ck(If==I);hh={T:F(0) for T in range(1,1<<m)}
            for A in range(1,1<<(m+1)):
                C,r=full(A,E,m+1);B=A>>1;k=B.bit_count()
                expected={B:F(1,32**k)} if not A&1 else ({1<<j:F(1,32) for j in range(m)} if not k else {**{B:a(k)},**{B|1<<j:b(k) for j in range(m) if not B>>j&1}})
                ck(C==expected)
                q=sum(c*F(1,m**T.bit_count()) for T,c in C.items())/D
                for T,c in C.items():hh[T]+=P[A]*c*4**T.bit_count()/q
            ck(all(hh[T]==h[T.bit_count()] for T in hh))
        rows.append({'m':m,'I':str(I),'old_gap':str(go),'new_gap':str(gn),'strict':gn<go,'new_lp':cert})
    return rows

def main():
    started=time.monotonic();pilot='--pilot' in sys.argv;rows=[]
    source=Path(r'agents/A006/runs/20261014T074929Z-fleet05-A006-posterior-forest-optimization/out/GRAPH_CAP_FULL.json')
    prior={tuple(map(tuple,r['edges'])):r for r in json.loads(source.read_text(encoding='utf-8'))['rows']}
    n=3 if pilot else 4;edges=list(combinations(range(n),2))
    jobs=[(n,tuple(e for i,e in enumerate(edges) if mask>>i&1),True) for mask in range(1,1<<len(edges))]
    if not pilot:
        jobs += [(5,tuple(E),False) for E in [
            [(0,1),(1,2),(2,3),(3,4),(0,4)],
            [(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)],
            [(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)],
            [(0,1),(1,2),(2,3),(0,3),(1,4),(2,4)]]]
    for n,E,compare in jobs:
        row=graph(E,n,prior[E] if compare and not pilot else None);rows.append(row)
        (BASE/'out'/('PILOT_CHECKPOINT.json' if pilot else 'CHECKPOINT.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
        ck(time.monotonic()-started<(55 if pilot else 240))
    ss=stars(4 if pilot else 32)
    # Sharp pair cap does not describe the joint feasible law.
    p1,p2,p12=F(15,17),F(1,17),F(1,17)
    ck(p1+p2+p12==1 and p12==cap(2,F(1)))
    l1,l2=4*p12/p2,4*p12/p1
    ck(l1+l2>1 and 4*p12*(p1+p2)>p1*p2)
    result={'status':'PASS','helper_version':'A010-full-parent-map-v6','graphs':len(rows),'assertions':checks,'distinct_runs_counted':sum(r['runs'] for r in rows),'strict_graph_improvements':sum(r['strict_gap_improvement'] for r in rows),'star_cases':len(ss),'strict_star_improvements':sum(r['strict'] for r in ss),'seconds':time.monotonic()-started,'nonphysical_cap_point':{'p':[str(p1),str(p2),str(p12)],'recovered_lambda':[str(l1),str(l2)]},'rows':rows,'stars':ss}
    target=BASE/'out'/('PILOT.json' if pilot else 'CHECK.json');target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','stars')}))
if __name__=='__main__':main()
