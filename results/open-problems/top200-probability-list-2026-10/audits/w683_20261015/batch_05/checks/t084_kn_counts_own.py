"""Independent labelled, unrooted forest census through K6 and Hermite checks."""
from pathlib import Path
from collections import Counter
from itertools import combinations
import sympy as S
import json

t,z,a,b=S.symbols('t z a b')
results=[]
for n in range(1,7):
    edges=list(combinations(range(n),2));Z=Counter();E=Counter();Adj=Counter();Disj=Counter();H=Counter()
    ie=edges.index((0,1)) if n>=2 else -1
    ia=edges.index((0,2)) if n>=3 else -1
    idj=edges.index((2,3)) if n>=4 else -1
    def visit(j,parent,chosen,k,degree):
        if j==len(edges):
            Z[k]+=1;H[(k,degree)]+=1
            if ie in chosen:
                E[k]+=1
                if ia in chosen:Adj[k]+=1
                if idj in chosen:Disj[k]+=1
            return
        visit(j+1,parent,chosen,k,degree)
        u,v=edges[j]
        def find(x):
            while parent[x]!=x:x=parent[x]
            return x
        ru,rv=find(u),find(v)
        if ru!=rv:
            new=parent.copy();new[ru]=rv
            visit(j+1,new,chosen|{j},k+1,degree+int(u==0 or v==0))
    visit(0,list(range(n)),set(),0,0)
    N=n-1;P=[S.Integer(1),b]
    for k in range(2,N+1):P.append(S.expand(b*P[-1]-a*(k-1)*P[-2]))
    Q=P[N]-N*P[N-1] if N else P[0]
    predicted=S.Poly(S.cancel(t**N*Q.subs(b,N+a+z).subs(a,1/t)),t,z)
    assert {tuple(k):int(v) for k,v in predicted.terms()}==dict(H),(n,predicted,H)
    def poly(counter):return sum(c*t**k for k,c in counter.items())
    disj=S.expand(poly(E)**2-poly(Z)*poly(Disj)) if n>=4 else None
    adj=S.expand(poly(E)**2-poly(Z)*poly(Adj)) if n>=3 else None
    expected={4:t**4*(2+4*t),5:t**4*(2+24*t+84*t*t+100*t**3),6:t**4*(2+48*t+462*t*t+2172*t**3+5184*t**4+5184*t**5)}
    if n>=4:assert S.expand(disj-expected[n])==0
    row={'n':n,'forest_count':sum(Z.values()),'partition':dict(Z),'edge':dict(E),'adjacent_pair':dict(Adj),'disjoint_pair':dict(Disj),'vertex_degree_coefficients':[[k,d,c] for (k,d),c in sorted(H.items())],'hermite_identity':True,'disjoint_Rayleigh':str(disj),'adjacent_Rayleigh':str(adj)}
    results.append(row)
    Path('checks/t084_kn_counts_own.json').write_text(json.dumps({'complete':n==6,'method':'Own labelled edge-subset recursion with union-find cycle rejection; no rooted-component weights','rows':results},indent=2)+'\n',encoding='utf8')
    print('K'+str(n)+' forests='+str(sum(Z.values()))+' Hermite PASS'+(' disjoint base PASS' if n>=4 else ''),flush=True)
