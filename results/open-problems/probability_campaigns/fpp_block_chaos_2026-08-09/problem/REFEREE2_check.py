# Referee 2: independent numerical / symbolic verification of the I3 entropy walk's S8 chase
# and the S9-a overlap bracket.  Nothing here reads the walk's arithmetic; each block
# re-derives from the definitions and then compares to the walk's printed constant.
import io, sys, math, itertools, random
import numpy as np
import sympy as sp

out = io.StringIO()
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.write(s + "\n")

# ---------------------------------------------------------------- 1. the q function
# q(x) = x(e^x - 1).  Walk uses: q nondecreasing on [0,inf); q(x) <= 2 x^2 on [0,1].
x = sp.symbols('x', positive=True)
q = x*(sp.exp(x)-1)
say("q'(x) =", sp.simplify(sp.diff(q, x)), " -> nonneg on x>=0:",
    all(float(sp.diff(q,x).subs(x, v)) >= 0 for v in np.linspace(0, 5, 200)))
xs = np.linspace(1e-9, 1.0, 200001)
ratio = (xs*(np.exp(xs)-1))/xs**2
say("sup_{x in (0,1]} q(x)/x^2 =", ratio.max(), " (= e-1 =", math.e-1, ")  <= 2:", ratio.max() <= 2)
# also on the actual window lambda*tau' <= 1/2
xs2 = np.linspace(1e-9, 0.5, 100001)
say("sup_{x in (0,1/2]} q(x)/x^2 =", ((xs2*(np.exp(xs2)-1))/xs2**2).max())

# ---------------------------------------------------------------- 2. BLM / DHS lemma form
# Ent e^{lam X} <= E[ e^{lam X} q(lam (X'-X)_+) ],  X' an independent copy.
# Verified numerically on several laws and lambdas (this is the exact form S4 consumes).
def ent(v, p):
    f = v*p
    Ef = f.sum()
    return float((f*np.log(np.where(f > 0, v, 1))).sum() - Ef*math.log(Ef)) if Ef > 0 else 0.0

def blm_check(vals, probs, lams):
    vals = np.asarray(vals, float); probs = np.asarray(probs, float)
    probs = probs/probs.sum()
    worst = -1e9; arg = None
    for lam in lams:
        e = np.exp(lam*vals)
        lhs = float((e*np.log(e)*probs).sum() - (e*probs).sum()*math.log((e*probs).sum()))
        d = vals[None, :] - vals[:, None]           # d[i,j] = X'_j - X_i
        dp = np.clip(lam*d, 0, None)
        rhs = float((probs[:, None]*probs[None, :]*e[:, None]*(dp*(np.exp(dp)-1))).sum())
        if lhs - rhs > worst:
            worst = lhs - rhs; arg = lam
    return worst, arg

lams = list(np.linspace(-3, 3, 121))
tests = {
  "two-point {1,2}":            ([1.0, 2.0], [0.5, 0.5]),
  "two-point skew {1,2}":       ([1.0, 2.0], [0.9, 0.1]),
  "uniform grid [1,2] (11 pts)":(list(np.linspace(1, 2, 11)), [1]*11),
  "heavy-ish {0,1,5}":          ([0.0, 1.0, 5.0], [0.6, 0.3, 0.1]),
  "sum of 8 iid two-point":     None,
}
for name, t in tests.items():
    if t is None:
        # law of S = sum of 8 iid Bernoulli-type weights in {1,2}: binomial shape
        k = 8
        v = [8 + i for i in range(k+1)]
        p = [math.comb(k, i)*0.5**k for i in range(k+1)]
        t = (v, p)
    w, lam = blm_check(t[0], t[1], lams)
    say(f"BLM form  max(LHS-RHS) over lambda for {name:28s} = {w: .3e}  at lam={lam: .2f}   -> holds:", w <= 1e-12)

# ---------------------------------------------------------------- 3. S8 assembly, symbolically
lam, b, aw, r, a0, t, u = sp.symbols('lambda b a_w r a_0 t u', positive=True)
Eq_bound = 2*lam**2*b**2                       # E q(lam tau') <= 2 lam^2 b^2  for lam <= 1/b
A = a0*Eq_bound                                # = a0 E q
logmom = (b/aw)*r/a0                           # log E exp(#G_+/a0), deterministic (Claim 4)
# survey display: Ent <= [A/(1-A)] * logmom * E e^{lam T}
lam_win = sp.Rational(1,2)/b                   # walk's window lambda <= 1/(2b)
A_at = A.subs({a0: 1})
say("a0=1: A(lambda) =", A_at, "; A at lambda=1/(2b) =", sp.simplify(A_at.subs(lam, lam_win)))
C_walk = sp.simplify((A_at/(1-A_at)).subs(lam, lam_win)/ (lam_win**2) )  # crude: use A/(1-A)<=2A
C_via_2A = sp.simplify(2*A_at*logmom.subs(a0,1)/lam**2)                  # coefficient of lam^2
say("walk's Ent coefficient (via A/(1-A) <= 2A):", C_via_2A, "  == 4 b^3 r / a_w :",
    sp.simplify(C_via_2A - 4*b**3*r/aw) == 0)

