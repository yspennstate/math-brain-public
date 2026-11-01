#!/usr/bin/env python3
"""Exact adversarial witnesses: three order-12 Conder arc-transitive graphs are not distance-regular."""
from collections import deque

GRAPHS={
2:{1:[2,5,9,12],2:[1,6,10,12],3:[5,7,10,11],4:[8,9,11,12],
5:[1,3,9,10],6:[2,7,8,10],7:[3,6,8,11],8:[4,6,7,12],
9:[1,4,5,11],10:[2,3,5,6],11:[3,4,7,9],12:[1,2,4,8]},
3:{1:[2,4,8,10],2:[1,5,7,11],3:[4,6,10,12],4:[1,3,7,9],
5:[2,6,8,12],6:[3,5,9,11],7:[2,4,8,10],8:[1,5,7,11],
9:[4,6,10,12],10:[1,3,7,9],11:[2,6,8,12],12:[3,5,9,11]},
5:{1:[2,3,6,8,11,12],2:[1,3,4,7,9,12],3:[1,2,4,5,8,10],
4:[2,3,5,6,9,11],5:[3,4,6,7,10,12],6:[1,4,5,7,8,11],
7:[2,5,6,8,9,12],8:[1,3,6,7,9,10],9:[2,4,7,8,10,11],
10:[3,5,8,9,11,12],11:[1,4,6,9,10,12],12:[1,2,5,7,10,11]}}
WIT={
2:((3,(1,2,1)),(4,(2,2,0))),
3:((5,(2,0,2)),(7,(4,0,0))),
5:((4,(4,2,0)),(5,(3,3,0))),
}

def distances(adj, root):
    d={root:0}; q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in d: d[v]=d[u]+1; q.append(v)
    return d

def intersection_tuple(adj,d,w):
    r=d[w]
    return (sum(d[z]==r-1 for z in adj[w]),
            sum(d[z]==r for z in adj[w]),
            sum(d[z]==r+1 for z in adj[w]))

for idx,adj in GRAPHS.items():
    d=distances(adj,1)
    (u,tu),(v,tv)=WIT[idx]
    assert d[u]==d[v]==2
    assert intersection_tuple(adj,d,u)==tu
    assert intersection_tuple(adj,d,v)==tv
    assert tu!=tv
    print("graph",idx,"root 1 distance-2 witnesses",u,tu,"vs",v,tv,"NOT_DISTANCE_REGULAR")
print("RESULT PASS")
