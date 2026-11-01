import sympy as sp
import mpmath as mp

# Exact algebraic identity behind the Gaussian normalization.
a, c = sp.symbols('a c', positive=True, real=True)
d = sp.sqrt(1-a**2)
F = ((c-d)**2)/a**2 + (1-c**2)/a
alpha = sp.sqrt(1+a)
beta = sp.sqrt(1-a)
assert sp.simplify(a**2*(1+F) - (alpha-beta*c)**2) == 0

mp.mp.dps = 50

def Fm(a, th):
    d = mp.sqrt(1-a*a)
    return ((mp.cos(th)-d)**2)/(a*a) + (mp.sin(th)**2)/a

def L(s):
    if s == 0:
        return mp.mpf(1)
    return mp.sqrt(mp.pi/(6*s))*mp.erf(mp.sqrt(mp.mpf('1.5')*s))

def R(s):
    return mp.sqrt(1+s)*L(s)

def C(a):
    return 3/(mp.pi*mp.sqrt(a))*mp.quad(lambda th: L(Fm(a, th)), [0, 2*mp.pi])

def gaussian_normalization(a):
    return 3/(mp.pi*mp.sqrt(a))*mp.quad(
        lambda th: 1/mp.sqrt(1+Fm(a, th)), [0, 2*mp.pi]
    )

r1 = R(mp.mpf(1))
uniform_ceiling = (3*mp.sqrt(2)/2)*(1+r1)
print('symbolic_perfect_square=0')
print('R1=', mp.nstr(r1, 30))
print('uniform_ceiling=', mp.nstr(uniform_ceiling, 30))
print('3sqrt2=', mp.nstr(3*mp.sqrt(2), 30))
print('gap=', mp.nstr(3*mp.sqrt(2)-uniform_ceiling, 30))

for av in ['0.01','0.05','0.1','0.2','0.4','0.6','0.8','1']:
    aa = mp.mpf(av)
    cc = C(aa)
    gg = gaussian_normalization(aa)
    print('a', av, 'C', mp.nstr(cc, 20),
          'gauss_identity', mp.nstr(gg, 20),
          'below_uniform_bound', cc < uniform_ceiling)

# The proof that R decreases uses L(s) > (1+s)e^{-3s/2}.
for sv in ['0.001','0.01','0.1','1','10','100']:
    s = mp.mpf(sv)
    margin = L(s) - (1+s)*mp.e**(-mp.mpf('1.5')*s)
    print('s', sv, 'monotonic_margin', mp.nstr(margin, 20))
    assert margin > 0

assert uniform_ceiling < 3*mp.sqrt(2)
print('PASS QFORM_ONE_HEAVY_UNIFORM_GAP')
