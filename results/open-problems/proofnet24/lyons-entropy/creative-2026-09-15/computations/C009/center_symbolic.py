import sympy as S
x,y,t=S.symbols('x y t',real=True)
R=[S.Matrix(r) for r in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
v=S.Matrix([y,0,x]);J=S.zeros(3);Cd=S.zeros(3)
for r in R:
 w=1-(v.dot(r));d=r-v
 J+=d*d.T/w
 for i in range(3):
  for j in range(3):
   if i!=j:Cd[i,j]+=r[i]*r[j]*(v.dot(r))/w
Jd=J.applyfunc(lambda z:S.factor(x*S.diff(z,x)+y*S.diff(z,y)))
P=(Jd-Cd).applyfunc(S.factor)
print('P entries')
for i in range(3):
 for j in range(i,3): print(i,j,P[i,j])
print('minors')
for inds in [[0,1],[0,2],[1,2],[0,1,2]]:
 print(inds,S.factor(P.extract(inds,inds).det(method='domain-ge')))
open('/workspace/scratch/f042dae27852/creative-lyons-20260915/computations/C009/center_symbolic_repr.txt','w').write(repr(P))

Delta=(1-(x+y)**2)*(1-(x-y)**2)
A=S.Matrix([[x*x,x**3,0],[x**3,x*x+y*y,y**3],[0,y**3,y*y]])
w=S.Matrix([x,1,y]);P_sos=8*A/Delta+64*x*x*y*y*w*w.T/Delta**2
assert all(S.factor(z)==0 for z in P-P_sos)
z1=S.Matrix([1,x,0]);z2=S.Matrix([0,y,1]);e2=S.Matrix([0,1,0])
assert all(S.expand(z)==0 for z in A-x*x*z1*z1.T-y*y*z2*z2.T-(x*x*(1-x*x)+y*y*(1-y*y))*e2*e2.T)
print('Exact symbolic SOS identities: passed')
