exec(open('computations/C053/explore.py').read().split('best=None')[0])
from scipy.optimize import minimize_scalar
for x,r in [(np.array([1,1.01,2,3]),np.array([1,1,1,25])),(np.array([1,1.001,2,3]),np.array([1,1,1,25])),(np.array([2,3.5,3.501,6]),np.array([100,16,16,250])),(np.array([1,1.01,2,3]),np.array([1,1,1,10]))]:
 e1,e2,K,p,C,data=calc(x,r)
 nu=np.sqrt(p)*(masks.sum(axis=1)-p@masks.sum(axis=1));P=[];ds=[];cs=[]
 for i,j in edges:
  idx=(masks[:,i]+2*masks[:,j]).astype(int);w=np.bincount(idx,weights=p,minlength=4)
  pe=(np.sqrt(p)[:,None]*np.sqrt(p)[None,:])*(idx[:,None]==idx[None,:])/w[idx,None]-np.sqrt(p)[:,None]*np.sqrt(p)[None,:]
  P.append(pe);ds.append(2*(1+(w[1]+w[2])/(2*np.sqrt(w[0]*w[3]))));cs.append(C[i,j])
 def f(t):return eigvalsh(t*np.outer(nu,nu)+sum((c-t)/d*pe for c,d,pe in zip(cs,ds,P)))[-1]
 opt=minimize_scalar(f,bounds=(0,min(cs)),method='bounded')
 print('x,r=',x,r,'eig1,2=',e1,e2,'alloc=',opt.fun,'t=',opt.x,'K=',K, 'C_eig=',eigvalsh(C)[-1],sep='\n')
