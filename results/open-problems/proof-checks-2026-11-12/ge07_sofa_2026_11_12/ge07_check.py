# GE07 moving sofa: numerical checks on Gerver's sofa and on the arm-length iteration of
# Baek, "Optimality of Gerver's Sofa" (arXiv 2411.19826), Sections 1.7, 6.5, 8.4.
# Gerver's sofa is taken from Romik (arXiv 1606.08111), Theorem 3 and Table 1.
# Floating point; nothing here is a proof.
import math
import numpy as np
import sympy as sp

def out(*a):
    print(*a, flush=True)

PI2 = math.pi / 2
# ---- Romik, Table 1 -------------------------------------------------------------------------
phi = 0.039177364790083641
theta = 0.681301509382724894
a1, a2 = 1.210322422072688751, -0.25
b1, b2 = -0.527624598026784624, 0.920258385160637622
c1, c2 = 0.626045522848465867, -0.944750803946430751
d1, d2 = 1.313022761424232933, -0.525382670414554437
e1, e2 = 1.210322422072688751, 0.25
kap = [(-0.210322422072688751, 0.25), (-0.919179292771593322, 0.472406619750805465),
       (-0.613763229430251668, 0.889626479003221860), (-0.308347166088910014, 0.472406619750805465),
       (-1.017204036787814585, 0.25)]
T = [0.0, phi, theta, PI2 - theta, PI2 - phi, PI2]

t = sp.symbols('t', real=True)
W = [sp.Matrix([a1*sp.cos(t) + a2*sp.sin(t) - 1, -a2*sp.cos(t) + a1*sp.sin(t) - sp.Rational(1, 2)]),
     sp.Matrix([-t**2/4 + b1*t + b2, t/2 - b1 - 1]),
     sp.Matrix([c1 - t, c2 + t]),
     sp.Matrix([-t/2 + d1 - 1, -t**2/4 + d1*t + d2]),
     sp.Matrix([e1*sp.cos(t) + e2*sp.sin(t) - sp.Rational(1, 2), -e2*sp.cos(t) + e1*sp.sin(t) - 1])]
Rt = sp.Matrix([[sp.cos(t), -sp.sin(t)], [sp.sin(t), sp.cos(t)]])
mu = sp.Matrix([sp.cos(t), sp.sin(t)])
nu = sp.Matrix([-sp.sin(t), sp.cos(t)])

def lam(M):
    f0 = sp.lambdify(t, M[0], 'numpy')
    f1 = sp.lambdify(t, M[1], 'numpy')
    return lambda s: np.array([f0(s) + 0*s, f1(s) + 0*s])

P = []   # per piece: dict of numeric functions
for j in range(5):
    x = Rt*W[j] + sp.Matrix(kap[j])
    xp = x.diff(t)
    A = x + (xp.dot(mu))*nu + mu
    B = x + (xp.dot(mu))*nu
    C = x - (xp.dot(nu))*mu + nu
    D = x - (xp.dot(nu))*mu
    d = {}
    for name, M in (('x', x), ('xp', xp), ('A', A), ('B', B), ('C', C), ('D', D),
                    ('Ap', A.diff(t)), ('Bp', B.diff(t)), ('Cp', C.diff(t)), ('Dp', D.diff(t))):
        d[name] = lam(M)
    P.append(d)

def piece(s):
    s = np.asarray(s, dtype=float)
    j = np.zeros(s.shape, dtype=int)
    for k in range(1, 5):
        j[s >= T[k]] = k
    return j

def ev(name, s):
    s = np.atleast_1d(np.asarray(s, dtype=float))
    j = piece(s)
    res = np.zeros((2,) + s.shape)
    for k in range(5):
        m = (j == k)
        if m.any():
            res[:, m] = P[k][name](s[m])
    return res

def U(s):
    return np.array([np.cos(s), np.sin(s)])

def V(s):
    return np.array([-np.sin(s), np.cos(s)])

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

out("== 1. Romik's table: gluing conditions")
out("x(0) =", P[0]['x'](np.array([0.0])).ravel(), " A(0) =", P[0]['A'](np.array([0.0])).ravel())
for k in range(1, 5):
    s = np.array([T[k]])
    dx = np.abs(P[k-1]['x'](s) - P[k]['x'](s)).max()
    dxp = np.abs(P[k-1]['xp'](s) - P[k]['xp'](s)).max()
    out("  break t%d = %.15f  |x jump| %.2e  |x' jump| %.2e" % (k, T[k], dx, dxp))
