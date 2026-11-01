"""Section 12/14 scalar facts, checked independently (agent J). nu from the shaped ReLU directly:
sigma(x) = s+ x^+ + s- x^-, s+- = 1 + c+-/sqrt(n); the normalised kernel is rho + nu(rho)/n + O(n^-3/2)."""
import mpmath as mp
mp.mp.dps = 40
def nu(r, D=1): return D/(2*mp.pi)*(mp.sqrt(1-r*r) - r*mp.acos(r))
def relu_kernel(r):  # E[relu(g_a) relu(g_b)], unit variances, correlation r (closed form, Cho-Saul)
    return (mp.sqrt(1-r*r) + (mp.pi - mp.acos(r))*r)/(2*mp.pi)
# (1) nu from the shaped ReLU: n -> inf limit of n * (normalised kernel - rho)
cp, cm = mp.mpf('0.7'), mp.mpf('-1.3'); worst = 0
for r in [mp.mpf(x)/10 for x in range(-9, 10)]:
    n = mp.mpf(10)**16; sp, sm = 1+cp/mp.sqrt(n), 1+cm/mp.sqrt(n); e = sp - sm
    num = sm**2*r + 2*sm*e*r/2 + e**2*relu_kernel(r)
    den = sm**2 + sm*e + e**2/2
    lim = n*(num/den - r)
    worst = max(worst, abs(lim - nu(r, (cp-cm)**2)))
print("nu from the shaped ReLU, max gap", mp.nstr(worst, 3))
# (2) pi (k1 - rho) identity, k1 = 2 E relu relu
print("k1 identity gap", mp.nstr(max(abs(mp.pi*(2*relu_kernel(r) - r) - (mp.sqrt(1-r*r) - r*mp.acos(r))) for r in mp.linspace(-1, 1, 201)), 3))
# (3) nu >= 0 and max nu/(Delta (1 - rho)) = 1/4 at rho = -1
g = lambda r: nu(r)/(1-r)
pts = mp.linspace(-1, mp.mpf(1)-mp.mpf(10)**-12, 20001)
print("min nu", mp.nstr(min(nu(r) for r in pts), 3), "max nu/(1-rho)", mp.nstr(max(g(r) for r in pts), 12), "at -1:", mp.nstr(g(-1), 12))
print("d/drho of nu/(1-rho) on (-1,1) max", mp.nstr(max(mp.diff(g, r) for r in mp.linspace(-0.999, 0.999, 2001)), 4))
