from math import comb
import sympy as sp

# Exact symbolic certificate for the R7-04 arbitrary positive three-point theorem.
# All arithmetic is exact over QQ.  The only finite positivity step is a tensor
# Bernstein certificate on [0,1]^4 for the last one-hill far-tail topology.

# ---------------------------------------------------------------------------
# Generic normalized three-point law
# X in {1, 1+s, 1+s+d}, masses p,q,r, p+q+r=1.
# ---------------------------------------------------------------------------
p, q, r, s, d, lam = sp.symbols('p q r s d lam', positive=True)
t = q + r
b = 1 + s
mu = 1 + t*s
m = mu + r*d
H = s + r*d/t
h0 = 1/p
h = mu/(1-r)
d0 = t*(1-p*s)/(p*r)
d1 = s*t/q
Delta = q - p*s*t
alpha = 1-lam
beta = 1-lam*mu
V = p + t*b**2
M2 = p + q*b**2 + r*(b+d)**2
rho = lam*m

mass = {p: 1-q-r}

# Threshold ordering identities.
assert sp.factor(((h-h0) + Delta/(p*(1-r))).subs(mass)) == 0
assert sp.factor(((h-d1) - Delta/(q*(1-r))).subs(mass)) == 0
assert sp.factor(((d0-h0) - Delta/(p*r)).subs(mass)) == 0
assert sp.factor(((d0-h) - Delta/(p*r*(1-r))).subs(mass)) == 0
print('THRESHOLD_IDENTITIES_PASS')

# ---------------------------------------------------------------------------
# Internal-switch topology Delta<0, d0<d<=d1.
# Exact cross-valley prefix charge, split at fresh-contact d=h0.
# ---------------------------------------------------------------------------
ell0 = h0 - r*d/t
z = q*d/t
C0L = 1 + q*ell0**2 + r*(h0+z)**2
TM1 = 1 + lam/(2*alpha)
TG1L = 1 + lam*C0L/(2*alpha)
DshortL = TM1-TG1L
DbL = lam*ell0/alpha
DcL = lam*(d+ell0)/alpha
DL = sp.factor((p*DshortL + q*DbL + r*DcL).subs(mass))
targetL = sp.factor((lam*(t**2-p**2*q*r*d**2)/(2*t*p*alpha)).subs(mass))
assert sp.factor(DL-targetL) == 0

ell = q/(p*t)
C0U = 1 + t*ell**2 + r*h0**2
TG1U = 1 + lam*C0U/(2*alpha)
DshortU = TM1-TG1U
DbU = lam*ell/alpha
DcU = lam*h0/alpha
DU = sp.factor((p*DshortU + q*DbU + r*DcU).subs(mass))
targetU = sp.factor((lam*(t**2-q*r)/(2*t*p*alpha)).subs(mass))
assert sp.factor(DU-targetU) == 0
print('INTERNAL_SWITCH_PREFIX_CHARGE_PASS')

# ---------------------------------------------------------------------------
# Terminal-only topology Delta>=0, h<d<=d0.
# ---------------------------------------------------------------------------
Wh = lam*(V+r*h**2)/(2*beta)
D_terminal = sp.factor(((p+q)*(-lam*r*h**2/(2*beta)) + r*lam*mu*h/beta).subs(mass))
target_terminal = sp.factor((lam*r*mu**2/(2*(1-r)*beta)).subs(mass))
assert sp.factor(D_terminal-target_terminal) == 0
print('TERMINAL_ONLY_GAP_PASS')

# ---------------------------------------------------------------------------
# Two-hill far-tail topology Delta<0, d>d1.
# ---------------------------------------------------------------------------
ell = q/(p*t)
h1 = s*t/q
TG1wait = lam*(1+t*ell**2+r*h0**2)/(2*alpha)
D1 = lam/(2*alpha)-TG1wait
Db = lam*ell/alpha - lam*r*h1**2/(2*alpha*beta)
Dc = lam/alpha*(h1*t*s/beta + h0)
D_twohill = sp.factor((p*D1+q*Db+r*Dc).subs(mass))
target_twohill = sp.factor((lam/(2*alpha)*((q**2+r*t)/(p*t) + r*s**2*t**2/(q*beta))).subs(mass))
assert sp.factor(D_twohill-target_twohill) == 0
print('TWO_HILL_GAP_PASS')

# ---------------------------------------------------------------------------
# One-hill far-tail topology Delta>=0, d>d0.
# D is independent of d and factor-two slack increases with d.
# ---------------------------------------------------------------------------
D_onehill = sp.simplify(
    p*(lam/(2*alpha)-Wh)
    + q*(b*lam/alpha + lam*V/(2*alpha*beta)-Wh)
    + r*(lam*mu*h/beta)
)
assert sp.diff(D_onehill, d) == 0

