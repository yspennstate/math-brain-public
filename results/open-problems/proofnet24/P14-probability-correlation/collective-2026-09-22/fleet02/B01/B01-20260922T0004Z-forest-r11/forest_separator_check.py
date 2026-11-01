#!/usr/bin/env python3
"""Exact finite regression for the FOREST two-separator reduction.

For every simple graph A on <=5 labeled vertices, every absent terminal edge h=uv,
and every distinct physical edge pair e,f of A, split forest counts by:
  - e/f occupancy (00,01,10,11)
  - whether u,v are disconnected (d) or connected (c).

If an external two-terminal network induces virtual-edge weight lambda>=0, put
r=1+lambda>=1.  The same-side Rayleigh gap is
  P(r)=(r*d10+c10)(r*d01+c01)-(r*d00+c00)(r*d11+c11).
The script minimizes this quadratic exactly over r>=1 and also records the first
failure of the false shortcut "the connected boundary sector is Rayleigh".
"""
from fractions import Fraction
from itertools import combinations

def is_forest(n, edges, mask):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for k,(u,v) in enumerate(edges):
        if (mask>>k)&1:
            ru,rv=find(u),find(v)
            if ru==rv:
                return False
            parent[ru]=rv
    return True

def connected(n, edges, mask, s, t):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for k,(u,v) in enumerate(edges):
        if (mask>>k)&1:
            ru,rv=find(u),find(v)
            if ru!=rv:
                parent[ru]=rv
    return find(s)==find(t)

def boundary_cells(n, edges, terminals, eidx, fidx):
    d=[0]*4
    c=[0]*4
    for mask in range(1<<len(edges)):
        if not is_forest(n, edges, mask):
            continue
        idx=(((mask>>eidx)&1)<<1)|((mask>>fidx)&1)  # 00,01,10,11
        (c if connected(n, edges, mask, *terminals) else d)[idx]+=1
    return d,c

def coeffs(d,c):
    # P(r)=A*r^2+B*r+C
    A=d[2]*d[1]-d[0]*d[3]
    B=d[2]*c[1]+c[2]*d[1]-d[0]*c[3]-c[0]*d[3]
    C=c[2]*c[1]-c[0]*c[3]
    return A,B,C

def min_on_ge1(A,B,C):
    # Returns exact minimum value and a minimizer when bounded below.
    if A<0:
        return None
    candidates=[(Fraction(A+B+C), Fraction(1))]
    if A>0 and B < -2*A:
        r=Fraction(-B,2*A)
        candidates.append((A*r*r+B*r+C, r))
    return min(candidates)

checked=0
by_n={}
weighted_failures=[]
sector_witness=None

for n in range(2,6):
    all_edges=list(combinations(range(n),2))
    per_n=0
    for graph_mask in range(1<<len(all_edges)):
        edges=[all_edges[k] for k in range(len(all_edges)) if (graph_mask>>k)&1]
        if len(edges)<2:
            continue
        eset=set(edges)
        for h in (x for x in all_edges if x not in eset):
            for eidx,fidx in combinations(range(len(edges)),2):
                d,c=boundary_cells(n,edges,h,eidx,fidx)
                A,B,C=coeffs(d,c)
                checked+=1
                per_n+=1
                minimum=min_on_ge1(A,B,C)
                if A<0 or (minimum is not None and minimum[0]<0):
                    weighted_failures.append(
                        (n,edges,h,edges[eidx],edges[fidx],d,c,(A,B,C),minimum)
                    )
                if sector_witness is None:
                    connected_gap=c[2]*c[1]-c[0]*c[3]
                    if connected_gap<0:
                        sector_witness=(
                            n,edges,h,edges[eidx],edges[fidx],d,c,
                            (A,B,C),connected_gap,minimum
                        )
    by_n[n]=per_n

print("FOREST_TWO_SEPARATOR_EXACT_REGRESSION")
print(f"weighted_instances_checked={checked}")
print("instances_by_n=" + repr(by_n))
print(f"weighted_failures_r_ge_1={len(weighted_failures)}")
if weighted_failures:
    print("first_weighted_failure=" + repr(weighted_failures[0]))
else:
    print("first_weighted_failure=None")

print("first_connected_sector_failure=" + repr(sector_witness))
expected=(
    4,
    [(0,2),(0,3),(1,2),(1,3)],
    (0,1),
    (0,2),
    (1,2),
    [3,3,3,0],
    [1,1,1,3],
    (9,-3,-2),
    -2,
    (Fraction(4,1),Fraction(1,1)),
)
assert sector_witness == expected
assert not weighted_failures
assert checked == 46563
print("K22_regression=PASS")
print("all_exact_assertions=PASS")
