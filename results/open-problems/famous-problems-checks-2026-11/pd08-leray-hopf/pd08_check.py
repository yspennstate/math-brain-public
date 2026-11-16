# PD08: two independent checks on Hou-Wang-Yang, arXiv 2509.25116v2.
#  A. Section 4.5: the chain of inequalities that closes Propositions 1 and 2, recomputed from the
#     constants printed in (4.44)-(4.63). Each printed step is tested; then the chain is rerun with
#     the worst reading of every step that did not reproduce.
#  B. Section 6.2: the number of eigenvalues below 10 of the divergence-free Laplacian on the ball of
#     radius 32, by parity class, from the Bessel equations (6.3) and (6.4) of Lemma 4, against the
#     paper's N = 1257 (profile U) and N = 1260 (eigenfunction v).
import math
import numpy as np
from scipy.special import jv, jvp

out = []
def say(s=""):
    print(s, flush=True)
    out.append(s)

fails = 0
def step(name, value, printed, kind):
    # kind "le": the paper prints value <= printed ; "ge": value >= printed
    global fails
    ok = value <= printed * (1 + 1e-12) if kind == "le" else value >= printed * (1 - 1e-12)
    if not ok:
        fails += 1
    say(f"  {'ok  ' if ok else 'FAIL'} {name}: recomputed {value:.6g}, printed {'<=' if kind == 'le' else '>='} {printed:g}")
    return ok

say("A. Section 4.5, printed constants")
epsU, eta1, eta2, lamQ = 6.5e-7, 0.199, 0.005, 4.5
K5, K6, eps3, eps4 = 0.47, 0.46, 5.3e-5, 5.3e-5
K7U, GU, SgradU, SquadU, SphiU = 0.0012, 0.025, 1.33, 0.12, 0.36
epsv, lam, vinf, gvinf, K4 = 1.9e-5, 0.113, 2.52, 3.4, 0.091
K7v, Gv, Sphiv, M0in = 0.004, 0.029, 1.02, 6.38

M1 = K5 + K6 / (1 - eps4) ** 2
step("M1 (U and v)", M1, 0.9301, "le")
M2U = eta2 * 0.9301 + eps3 * lamQ + K7U
step("M2U", M2U, 0.0061, "le")
M3U = math.sqrt(GU) * SgradU + GU * SquadU
step("M3U", M3U, 0.22, "le")
cU = 0.25 - eta1 - 0.0061
M4U = cU ** 2 - 4 * 0.22 * epsU
step("M4U", M4U, 0.002, "ge")
x0U = 2 * epsU / (cU + math.sqrt(0.002))
okx0 = step("x0U (with M2U <= 0.0061)", x0U, 1.44e-5, "le")
x0U_paper = 2 * epsU / (0.25 - 0.199 - 0.005 + math.sqrt(0.002))
say(f"       the printed line uses 0.005 in place of 0.0061: that gives {x0U_paper:.6g}")
x1U = math.sqrt((0.25 - eta1) / (1 - 0.9301)) * 1.44e-5 / 2
step("x1U (from the printed x0U)", x1U, 6.2e-6, "le")
y0U = 1.44e-5 * GU * SphiU
step("y0U as printed (first power of the Gram norm)", y0U, 1.3e-7, "le")
y1U = 1.44e-5 * GU * SgradU
step("y1U as printed (first power of the Gram norm)", y1U, 4.8e-7, "le")
lcon = 6.2e-6 * vinf + 4.8e-7
step("lambda_con", lcon, 1.62e-5, "le")
eps5 = (1.44e-5 + 1.3e-7) * gvinf + 6.2e-6 * vinf + 4.8e-7
step("eps5", eps5, 6.6e-5, "le")
M5a = 0.25 - eta1 + lam - 2 * K4 * 6.2e-6 - 4.8e-7 - 1.62e-5
step("M5 before M2v", M5a, 0.1639, "ge")
M2v = eta2 * 0.9301 + lamQ * eps3 + K7v
step("M2v", M2v, 0.0089, "le")
M5 = 0.1639 - 0.0089
M0 = M0in + 6.6e-5
step("M0", M0, 6.4, "le")
M3v = 6.4 * (1 + Sphiv * math.sqrt(Gv)) ** 2
step("M3v", M3v, 8.82, "le")
M4v = M5 ** 2 - 4 * 8.82 * 8.5e-5
step("M4v", M4v, 0.021, "ge")
x0v = 2 * 8.5e-5 / (M5 + math.sqrt(0.021))
step("x0v", x0v, 5.67e-4, "le")
x1v = math.sqrt(M5 / (1 - 2 * K4 * 6.2e-6 - 0.9301)) * 5.67e-4 / 2
step("x1v", x1v, 4.3e-4, "le")
llin = 6.4 * (1 + Sphiv * math.sqrt(Gv)) * 5.67e-4
step("lambda_lin", llin, 0.0044, "le")
step("lambda_lin + lambda_con", 0.0044 + 1.62e-5, 0.0045, "le")
say(f"  printed steps that did not reproduce: {fails}")

