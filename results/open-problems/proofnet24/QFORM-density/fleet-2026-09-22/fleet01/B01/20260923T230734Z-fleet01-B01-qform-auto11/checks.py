import mpmath as mp
import sympy as sp

mp.mp.dps = 50

def Kbeta(beta):
    b = mp.mpf(beta)
    return (2*mp.pi)**b/(mp.gamma(b)*mp.cos(mp.pi*b/2)*b*(1-2*b))

def Jbeta(beta):
    b = mp.mpf(beta)
    j_plus = mp.beta(mp.mpf('0.5'), mp.mpf('0.5')-b) + mp.beta(mp.mpf('0.5')-b, b)
    j_minus = mp.beta(mp.mpf('0.5'), b)
    return j_plus, j_minus, max(j_plus, j_minus)

def Cbeta(beta):
    b = mp.mpf(beta)
    return (Jbeta(b)[2]*Kbeta(b))**(1/(1+2*b))

for b in (mp.mpf(1)/5, mp.mpf(1)/4):
    jp, jm, j = Jbeta(b)
    print('beta=', b)
    print('K_beta=', Kbeta(b))
    print('J_plus=', jp)
    print('J_minus=', jm)
    print('C_two_square=', Cbeta(b))

b = mp.mpf(1)/4
print('partner-family direct bound with M1=sqrt(2)=', Cbeta(b)*2**(mp.mpf(1)/3))
print('threshold example=', Cbeta(b)*(mp.mpf(1)/64)**(-mp.mpf(1)/2)*(mp.mpf(1)/64)**(-mp.mpf(1)/3)*(mp.mpf(1)/4)**(-mp.mpf(1)/6))

lam = sp.symbols('lambda')
eps = sp.Rational(1,2)
A = sp.Matrix([
    [1,0,eps,0],
    [0,1,0,eps],
    [eps,0,eps**2-1,1],
    [0,eps,1,eps**2-1],
])
print('charpoly=', sp.factor(A.charpoly(lam).as_expr()))
print('eigenvalues=', sorted([sp.N(x,20) for x in A.eigenvals().keys()], key=float))

# Direct numerical check of the square-kernel beta integrals at beta=1/4.
# mpmath's direct improper quadrature across an algebraic singularity is
# expected to lose several digits, so this diagnostic uses a 1e-12 threshold.
beta = mp.mpf(1)/4
gamma = beta + mp.mpf(1)/2
for d in (mp.mpf('-3'), mp.mpf('-0.4'), mp.mpf('0.4'), mp.mpf('3')):
    if d < 0:
        integ = mp.quad(lambda u: u**(-mp.mpf('0.5'))*(abs(d)+u)**(-gamma), [0,1, mp.inf])
        rhs = abs(d)**(-beta)*mp.beta(mp.mpf('0.5'), beta)
    else:
        integ = mp.quad(lambda u: u**(-mp.mpf('0.5'))*abs(d-u)**(-gamma), [0,d, mp.inf])
        rhs = d**(-beta)*(mp.beta(mp.mpf('0.5'),mp.mpf('0.5')-beta)+mp.beta(mp.mpf('0.5')-beta,beta))
    rel = abs(integ-rhs)/rhs
    print('d=', d, 'relative_beta_integral_error=', rel)
    assert rel < mp.mpf('1e-12')

assert Cbeta(mp.mpf(1)/4) < mp.mpf('13.185')
assert Cbeta(mp.mpf(1)/5) < mp.mpf('12.392')
print('STATUS=PASS')
