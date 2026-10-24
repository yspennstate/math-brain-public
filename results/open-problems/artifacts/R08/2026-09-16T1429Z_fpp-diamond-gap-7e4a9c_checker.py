#!/usr/bin/env python3
from fractions import Fraction
from heapq import heappush, heappop
import itertools, hashlib

def add_edge(adj,a,b,w):
    adj.setdefault(a,[]).append((b,w))
    adj.setdefault(b,[]).append((a,w))

def dijkstra_count(adj,s):
    dist={s:Fraction(0)}
    count={s:1}
    pq=[(Fraction(0),s)]
    while pq:
        d,u=heappop(pq)
        if d!=dist[u]: continue
        for v,w in adj[u]:
            nd=d+w
            if v not in dist or nd<dist[v]:
                dist[v]=nd
                count[v]=count[u]
                heappush(pq,(nd,v))
            elif nd==dist[v]:
                count[v]+=count[u]
    return dist,count

def l_route_box(m):
    H=Fraction(10*m+1)
    adj={}
    for x in range(m+1):
        for y in range(m+1):
            if x<m:
                a=(x,y); b=(x+1,y)
                w=Fraction(1) if y==0 else H
                add_edge(adj,a,b,w)
            if y<m:
                a=(x,y); b=(x,y+1)
                w=Fraction(1) if x==m else H
                add_edge(adj,a,b,w)
    return adj,H

def check_x002():
    cases=0
    for m in range(1,13):
        adj,H=l_route_box(m)
        A=(0,0); B=(m,0); C=(m,m)
        dA,cA=dijkstra_count(adj,A)
        dB,cB=dijkstra_count(adj,B)
        assert dA[B]==m and cA[B]==1
        assert dB[C]==m and cB[C]==1
        assert dA[C]==2*m and cA[C]==1
        assert dA[C]==dA[B]+dB[C]
        delta=Fraction(1,100*m)
        assert 2*m*(1+delta) < H
        # On the open cylinder in which every L-route edge lies in
        # (1,1+delta) and every off-L edge lies in (H,H+delta), the
        # L-route costs < 2m(1+delta) < H, whereas every competitor uses
        # an off-L edge and costs > H. Thus finite triangle equality
        # persists on a positive-volume cylinder event under Exp(1).
        cases+=1
    return cases

def all_bits(n):
    return list(itertools.product([0,1], repeat=n))

def is_monotone_table(table, configs):
    n=len(configs[0])
    for x in configs:
        if not table[x]: continue
        for i in range(n):
            if x[i]==0:
                y=list(x); y[i]=1; y=tuple(y)
                if not table[y]:
                    return False
    return True

def prob_event(table, configs, p):
    n=len(configs[0])
    ans=Fraction(0)
    for x in configs:
        if table[x]:
            k=sum(x)
            ans += p**k * (1-p)**(n-k)
    return ans

def check_r09_passage():
    pairs=[
        (Fraction(1,7),Fraction(2,5)),
        (Fraction(1,4),Fraction(3,4)),
        (Fraction(2,3),Fraction(5,6)),
        (Fraction(0),Fraction(1,3)),
    ]
    counts={}
    checks=0
    for n in [1,2,3,4]:
        configs=all_bits(n)
        monotone=[]
        for mask in range(1<<len(configs)):
            table={configs[j]: ((mask>>j)&1) for j in range(len(configs))}
            if is_monotone_table(table,configs):
                monotone.append(table)
        counts[n]=len(monotone)
        for table in monotone:
            for q,p in pairs:
                Pq=prob_event(table,configs,q)
                Pp=prob_event(table,configs,p)
                diff=Pp-Pq
                coupling=1-(1-(p-q))**n
                union=n*(p-q)
                assert Fraction(0)<=diff<=coupling<=union
                checks+=1
    assert counts=={1:3,2:6,3:20,4:168}, counts
    return counts,checks

if __name__=="__main__":
    xc=check_x002()
    counts,checks=check_r09_passage()
    print("PASS")
    print("R08-X002 exact L-corridor cases:",xc)
    print("R09-PASSAGE-02 monotone counts:",counts)
    print("R09-PASSAGE-02 exact rational event/parameter checks:",checks)
    print("Certificate: exact Fraction arithmetic; no floating-point proof claims.")
