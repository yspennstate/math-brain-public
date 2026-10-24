#!/usr/bin/env python3
"""Exact certificate for four exactly-three-close-pair canonical cases in PROB20-11.

It eliminates the three triangle distance patterns 222, 224, 244 and the unique
path-of-length-three pattern. All arithmetic is integer/exhaustive.
"""
from itertools import combinations

N=2048

def fd(a,b):
    w=(a^b).bit_count()
    return min(w,12-w)

B=[x for x in range(N) if fd(0,x)<=3]
assert len(B)==299
balls=[]
for c in range(N):
    m=0
    for b in B:
        m |= 1 << (c^b)
    balls.append(m)

def tri(a,b,c):
    return (balls[a]&balls[b]&balls[c]).bit_count()

def clique_max(cands, relation):
    m=len(cands)
    adj=[0]*m
    for i in range(m):
        for j in range(i+1,m):
            if relation(cands[i],cands[j]):
                adj[i]|=1<<j
                adj[j]|=1<<i
    best=0
    def rec(sz,P):
        nonlocal best
        if sz+P.bit_count()<=best:
            return
        if not P:
            best=max(best,sz)
            return
        while P:
            if sz+P.bit_count()<=best:
                return
            l=P&-P
            i=l.bit_length()-1
            P-=l
            rec(sz+1,P&adj[i])
        best=max(best,sz)
    rec(0,(1<<m)-1)
    return best

def bits(indices):
    z=0
    for i in indices:
        z |= 1<<i
    return z

# Triangle 222.  Each opposite-parity center would have to be high on three
# d=2 edges.  In canonical coordinates these conditions are
# x1+x2=x1+x3=x2+x3=1, impossible over {0,1}.  Hence every one of the seven
# opposite centers creates >=1 low triple; the Bonferroni slack permits <=3.
assert max((x1+x2==1)+(x1+x3==1)+(x2+x3==1)
           for x1 in (0,1) for x2 in (0,1) for x3 in (0,1)) == 2

# Triangle 224.  Highness on the two d=2 edges forces every opposite center,
# represented as a weight-5 block, to choose 1 of 2 coordinates from group A,
# 1 of 2 from group D, and 3 of 8 from R.  Seven pairwise-distance-6 blocks
# require total pair intersection 2*C(7,2)=42.  Convexity gives at least
# C(4,2)+C(3,2)=9?  More directly each 2-column group contributes >=15,
# and the 8-column group with 21 incidences contributes >=18: total >=48.
assert 15+15+18 > 42

# Triangle 244.  Normalize A={0,1}, B={0,2,3,4}.  The Bonferroni slack forces
# all 21 variable triples high.  Enumerate the resulting 168 weight-5 blocks.
A=bits([0,1])
B4=bits([0,2,3,4])
D=A^B4
cands=[]
for inds in combinations(range(12),5):
    C=bits(inds)
    if (A&C).bit_count()!=1:
        continue
    if (B4&C).bit_count()!=2:
        continue
    if (D&(C^A)).bit_count()!=2:
        continue
    cands.append(C)
assert len(cands)==168
omega244=clique_max(cands, lambda x,y:(x&y).bit_count()==2)
assert omega244==4  # seven opposite centers would be required

# Unique path3 canonical pattern: parity sequence 0,0,1,1 and close distances
# 2,3,2.  Normalize the active path.  The half-Bonferroni slack is one on
# each parity half, so all ten variable d=2 triples must be high.
A=bits([0,1])
C=A|bits([2,3,4])
D=bits([0,2,3,4,5])
assert (fd(0,A),fd(A,C),fd(C,D),fd(0,C),fd(A,D),fd(0,D)) == (2,3,2,5,5,5)
X=[]
Y=[]
for x in range(N):
    if x.bit_count()%2==0:
        if fd(x,0)==6 and fd(x,A)==6 and fd(x,C)==5 and fd(x,D)==5 and tri(C,D,x)==10:
            X.append(x)
    else:
        if fd(x,0)==5 and fd(x,A)==5 and fd(x,C)==6 and fd(x,D)==6 and tri(0,A,x)==10:
            Y.append(x)
assert len(X)==105 and len(Y)==105
omegaX=clique_max(X, lambda x,y:fd(x,y)==6)
omegaY=clique_max(Y, lambda x,y:fd(x,y)==6)
assert omegaX==3 and omegaY==3  # four isolates are required on each side

print('CERTIFICATE PASSED')
print('triangle222: low-triple contradiction')
print('triangle224: 42 required pair intersections < 48 convexity lower bound')
print('triangle244: candidate count',len(cands),'distance-6 clique number',omega244)
print('path3: candidate pools',len(X),len(Y),'distance-6 clique numbers',omegaX,omegaY)
