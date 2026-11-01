"""Finite entropy tests and periodic Green shell check; not a gas simulation."""
import math,json,pathlib,time
import numpy as np
from scipy.special import erfc
root=pathlib.Path(__file__).resolve().parent
start=time.monotonic()
results=[]
def comps(n,m):
    if m==1:
        yield (n,)
    else:
        for k in range(n+1):
            for rest in comps(n-k,m-1): yield (k,)+rest
N,m=12,3
states=list(comps(N,m))
logP=np.array([math.lgamma(N+1)-sum(math.lgamma(k+1) for k in s)-N*math.log(m) for s in states])
energy=np.array([sum((k-N/m)**2 for k in s)/2 for s in states])
h=N-N*math.log(N)+math.lgamma(N+1)
for beta in [0,.01,.2,2]:
    weights=np.exp(logP-beta*energy)
    Q=weights/weights.sum()
    KL=float(np.sum(Q*(np.log(Q)-logP)))
    marginal=np.array([sum(p for s,p in zip(states,Q) if s[0]==k) for k in range(N+1)])
    logpoi=np.array([-N/m+k*math.log(N/m)-math.lgamma(k+1) for k in range(N+1)])
    cellKL=float(sum(p*(math.log(p)-lp) for p,lp in zip(marginal,logpoi) if p))
    poi=np.exp(logpoi)
    TV=float((np.abs(marginal-poi).sum()+1-poi.sum())/2)
    assert m*cellKL<=KL+h+1e-10
    assert 2*TV**2<=cellKL+1e-10
    assert h<=1+math.log(N)
    results.append(dict(test='canonical spatial entropy',N=N,m=m,beta=beta,labeled_KL=KL,canonical_correction=h,sum_cell_KL=m*cellKL,total_PPP_KL=KL+h,cell_TV=TV))

# d=3 unit-torus mean-zero Green function in the standard Ewald representation.
# G_L(x)=G_1(x/L)/L, alpha=4, real cutoff 2, reciprocal cutoff 6.
alpha=4.
real=np.array([(i,j,k) for i in range(-2,3) for j in range(-2,3) for k in range(-2,3)],dtype=float)
recip=np.array([(i,j,k) for i in range(-6,7) for j in range(-6,7) for k in range(-6,7) if (i,j,k)!=(0,0,0)],dtype=float)
sq=(recip**2).sum(axis=1)
coef=np.exp(-math.pi**2*sq/alpha**2)/(math.pi*sq)
def green(points):
    points=np.atleast_2d(points)
    out=[]
    for j in range(0,len(points),128):
        pts=points[j:j+128]
        distances=np.linalg.norm(pts[:,None,:]+real[None,:,:],axis=2)
        short=(erfc(alpha*distances)/distances).sum(axis=1)
        long=np.cos(2*math.pi*pts@recip.T)@coef
        out.extend(short+long-math.pi/alpha**2)
    return np.array(out)
M=4096
idx=np.arange(M)
z=1-2*(idx+.5)/M
angles=idx*(math.pi*(3-math.sqrt(5)))
omega=np.column_stack((np.sqrt(1-z*z)*np.cos(angles),np.sqrt(1-z*z)*np.sin(angles),z))
L=8.
a=4*math.pi/(6*L**3)
for radius in [.5,1.5,3.]:
    x=np.array([radius,0,0])
    original=float(green(x/L)[0]/L)
    average=float(green((x+omega)/L).mean()/L)
    f=max(1/radius-1,0)
    prediction=original-f+a
    error=average-prediction
    assert abs(error)<3e-5,(radius,error)
    results.append(dict(test='periodic shell identity',L=L,radius=radius,original=original,average=average,predicted=prediction,background_shift=a,error=error))

for n in [10**3,10**6,10**12]:
    q=max(1,int(n**.25))
    v=n/q**3
    results.append(dict(test='localized regime exponents',N=n,beta=n**(-1/3),cell_side=n**(1/3)/q,Debye=n**(1/6),beta_volume=n**(-1/3)*v,conditioning_density=v*(1+math.log(n))/n))

out={'seconds':time.monotonic()-start,'results':results,'status':'all assertions passed','memory':'chunked Ewald arrays; well below 1 GB'}
(root/'second_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2),flush=True)
