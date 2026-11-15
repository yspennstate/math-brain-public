"""Conditional central-moment recursion; long double, checked separately in Decimal."""
from common import log
import argparse, csv, json
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=4000)
a=p.parse_args(); N=a.n
T=np.longdouble
M=np.zeros((N+1,4,4),dtype=T) # index S,C,QC,D=S-C; mean,var,central3,central4
cov=np.zeros(N+1,dtype=T)
h=T(0)
max_mass=T(0)
for n in range(2,N+1):
    h+=T(1)/(n-1)
    i=np.arange(1,n,dtype=T);j=n-i
    q=T(n)/(2*h*i*j)
    max_mass=max(max_mass,abs(np.sum(q)-1))
    toll=np.stack([np.full(n-1,n,dtype=T),abs(n-2*i),(n-2*i)**2,2*np.minimum(i,j)],axis=1)
    left=M[1:n];right=left[::-1]
    mean=left[:,:,0]+right[:,:,0]+toll
    mu=np.sum(q[:,None]*mean,axis=0)
    d=mean-mu
    v=left[:,:,1]+right[:,:,1]
    c3=left[:,:,2]+right[:,:,2]
    M[n,:,0]=mu
    M[n,:,1]=np.sum(q[:,None]*(v+d*d),axis=0)
    M[n,:,2]=np.sum(q[:,None]*(c3+3*d*v+d**3),axis=0)
    M[n,:,3]=np.sum(q[:,None]*(left[:,:,3]+right[:,:,3]+6*left[:,:,1]*right[:,:,1]+4*d*c3+6*d*d*v+d**4),axis=0)
    cov[n]=np.sum(q*(cov[1:n]+cov[1:n][::-1]+d[:,0]*d[:,1]))
    if n in (100,256,500,1000,2000,4000,8000,N):
        rows=[]
        for k,name in enumerate(('S','C','QC','D')):
            mu,v,c3,c4=M[n,k];scale=T(n)**(4 if k==2 else 2)*np.log(T(n))**2
            rows.append({'index':name,'mean':float(mu),'variance':float(v),'variance_scaled':float(v/scale),'skew':float(c3/v**T(1.5)) if v else 0,'kurtosis':float(c4/v**2) if v else 0})
        log('Central recursion n='+str(n)+': '+json.dumps(rows)+', corr(S,C)='+str(float(cov[n]/np.sqrt(M[n,0,1]*M[n,1,1]))))
np.savez('moments.npz',moments=M,covariance_SC=cov)
with open('moments.csv','w') as f:
    w=csv.writer(f);w.writerow(['n','index','mean','variance','central3','central4','skewness','kurtosis'])
    for n in range(2,N+1):
        for k,name in enumerate(('S','C','QC','D')):
            mu,v,c3,c4=M[n,k];w.writerow([n,name,*map(str,(mu,v,c3,c4,c3/v**T(1.5) if v else 0,c4/v**2 if v else 0))])
log('Saved moments.csv and moments.npz; largest split probability mass error '+str(max_mass)+'; longdouble bits='+str(np.finfo(T).nmant))
