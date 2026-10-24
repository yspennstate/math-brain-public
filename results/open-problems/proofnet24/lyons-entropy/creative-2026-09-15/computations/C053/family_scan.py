exec(open('computations/C053/search_separation.py').read().split('best=None')[0])
x=np.array([200,201,202,208]);r=np.array([600,1600,400,2000]);
for t in [.5,.75,.9,.95,1,1.05,1.1,1.25,1.5,2]:
 e1,e2,K,p,C,data=calc(x,t*r)
 print(t,e1,e2,allocation(K,p,C))
 if t==1:
  print('K=',K,'p=',p,'C=',C,sep='\n');print('eigs',eigvalsh(K))
