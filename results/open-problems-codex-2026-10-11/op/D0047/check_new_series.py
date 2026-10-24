import sympy as sp,pathlib
r,a,b,d=sp.symbols('r a b d')
PV=lambda S:(r*sp.diff(S,r,2))**2+4*(r*sp.diff(S,r)-S)*(r*sp.diff(S,r)-S+sp.diff(S,r)**2)
print('Initial branch coefficient:',sp.factor(sp.expand(PV(-a*r+b*r*r)).coeff(r,2)))
for n in range(3,11):
 coeffs=sp.symbols('u3:'+str(n+1));S=-a*r-a*a*r*r+sum(coeffs[j-3]*r**j for j in range(3,n+1))
 delta=sp.diff(sp.expand(PV(S+d*r**n)),d).subs(d,0).expand().coeff(r,n)
 assert sp.simplify(delta+4*a*a*(n-1)**2)==0
 print('First-difference coefficient n='+str(n)+':',sp.factor(delta))
# Construct exact formal non-linear branch to order 9.
S=-a*r-a*a*r*r;series=[]
for n in range(3,10):
 t=sp.symbols('t');coef=sp.expand(PV(S+t*r**n)).coeff(r,n);sol=sp.solve(coef,t)[0];S+=sol*r**n;series.append((n,sp.factor(sol)))
print('Sigma coefficients:',series)
F=sp.series(sp.exp(sp.integrate(S/r,r)),r,0,8)
print('Formal gap F(2r)=',F)
pathlib.Path('new_symbolic_checks.txt').write_text('Initial coefficient r^2: '+str(sp.factor(sp.expand(PV(-a*r+b*r*r)).coeff(r,2)))+'\nFirst-difference coefficient checked for n=3,...,10: -4*a^2*(n-1)^2\nSigma coefficients: '+str(series)+'\nFormal gap: '+str(F)+'\n',encoding='utf8')