r43 = np.abs(P[0]['x'](np.array([phi])) - P[3]['B'](np.array([PI2 - theta]))).max()
r44 = np.abs(P[4]['x'](np.array([PI2 - phi])) - P[1]['D'](np.array([theta]))).max()
out("  (43) |x(phi) - B(pi/2-theta)| = %.2e   (44) |x(pi/2-phi) - D(theta)| = %.2e" % (r43, r44))
s = np.linspace(0, PI2, 2001)
xs = ev('x', s); xr = ev('x', PI2 - s)
xend = ev('x', np.array([PI2])).ravel()
out("  x(pi/2) = (%.15f, %.3e)" % (xend[0], xend[1]))
out("  symmetry: max |x1(pi/2-t) + x1(t) - x1(pi/2)| = %.2e, max |x2(pi/2-t) - x2(t)| = %.2e"
    % (np.abs(xr[0] + xs[0] - xend[0]).max(), np.abs(xr[1] - xs[1]).max()))

out("== 2. Arm lengths f = 1 - <x',u>, g = 1 + <x',v> (injectivity condition asks f, g > 1 on (0, pi/2))")
N = 200001
s = np.linspace(0, PI2, N)
xp = ev('xp', s)
f = 1 - dot(xp, U(s)); g = 1 + dot(xp, V(s))
out("  f(0) = %.3e + 1, g(0) = %.12f, f(pi/2) = %.12f, g(pi/2) = 1 + %.3e" % (f[0]-1, g[0], f[-1], g[-1]-1))
inner = slice(1, N-1)
out("  min f on interior grid = %.6f at t = %.6f ; min g = %.6f at t = %.6f"
    % (f[inner].min(), s[inner][f[inner].argmin()], g[inner].min(), s[inner][g[inner].argmin()]))
out("  smallest (f-1)/t near 0: %.6f ; f increasing: %s ; g decreasing: %s"
    % (((f[1:2000]-1)/s[1:2000]).min(), bool((np.diff(f) > -1e-13).all()), bool((np.diff(g) < 1e-13).all())))
out("  x1(t) strictly decreasing: %s" % bool((np.diff(ev('x', s)[0]) < 0).all()))

out("== 3. Romik's balance equations on each interval (max abs residual; a small number means the equation holds)")
names = ["(21)v <A',v>=0", "(17) <A',v>=<x',v>", "(20) <A',v>=<-B'+x',v>", "(22)v <A',v>=<-B',v>",
         "(21)u <-C',u>=0", "(18) <-C',u>=<-x',u>", "(19) <-C',u>=<D'-x',u>", "(22)u <-C',u>=<D',u>"]
for k in range(5):
    ss = np.linspace(T[k], T[k+1], 4001)[1:-1]
    u = U(ss); v = V(ss)
    Ap = P[k]['Ap'](ss); Bp = P[k]['Bp'](ss); Cp = P[k]['Cp'](ss); Dp = P[k]['Dp'](ss); xq = P[k]['xp'](ss)
    res = [np.abs(dot(Ap, v)).max(), np.abs(dot(Ap, v) - dot(xq, v)).max(),
           np.abs(dot(Ap, v) - dot(-Bp + xq, v)).max(), np.abs(dot(Ap, v) + dot(Bp, v)).max(),
           np.abs(dot(Cp, u)).max(), np.abs(-dot(Cp, u) + dot(xq, u)).max(),
           np.abs(-dot(Cp, u) - dot(Dp - xq, u)).max(), np.abs(-dot(Cp, u) - dot(Dp, u)).max()]
    hold = [names[i] for i in range(8) if res[i] < 1e-9]
    out("  I%d: holds: %s" % (k+1, "; ".join(hold)))
    out("      residuals: " + " ".join("%.1e" % r for r in res))
    out("      <A',u> max abs %.1e ; <A',v> range [%.5f, %.5f] ; <-B',v> range [%.5f, %.5f] ; <-C',u> range [%.5f, %.5f]"
        % (np.abs(dot(Ap, u)).max(), dot(Ap, v).min(), dot(Ap, v).max(), -dot(Bp, v).max(), -dot(Bp, v).min(),
           -dot(Cp, u).min(), -dot(Cp, u).max()))

out("== 4. Baek (1.9), (1.10), (1.11) evaluated on Gerver's sofa")
def k0(y):
    return np.maximum(np.abs(y - 1), (np.abs(y - 1) + 1)/2)
def m0(y):
    return y - k0(y)
