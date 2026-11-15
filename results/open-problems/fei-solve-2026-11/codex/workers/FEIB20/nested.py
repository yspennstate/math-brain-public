#!/usr/bin/env python3
"""Arbitrary-order resampling moments for the two-level tree DNF. Bits are 0/1."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import sys, math, json, time
import numpy as np
F=np.longdouble

def phi(p,q):
    p,q=max(F(0),p),max(F(0),q)
    if p==0 or q==0:return F(0)
    return (p*np.log1p(q/p)+q*np.log1p(p/q))/np.log(F(2))

class Model:
    def __init__(self,w,D):
        self.w,self.D,self.L=w,D,w-1
        self.M=D*self.L; self.n=1+self.M+self.M*(D-1)*self.L
        self.a=F(2)**(-self.L); self.s=(1-self.a)**(D-1)
        self.EN=(1-(1-self.s)/2)**self.M
        self.EM=((1-(1-self.s)/2)**self.L-(self.s/2)**self.L)**D
        self.meanP=(self.EN+self.EM)/2
    def leaf(self,m,c,l):return 1+self.M+(m*(self.D-1)+c)*self.L+l
    def decode(self,i):
        if i==0:return ('root',)
        if i<=self.M:return ('mate',i-1)
        m,r=divmod(i-1-self.M,(self.D-1)*self.L); c,l=divmod(r,self.L)
        return ('leaf',m,c,l)
    def order(self,kind,seed=20261110):
        mates=list(range(1,1+self.M)); leaves=list(range(1+self.M,self.n))
        if kind=='leaves_first':return [0]+leaves+mates
        if kind=='mates_first':return [0]+mates+leaves
        if kind=='clause':
            return [0]+[v for m in range(self.M) for v in [m+1]+[self.leaf(m,c,l) for c in range(self.D-1) for l in range(self.L)]]
        if kind=='block':
            return [0]+[v for t in range(self.D) for v in [self.leaf(m,c,l) for m in range(t*self.L,(t+1)*self.L) for c in range(self.D-1) for l in range(self.L)]+list(range(1+t*self.L,1+(t+1)*self.L))]
        if kind=='random':return np.random.default_rng(seed).permutation(self.n).tolist()
        if kind=='private_last':
            private=[self.leaf(0,0,l) for l in range(1,self.L)]
            avoid=set(private);return [v for v in self.order('clause') if v not in avoid]+private
        raise ValueError(kind)

class State:
    def __init__(self,T):
        self.T=T; D,L,M=T.D,T.L,T.M
        self.root=False; self.z=np.zeros(M,dtype=bool);self.r=np.zeros((M,D-1),dtype=np.int16)
        self.ss=np.full(M,T.s,dtype=F)
        self.mn=np.full(M,1-(1-T.s)/2,dtype=F)
        self.mb=np.full(M,T.s/2,dtype=F);self.bb=self.mb.copy()
        self.bn=np.full(D,self.mn[0]**L,dtype=F)
        self.bc=np.full(D,self.mb[0]**L,dtype=F);self.bd=self.bc.copy()
        self.prods=np.array([self.bn[0]**D,(self.bn[0]-self.bc[0])**D,(self.bn[0]-2*self.bc[0]+self.bd[0])**D],dtype=F)
    def corr(self):
        a,b,c=self.prods
        pp=(a+2*b+c)/4 if self.root else (a+c)/2
        return 1-4*self.T.meanP+4*pp
    def update(self,i):
        d=self.T.decode(i)
        if d[0]=='root':self.root=True;return
        m=d[1];t=m//self.T.L;T=self.T
        old=np.array([self.bn[t],self.bn[t]-self.bc[t],self.bn[t]-2*self.bc[t]+self.bd[t]],dtype=F)
        if d[0]=='mate':self.z[m]=True
        else:
            c=d[2];r=int(self.r[m,c]);self.r[m,c]+=1
            self.ss[m]*=(1-2*T.a+T.a*F(2)**(-r-1))/(1-2*T.a+T.a*F(2)**(-r))
        zz=F(.25) if self.z[m] else F(.5)
        nn=T.s+zz*(1-2*T.s+self.ss[m]);nb=T.s/2-zz*(T.s-self.ss[m]);bb=zz*self.ss[m]
        self.bn[t]*=nn/self.mn[m];self.bc[t]*=nb/self.mb[m];self.bd[t]*=bb/self.bb[m]
        self.mn[m],self.mb[m],self.bb[m]=nn,nb,bb
        new=np.array([self.bn[t],self.bn[t]-self.bc[t],self.bn[t]-2*self.bc[t]+self.bd[t]],dtype=F)
        self.prods*=new/old

def witness(T,i,order,checks=False):
    a,b=State(T),State(T); b.update(i)
    def wg():
        # C(R)=G(R)+W(R), C(R+i)=G(R).
        g=b.corr();return a.corr()-g,g
    w,g=wg();delta=w;total=F(0);massp=massq=F(0); minstep=F(0)
    for j in reversed(order):
        if j==i:continue
        a.update(j);b.update(j);nw,ng=wg();p,q=g-ng,w-nw
        minstep=min(minstep,p,q);total+=phi(p,q);massp+=p;massq+=q;w,g=nw,ng
    total+=phi(g,w)
    return {'inf':float(delta),'ratio':float(total/delta),'min_step':float(minstep),'mass_error':float(max(abs(massp+g-(1-delta)),abs(massq+w-delta)))}

def fwht(v):
    v=v.astype(float);h=1
    while h<len(v):
        a=v.reshape(-1,2,h); left=a[:,0].copy();right=a[:,1].copy();a[:,0]=left+right;a[:,1]=left-right;h*=2
    return v/len(v)
def spectrum(T):
    xs=np.arange(1<<T.n,dtype=np.uint32);bit=lambda k:((xs>>k)&1).astype(bool)
    root=bit(0);ans=np.zeros(len(xs),bool)
    for t in range(T.D):
        A=np.ones(len(xs),bool)
        for j in range(T.L):
            m=t*T.L+j;z=bit(1+m);A &= z;Q=np.zeros(len(xs),bool)
            for c in range(T.D-1):
                C=np.ones(len(xs),bool)
                for l in range(T.L):C &= bit(T.leaf(m,c,l))
                Q |= C
            ans |= z & Q
        ans |= root & A
    return fwht(1-2*ans.astype(float))**2

def paired(mu,i):
    a=mu.reshape(-1,2,1<<i);return a[:,0].reshape(-1),a[:,1].reshape(-1)
def entropy(p,q):
    s=p+q;out=np.zeros_like(s);ok=(p>0)&(q>0)
    out[ok]=(p[ok]*np.log1p(q[ok]/p[ok])+q[ok]*np.log1p(p[ok]/q[ok]))/math.log(2)
    return float(out.sum())
def spectral_witness(mu,i,order):
    p,q=paired(mu,i); ids=np.arange(len(p),dtype=np.uint32);labels=np.zeros(len(p),np.int16)
    for k,j in enumerate(order):
        if j==i:continue
        b=j if j<i else j-1;labels[(ids&(1<<b))!=0]=k+1
    A=np.bincount(labels,weights=p,minlength=len(order)+1);B=np.bincount(labels,weights=q,minlength=len(order)+1)
    return entropy(A,B)/q.sum()

def validate():
    out=[]
    for w,D in [(3,2),(4,2)]:
        T=Model(w,D);mu=spectrum(T);ids=np.arange(len(mu),dtype=np.uint32);rng=np.random.default_rng(51)
        maxcorr=maxwit=0.
        for _ in range(12):
            R=rng.choice(T.n,size=int(rng.integers(T.n+1)),replace=False);state=State(T);mask=0
            for j in R:state.update(int(j));mask|=1<<int(j)
            maxcorr=max(maxcorr,abs(float(state.corr())-mu[(ids&mask)==0].sum()))
        reps=[0,1,T.leaf(0,0,0)]
        for i in reps:
            for kind in ['leaves_first','mates_first','clause','block','random','private_last']:
                order=T.order(kind);a=witness(T,i,order);b=spectral_witness(mu,i,order);maxwit=max(maxwit,abs(a['ratio']-b))
        row={'w':w,'D':D,'n':T.n,'mass':float(mu.sum()),'max_corr_error':maxcorr,'max_witness_ratio_error':maxwit}
        assert maxcorr<1e-11 and maxwit<1e-9,row
        out.append(row);print(json.dumps(row),flush=True)
    return out

def rows():
    out=[]
    for w,D in [(10,8),(12,16),(14,30),(16,55)]:
        T=Model(w,D)
        for kind in ['leaves_first','mates_first','clause','block','random','private_last']:
            order=T.order(kind)
            for name,i in [('root',0),('mate',1),('leaf',T.leaf(0,0,0))]:
                if kind=='private_last' and name!='leaf':continue
                start=time.time();r={'w':w,'D':D,'n':T.n,'coordinate':name,'order':kind,**witness(T,i,order),'seconds':time.time()-start}
                out.append(r);print(json.dumps(r),flush=True)
        with open('rows.json','w') as f:json.dump(out,f,indent=2)
    return out
if __name__=='__main__':
    if sys.argv[1]=='validate':validate()
    elif sys.argv[1]=='rows':rows()
