from fractions import Fraction as F
from itertools import combinations,product
from math import factorial,prod
from pathlib import Path
import json,sys,time
OUT=Path(__file__).resolve().parents[1]/'out'
def spectrum(n,edges):
    values=[1 if any((x>>u&1) and (x>>v&1) for u,v in edges) else -1 for x in range(1<<n)]
    w=values[:]; step=1
    while step<len(w):
        for i in range(0,len(w),2*step):
            for j in range(i,i+step): w[j],w[j+step]=w[j]+w[j+step],w[j]-w[j+step]
        step*=2
    P={a:F(w[a]**2,1<<(2*n)) for a in range(1,1<<n) if w[a]}
    I=sum(P[a]*a.bit_count() for a in P)
    piv=F(sum(values[x]!=values[x^(1<<v)] for x in range(1<<n) for v in range(n)),1<<n)
    assert I==piv
    return P,I
def coefficients(n,edges,A):
    inside=[i for i,e in enumerate(edges) if all(A>>v&1 for v in e)]; result={}
    for bits in range(1<<len(inside)):
        M=[inside[j] for j in range(len(inside)) if bits>>j&1]
        vertices=[v for i in M for v in edges[i]]; owned=set(vertices)
        if len(vertices)!=len(owned): continue
        if any(all(v not in owned for v in edges[i]) for i in inside): continue
        U=[u for u in range(n) if A>>u&1 and u not in owned]
        choices=[[(i,e[1] if e[0]==u else e[0]) for i,e in enumerate(edges) if u in e] for u in U]
        for nu in product(*choices):
            used=M+[i for i,v in nu]; assert len(set(used))==len(used)
            T=sum(1<<i for i in used); h={v:0 for v in owned}; c=F(1,24)**len(M)
            for i,v in nu:
                if v in owned: h[v]+=1; c*=F(1,8)
                else: c*=F(1,32)
            for i in M:
                u,v=edges[i]; k=h[u]+h[v]
                c*=F(factorial(h[u])*factorial(h[v]),(k+1)**2*(k+2))
            result[T]=result.get(T,F(0))+c
    return result
def check(n,edges,lam):
    P,I=spectrum(n,edges); v=sum(P.values()); N=len(edges)
    assert all(sum(lam[i] for i,e in enumerate(edges) if u in e)<=1 for u in range(n))
    D=prod(1+x/4 for x in lam)-1
    p={T:prod(lam[i]/4 for i in range(N) if T>>i&1)/D for T in range(1,1<<N)}
    assert sum(p.values())==1
    K={A:{T:c*4**T.bit_count() for T,c in coefficients(n,edges,A).items()} for A in P}
    q={A:sum(c*p[T] for T,c in row.items()) for A,row in K.items()}
    assert all(q[A]>0 for A in P)
    for A in P:
        W=sum(c*prod(lam[i] for i in range(N) if T>>i&1) for T,c in coefficients(n,edges,A).items())
        assert q[A]==W/D
    h={T:sum(P[A]*K[A].get(T,0)/q[A] for A in P) for T in p}
    assert sum(p[T]*h[T] for T in p)==v
    gamma=max(h.values())-v; assert gamma>=0
    return {'n':n,'edges':edges,'I':str(I),'V':str(v),'Gamma':str(gamma),'argmax':max(h,key=h.get),'coefficient_terms':sum(map(len,K.values()))},(P,I,v,D,K,q,h)
if __name__=='__main__':
    start=time.monotonic(); pilot='pilot' in sys.argv; n=3 if pilot else 4; allE=list(combinations(range(n),2)); rows=[]
    for bits in range(1,1<<len(allE)):
        E=[e for i,e in enumerate(allE) if bits>>i&1]; deg=[sum(u in e for e in E) for u in range(n)]
        for name,lam in [('uniform',[F(1,max(deg))]*len(E)),('local',[F(1,deg[u]+deg[v]) for u,v in E])]:
            row,_=check(n,E,lam); row['weights']=name; rows.append(row)
        assert time.monotonic()-start<(60 if pilot else 300)
        (OUT/'checkpoint.json').write_text(json.dumps({'graphs_completed':bits,'references_completed':len(rows)}))
    stars=[]
    for m in range(2,4 if pilot else 9):
        E=[(0,i) for i in range(1,m+1)]; P,I,v,D,K,q,h=check(m+1,E,[F(1,m)]*m)[1]
        A=(1<<(m+1))-1; T=(1<<m)-1
        assert P[A]==F(1,4**m) and I==1+F(m-1,2**m) and v==1-F(1,4**m)
        assert set(K[A])=={T}
        assert K[A][T]==F(factorial(m-1),3*2**m*m*(m+1))
        assert P[A]*K[A][T]/q[A]==D*m**m
        gamma=max(h.values())-v; bound=F(m**m,4)-v
        assert gamma>=D*m**m-v>bound
        stars.append({'m':m,'Gamma':str(gamma),'all_weight_lower_bound':str(bound),'I':str(I),'full_set_column':str(K[A][T])})
        assert time.monotonic()-start<(60 if pilot else 300)
    result={'helper':'A010-root-law-independent-v1','graphs':len(rows)//2,'references':len(rows),'stars':stars,'rows':rows,'elapsed_seconds':time.monotonic()-start,'verdict':'PASS exact coefficient/root-law identity, gradient averaging and actual-star certificate-gap obstruction'}
    (OUT/('pilot.json' if pilot else 'rootlaw.json')).write_text(json.dumps(result,indent=2)); print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
