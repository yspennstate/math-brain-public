#!/usr/bin/env python3
from decimal import Decimal, getcontext
from math import comb
getcontext().prec=120
D2=Decimal(2); LN2=D2.ln()
def pw2(n): return D2**n
def lg(x): return x.ln()/LN2

def U(t,k,h,l):
    d=pw2(-t)
    if k==0:return Decimal(t)
    e=pw2(-k); dust=4*e*e; muc=(1-2*e)**2
    D=4*e*(1-pw2(-l)); A=pw2(t-h)
    L=Decimal(0)
    for j in range(h):L+=comb(h,j)*lg(1-D*pw2(-(t-j)))
    E=Decimal(0)
    if muc:E+=muc*lg((A-D)/muc)
    for j in range(l):E+=comb(l,j)*dust*lg((A-4*e*(1-pw2(-j)))/dust)
    for j in range(k+1):
        cnt=comb(k,j)-(comb(l,j) if j<=l else 0)
        if cnt and j<k:E+=cnt*dust*(k-j)
    return t+d*(-(t-h)+L+E)

def z0ratio(t,k,h,l):
    assert l<k
    charge=U(t,k,h,l)-(U(t,k-1,h,l)+t)/2
    inf=pw2(1-t-k)
    return charge/inf

def GI(t,k,h,l):
    p=U(t,k,h,l); g=Decimal(0)
    if t:
      for bit,count in [(1,h),(0,t-h)]:
        if count:
          hp=h-bit
          g+=count*(p-(U(t-1,k+1,hp,l)+U(t-1,k+1,hp,l+1))/2)
          g+=count*(p-(U(t-1,k,hp,l)+Decimal(t-1))/2)
    if k:
      for bit,count in [(1,l),(0,k-l)]:
        if count:
          g+=count*(p-(U(t,k-1,h,l-bit)+Decimal(t))/2)
    rare=pw2(1-t-k)
    inf=Decimal(t)+l*(1-rare)+(k-l)*rare
    return g/inf,g,inf

tests=[]
for t in [1,2,3,4,8,16,32,64,128,256]:
  for k in [2,3,4,8,16,32]:
    for h,l in [(t,k-1),(0,0),(0,k-1),(t,0)]:
      tests.append((z0ratio(t,k,h,l),t,k,h,l))
tests.sort(reverse=True)
for row in tests[:30]:print(str(row[0])[:32],row[1:])
print('TOTALS')
for t in [4,8,16,32,64,128,256]:
  for k in [2,3,4,8]:
    r,g,i=GI(t,k,t,k-1)
    print(t,k,str(r)[:32],str(g)[:32],str(i)[:32])
