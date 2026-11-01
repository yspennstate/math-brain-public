#!/usr/bin/env python3
from fractions import Fraction

# Exact witness found in graph6 Gg\\oB{ on 8 vertices.
# Edges are listed explicitly so verification is independent of graph6 decoding.
edges = [
    (0,1),(1,2),(1,4),(2,4),(3,4),(1,5),(2,5),(3,5),
    (1,7),(2,7),(3,7),(4,7),(5,7),(6,7)
]
g_idx=9   # distinguished weighted edge g=(2,7)
e_idx=3   # tested edge e=(2,4)
f_idx=12  # tested edge f=(5,7)

class DSU:
    def __init__(self,n): self.p=list(range(n))
    def find(self,a):
        while self.p[a]!=a:
            self.p[a]=self.p[self.p[a]]; a=self.p[a]
        return a
    def union(self,a,b):
        a=self.find(a); b=self.find(b)
        if a==b: return False
        self.p[b]=a; return True

# [A,B,Ae,Be,Af,Bf,Aef,Bef]
c=[0]*8
forest_count=0
for mask in range(1<<len(edges)):
    d=DSU(8)
    ok=True
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            if not d.union(u,v):
                ok=False; break
    if not ok: continue
    forest_count += 1
    hasg=(mask>>g_idx)&1; hase=(mask>>e_idx)&1; hasf=(mask>>f_idx)&1
    base=1 if hasg else 0
    c[base]+=1
    if hase: c[2+base]+=1
    if hasf: c[4+base]+=1
    if hase and hasf: c[6+base]+=1
A,B,Ae,Be,Af,Bf,Aef,Bef=c
q0=Ae*Af-A*Aef
q1=Ae*Bf+Be*Af-A*Bef-B*Aef
q2=Be*Bf-B*Bef
assert forest_count==A+B
assert (A,B,Ae,Be,Af,Bf,Aef,Bef)==(2888,1304,1072,328,976,328,344,80)
assert (q0,q1,q2)==(52800,-7872,3264)
# derivative q1+2q2 lambda, stationary point
lam_star=Fraction(-q1,2*q2)
minval=Fraction(q0,1)+q1*lam_star+q2*lam_star*lam_star
disc=q1*q1-4*q0*q2
assert lam_star==Fraction(41,34)
assert minval==Fraction(816912,17)
assert disc==-627388416
assert q0+q1+q2==48192
assert q1<0 and disc<0 and q2>0

print('claim=P14-ONEEDGE-MONOTONICITY-NOGO-56')
print('graph6=Gg\\\\oB{')
print('vertices=8 edges=14 edge_subsets_checked=%d' % (1<<len(edges)))
print('edge_list=' + repr(edges))
print('g_index=9 g=(2,7) e_index=3 e=(2,4) f_index=12 f=(5,7)')
print('A,B,Ae,Be,Af,Bf,Aef,Bef=' + repr(tuple(c)))
print('Delta(lambda)=%d + (%d)*lambda + %d*lambda^2' % (q0,q1,q2))
print('Delta(1)=%d' % (q0+q1+q2))
print('derivative_at_0=%d' % q1)
print('stationary_lambda=%s' % lam_star)
print('minimum_value=%s' % minval)
print('discriminant=%d' % disc)
print('VERDICT: exact route-kill: Delta is not monotone increasing on lambda>0, but this witness remains positive for every lambda>0.')
print('EXACT_CHECK_PASS')
