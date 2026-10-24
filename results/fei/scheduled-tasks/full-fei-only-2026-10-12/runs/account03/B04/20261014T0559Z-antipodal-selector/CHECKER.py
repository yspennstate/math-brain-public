#!/usr/bin/env python3
"""Account03/B04 synthetic GU two-antipodal selector checker. Stdlib only."""
from math import log2, comb
from fractions import Fraction
checks=0
def ck(x,msg):
 global checks
 checks+=1
 if not x: raise AssertionError(msg)
def fwht(v):
 v=v[:]; n=len(v); s=1
 while s<n:
  for base in range(0,n,2*s):
   for i in range(s):
    a,b=v[base+i],v[base+s+i]
    v[base+i],v[base+s+i]=a+b,a-b
  s*=2
 return v
def stats(v):
 n=len(v).bit_length()-1; N=1<<n; q=[a*a for a in fwht(v)]
 ck(sum(q)==N*N,'parseval')
 pi=q[:]
 for j in range(n):
  bit=1<<j
  for s in range(N):
   if not s&bit: pi[s]+=pi[s|bit]
 ck(pi[0]==N*N,'empty upper')
 U=I=0.
 for s,p in enumerate(q):
  if p:
   ck(pi[s]>=p,'upper>=atom')
   U+=p/(N*N)*log2(pi[s]/p)
   I+=p/(N*N)*s.bit_count()
 return U,I,q
def f(m):
 full=(1<<m)-1; ans=[]
 for v in range(1<<(2*m+1)):
  x=v&full; z=(v>>m)&full; y=(v>>(2*m))&1
  ans.append(-1 if (((x&z).bit_count()&1) ^ (y and x in (0,full))) else 1)
 return ans
def restrict(v,n,j,a):
 mask=(1<<j)-1
 return [v[(i&mask)|((i>>j)<<(j+1))|(a<<j)] for i in range(1<<(n-1))]
def form(m):
 r=m-1; N=1<<r; L=log2(N-1)
 U=m-r/(2*N); I=m+1/N
 Z0=r+(11-3*r)/(4*N)
 Z1=r+(11-3*r+L)/(4*N)+sum(comb(r,k)*log2(1-2**(-(r-k+1))) for k in range(1,r))/N
 D=(Z0+Z1)/2-r
 G=2*m-((m+1)*r)/(2*N)-m*D
 return U,I,Z0,Z1,1-r/(2*N)-D,-r/(2*N),G
for m in range(2,7):
 v=f(m); n=2*m+1; U,I,q=stats(v)
 u,i,z0,z1,dz,dy,g=form(m)
 ck(abs(U-u)<2e-10,'U'); ck(abs(I-i)<2e-10,'I')
 ck(sum(p>0 for p in q)==1<<(2*m),'support size')
 for A in range(1<<m):
  for B in range(1<<m):
   Y=int(B in (0,(1<<m)-1))
   ck(q[A|(B<<m)|(Y<<(2*m))]==1<<(2*m+2),'flat Walsh')
 inc=[]
 for j in range(n):
  v0=stats(restrict(v,n,j,0))[0]
  v1=stats(restrict(v,n,j,1))[0]
  d=U-(v0+v1)/2
  inc.append(d)
  if j<m: ck(abs(d-1)<2e-10,'x')
  elif j<2*m:
   ck(abs(d-dz)<2e-10,'z'); ck(abs(v0-z0)<2e-10,'z0'); ck(abs(v1-z1)<2e-10,'z1')
  else: ck(abs(d-dy)<2e-10,'selector')
 ck(abs(sum(inc)-g)<3e-9,'G')
 ck(g<=2.25*I+1e-12,'9/4')
 print('WALSH m=%d U=%.12g I=%.12g G=%.12g G/I=%.12g'%(m,U,I,g,g/I))
for r in range(1,4):
 ck(Fraction(11-3*r,4*2**r)-Fraction(1,2)*Fraction(3,4)**r >= -Fraction(1,4),'small-r D lower')
for r in range(4,400):
 ck(Fraction(3*r-11,4*2**r)<=Fraction(1,32),'large-r D lower')
ck(Fraction(1,32)+Fraction(81,512)<Fraction(1,4),'global D lower')
ck(Fraction(3,2)**7>17,'power start')
for r in range(7,400):
 m=r+1
 ck(m*(Fraction(3,2)**r-13)+(Fraction(m,2)-2)*r-8>0,'coefficient two')
for m in range(7,15):
 U,I,z0,z1,dz,dy,g=form(m)
 ck(g<2.25*I,'9/4 form')
 if m>=8: ck(g>2*I,'not 2 form')
 print('FORMULA m=%d ratio=%.12g Gminus2I=%.12g'%(m,g/I,g-2*I))
print('PASS assertions=%d failures=0'%(checks))