worst19 = -1e9; worst110 = -1e9; worst111 = 1e9
for k in range(5):
    ss = np.linspace(T[k], T[k+1], 20001)[1:-1]
    u = U(ss); v = V(ss)
    Ap = P[k]['Ap'](ss); Bp = P[k]['Bp'](ss); xq = P[k]['xp'](ss)
    lhs = dot(Ap, v)
    rhs = np.maximum(-dot(Bp, v), 0) + np.abs(dot(xq, v))
    gk = 1 + dot(xq, v)
    fprime = gk - lhs
    e19 = (lhs - rhs).max(); e110 = (lhs - k0(gk)).max(); e111 = (fprime - m0(gk)).min()
    # f' from finite differences as a cross-check of f' = g - <A',v>
    fk = 1 - dot(xq, u)
    fd = np.gradient(fk, ss)
    out("  I%d: max(lhs-rhs of 1.9) = %+.3e ; max(<A',v> - k0(g)) = %+.3e ; min(f' - m0(g)) = %+.3e ; |f' - (g-<A',v>)| fd %.1e"
        % (k+1, e19, e110, e111, np.abs(fd - fprime)[2:-2].max()))
    worst19 = max(worst19, e19); worst110 = max(worst110, e110); worst111 = min(worst111, e111)
out("  overall: (1.9) violated by at most %+.3e ; (1.10) margin %+.3e ; (1.11) margin %+.3e" % (worst19, worst110, worst111))

out("== 5. The iteration f_{n+1} = max(f_n, F f_n), F f(x) = 1 + int_0^x m0(f(pi/2-u)) du  (Def. 6.5.1, 6.5.2)")
M = 400001
xg = np.linspace(0, PI2, M)
h = xg[1] - xg[0]
def Fop(fn):
    y = m0(fn[::-1])
    cum = np.concatenate(([0.0], np.cumsum((y[1:] + y[:-1])*h/2)))
    return 1 + cum
fG = 1 - dot(ev('xp', xg), U(xg))
fn = np.zeros(M)
pos = xg > 1e-3
for n in range(1, 41):
    fn = np.maximum(fn, Fop(fn))
    if n <= 12 or n in (20, 40):
        jc = np.maximum(1 - xg, (n-1)/12.0)
        line = "  n=%2d  min f_n = %.6f  min over x>0.001 of (f_n - 1) = %+.6f  min(f_G - f_n) = %+.6f" % (
            n, fn.min(), (fn[pos] - 1).min(), (fG - fn).min())
        if n <= 10:
            line += "  min(f_n - j_{(n-1)/12}) = %+.2e" % (fn - jc).min()
        out(line)
out("  after 40 steps: f_n(pi/2) = %.6f, f_G(pi/2) = %.6f, max(f_G - f_n) = %.6f" % (fn[-1], fG[-1], (fG - fn).max()))

out("== 6. Lemma 6.5.3: the two minima")
c = sp.symbols('c', real=True)
d1e = 1 - (1 - sp.Rational(3, 2)*c)*(sp.pi/2 - 1 + c) - c - sp.Rational(1, 12)
c1s = sp.solve(sp.diff(d1e, c), c)[0]
out("  case 1: minimiser c =", c1s, " value =", sp.simplify(d1e.subs(c, c1s)), "=", float(d1e.subs(c, c1s)))
d2e = sp.Rational(5, 3) - sp.pi/2 + sp.Rational(3, 4)*c*(c + sp.pi - 2) - c - sp.Rational(1, 12)
c2s = sp.solve(sp.diff(d2e, c), c)[0]
out("  case 2: minimiser c =", c2s, " value =", sp.simplify(d2e.subs(c, c2s)), "=", float(d2e.subs(c, c2s)))
# direct numeric check of F j_c >= j_{c+1/12} on a grid of c in [0, 2/3]
worst = 1e9
M2 = 20001
x2 = np.linspace(0, PI2, M2); h2 = x2[1] - x2[0]
for cc in np.linspace(0, 2/3, 401):
    jc = np.maximum(1 - x2, cc)
    y = m0(jc[::-1])
    Fj = 1 + np.concatenate(([0.0], np.cumsum((y[1:] + y[:-1])*h2/2)))
    worst = min(worst, (Fj - np.maximum(1 - x2, cc + 1/12)).min())
out("  numeric: min over c in [0,2/3], x in [0,pi/2] of F j_c(x) - j_{c+1/12}(x) = %+.6f" % worst)