say()
say("A2. The same chain with the conservative reading of every doubtful step")
say("    (x0U from M2U <= 0.0061; U2 bounds with the square root of the Gram norm, as in M3U and M3v,")
say("     since sum_j <U1, w_j>^2 <= lambda_max(G) |U1|^2 for the Gram matrix G of the w_j)")
x0 = 2 * epsU / (cU + math.sqrt(cU ** 2 - 4 * M3U * epsU))
x1 = math.sqrt((0.25 - eta1) / (1 - M1)) * x0 / 2
y0 = x0 * math.sqrt(GU) * SphiU
y1 = x0 * math.sqrt(GU) * SgradU
lc = x1 * vinf + y1
e5 = (x0 + y0) * gvinf + x1 * vinf + y1
m5 = 0.25 - eta1 + lam - 2 * K4 * x1 - y1 - lc - (eta2 * M1 + lamQ * eps3 + K7v)
m0 = M0in + e5
m3 = m0 * (1 + Sphiv * math.sqrt(Gv)) ** 2
m4 = m5 ** 2 - 4 * m3 * (epsv + e5)
xv = 2 * (epsv + e5) / (m5 + math.sqrt(m4))
ll = m0 * (1 + Sphiv * math.sqrt(Gv)) * xv
say(f"  x0U {x0:.4g}  x1U {x1:.4g}  y0U {y0:.4g}  y1U {y1:.4g}  lambda_con {lc:.4g}  eps5 {e5:.4g}")
say(f"  M4U {cU**2 - 4*M3U*epsU:.5g} > 0 ; 1 - M1 {1 - M1:.4g} > 0 ; M5 {m5:.5g} ; M3v {m3:.4g} ; M4v {m4:.5g} > 0")
say(f"  |lambda shift| <= {ll + lc:.4g}  against |lambda_bar| = 0.113 : eigenvalue stays negative: {ll + lc < 0.113}")
A2 = (cU ** 2 - 4 * M3U * epsU > 0) and (1 - M1 > 0) and (m4 > 0) and (ll + lc < 0.113)
say(f"  conservative chain closes: {A2}")

say()
say("B. Eigenvalues below 10 on the ball of radius 32 (alpha < 32 sqrt(10)), from (6.3) and (6.4)")
R0 = 32.0
amax = R0 * math.sqrt(10.0)
h = 0.004
r = np.arange(0.05, amax, h)
def nroots(f):
    s = np.sign(f)
    s = s[s != 0]
    return int(np.count_nonzero(s[1:] != s[:-1]))
cnt = {"Y": {}, "Z": {}}
lmax = 0
for l in range(1, 112):  # the first root of either equation exceeds l, and alpha < 101.2
    nu = l + 0.5
    J = jv(nu, r)
    dJ = jvp(nu, r)
    fz = r * dJ - 0.5 * J
    a, b, c = l * (l - 1) * (l + 2), l * (l - 1), (l - 1) * (l + 2)
    fy = (r * r - a) * (r * dJ - 1.5 * J) + (r * r - b) * (r * r - c) * J
    nz, ny = nroots(fz), nroots(fy)
    cnt["Z"][l], cnt["Y"][l] = nz, ny
    if nz or ny:
        lmax = l
