import numpy as np, json

def fwht(a):
 a=a.copy()
 if a.ndim==1:a=a[None,:]
 N=a.shape[1]
 for i in range(N.bit_length()-1):
  r=a.reshape(len(a),-1,2<<i);u=r[:,:,:1<<i].copy();v=r[:,:,1<<i:].copy();r[:,:,:1<<i]=u+v;r[:,:,1<<i:]=u-v
 return a

def degrees(a):
 a=a.astype(np.int64).copy()
 if a.ndim==1:a=a[None,:]
 N=a.shape[1]
 for i in range(N.bit_length()-1):
  r=a.reshape(len(a),-1,2<<i);r[:,:,1<<i:]^=r[:,:,:1<<i]
 wt=np.array([x.bit_count() for x in range(N)])
 return np.max(np.where(a!=0,wt[None,:],-1),axis=1)

out={}
for n in range(1,5):
 N=1<<n; tt=1-2*((np.arange(1<<N,dtype=np.int64)[:,None]>>np.arange(N)[None,:])&1)
 W=fwht(tt); absw=abs(W); good=np.all((absw&(absw-1))==0,axis=1); W=W[good];absw=absw[good]
 degs={str(r):dict(zip(*[l.tolist() for l in np.unique(degrees(absw==(1<<r)),return_counts=True)])) for r in range(n+1)}
 dcell=[];bad=[]
 for r in range(n):
  ind=absw==(1<<r);ds=degrees(ind);non=ds>=0
  # does exact level polynomial have degree <= r-1? 
  ids=np.flatnonzero(non & (ds>r-1))
  if len(ids):bad.append({'r':r,'bad':len(ids),'W':W[ids[0]].tolist(),'degree':int(ds[ids[0]])})
 p=W.astype(float)**2/N**2; I=p@np.array([x.bit_count() for x in range(N)]); H=-np.sum(p*np.log2(np.maximum(p,1e-100)),axis=1)
 out[n]={'count':len(W),'max_ratio':float(np.max(H/np.maximum(I,1e-100))),'level_degrees':degs,'bad':bad}
print(json.dumps(out,indent=2))