out("== 7. Area of the shape cut out by the rotating hallway (column method, no structural assumption)")
def area_columns(xfun, NT=40000, NX=8001):
    tt = (np.arange(NT) + 0.5)*(PI2/NT)
    xx = xfun(tt)
    xe = xfun(np.array([PI2]))
    Xmin = float(xe[0][0]) - 1.0
    X = np.linspace(Xmin, 1.0, NX)
    ct = np.cos(tt); st = np.sin(tt)
    lower = np.zeros(NX); upper = np.ones(NX)
    for i0 in range(0, NX, 100):
        Xc = X[i0:i0+100][:, None]
        dxx = Xc - xx[0][None, :]
        U1 = xx[1][None, :] + (1 - ct[None, :]*dxx)/st[None, :]
        U2 = xx[1][None, :] + (1 + st[None, :]*dxx)/ct[None, :]
        Lw = xx[1][None, :] + np.minimum(-(ct/st)[None, :]*dxx, (st/ct)[None, :]*dxx)
        upper[i0:i0+100] = np.minimum(1.0, np.minimum(U1.min(axis=1), U2.min(axis=1)))
        lower[i0:i0+100] = np.maximum(0.0, Lw.max(axis=1))
    wdt = upper - lower
    area = np.trapezoid(np.maximum(wdt, 0), X) if hasattr(np, 'trapezoid') else np.trapz(np.maximum(wdt, 0), X)
    return area, X, lower, upper
def hamm(tt):
    r = 2/math.pi
    return np.array([r*(np.cos(2*tt) - 1), r*np.sin(2*tt)])
aH, _, _, _ = area_columns(hamm)
out("  Hammersley's sofa: %.8f  (exact pi/2 + 2/pi = %.8f)" % (aH, math.pi/2 + 2/math.pi))
aG, X, lower, upper = area_columns(lambda tt: ev('x', tt))
out("  Gerver's sofa:     %.8f  (literature 2.21953166...)" % aG)
aG2, _, _, _ = area_columns(lambda tt: ev('x', tt), NT=80000, NX=16001)
out("  Gerver's sofa, finer grid: %.8f" % aG2)
wdt = (upper - lower)[1:-1]
out("  thinnest interior column of the shape: %.6f at X = %.4f (connected if positive)" % (wdt.min(), X[1:-1][wdt.argmin()]))

out("== 8. Area from the boundary curves (Green's theorem; uses the description in Theorem 8.4.1)")
def green(curve):   # curve: 2 x n points along an oriented path
    xq, yq = curve
    return 0.5*np.sum(xq[:-1]*yq[1:] - xq[1:]*yq[:-1])
n = 400001
sA = np.linspace(0, PI2, n)
Ac = ev('A', sA); Cc = ev('C', sA)
capb = np.concatenate([Ac, Cc, Ac[:, :1]], axis=1)       # A up the right side, top segment, C down the left side, bottom segment
areaK = green(capb)
out("  A(0) = (%.6f, %.6f), A(pi/2) = (%.6f, %.6f), C(0) = (%.6f, %.6f), C(pi/2) = (%.6f, %.6f)"
    % (Ac[0, 0], Ac[1, 0], Ac[0, -1], Ac[1, -1], Cc[0, 0], Cc[1, 0], Cc[0, -1], Cc[1, -1]))
sB = np.linspace(T[3], T[5], n)[::-1]
sx = np.linspace(T[1], T[4], n)
sD = np.linspace(T[0], T[2], n)[::-1]
Bc = ev('B', sB); xc = ev('x', sx); Dc = ev('D', sD)
out("  niche corners: D(0) = (%.6f, %.2e), B(pi/2) = (%.6f, %.2e); |B(t3)-x(t1)| = %.1e, |x(t4)-D(t2)| = %.1e"
    % (Dc[0, -1], Dc[1, -1], Bc[0, 0], Bc[1, 0], np.abs(Bc[:, -1] - xc[:, 0]).max(), np.abs(xc[:, -1] - Dc[:, 0]).max()))
nb = np.concatenate([Bc, xc, Dc, Bc[:, :1]], axis=1)
areaN = green(nb)
out("  |K| = %.9f, |N| = %.9f, |K| - |N| = %.9f" % (areaK, areaN, areaK - areaN))
out("  difference from the column method (finer grid): %.2e" % (areaK - areaN - aG2))

out("== 9. How close the core's endpoints come to the inner walls (Gerver's remark, quoted in Remark 8.4.1)")
p = ev('x', np.array([phi])).ravel()
tt = np.linspace(phi, PI2, 400001)
xx = ev('x', tt)
q1 = np.cos(tt)*(p[0] - xx[0]) + np.sin(tt)*(p[1] - xx[1])
q2 = -np.sin(tt)*(p[0] - xx[0]) + np.cos(tt)*(p[1] - xx[1])
clear = np.maximum(q1, q2)          # >= 0 means the point is outside the open inner quadrant
far = tt > theta
i = clear[far].argmin()
out("  point x(phi): smallest clearance from the inner quadrant over t in (theta, pi/2]: %.6f at t = %.6f (pi/4 = %.6f)"
    % (clear[far][i], tt[far][i], math.pi/4))
j = np.abs(tt - math.pi/4).argmin()
out("  at t = pi/4: distances of x(phi) to the two inner-wall lines: %.6f and %.6f" % (q1[j], q2[j]))
out("done")
