exec(open('computations/X070/shift_matrix.py').read().split('for name,L in [')[0])
def N(L,s):
 T=L+(1+s)*mp.eye(3);Z=mp.det(T);x=[L[i,i]+s for i in range(3)]
 d=[x[1]*x[2]-abs(L[1,2])**2,x[0]*x[2]-abs(L[0,2])**2,x[0]*x[1]-abs(L[0,1])**2]
 C=mp.diag([mp.log(x[1]*x[2]/d[0]),mp.log(x[0]*x[2]/d[1]),mp.log(x[0]*x[1]/d[2])]);tau=mp.log(mp.fprod(d)/(mp.fprod(x)*mp.det(L+s*mp.eye(3))))
 return (T*C*T+tau*(T*T-T))/Z**2
for a,b,d,c,e in [(1,1,1,.9,.01),(.1,1,10,.2,.1),(1,100,.1,8,.01),(100,1,.1,8,.01),(.1,.1,10,.09,.01)]:
 L=mp.matrix([[a,c,e],[c,b,0],[e,0,d]])
 for k in range(8):
  A=mp.diff(lambda s:N(L,s),0,k)*(-1)**k
  ev,V=mp.eigsy(A)
  if ev[0]<-mp.mpf('1e-20'):print('FAIL',a,b,d,c,e,k,float(ev[0]),[float(V[i,0]) for i in range(3)],flush=True)
print('done')
