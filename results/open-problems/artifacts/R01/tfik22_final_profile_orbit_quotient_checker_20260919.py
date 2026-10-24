#!/usr/bin/env python3
"""Exact symmetry quotient for R01 TFIK22 profile (n4,n3)=(2,12).

This independently checks the largest finite core from the earlier profile proof.
It encodes the adjacent-degree-4 nonplanar case by alternating R/B words on
the 9 edges of K_{3,3}, quotients by Aut(K_{3,3}) x C2 swapping the two
degree-4 vertices, and tests 2-apex on one representative per structural orbit.

All counts are integer/combinatorial. NetworkX planarity is combinatorial.
This is a self-check, not an independent audit.
"""
from __future__ import annotations
import itertools
from collections import Counter, defaultdict
import networkx as nx

PERMS = tuple(itertools.permutations(range(3)))
EDGES = tuple((i,j) for i in range(3) for j in range(3))
EIDX = {e:k for k,e in enumerate(EDGES)}


def alt_word(k,start):
    other = 'B' if start == 'R' else 'R'
    return ''.join(start if i%2==0 else other for i in range(k))


WORD_OPTIONS = ['']
for k in range(1,7):
    WORD_OPTIONS += [alt_word(k,'R'), alt_word(k,'B')]
WORD_OPTIONS = tuple(dict.fromkeys(WORD_OPTIONS))


def word_assignments(rtot, btot):
    out=[]
    def rec(i,r,b,cur):
        if i==9:
            if (r,b)==(rtot,btot): out.append(tuple(cur))
            return
        for w in WORD_OPTIONS:
            rr=w.count('R'); bb=w.count('B')
            if r+rr<=rtot and b+bb<=btot:
                cur.append(w); rec(i+1,r+rr,b+bb,cur); cur.pop()
    rec(0,0,0,[])
    return out


def one_edge_poly(maxr=3,maxb=3):
    c=Counter()
    for w in WORD_OPTIONS:
        r=w.count('R'); b=w.count('B')
        if r<=maxr and b<=maxb: c[(r,b)] += 1
    return c


def poly_pow_coeff(base, power, rr, bb):
    cur={(0,0):1}
    for _ in range(power):
        nxt=defaultdict(int)
        for (a,b),u in cur.items():
            for (c,d),v in base.items():
                if a+c<=rr and b+d<=bb: nxt[(a+c,b+d)] += u*v
        cur=dict(nxt)
    return cur.get((rr,bb),0)


def transform(A,p,q,side_swap,color_swap):
    B=['']*9
    table=str.maketrans('RB','BR')
    for k,(i,j) in enumerate(EDGES):
        w=A[k]
        if side_swap:
            e=(q[j],p[i]); w=w[::-1]
        else:
            e=(p[i],q[j])
        if color_swap: w=w.translate(table)
        B[EIDX[e]]=w
    return tuple(B)


GROUP=tuple((p,q,s,c) for p in PERMS for q in PERMS for s in (False,True) for c in (False,True))
assert len(GROUP)==144


def canonical(A):
    return min(transform(A,*g) for g in GROUP)


def subdivided_k33(A):
    G=nx.Graph(); G.add_nodes_from(range(6))
    nxt=6; R=[]; B=[]
    for (i,j),w in zip(EDGES,A):
        u=i; v=3+j; last=u
        for col in w:
            z=nxt; nxt+=1
            G.add_edge(last,z); last=z
            (R if col=='R' else B).append(z)
        G.add_edge(last,v)
    return G,nxt,R,B


def build(A):
    G,nxt,R,B=subdivided_k33(A)
    assert nxt==12 and len(R)==len(B)==3
    a,b=12,13
    G.add_edge(a,b)
    G.add_edges_from((a,z) for z in R)
    G.add_edges_from((b,z) for z in B)
    return G


def is_2apex(G):
    for u,v in itertools.combinations(sorted(G.nodes()),2):
        H=G.copy(); H.remove_nodes_from((u,v))
        if nx.check_planarity(H)[0]: return True,(u,v)
    return False,None


def graph_from_edges(E):
    G=nx.Graph(); G.add_nodes_from(range(14)); G.add_edges_from(E); return G


POS = (
("C14_PLUS_EDGE", ((0,7),(0,8),(0,9),(0,10),(1,7),(1,10),(1,11),(2,7),(2,12),(2,13),
 (3,8),(3,10),(3,12),(4,8),(4,11),(4,13),(5,9),(5,10),(5,13),(6,9),(6,11),(6,12))),
("H13_VERTEX_SPLIT", ((0,6),(0,7),(0,8),(1,6),(1,9),(1,10),(2,7),(2,9),(2,11),(3,4),
 (3,7),(3,10),(3,12),(4,8),(4,9),(4,13),(5,8),(5,10),(5,11),(6,12),(11,13),(12,13))),
("K3311_UNIQUE_ORDER14", ((0,5),(0,8),(0,9),(1,4),(1,10),(1,11),(2,3),(2,12),(2,13),(3,8),
 (3,10),(4,9),(4,12),(5,11),(5,13),(6,7),(6,8),(6,11),(6,12),(7,9),(7,10),(7,13))),
)
POSG=[(name,graph_from_edges(E)) for name,E in POS]


def matrix(A):
    return tuple(tuple(A[3*i+j] for j in range(3)) for i in range(3))


def main():
    p=one_edge_poly()
    c11=poly_pow_coeff(p,9,1,1)
    c33=poly_pow_coeff(p,9,3,3)
    A11=word_assignments(1,1)
    A33=word_assignments(3,3)
    assert c11==len(A11)==90
    assert c33==len(A33)==22530

    buckets=defaultdict(list)
    for A in A33: buckets[canonical(A)].append(A)
    assert len(buckets)==199
    dist=Counter(len(v) for v in buckets.values())
    assert dist==Counter({144:124,72:59,36:9,18:3,12:4})
    assert sum(k*v for k,v in dist.items())==22530

    non2=[]; two_orbits=0
    for rep,orb in sorted(buckets.items()):
        G=build(rep); ok,_=is_2apex(G)
        if ok:
            two_orbits += 1
        else:
            matches=tuple(name for name,P in POSG if nx.is_isomorphic(G,P))
            assert len(matches)==1
            non2.append((rep,len(orb),matches[0]))
    assert two_orbits==196
    assert len(non2)==3
    assert sorted(sz for _,sz,_ in non2)==[12,12,36]
    assert sum(sz for _,sz,_ in non2)==60
    assert {name for _,_,name in non2}=={name for name,_ in POSG}

    print('ONE_EDGE_POLY', sorted(p.items()))
    print('COEFF_XY_F9', c11)
    print('COEFF_X3Y3_F9', c33)
    print('GROUP_ORDER', len(GROUP))
    print('STRUCTURAL_ORBITS', len(buckets))
    print('ORBIT_SIZE_DISTRIBUTION', tuple(sorted(dist.items())))
    print('TWO_APEX_ORBITS', two_orbits)
    print('NON2_ORBITS', len(non2), 'RAW_MASS', sum(sz for _,sz,_ in non2))
    for rep,sz,name in sorted(non2, key=lambda z:z[2]):
        print('SURVIVOR', name, 'ORBIT_SIZE', sz, 'WORD_MATRIX', matrix(rep))
    print('ALL_EXACT_TFIK22_ORBIT_QUOTIENT_CHECKS_PASS')


if __name__=='__main__': main()