Ye = sum(v for l, v in cnt["Y"].items() if l % 2 == 0)
Yo = sum(v for l, v in cnt["Y"].items() if l % 2 == 1)
Ze = sum(v for l, v in cnt["Z"].items() if l % 2 == 0)
Zo = sum(v for l, v in cnt["Z"].items() if l % 2 == 1)
say(f"  grid step {h}, largest l with a root: {lmax}")
say(f"  roots: Y even l {Ye}, Y odd l {Yo}, Z even l {Ze}, Z odd l {Zo}; l=1: Y {cnt['Y'][1]}, Z {cnt['Z'][1]}")
NU = Ye + Zo
Nv = Yo + Ze
say(f"  class of U (even l for Y, odd l for Z): {NU}   paper N = 1257")
say(f"  class of v (odd l for Y, even l for Z): {Nv}, with the zero mode {Nv + 1}   paper N = 1260")
B = (NU in (1257, 1256)) and (Nv in (1260, 1259))
say(f"  counts agree with the paper's N (allowing the zero mode in one class): {B}")
# a second pass at half the step, to see that no root was missed or doubled
r2 = np.arange(0.05, amax, h / 2)
tot1 = Ye + Yo + Ze + Zo
tot2 = 0
for l in range(1, lmax + 2):
    nu = l + 0.5
    J = jv(nu, r2); dJ = jvp(nu, r2)
    a, b, c = l * (l - 1) * (l + 2), l * (l - 1), (l - 1) * (l + 2)
    tot2 += nroots(r2 * dJ - 0.5 * J) + nroots((r2 * r2 - a) * (r2 * dJ - 1.5 * J) + (r2 * r2 - b) * (r2 * r2 - c) * J)
say(f"  total roots at step {h}: {tot1}; at step {h/2}: {tot2}; equal: {tot1 == tot2}")

say()
say("B2. The roots themselves: the (N+1)-th scaled eigenvalue for the paper's N, and K5 = 4.5 / (eta2 + lambda_{N+1})")
from scipy.optimize import brentq
def fz1(x, nu):
    return x * jvp(nu, x) - 0.5 * jv(nu, x)
def fy1(x, nu, a, b, c):
    J = jv(nu, x)
    return (x * x - a) * (x * jvp(nu, x) - 1.5 * J) + (x * x - b) * (x * x - c) * J
def roots_of(fvals, fun, args):
    idx = np.nonzero((np.sign(fvals[1:]) * np.sign(fvals[:-1])) < 0)[0]
    return [brentq(fun, r[i], r[i + 1], args=args, xtol=1e-12) for i in idx]
clsU, clsv = [], [0.0]            # the zero mode (constant field along the axis) is odd: class of v
for l in range(1, lmax + 1):
    nu = l + 0.5
    J = jv(nu, r); dJ = jvp(nu, r)
    a, b, c = l * (l - 1) * (l + 2), l * (l - 1), (l - 1) * (l + 2)
    rz = roots_of(r * dJ - 0.5 * J, fz1, (nu,))
    ry = roots_of((r * r - a) * (r * dJ - 1.5 * J) + (r * r - b) * (r * r - c) * J, fy1, (nu, a, b, c))
    lz = [(x / R0) ** 2 for x in rz]
    ly = [(x / R0) ** 2 for x in ry]
    if l % 2 == 0:
        clsU += ly; clsv += lz
    else:
        clsU += lz; clsv += ly
clsU.sort(); clsv.sort()
say(f"  roots located: class U {len(clsU)}, class v {len(clsv)} (with the zero mode); smallest positive: U {clsU[0]:.6f}, v {clsv[1]:.6f}")
B2 = True
for name, cls, N in (("U", clsU, 1257), ("v", clsv, 1260)):
    for shift in (0, -1, 1):
        if N + shift < len(cls):
            lamN, lamN1 = cls[N + shift - 1], cls[N + shift]
            k5 = 4.5 / (0.005 + lamN1)
            tag = "" if shift == 0 else f" (index shifted by {shift})"
            say(f"  class {name}, N = {N}{tag}: lambda_N {lamN:.4f}, lambda_(N+1) {lamN1:.4f}, K5 {k5:.4f}; K5 <= 0.47: {k5 <= 0.47}; lambda_(N+1) > 10: {lamN1 > 10}")
            if shift == 0 and not k5 <= 0.47:
                B2 = False
for name, cls in (("U", clsU), ("v", clsv)):
    n957 = sum(1 for x in cls if x < 4.5 / 0.47 - 0.005)
    say(f"  class {name}: eigenvalues below 10: {sum(1 for x in cls if x < 10)}; below 4.5/0.47 - eta2 = {4.5/0.47 - 0.005:.4f}: {n957}")

say()
say(f"SUMMARY: printed steps not reproduced {fails}; conservative chain closes {A2}; counts below 10 equal the paper's N {B}; K5 <= 0.47 at the paper's N {B2}; root count stable {tot1 == tot2}")
