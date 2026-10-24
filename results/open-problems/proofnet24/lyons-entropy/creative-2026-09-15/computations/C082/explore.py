import numpy as np
from itertools import product
rng=np.random.default_rng(8209)

def scalar(t,r,z):
    # r indices complement the site: (23,13,12).
    u=1-r*r
    D=1-np.sum(r*r)+2*np.prod(r)*z
    if D<=0:return None
    Z=1+np.sum(t)+np.dot(u,np.array([t[1]*t[2],t[0]*t[2],t[0]*t[1]]))+np.prod(t)*D
    k=np.zeros(3); minors=np.zeros(3); w=np.zeros(3)
    for i in range(3):
        j,h=[a for a in range(3) if a!=i]
        k[i]=t[i]*(1+t[j]*u[h]+t[h]*u[j]+t[j]*t[h]*D)/Z
        minors[i]=t[j]*t[h]*(u[i]+t[i]*D)/Z
        w[i]=t[j]*t[h]*(r[i]**2*(1+t[i])**2+t[i]**2*r[j]**2*r[h]**2-2*t[i]*(1+t[i])*np.prod(r)*z)/Z**2
    c=-np.log(u); tau=np.log(np.prod(u)/D)
    d=c+tau*k
    de=np.prod(c)+tau*(c[0]*c[1]*k[2]+c[0]*c[2]*k[1]+c[1]*c[2]*k[0])+tau*tau*np.dot(c,minors)+tau**3*np.prod(t)*D/Z
    T=de*np.sum(k*(1-k)/d**2)+2*(tau*tau-de)*sum(w[i]/(d[(i+1)%3]*d[(i+2)%3]) for i in range(3))
    tr=sum(d); tr2=sum(d*d)+2*tau*tau*sum(w)
    v=sum(k*(1-k))-2*sum(w)
    count=tr*tr-2*tr2-2*v*de
    C=np.diag(d*d+de*k*(1-k))
    for i in range(3):
        j,h=[a for a in range(3) if a!=i]
        C[j,h]=C[h,j]=(tau*tau-de)*w[i]
    optimal=float(d@np.linalg.solve(C,d))
    return T,optimal,count,tau,min(d)

for lo,hi in [(.1,.2),(.15,.45),(.2,.4),(.2,.5),(.25,.5),(.1,.45),(.15,.5),(.2,.55),(.2,.6),(.3,.6)]:
    worst=(-1,None); opt=(10,None); bad=0
    samples=list(product([.5,2],repeat=3))
    rs=list(product([lo,hi],repeat=3))
    vals=[(np.array(t),np.array(r),z) for t in samples for r in rs for z in [-1,0,1]]
    vals += [(np.exp(rng.uniform(np.log(.5),np.log(2),3)),rng.uniform(lo,hi,3),rng.uniform(-1,1)) for _ in range(5000)]
    for t,r,z in vals:
        res=scalar(t,r,z)
        if res is None:bad+=1;continue
        T,o,*_=res
        if T>worst[0]:worst=(T,(t,r,z,res))
        if o<opt[0]:opt=(o,(t,r,z,res))
    print(lo,hi,'worst T',worst,'min optimal',opt,'invalid',bad,flush=True)
