#!/usr/bin/env python3
"""Exact finite search for the two path2+disjoint-edge K=3 canonical patterns.

The (2,4)+d2 and (4,4)+d2 patterns are normalized by coordinate symmetry.
The search enforces every exact folded distance and the third-Bonferroni low-triple
budget.  It then exhausts all three even isolates and four odd isolates.

The component searches executed in the originating run returned:
  (2,4): 2210 admissible odd d2 pairs, 328320 even 3-cliques, no completion.
  (4,4):  630 admissible odd d2 pairs,  38880 even 3-cliques, no completion.
"""
N=2048

def fd(x,y):
    w=(x^y).bit_count(); return min(w,12-w)
B=[x for x in range(N) if fd(0,x)<=3]
balls=[]
for c in range(N):
    m=0
    for b in B:m|=1<<(c^b)
    balls.append(m)
def tri(a,b,c):return (balls[a]&balls[b]&balls[c]).bit_count()
def bits(L):
    z=0
    for i in L:z|=1<<i
    return z

def clique_indices(cands,k):
    m=len(cands);adj=[0]*m;out=[]
    for i in range(m):
      for j in range(i+1,m):
        if fd(cands[i],cands[j])==6:
          adj[i]|=1<<j;adj[j]|=1<<i
    def rec(pref,P):
      if len(pref)==k:out.append(tuple(pref));return
      need=k-len(pref)
      while P and P.bit_count()>=need:
        l=P&-P;i=l.bit_length()-1;P-=l
        rec(pref+[i],P&adj[i])
    rec([], (1<<m)-1)
    return out

def odd4_exists(O,budget,a0,b0,c0):
    m=len(O);adj=[0]*m
    for i in range(m):
      for j in range(i+1,m):
        if fd(O[i][0],O[j][0])==6:
          adj[i]|=1<<j;adj[j]|=1<<i
    def rec(ch,P,a,b):
      if ch==4:return True
      if P.bit_count()<4-ch:return False
      while P:
        l=P&-P;i=l.bit_length()-1;P-=l
        na=a+O[i][1];nb=b+O[i][2]
        if budget(na,nb,c0) and rec(ch+1,P&adj[i],na,nb):return True
      return False
    return rec(0,(1<<m)-1,a0,b0)

def run(kind):
    if kind=='24':
      A=bits([0,1]);C=bits([0,1,2,3,4,5]);dA=2
      def budget(a,b,c):return 4*a+b+6*c<=4 and 6*a+3*b+4*c<=8
    else:
      A=bits([0,1,2,3]);C=bits([0,1,2,4,5,6]);dA=4
      def budget(a,b,c):return a+b+6*c<=2 and 3*(a+b)+4*c<=4
    active=[0,A,C]
    assert fd(0,A)==dA and fd(A,C)==4 and fd(0,C)==6
    odd=[]
    for y in range(N):
      if y.bit_count()%2==0:continue
      if fd(y,0)==5 and fd(y,A)==5 and fd(y,C)==5:
        la=0 if tri(0,A,y)==(10 if dA==2 else 4) else 1
        lb=0 if tri(A,C,y)==4 else 1
        odd.append((y,la,lb))
    Ebase=[x for x in range(N) if x.bit_count()%2==0 and x not in active and all(fd(x,e)==6 for e in active)]
    paircount=even3=0
    for i,(u,au,bu) in enumerate(odd):
      for v,av,bv in odd[i+1:]:
        if fd(u,v)!=2:continue
        a0=au+av;b0=bu+bv;c0=sum(tri(u,v,e)!=10 for e in active)
        if not budget(a0,b0,c0):continue
        paircount+=1
        E=[x for x in Ebase if fd(x,u)==5 and fd(x,v)==5 and tri(u,v,x)==10]
        for inds in clique_indices(E,3):
          even3+=1
          es=[E[j] for j in inds]
          O=[(y,aa,bb) for y,aa,bb in odd if y not in (u,v) and fd(y,u)==6 and fd(y,v)==6 and all(fd(y,e)==5 for e in es) and budget(a0+aa,b0+bb,c0)]
          if len(O)>=4 and odd4_exists(O,budget,a0,b0,c0):
            return False,(paircount,even3)
    return True,(paircount,even3)

r24,s24=run('24')
r44,s44=run('44')
assert r24 and r44
print('CERTIFICATE PASSED')
print('(2,4)+d2:',s24)
print('(4,4)+d2:',s44)
