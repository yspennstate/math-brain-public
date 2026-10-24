import sympy as s
r,a,b,c,d=s.symbols('r a b c d')
S=-a*r-a*a*r*r-a**3*r**3+b*r**4+c*r**5+d*r**6
R=s.expand((r*s.diff(S,r,2))**2+4*(r*s.diff(S,r)-S)*(r*s.diff(S,r)-S+s.diff(S,r)**2))
for n in range(2,8):print(n,s.factor(R.coeff(r,n)))
