import math
import numpy as np

q=1.5
c=0.25
gamma=0.20
JMAX=240
A=sum((2.0**((1-q)*j))/(j*j) for j in range(1,JMAX+1))*c
B=sum((2.0**(-q*j))/(j*j) for j in range(1,JMAX+1))*c
p1=1.0-A
p0=A-B
print('A tail mean',A,'B tail prob',B,'p0',p0,'p1',p1,'sum',p0+p1+B)
assert p0>0 and p1>0

def prob_at(d):
    if d==0:return p0
    if d==1:return p1
    if d>0 and (d & (d-1))==0:
        j=int(round(math.log2(d)))
        if j>=1:return c/(j*j*(2.0**(q*j)))
    return 0.0

def offspring_pmf(maxd):
    arr=np.zeros(maxd+1,dtype=float)
    arr[0]=p0
    if maxd>=1:arr[1]=p1
    j=1
    while 2**j<=maxd:
        d=2**j
        arr[d]=prob_at(d)
        j+=1
    return arr

def conv_target(base, reps, maxsum):
    dp=np.array([1.0])
    for _ in range(reps):
        dp=np.convolve(dp,base)[:maxsum+1]
    if len(dp)<maxsum+1:
        dp=np.pad(dp,(0,maxsum+1-len(dp)))
    return dp

def full_power_pmf(base,reps):
    maxd=len(base)-1
    need=reps*maxd+1
    L=1
    while L<need:L*=2
    f=np.fft.rfft(np.pad(base,(0,L-len(base))))
    out=np.fft.irfft(f**reps,n=L)[:need]
    out=np.maximum(out,0.0)
    return out

def Vpi(R):
    val=0.0
    maxd=int(math.floor(R))
    for d in range(maxd+1):
        p=prob_at(d)
        val += d*d*p
    return val

for n in [32,64,128,256]:
    base=offspring_pmf(n-1)
    dpn=conv_target(base,n,n-1)
    a=dpn[n-1]
    dpm1=conv_target(base,n-1,n-1)
    mu=np.zeros(n)
    for d in range(n):
        p=base[d]
        if p and n-1-d>=0:
            mu[d]=p*dpm1[n-1-d]/a
    musum=mu.sum()
    mean=(mu*np.arange(n)).sum()
    kl=0.0
    for d,m in enumerate(mu):
        if m>0:
            kl+=m*math.log(m/base[d])
    x=n*kl
    lam=-math.log(a)
    tc=lam-x
    R=(n/(x+1.0))**gamma
    V=Vpi(R)
    pmf=full_power_pmf(mu,n)
    maxatom=float(pmf.max())
    target=float(pmf[n-1])
    tax=0.5*math.log(n)+0.5*math.log(max(V,1e-300))
    print('\nn',n,'a',a,'lambda',lam)
    print('mu sum',musum,'mean',mean,'expected',1-1/n)
    print('x=nKL',x,'TC exact',tc,'target atom',target,'-log target',-math.log(target))
    print('R',R,'V',V,'maxatom',maxatom,'scaled',maxatom*math.sqrt(n*V) if V>0 else None,'tax no C',tax)
    assert abs(musum-1)<1e-9
    assert abs(mean-(1-1/n))<1e-8
    assert tc+1e-8>=-math.log(target)
