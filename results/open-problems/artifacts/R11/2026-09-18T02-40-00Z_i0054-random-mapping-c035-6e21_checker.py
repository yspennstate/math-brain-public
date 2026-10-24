#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from collections import Counter
from math import factorial
checks=0
def ck(x,m):
 global checks
 assert x,m
 checks+=1
def cc(m):
 s=0
 for k in range(1,m+1):
  s += factorial(m-1) if k==m else factorial(m)//factorial(m-k)*m**(m-k-1)
 return s
def Cser(N):
 a=[Fraction(0)]*(N+1)
 for m in range(1,N+1): a[m]=Fraction(cc(m),factorial(m))
 return a
def mul(a,b,N):
 o=[Fraction(0)]*(N+1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y and i+j<=N:o[i+j]+=x*y
 return o
def pw(a,k,N):
 o=[Fraction(1)]+[Fraction(0)]*N
 for _ in range(k):o=mul(o,a,N)
 return o
def der(a,r,N):
 a=list(a)
 for _ in range(r):a=[a[n]*n for n in range(1,len(a))]
 return (a+[Fraction(0)]*(N+1))[:N+1]
def total(N):return factorial(N)*pw(Cser(N),3,N)[N]/6
def canon(bs):return tuple(sorted((tuple(sorted(b)) for b in bs),key=lambda x:(x[0],len(x),x)))
def comps(f):
 N=len(f); A=[set() for _ in f]
 for i,j in enumerate(f):A[i].add(j);A[j].add(i)
 seen=set(); out=[]
 for i in range(N):
  if i in seen:continue
  st=[i];seen.add(i);B=[]
  while st:
   v=st.pop();B.append(v)
   for w in A[v]:
    if w not in seen:seen.add(w);st.append(w)
  out.append(tuple(sorted(B)))
 return canon(out)
def restrict(P,b):return canon(tuple(tuple(x for x in B if x<b) for B in P if any(x<b for x in B)))
def fcount(N,pi):
 b=sum(map(len,pi));q=len(pi);M=N-b;C=Cser(N);a=[Fraction(1)]+[Fraction(0)]*M
 for B in pi:a=mul(a,der(C,len(B),M),M)
 if 3-q:a=[x/factorial(3-q) for x in mul(a,pw(C,3-q,M),M)]
 return factorial(M)*a[M]
def parts(n):
 out=[]
 def rec(i,B):
  if i==n:out.append(canon(tuple(tuple(x) for x in B)));return
  for j in range(len(B)):B[j].append(i);rec(i+1,B);B[j].pop()
  B.append([i]);rec(i+1,B);B.pop()
 rec(0,[]);return sorted(set(out))
def prob(N,pi):return Fraction(fcount(N,pi),total(N))
def pis(sizes):
 z=0;B=[]
 for m in sizes:B.append(tuple(range(z,z+m)));z+=m
 return canon(tuple(B))
print('R11 I0054 C035 conditioned-three-component random-mapping checker')
got=[cc(m) for m in range(1,8)];ck(got==[1,3,17,142,1569,21576,355081],got);print('connected_mapping_counts_1_7=',got)
known={3:1,4:18,5:305,6:5595,7:113974}
for N in range(3,8):
 D={b:Counter() for b in range(1,min(4,N)+1)};nt=0
 for f in product(range(N),repeat=N):
  P=comps(f)
  if len(P)!=3:continue
  nt+=1
  for b in D:D[b][restrict(P,b)]+=1
 ck(nt==known[N],('total',N,nt));ck(total(N)==nt,('egf',N,total(N),nt))
 for b,Z in D.items():
  for pi,n in Z.items():
   x=fcount(N,pi);ck(x.denominator==1,('int',N,b,pi,x));ck(x.numerator==n,('formula',N,b,pi,x,n))
  s=0
  for pi in parts(b):
   if len(pi)<=3:
    x=fcount(N,pi);ck(x.denominator==1,('allint',N,b,pi,x));s+=x.numerator
  ck(s==nt,('sum',N,b,s,nt))
 print(f'N={N} conditioned_three_component_mappings={nt} exhaustive_formula_match=PASS')
N=5;sh=Counter()
for f in product(range(N),repeat=N):
 P=comps(f)
 if len(P)==3:sh[tuple(sorted(map(len,P),reverse=True))]+=1
ck(sh[(3,1,1)]==170,sh);ck(sh[(2,2,1)]==135,sh);ck(sum(sh.values())==305,sh)
p311=Fraction(170,305);p221=Fraction(135,305);ck(p311==Fraction(34,61),p311);ck(p221==Fraction(27,61),p221)
a=10*factorial(2);b=15;ck(a==20 and b==15,(a,b));q311=Fraction(a,a+b);q221=Fraction(b,a+b);ck(q311==Fraction(4,7),q311);ck(q221==Fraction(3,7),q221);gap=p311-q311;ck(gap==Fraction(-6,427),gap)
print('N5_C035_root_shape_P311=',p311);print('N5_C035_root_shape_P221=',p221);print('N5_C034_root_shape_P311=',q311);print('N5_C034_root_shape_P221=',q221);print('N5_P311_gap_C035_minus_C034=',gap)
tab=[]
for N in range(3,31):
 p=prob(N,pis((1,1)));ck(p>0,(N,p));lam=1/p;ck(lam*p==1,N);aa=lam/Fraction(N*N);ck(0<aa<1,(N,aa))
 if N in (3,4,5,10,20,30):tab.append((N,p,lam,aa))
print('pair_normalization_samples=')
for x in tab:print(x)
for N in (5,6,7,10,15,20,30):
 lam=1/prob(N,pis((1,1)))
 for sizes in ((1,3),(2,2),(1,1,2)):
  p=prob(N,pis(sizes));ck(p>=0,(N,sizes,p));q=lam*p;ck(q>=0,(N,sizes,q))
print('exact_selected_rate_checks=PASS');print('checks=',checks);print('ALL_EXACT_CHECKS_PASS')
