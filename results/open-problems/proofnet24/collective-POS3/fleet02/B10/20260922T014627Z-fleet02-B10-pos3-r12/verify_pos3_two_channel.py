#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction

def closure(n, rels):
    lt=[[False]*n for _ in range(n)]
    for a,b in rels:
        lt[a][b]=True
    for k in range(n):
        for i in range(n):
            if lt[i][k]:
                for j in range(n):
                    if lt[k][j]:
                        lt[i][j]=True
    return lt

def extensions(n, rels):
    lt=closure(n,rels)
    pred=[sum((1<<i) for i in range(n) if lt[i][j]) for j in range(n)]
    out=[]
    def rec(mask,order):
        if len(order)==n:
            out.append(tuple(order)); return
        for v in range(n):
            if not ((mask>>v)&1) and (pred[v] & ~mask)==0:
                rec(mask|(1<<v),order+[v])
    rec(0,[])
    return lt,out

def blockers(lt,x,y):
    S=[z for z in range(len(lt)) if lt[x][z] and not lt[z][y] and not lt[y][z]]
    return [z for z in S if not any(w!=z and w in S and lt[w][z] for w in S)]

def count(exts,a,b):
    return sum(e.index(a)<e.index(b) for e in exts)

def check(name,n,rels,x,y,expected_E,expected_e):
    lt,exts=extensions(n,rels)
    B=blockers(lt,x,y)
    assert len(B)==2
    s,t=B
    E=len(exts)
    assert E==expected_E and count(exts,x,y)==expected_e
    sk=defaultdict(lambda:[0,0])
    for e in exts:
        tau=tuple(z for z in e if z not in (x,y))
        sk[tau][e.index(x)>e.index(y)]+=1
    phi={s:0,t:0}; U={s:0,t:0}; neg=0; posfib={s:0,t:0}
    for tau,(nxy,nyx) in sk.items():
        pos={v:i+1 for i,v in enumerate(tau)}
        m=len(tau)
        def I(z):
            a=max([pos[v] for v in tau if lt[v][z]]+[0])
            b=min([pos[v]-1 for v in tau if lt[z][v]]+[m])
            return a,b
        a,b=I(x); c,d=I(y)
        assert c<=a
        delta=nxy-nyx
        if delta<0: neg += -delta
        if d<=b:
            assert delta<=0
            continue
        nn=b-a+1; L=a-c; R=d-b
        assert nxy==nn*R+nn*(nn+1)//2
        assert nyx==nn*L+nn*(nn+1)//2
        first=min((v for v in tau if lt[x][v]), key=lambda v:tau.index(v))
        assert first in B
        U[first]+=nn*R
        if delta>0:
            phi[first]+=delta
            posfib[first]+=1
    triple={
        s:sum(e.index(s)<e.index(y) and e.index(s)<e.index(t) for e in exts),
        t:sum(e.index(t)<e.index(y) and e.index(t)<e.index(s) for e in exts),
    }
    assert U==triple
    Q=sum(e.index(y)<e.index(s) and e.index(y)<e.index(t) for e in exts)
    A={s:count(exts,y,s),t:count(exts,y,t)}
    D=2*count(exts,x,y)-E
    assert sum(U.values())==E-Q
    assert D<=sum(U.values())
    assert Q*E>=A[s]*A[t]
    cap=Fraction(1,1)-Fraction(A[s]*A[t],2*E*E)
    assert Fraction(count(exts,x,y),E)<=cap
    if all(A[b]*3>2*E for b in B) and D*3>E:
        assert all(phi[b]>neg for b in B)
    return dict(name=name,E=E,e_xy=count(exts,x,y),blockers=B,
                y_before={str(k):A[k] for k in B},joint_y_first=Q,
                right_fringe=U,positive_defect=phi,negative_defect=neg,
                positive_fibers=posfib,cap=str(cap))

cases=[
 check("partner_79",7,
       [(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(1,5),(2,5),(4,5),(4,6)],
       0,1,79,54),
 check("prior_local_91",7,
       [(0,1),(1,3),(0,5),(4,5),(3,6),(4,6)],
       4,2,91,62),
]
for d in cases:
    print(d)
print("POS3_TWO_CHANNEL_MASS_TRANSPORT_CHECK_PASS")
