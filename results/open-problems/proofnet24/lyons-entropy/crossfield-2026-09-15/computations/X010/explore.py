"""Small deterministic checks of the exterior-martingale bridge, not a proof search."""
import itertools,json
import numpy as np

def basis(n):
 out=[]
 for i in range(n):
  a=np.zeros((n,n),complex);a[i,i]=1;out.append(a)
 for i in range(n):
  for j in range(i+1,n):
   a=np.zeros((n,n),complex);a[i,j]=a[j,i]=1/np.sqrt(2);out.append(a)
   a=np.zeros((n,n),complex);a[i,j]=1j/np.sqrt(2);a[j,i]=-1j/np.sqrt(2);out.append(a)
 return out

def atom_data(K,A):
 n=len(K); I=np.eye(n);bits=np.array(list(itertools.product((0,1),repeat=n)))
 pp=[];aa=[];bb=[]
 for x in bits:
  F=K-np.diag(1-x);inv=np.linalg.inv(F);D=inv@A
  p=(((-1)**sum(1-x))*np.linalg.det(F)).real
  s=np.trace(D).real;t=(s*s-np.trace(D@D)).real
  pp.append(p);aa.append(p*s);bb.append(p*t)
 return bits,np.array(pp),np.array(aa),np.array(bb)

def levels(K,A,order=None, nodes=False):
 n=len(K);order=list(range(n)) if order is None else order
 bits,p,a,b=atom_data(K,A);f=np.log(p);out=np.zeros(n);nd=[]
 for j,k in enumerate(order):
  for h in itertools.product((0,1),repeat=j):
   idx=np.all(bits[:,order[:j]]==h,axis=1) if j else np.ones(len(p),bool)
   z0=idx&(bits[:,k]==0);z1=idx&(bits[:,k]==1)
   w=p[idx].sum();p0=p[z0].sum();p1=p[z1].sum();q=p1/w
   ds=a[z1].sum()/p1-a[z0].sum()/p0
   dt=b[z1].sum()/p1-b[z0].sum()/p0
   df=(p[z1]*f[z1]).sum()/p1-(p[z0]*f[z0]).sum()/p0
   val=w*q*(1-q)*(ds*ds+dt*df)
   out[j]+=val;nd.append((j,h,float(val),float(ds),float(dt),float(df)))
 assert abs(out.sum()-(sum(a*a/p)+sum(b*f)))<1e-8
 return nd if nodes else out

def level_matrix(K,order=None):
 bs=basis(len(K));dim=len(bs);H=np.zeros((len(K),dim,dim))
 d=[levels(K,a,order) for a in bs]
 for i in range(dim):
  H[:,i,i]=d[i]
  for j in range(i):
   H[:,i,j]=H[:,j,i]=(levels(K,bs[i]+bs[j],order)-d[i]-d[j])/2
 return H,bs

if __name__=='__main__':
 matrices={
 'diagonal_two':np.diag([.75,.75]),
 'coherent_two':np.array([[.7,.2],[.2,.3]]),
 'C057_obstruction':np.array([[.5,.1,0],[.1,.22,.1],[0,.1,.8]]),
 'balanced_three':np.array([[.5,.1,.1],[.1,.5,.2],[.1,.2,.5]]),
 'complex_three':np.array([[.31,.12,.09j],[.12,.61,.15],[-.09j,.15,.72]]),
 'complex_four':np.array([[.32,.11,0,.07j],[.11,.61,.08,0],[0,.08,.44,.12],[-.07j,0,.12,.73]])}
 result={}
 for name,K in matrices.items():
  H,bs=level_matrix(K)
  vals=[np.linalg.eigvalsh(h).tolist() for h in H]
  cumulative=[np.linalg.eigvalsh(H[j:].sum(axis=0)).tolist() for j in range(len(K))]
  result[name]={'spectral_margin':float(min(np.linalg.eigvalsh(K).min(),np.linalg.eigvalsh(np.eye(len(K))-K).min())),
   'level_eigenvalues':vals,'suffix_eigenvalues':cumulative}
  print(name,'level minima',[round(x[0],8) for x in vals], 'suffix minima',[round(x[0],8) for x in cumulative])
  if min(x[0] for x in vals)<-1e-8:
   j=min(range(len(K)),key=lambda j:vals[j][0]);v=np.linalg.eigh(H[j])[1][:,0]
   A=sum(x*b for x,b in zip(v,bs));result[name]['negative_direction_real']=A.real.tolist();result[name]['negative_direction_imag']=A.imag.tolist();result[name]['negative_levels']=levels(K,A).tolist()
 print('diagonal nodes:',levels(matrices['diagonal_two'],np.array([[0.,1.],[1.,0.]]),nodes=True))
 with open('crossfield-lyons-20260915/computations/X010/exploration.json','w') as f:json.dump(result,f,indent=2)
