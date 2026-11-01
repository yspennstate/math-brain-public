#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
from functools import reduce
from math import gcd
from hashlib import sha256
import multiprocessing as mp
import numpy as np

def q(a=0,b=0): return (F(a),F(b))
def qadd(x,y): return (x[0]+y[0],x[1]+y[1])
def qsub(x,y): return (x[0]-y[0],x[1]-y[1])
def qneg(x): return (-x[0],-x[1])
def qmul(x,y): return (x[0]*y[0]+3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qdiv_rat(x,r): return (x[0]/r,x[1]/r)
def vadd(A,B): return (qadd(A[0],B[0]),qadd(A[1],B[1]))
def vsub(A,B): return (qsub(A[0],B[0]),qsub(A[1],B[1]))
def smul(s,A): return (qmul(s,A[0]),qmul(s,A[1]))
def dot(A,B): return qadd(qmul(A[0],B[0]),qmul(A[1],B[1]))
def cross(A,B): return qsub(qmul(A[0],B[1]),qmul(A[1],B[0]))
def norm2(A): return dot(A,A)
def dist2(A,B): return norm2(vsub(A,B))
P=[(q(0),q(0)),(q(0,F(1,2)),q(F(1,2))),(q(0),q(1)),(q(0,-F(1,2)),q(F(1,2))),(q(0,-F(1,2)),q(-F(1,2))),(q(0),q(-1)),(q(0,F(1,2)),q(-F(1,2))),(q(0,1),q(0)),(q(0,F(1,2)),q(F(3,2))),(q(0,1),q(1)),(q(0,1),q(2)),(q(0,F(1,2)),q(F(5,2))),(q(0,F(3,2)),q(F(1,2))),(q(0,F(3,2)),q(-F(1,2)))]
by=defaultdict(list)
for i,j in combinations(range(14),2):
 d=dist2(P[i],P[j]); assert d[1]==0 and d[0].denominator==1; by[d[0]].append((i,j))
assert {k:len(v) for k,v in by.items()}=={F(1):27,F(3):18,F(4):14,F(7):18,F(9):5,F(12):5,F(13):4}

def frame(a,b):
 A,B=P[a],P[b]; u=vsub(B,A); r=norm2(u)[0]
 return tuple((qdiv_rat(dot(vsub(X,A),u),r),qdiv_rat(cross(u,vsub(X,A)),r)) for X in P)
FR={(a,b):frame(a,b) for pairs in by.values() for a,b in pairs}
def trans(a,b,C,D,ori):
 v=vsub(D,C); J=(qneg(v[1]),v[0]); out=[]
 for al,be0 in FR[(a,b)]:
  be=be0 if ori>0 else qneg(be0); out.append(vadd(C,vadd(smul(al,v),smul(be,J))))
 return tuple(out)
# First-generation point union only (all equal-distance seed pair maps)
W=set(P); raw1=0
for dv in sorted(by):
 pairs=by[dv]
 for a,b in pairs:
  for c,d in pairs:
   for cc,dd in ((c,d),(d,c)):
    for ori in (1,-1):
     raw1+=1; W.update(trans(a,b,P[cc],P[dd],ori))
W=sorted(W); assert raw1==6556 and len(W)==505
D3=[(i,j) for i,j in combinations(range(505),2) if dist2(W[i],W[j])==(F(3),F(0))]
assert len(D3)==1702
# fork-shared globals
_GW=W; _D3=D3

def shard(ab):
 a,b=ab; pts=set()
 for c,d in _D3:
  for cc,dd in ((c,d),(d,c)):
   C,D=_GW[cc],_GW[dd]
   for ori in (1,-1): pts.update(trans(a,b,C,D,ori))
 return pts
if __name__=='__main__':
 ctx=mp.get_context('fork')
 with ctx.Pool(processes=min(18, mp.cpu_count())) as pool:
  parts=pool.map(shard, by[F(3)])
 W3=set(W)
 for S in parts: W3.update(S)
 W3=sorted(W3); assert len(W3)==3471
 # every coefficient 3-integral, compute common denominator
 dens=[x.denominator for p in W3 for z in p for x in z]
 assert all(d%3 for d in dens)
 def lcm(a,b): return a//gcd(a,b)*b
 L=reduce(lcm,dens,1); assert L==182
 def sc(p): return tuple(int(v*L) for z in p for v in z)
 A=np.array([sc(p) for p in W3],dtype=np.int64); target=L*L
 def rmod3(x):
  d=x.denominator%3; return (x.numerator%3)*(1 if d==1 else 2)%3
 col=np.array([(rmod3(p[0][0])+rmod3(p[1][0]))%3 for p in W3],dtype=np.int8)
 edges=0; mono=0
 for i in range(len(A)-1):
  D=A[i+1:]-A[i]
  rat=D[:,0]*D[:,0]+3*D[:,1]*D[:,1]+D[:,2]*D[:,2]+3*D[:,3]*D[:,3]
  irr=2*(D[:,0]*D[:,1]+D[:,2]*D[:,3])
  hit=np.flatnonzero((rat==target)&(irr==0)); edges+=len(hit)
  if len(hit): mono+=int(np.sum(col[i+1+hit]==col[i]))
 assert edges==17586 and mono==0
 counts=[int(np.sum(col==c)) for c in range(3)]; assert counts==[1154,1160,1157]
 def fs(x): return f'{x.numerator}/{x.denominator}'
 cert='\n'.join('|'.join(fs(v) for z in p for v in z)+f'|{int(col[i])}' for i,p in enumerate(W3))+'\n'
 print('BASE_DISTANCE_HIST',' '.join(f'{int(k)}:{len(by[k])}' for k in sorted(by)))
 print('FIRST_RAW_ALIGNMENTS',raw1)
 print('FIRST_UNION_VERTICES',len(W))
 print('FIRST_D2_3_TARGET_PAIRS',len(D3))
 print('SECOND_RAW_D3_ALIGNMENTS',len(by[F(3)])*len(D3)*4)
 print('SECOND_UNION_VERTICES',len(W3))
 print('COMMON_DENOMINATOR',L)
 print('COMPLETE_UNIT_EDGES',edges)
 print('THREE_COLOR_COUNTS',*counts)
 print('MONOCHROMATIC_UNIT_EDGES',mono)
 print('POINT_COLOR_CERT_SHA256',sha256(cert.encode()).hexdigest())
 print('ALL_EXACT_D3_CHECKS_PASSED')
