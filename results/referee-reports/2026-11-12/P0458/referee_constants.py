"""Direct high precision integration of the normal limit's moments."""
import mpmath as m
m.mp.dps = 60
phi = lambda z: m.exp(-z*z/2)/m.sqrt(2*m.pi)
Phi = lambda z: m.erfc(-z/m.sqrt(2))/2
g = lambda z: phi(z)+z*Phi(z)
e = m.quad(lambda z: g(z)*phi(z),[-m.inf,-2,0,2,m.inf])
e2 = m.quad(lambda z: g(z)**2*phi(z),[-m.inf,-2,0,2,m.inf])
var = e2-e*e
for name,x,target in [('Eg',e,1/m.sqrt(m.pi)),
                      ('Eg2',e2,m.mpf(1)/3+m.sqrt(3)/(2*m.pi)),
                      ('Var',var,m.mpf(1)/3+(m.sqrt(3)-2)/(2*m.pi))]:
    print(name,m.nstr(x,52),'absolute error',m.nstr(abs(x-target),5))
    assert abs(x-target)<m.mpf('1e-50')
print('upper endpoint',m.nstr(e/m.sqrt(var),45))
