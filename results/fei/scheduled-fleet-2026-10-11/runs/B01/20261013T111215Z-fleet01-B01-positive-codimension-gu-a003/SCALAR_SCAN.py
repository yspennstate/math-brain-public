#!/usr/bin/env python3
from functools import lru_cache
from math import comb, log, log2, log1p

LOG2E=1/log(2)

@lru_cache(None)
def U(t,k,h,l):
    assert 0<=h<=t and 0<=l<=k
    delta=2.0**(-t)
    if k==0:
        return float(t)
    eps=2.0**(-k); dust=4*eps*eps
    muc=(1-2*eps)**2
    D=4*eps*(1-2.0**(-l))
    L=0.0
    for j in range(h):
        x=D*2.0**(-(t-j))
        L += comb(h,j)*log1p(-x)*LOG2E
    A=2.0**(t-h)
    E=0.0
    if muc:
        E += muc*log2((A-D)/muc)
    for j in range(l):
        E += comb(l,j)*dust*log2((A-4*eps*(1-2.0**(-j)))/dust)
    for j in range(k+1):
        cnt=comb(k,j)-(comb(l,j) if j<=l else 0)
        if cnt and j<k:
            E += cnt*dust*(k-j)
    return t+delta*(-(t-h)+L+E)

def GI(t,k,h,l):
    p=U(t,k,h,l); g=0.0
    if t:
      for bit,count in [(1,h),(0,t-h)]:
        if not count:continue
        hp=h-bit
        dx=p-(U(t-1,k+1,hp,l)+U(t-1,k+1,hp,l+1))/2
        dy=p-(U(t-1,k,hp,l)+(t-1))/2
        g+=count*(dx+dy)
    if k:
      for bit,count in [(1,l),(0,k-l)]:
        if not count:continue
        lp=l-bit
        dz=p-(U(t,k-1,h,lp)+t)/2
        g+=count*dz
    rare=2.0**(1-t-k)
    I=t+l*(1-rare)+(k-l)*rare
    return g,I,g/I if I else 0

def coords(t,k,h,l):
    p=U(t,k,h,l); ans=[]
    if t:
      for bit,count in [(1,h),(0,t-h)]:
        if count:
          hp=h-bit
          dx=p-(U(t-1,k+1,hp,l)+U(t-1,k+1,hp,l+1))/2
          dy=p-(U(t-1,k,hp,l)+(t-1))/2
          ans += [('x'+str(bit),dx/.5),('y'+str(bit),dy/.5)]
    if k:
      rare=2.0**(1-t-k)
      for bit,count in [(1,l),(0,k-l)]:
        if count:
          lp=l-bit; dz=p-(U(t,k-1,h,lp)+t)/2
          den=(1-rare) if bit else rare
          if den: ans += [('z'+str(bit),dz/den)]
    return ans

def Hspec(t,k):
    if k==0:return 2.0*t
    eps=2.0**(-k); dust=4*eps*eps; muc=(1-2*eps)**2
    hm=0.0
    if muc:hm+=muc*log2(1/muc)
    if dust:hm+=(2**k-1)*dust*log2(1/dust)
    return 2*t+2**(-t)*hm

best=(-1,None); worstslack=(1e99,None)
besth=(-1,None)
bestc=(-1,None)
for t in range(0,25):
  for k in range(0,65):
    if t+k==0:continue
    for h in range(t+1):
      for l in range(k+1):
        g,i,r=GI(t,k,h,l)
        if r>best[0]: best=(r,(t,k,h,l,g,i,U(t,k,h,l)))
        if i and Hspec(t,k)/i>besth[0]:besth=(Hspec(t,k)/i,(t,k,h,l,Hspec(t,k),i))
        for typ,rr in coords(t,k,h,l):
            if rr>bestc[0]:bestc=(rr,(typ,t,k,h,l))
        slack=2.5*i-g
        if slack<worstslack[0]:worstslack=(slack,(t,k,h,l,g,i))
  if t%8==0:print('t',t,'best',best)
print('BEST',best)
print('MINSLACK',worstslack)
print('BEST_HI',besth)
print('BEST_COORD',bestc)
