exec(open('computations/C053/search_separation.py').read().split('best=None')[0])
for s in [10,20,50,100,200,1000,4000]:
 for factor in [1,2,5,10]:
  x=s+np.array([0,1,2,8]);r=factor*s*np.array([3,8,2,10]);e1,e2,K,p,C,_=calc(x,r)
  if e1<0 and e2>0:
   print('s,f=',s,factor,'eig1,2,alloc=',e1,e2,allocation(K,p,C),flush=True)
