exec(open('computations/C053/check_candidates.py').read().split('for x,r in')[0])
np.seterr(all='raise')
def allocation(K,p,C):
 nu=np.sqrt(p)*(masks.sum(axis=1)-p@masks.sum(axis=1));P=[];ds=[];cs=[]
 for i,j in edges:
  idx=(masks[:,i]+2*masks[:,j]).astype(int);w=np.bincount(idx,weights=p,minlength=4)
  P.append((np.sqrt(p)[:,None]*np.sqrt(p)[None,:])*((idx[:,None]==idx[None,:])/w[idx,None]-1))
  ds.append(2*(1+(w[1]+w[2])/(2*np.sqrt(w[0]*w[3]))));cs.append(C[i,j])
 B0=sum(c/d*pe for c,d,pe in zip(cs,ds,P));B1=np.outer(nu,nu)-sum(pe/d for d,pe in zip(ds,P))
 def f(t):return eigvalsh(B0+t*B1)[-1]
 opt=minimize_scalar(f,bounds=(0,min(cs)),method='bounded',options={'xatol':1e-5})
 return min(opt.fun,f(0),f(min(cs)))
best=None
for it in range(50000):
 base=10**rng.uniform(1,4);x=np.sort(base+np.exp(rng.uniform(-2,3,4)))
 r=np.exp(rng.uniform(0,4,4))*base**rng.uniform(.8,1.3)
 try:e1,e2,K,p,C,_=calc(x,r)
 except (FloatingPointError,np.linalg.LinAlgError):continue
 if e1<-.1 and e2>.2:
  al=allocation(K,p,C)
  if al>1.05:
   score=min(-e1,e2,10*(al-1))
   if best is None or score>best[0]:
    best=(score,x,r,e1,e2,al);print(it,best,flush=True)
    if score>3:break
print('best',best)
