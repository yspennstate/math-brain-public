import sympy as S
r,s,z=S.symbols('r s z',real=True)
N=10
R=sum(r**(2*n+1)*z**(2*n+1)/S.Rational(2*n+1) for n in range(N//2+1))
SS=R.subs(r,s)
D=sum((r*s)**(2*n+1)*z**(4*n+2)/S.Rational(2*n+1) for n in range(N//4+1))
k=sum((r**(2*n)+s**(2*n))*z**(2*n)/S.Rational(2*n)-(r*s)**(2*n)*z**(4*n)/S.Rational(2*n) for n in range(1,N//2+1))
c=1-r*r*s*s*z**4
U=S.Matrix([[4/(1-r*r*z*z)-2*(1-s*s*z*z)/((1-r*r*z*z)*c),2/c-2*k],[2/c-2*k,4/(1-s*s*z*z)-2*(1-r*r*z*z)/((1-s*s*z*z)*c)]])
T=S.Matrix([[R+s*z*D,SS-s*z*k],[R-r*z*k,SS+r*z*D]])
M=U-T*T.T
for i in range(2):
 for j in range(i,2):
  print('ENTRY',i,j)
  x=S.series(M[i,j],z,0,N+1).removeO().expand()
  for n in range(0,N+1,2): print(n,S.factor(x.coeff(z,n)))
