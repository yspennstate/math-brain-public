import sympy as sp

K,k,x=sp.symbols('K k x', positive=True, integer=True)
tr=2*x-(K+k+2)
det=(x-1)*(x-(K+1)*(k+1))
disc=sp.factor(tr**2-4*det)
assert sp.expand(disc-((K-k)**2+4*K*k*x))==0

K0=sp.Integer(8); k0=sp.Integer(2); D=K0+k0+2*K0*k0
xx=sp.symbols('xx', real=True)
lamp=xx-sp.Rational(1,2)*(K0+k0+2)+sp.Rational(1,2)*sp.sqrt((K0-k0)**2+4*K0*k0*xx)
lam18=sp.simplify(lamp.subs(xx,18)); lam27=sp.simplify(lamp.subs(xx,27))
gap=sp.simplify(1-lam18/D)
assert lam18==12+3*sp.sqrt(33)
assert lam27==D
assert gap==sp.Rational(10,14)-sp.sqrt(33)/14

# (next type: 0=L,1=R, radial increment, multiplicity)
L=[(0,-2,1),(0,0,1),(0,2,16),(1,-1,8),(1,1,16)]
R=[(0,-1,2),(0,1,16),(1,-2,1),(1,0,7),(1,2,16)]
assert sum(c for _,_,c in L)==42 and sum(c for _,_,c in R)==42

theta=sp.symbols('theta', real=True)
M=sp.Matrix([
    [(sp.exp(-2*theta)+1+16*sp.exp(2*theta))/42,
     (8*sp.exp(-theta)+16*sp.exp(theta))/42],
    [(2*sp.exp(-theta)+16*sp.exp(theta))/42,
     (sp.exp(-2*theta)+7+16*sp.exp(2*theta))/42]
])
M0=sp.simplify(M.subs(theta,0))
T=sp.trace(M); Det=sp.det(M)
lam=sp.simplify((T+sp.sqrt(T**2-4*Det))/2)
assert sp.simplify(lam.subs(theta,0)-1)==0
v=sp.simplify(sp.diff(lam,theta).subs(theta,0))
sigma2=sp.simplify(sp.diff(lam,theta,2).subs(theta,0))
tau2=sp.simplify(sigma2/v**3)
assert v==sp.Rational(145,147)
assert sigma2==sp.Rational(15038,7203)
assert tau2==sp.Rational(6631758,3048625)
pi=sp.Matrix([[sp.Rational(3,7),sp.Rational(4,7)]])
assert sp.simplify(pi*M0-pi)==sp.zeros(1,2)

def mgf_half(row):
    return sp.simplify(sum(sp.Rational(c,42)*sp.Rational(2)**(-d) for _,d,c in row))

mL=mgf_half(L); mR=mgf_half(R)
assert mL==sp.Rational(11,14)
assert mR==sp.Rational(9,14)
assert 16<41

print('P26_T08_LINE_SQUARE_FINITE_RANGE_GREEN_EXACT_PASS')
print('spectral_discriminant=',disc)
print('degree=',D)
print('lambda_plus_18=',lam18)
print('lambda_plus_27=',lam27)
print('spectral_gap_lower=',gap,'~=',float(gap))
print('type_matrix_0=',M0)
print('radial_row_L=',L)
print('radial_row_R=',R)
print('stationary_type=(3/7,4/7)')
print('v=',v)
print('sigma2=',sigma2)
print('tau2=',tau2,'~=',float(tau2))
print('E_2^-Delta_L=',mL)
print('E_2^-Delta_R=',mR)
print('branching_mismatch=16<41')
