# E0024 checks. (1) Random test of the two-sided inequality
#   (a^2+b^2)/(2(1+c^2)) <= a^2+(b+d)^2 <= 2(1+c^2)(a^2+b^2)   whenever |d| <= c a, a>0.
# (2) Independent check on real Levy exponents: X = totally asymmetric 1-d stable (alpha=1.5),
#   Y = spectrally positive 1-d stable (beta=0.7, Kanda-Forst with c = tan(pi*beta/2)),
#   Z = (X,Y), Zs = (X, Y^s). Compute the lambda-energies of a concrete finite measure nu on R^2
#   for both and check the ratio stays in [1/(2(1+c^2)), 2(1+c^2)] for lambda = 1, 10, 100, 1000.
#   The second check does not use the algebra of (1); it evaluates the integrands directly.
import numpy as np, math
rng = np.random.default_rng(7)
worst_lo, worst_hi = 1e9, 0.0
for _ in range(200000):
    a = rng.exponential(3.0) + 1e-9
    b = rng.standard_cauchy() * rng.exponential(5.0)
    c = rng.exponential(2.0)
    d = rng.uniform(-1, 1) * c * a
    lhs, mid, rhs = (a*a + b*b) / (2*(1+c*c)), a*a + (b+d)**2, 2*(1+c*c)*(a*a+b*b)
    worst_lo = min(worst_lo, mid/lhs); worst_hi = max(worst_hi, mid/rhs)
print("random test of the two-sided inequality: min mid/lower =", worst_lo, " max mid/upper =", worst_hi, " (need >=1 and <=1)")

# (2) concrete exponents
alpha, beta = 1.5, 0.7
def psi_X(x):   # totally asymmetric stable, alpha in (1,2): |x|^alpha (1 - i sgn x tan(pi alpha/2)) -- Re>=0
    return np.abs(x)**alpha * (1 - 1j*np.sign(x)*math.tan(math.pi*alpha/2))
tb = math.tan(math.pi*beta/2)
def psi_Y(y):   # spectrally positive stable subordinator-type, beta<1: |y|^beta (1 - i sgn y tan(pi beta/2))
    return np.abs(y)**beta * (1 - 1j*np.sign(y)*tb)
c_kf = tb   # |Im psi_Y| = tb * Re psi_Y <= tb (1+Re psi_Y)
# nu: sum of three point masses in R^2 plus a smooth bump; nu-hat computed exactly.
pts = np.array([[0.0,0.0],[0.3,-0.2],[-0.5,0.7]]); w = np.array([1.0,0.5,0.7]); s = 0.15
def nu_hat(x, y):
    ph = sum(wi*np.exp(1j*(x*p[0]+y*p[1])) for p,wi in zip(pts,w))
    return ph + 0.8*np.exp(-0.5*s*s*(x*x+y*y))     # gaussian bump of width s at the origin
L = 400.0; N = 4001
x = np.linspace(-L, L, N); y = np.linspace(-L, L, N)
X, Y = np.meshgrid(x, y, indexing='ij')
PX, PY = psi_X(X), psi_Y(Y)
NH2 = np.abs(nu_hat(X, Y))**2
dx = x[1]-x[0]
lo, hi = 1/(2*(1+c_kf**2)), 2*(1+c_kf**2)
print("Kanda-Forst constant c =", c_kf, " admissible ratio band [", lo, ",", hi, "]")
for lam in [1.0, 10.0, 100.0, 1000.0]:
    RZ  = np.real(1.0/(lam + PX + PY))
    RZs = np.real(1.0/(lam + PX + np.real(PY)))
    EZ, EZs = (RZ*NH2).sum()*dx*dx, (RZs*NH2).sum()*dx*dx
    ratio_pt = RZ/RZs
    print(f"lambda={lam:7.1f}  E_Z={EZ:.6g}  E_Zs={EZs:.6g}  ratio={EZ/EZs:.4f}  pointwise ratio range [{ratio_pt.min():.4f},{ratio_pt.max():.4f}]")
