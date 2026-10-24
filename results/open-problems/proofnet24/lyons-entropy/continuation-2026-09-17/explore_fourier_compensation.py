"""Explore stronger compensation bounds; floats guide proofs, never certify them."""
import json,time
from pathlib import Path
import numpy as np
from search_shuffle import data

def channel():
    C=np.zeros((16,16));bits=data(4)
    for i,S in enumerate(bits):
        for j,T in enumerate(bits):
            if sum(S)!=sum(T):continue
            k=int(sum(S))
            if k in [0,4]:C[i,j]=1
            elif k in [1,3]:C[i,j]=.25
            else:
                ss=np.where(S)[0];tt=np.where(T)[0]
                so=(ss[1]-ss[0])%2==0;to=(tt[1]-tt[0])%2==0
                C[i,j]=0 if so and to else .25 if so or to else .125
    return C,bits

C,bits=channel();W=np.array([[1,0],[0,1],[-1,0],[0,-1]])

def components(lam):
    inputp=np.prod(np.where(bits,lam,1-lam),axis=1)
    score=(bits-lam)/(lam*(1-lam));d=inputp[:,None]*score
    d2=inputp[:,None,None]*score[:,:,None]*score[:,None,:]
    d2[:,np.arange(4),np.arange(4)]=0
    p=C@inputp;dp=C@d;ddp=(C@d2.reshape(16,16)).reshape(16,4,4)
    fisher=dp.T@(dp/p[:,None]);frozen=np.einsum('s,sij->ij',np.log(p),ddp)
    a=(lam[0]+lam[2])/2;b=(lam[1]+lam[3])/2;x=(lam[0]-lam[2])/2;y=(lam[1]-lam[3])/2
    O=p[5];P=p[3];f=4*P+2*O;delta=2*(x*x+y*y-(a-b)**2);z=delta/(2*f)
    M=np.array([[b*(1-b)+y*y,2*x*y],[2*x*y,a*(1-a)+x*x]])
    df=sum(dp[j] for j in range(16) if sum(bits[j])==2)@W
    diff=np.array([4*x,4*y])-2*z*df
    rank=np.outer(diff,diff)/(8*f*(1+z)*(1-z/2))
    bound=rank+4*np.log(6*O*P*P/(f*p[1]*p[7]))*M-2*np.log1p(-z/2)*np.eye(2)
    return a,b,x,y,delta,W.T@frozen@W,W.T@(fisher+frozen)@W,bound

def main():
    rng=np.random.default_rng(170917);n=30000;results={};start=time.time();neg=0
    for k in range(n):
        lam=rng.uniform(.00001,.99999,4) if k%2 else 1/(1+np.exp(rng.uniform(-11,11,4)))
        a,b,x,y,delta,frozen,full,bound=components(lam)
        if delta>=0:continue
        neg+=1
        for name,Q in [('frozen',frozen),('full',full),('bound',bound)]:
            w,V=np.linalg.eigh(Q)
            if name not in results or w[0]<results[name]['value']:
                results[name]=dict(value=float(w[0]),a=a,b=b,x=x,y=y,Delta=delta,direction=V[:,0].tolist(),lambda_values=lam.tolist())
    out=dict(status='numerical exploration only',generated=n,negative_imbalance=neg,worst=results,elapsed=time.time()-start)
    Path(__file__).with_name('fourier_compensation_exploration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