Winf = lam*M2/(2*(1-rho)*beta)
EG_onehill = p*(1+Wh) + q*(b+Wh) + r*(Winf+(b+d-h)/beta+h)
dEG = sp.simplify(sp.diff(EG_onehill, d))
positive_derivative = r*(
    lam/(2*beta)*(2*r*(b+d)/(1-rho) + lam*r*M2/(1-rho)**2)
    + 1/beta
)
assert sp.factor(dEG-positive_derivative) == 0
print('ONE_HILL_TAIL_CANCELLATION_AND_MONOTONICITY_PASS')

# ---------------------------------------------------------------------------
# Exact factor-two boundary certificate for the one-hill far-tail topology.
# Delta>=0 is parametrized by
#   p=1-T, r=T*VV, q=T*(1-VV), s=U*(1-VV)/(1-T), 0<T,VV,U<1,
# so U<=1 is exactly q-p*s*t>=0.  Put lam=X*p and d=d0.
# Then rho=X at the boundary.
# ---------------------------------------------------------------------------
T, VV, U, X = sp.symbols('T VV U X', nonnegative=True)
Pp = 1-T
R = T*VV
Q = T*(1-VV)
S = U*(1-VV)/(1-T)
B = 1+S
MU = 1+T*S
D0 = (1-U*(1-VV))/((1-T)*VV)
C = B+D0
LAM = X*Pp
ALPHA = 1-LAM
BETA = 1-LAM*MU
RHO = sp.factor(LAM*(MU+R*D0))
assert sp.factor(RHO-X) == 0
V2 = sp.expand(Pp+T*B**2)
M22 = sp.expand(Pp+Q*B**2+R*C**2)
HH = sp.simplify(MU/(1-R))
WH = sp.simplify(LAM*(V2+R*HH**2)/(2*BETA))
WINF = sp.simplify(LAM*M22/(2*(1-RHO)*BETA))
EG = sp.simplify(Pp*(1+WH) + Q*(B+WH) + R*(WINF+(C-HH)/BETA+HH))
DGAP = sp.simplify(
    Pp*(LAM/(2*ALPHA)-WH)
    + Q*(B*LAM/ALPHA + LAM*V2/(2*ALPHA*BETA)-WH)
    + R*(LAM*MU*HH/BETA)
)
F = sp.factor(sp.together(EG-DGAP))
num, den = sp.fraction(F)
Ppoly = sp.expand(-num)
denpos = sp.factor(-den)
expected_den = sp.factor(
    2*(1-T)*(1-X)*(1-T*VV)*(1-X*(1-T))*(1-X*MU*(1-T))
)
assert sp.factor(denpos-expected_den) == 0

degrees = sp.Poly(Ppoly, T, VV, U, X).degree_list()
assert degrees == (5,4,2,3)
poly = sp.Poly(Ppoly, T, VV, U, X)
terms = poly.terms()
bern = {}
for k0 in range(degrees[0]+1):
    for k1 in range(degrees[1]+1):
        for k2 in range(degrees[2]+1):
            for k3 in range(degrees[3]+1):
                ks = (k0,k1,k2,k3)
                val = sp.Rational(0)
                for exps, coef in terms:
                    if all(exps[j] <= ks[j] for j in range(4)):
                        fac = sp.Rational(1)
                        for j in range(4):
                            fac *= sp.Rational(comb(ks[j],exps[j]), comb(degrees[j],exps[j]))
                        val += coef*fac
                bern[ks] = sp.factor(val)
negative = [(k,z) for k,z in bern.items() if z < 0]
zero = [(k,z) for k,z in bern.items() if z == 0]
positive = [(k,z) for k,z in bern.items() if z > 0]
assert not negative
assert positive

print('ONE_HILL_BOUNDARY_DEGREES', degrees)
print('ONE_HILL_BOUNDARY_BERNSTEIN_TOTAL', len(bern))
print('ONE_HILL_BOUNDARY_BERNSTEIN_POSITIVE', len(positive))
print('ONE_HILL_BOUNDARY_BERNSTEIN_ZERO', len(zero))
print('ONE_HILL_BOUNDARY_BERNSTEIN_NEGATIVE', len(negative))
print('ONE_HILL_BOUNDARY_SMALLEST_POSITIVE', min(z for _,z in positive))
print('ALL_EXACT_CHECKS_PASS')
