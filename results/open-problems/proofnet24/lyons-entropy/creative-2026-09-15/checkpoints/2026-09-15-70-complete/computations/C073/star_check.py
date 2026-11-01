import itertools, json
import numpy as np
from scipy.integrate import quad

def data(w):
 m=len(w);n=m+1;ms=np.arange(1<<n);S=2*((ms[:,None]>>np.arange(n))&1)-1
 t=-S[:,0,None]*S[:,1:];q=1+t@w;p=q/(1<<n)
 der=np.column_stack([S[:,i]*(p+p[ms^(1<<i)]) for i in range(n)])
 J=der.T@(der/p[:,None]);C=np.zeros_like(J)
 for i in range(n):
  for j in range(i):
   ids=ms[((ms&(1<<i))==0)&((ms&(1<<j))==0)]
   a,b,c,d=(p[ids],p[ids^(1<<i)],p[ids^(1<<j)],p[ids^(1<<i)^(1<<j)])
   C[i,j]=C[j,i]=np.sum((a+b+c+d)*np.log(b*c/(a*d)))
 tt=np.array(list(itertools.product([-1,1],repeat=m)),float);qq=1+tt@w
 AA=np.mean(1/qq);L=np.mean(tt*np.log(qq)[:,None],axis=0)
 G=np.einsum('bi,bj,b->ij',tt,tt,qq*np.log(qq))/len(tt)
 vv=np.r_[1,w];JJ=4*np.diag(np.r_[0,np.ones(m)])+4*AA*np.outer(vv,vv)
 CC=np.zeros((n,n));CC[0,1:]=CC[1:,0]=4*L
 CC[1:,1:]=4*(np.outer(w,L)+np.outer(L,w)-G);np.fill_diagonal(CC,0)
 def integrand(u):
  x=w*u
  logM=-u+np.logaddexp(x,-x).sum()-m*np.log(2)
  M=np.exp(logM);v=np.tanh(x)/u if u else w
  d=w-v;ee=2*w*v-v*v
  R=M*np.outer(np.r_[1,d],np.r_[1,d]);R[0,0]-=np.exp(-u);R[1:,1:]+=M*np.diag(ee)
  return R
 RR=np.zeros((n,n))
 for i in range(n):
  for j in range(n):RR[i,j]=quad(lambda u:integrand(u)[i,j],0,np.inf,epsabs=2e-10)[0]
 return max(np.max(np.abs(J-JJ)),np.max(np.abs(C-CC))),np.max(np.abs((J-C-4*np.eye(n))/4-RR)),np.linalg.eigvalsh(J-C)[0]

rng=np.random.default_rng(730073);results=[]
for m in [1,2,3,4,5,6]:
 for strength in [.2,.8,.98]:
  w=rng.uniform(.01,1,m);w*=strength/w.sum()
  a,b,c=data(w);results.append({'leaves':m,'weights':w.tolist(),'formula_error':a,'integral_error':b,'smallest_J_minus_C':c})
print(json.dumps(results,indent=2))
open('computations/C073/star_check.json','w').write(json.dumps(results,indent=2)+'\n')
assert max(x['formula_error'] for x in results)<1e-10
assert max(x['integral_error'] for x in results)<1e-8
assert min(x['smallest_J_minus_C'] for x in results)>4
