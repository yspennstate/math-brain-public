import sympy as S,json
R=S.Rational;I=S.I
nchecks=0
def check(eq):
 global nchecks
 if isinstance(eq,S.MatrixBase): assert all(S.cancel(x)==0 for x in eq)
 else: assert S.cancel(eq)==0
 nchecks+=1

def minor(M,idx):return M.extract(idx,idx)
def atom(K,mask):
 n=K.rows;one=S.eye(n)
 return S.Matrix.hstack(*[(K if mask>>i&1 else one-K)[:,i] for i in range(n)]).det()

examples=[
(S.Matrix([[R(2,5),R(1,10)+I*R(1,20)],[R(1,10)-I*R(1,20),R(3,2)]]),S.Matrix([[R(2,3),1+I],[1-I,-R(2,5)]])),
(S.Matrix([[R(2,5),R(1,10),I*R(3,20)],[R(1,10),2,R(3,5)],[-I*R(3,20),R(3,5),3]]),S.Matrix([[R(1,3),R(2,5)+I*R(1,7),-R(1,5)+I*R(2,7)],[R(2,5)-I*R(1,7),-R(2,3),R(1,4)-I*R(1,6)],[-R(1,5)-I*R(2,7),R(1,4)+I*R(1,6),R(3,4)]]))]
for L,B in examples:
 n=L.rows;s0=R(2,7);Ls=L+s0*S.eye(n);T=S.eye(n)+Ls;RR=T.inv();K=S.eye(n)-RR;A=RR*B*RR
 Z=T.det();g=S.trace(RR*B);h=S.trace((RR*B)**2);BRB=B*RR*B
 t=S.symbols('t');p=[];p1=[];p2=[];w=[];bs=[]
 for mask in range(2**n):
  ids=[i for i in range(n) if mask>>i&1]
  ww=minor(Ls,ids).det() if ids else S.Integer(1)
  if ids:
   inv=minor(Ls,ids).inv();bb=S.trace(inv*minor(B,ids));cc=S.trace((inv*minor(B,ids))**2);dd=S.trace(inv*minor(BRB,ids))
  else:bb=cc=dd=S.Integer(0)
  poly=S.Poly(S.expand(atom(K+t*A,mask)),t)
  pp=poly.nth(0);qq=poly.nth(1);rr=2*poly.nth(2)
  check(pp-ww/Z);check(qq/pp-(bb-g));check(rr/pp-((bb-g)**2-cc+2*dd-h))
  p.append(pp);p1.append(qq);p2.append(rr);w.append(ww);bs.append(bb)
 check(sum(p)-1);check(sum(p1));check(sum(p2))
 check(T*A*T-B);check(2*T*A*T*A*T-2*BRB)
 if n==3:
  logw=S.symbols('l0:8');logw=list(logw);logw[0]=S.Integer(0)
  C=S.diag(logw[2]+logw[4]-logw[6],logw[1]+logw[4]-logw[5],logw[1]+logw[2]-logw[3])
  tau=logw[3]+logw[5]+logw[6]-logw[1]-logw[2]-logw[4]-logw[7]
  FI=sum(q*q/pp for q,pp in zip(p1,p))
  full=FI+sum(pp*ll for pp,ll in zip(p2,logw))
  physical=FI-2*S.trace((T*C*T+tau*(T*T-T))*B.adjugate())/Z**2
  check(S.expand(full-physical))
  fisher=sum(wi*bi**2/Z for wi,bi in zip(w,bs))-g*g
  check(fisher-FI)
  pair=sum(w[i]*w[j]*(bs[i]-bs[j])**2 for i in range(8) for j in range(i))/Z**2
  check(pair-FI)
  x=S.symbols('x');G=S.eye(3)+L
  for j in range(3):
   E=S.zeros(3);E[j,j]=1
   check(x*x*E+x*(G*E+E*G)+G*E*G-(x*S.eye(3)+G)*E*(x*S.eye(3)+G))
  check(x*x*S.eye(3)+x*(2*G-S.eye(3))+G*G-G-((x*S.eye(3)+G)**2-(x*S.eye(3)+G)))

L=S.Matrix([[R(1,10),R(9,100),R(1,100)],[R(9,100),R(1,10),0],[R(1,100),0,10]])
v=S.Matrix([1,-1,-R(1,1100)]);B=I*S.Matrix([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
check(B.adjugate()+v*v.T)
assert [minor(L,list(range(j))).det() for j in range(1,4)]==[R(1,10),R(19,10000),R(1899,100000)];nchecks+=1
x1,x2,x3,c,e=S.symbols('x1 x2 x3 c e');tree=S.Matrix([[x1,c,e],[c,x2,0],[e,0,x3]])
check((x1*x3-e*e)*(x1*x2-c*c)-x1*tree.det()-c*c*e*e)
x=S.symbols('x');check(1/x-1/(x+1)-1/(x+1)**2-1/(x*(x+1)**2))
output={'status':'PASS','exact_assertions':nchecks,'checks':['all normalized physical atom jets','full three-site log-coefficient identity','full Fisher normalization','heat-transform polynomial algebra','rational tree witness','diagonal Laplace calibration']}
open('computations/X070/results.json','w').write(json.dumps(output,indent=2)+'\n')
print(json.dumps(output))