# Herbst -> psi_c(lam) <= C lam^2 ; Chernoff at u = t sqrt(r)
def chernoff(C, lam_max):
    lam_star = sp.solve(sp.Eq(sp.diff(C*lam**2 - lam*u, lam), 0), lam)[0]
    val = sp.simplify((C*lam**2 - lam*u).subs(lam, lam_star))
    u_max = sp.solve(sp.Eq(lam_star, lam_max), u)[0]
    return lam_star, val, u_max

C1w = 4*b**3*r/aw
ls, val, umax = chernoff(C1w, 1/(2*b))
say("WALK   : lam* =", ls, "  exponent =", val, "  u_max =", sp.simplify(umax))
say("WALK   : exponent at u = t sqrt(r) :", sp.simplify(val.subs(u, t*sp.sqrt(r))),
    "  == -a_w t^2/(16 b^3):", sp.simplify(val.subs(u, t*sp.sqrt(r)) + aw*t**2/(16*b**3)) == 0)
say("WALK   : t_max =", sp.simplify(umax/sp.sqrt(r)), "  == 4 b^2 sqrt(r)/a_w:",
    sp.simplify(umax/sp.sqrt(r) - 4*b**2*sp.sqrt(r)/aw) == 0)

# alternative assembly: #G_+ <= (b/a_w) r deterministically, so skip the variational step entirely
C1s = 2*b**3*r/aw                              # Ent <= Eq * (b/a_w) r * E e^{lam T},  lam <= 1/b
ls2, val2, umax2 = chernoff(C1s, 1/b)
say("DIRECT : lam* =", ls2, "  exponent at u=t sqrt(r) :", sp.simplify(val2.subs(u, t*sp.sqrt(r))),
    "  t_max =", sp.simplify(umax2/sp.sqrt(r)))

# ---------------------------------------------------------------- 4. S9-a overlap bracket
z = sp.symbols('z', positive=True)
det_upper = (z/b)**2                  # deterministic branch empties for r < this
s8_lower  = (aw*z/(4*b**2))**2        # S8 admits t=z for r > this
say("s8_lower/det_upper =", sp.simplify(s8_lower/det_upper),
    " -> < 1 iff a_w < 4b (equality solution for a_w:", sp.solve(sp.Eq(s8_lower, det_upper), aw), ")")
rstar = z**2/(2*b**2)
say("r*=z^2/(2b^2):  r*/s8_lower =", sp.simplify(rstar/s8_lower),
    " (>1 iff a_w^2 < 8b^2);   det_upper/r* =", sp.simplify(det_upper/rstar))
# numeric sweep over weight pairs
bad = []
for aw_v in [0.01, 0.1, 0.5, 1.0, 2.0, 10.0]:
    for b_v in [aw_v, aw_v*1.0001, aw_v*2, aw_v*10, aw_v*1000]:
        for z_v in [0.001, 0.1, 1.0, 5.0, 100.0, 1e6]:
            lo = (aw_v*z_v/(4*b_v**2))**2; hi = (z_v/b_v)**2
            if not lo < hi: bad.append((aw_v, b_v, z_v, lo, hi))
            # every integer r >= 1 covered?
            if not (hi > 1 or lo < 1): bad.append(("r=1 gap", aw_v, b_v, z_v, lo, hi))
say("overlap sweep failures:", bad if bad else "NONE (all (a_w,b,z) covered, incl. every integer r>=1)")

# ---------------------------------------------------------------- 5. sanity vs Hoeffding on a toy
# single fixed path of m edges: T = sum tau_i, G_+ = all m edges.  Entropy method must be
# WEAKER than (or equal to) the exact log-mgf; a "too good" constant would signal an error.
m, b_v, aw_v = 40, 2.0, 1.0
lams_n = np.linspace(1e-4, 1/(2*b_v), 60)
worst = -1
for lv in lams_n:
    exact = m*math.log(0.5*math.exp(lv*aw_v) + 0.5*math.exp(lv*b_v)) - lv*m*1.5
    walk_bd = 4*(b_v**3)*m/aw_v*lv**2 / (b_v/aw_v)      # C = Eq*(#G bound); here #G=m so use direct
    direct_bd = 2*(b_v**2)*lv**2*m
    worst = max(worst, exact - direct_bd)
say("toy (m=40, weights {1,2}): max_lambda [exact psi_c - entropy-method bound] =", worst,
    "-> bound valid:", worst <= 0)

open("referee2_check_output.txt","w",encoding="utf-8").write(out.getvalue())
