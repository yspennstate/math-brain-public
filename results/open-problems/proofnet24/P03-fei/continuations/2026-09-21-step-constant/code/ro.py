"""Read-once formulas: exact spectral entropy, influence, and the restriction-step
constant rho_0(f) = min over relevant i of Delta_i H / Inf_i.

If sup_f rho_0(f) = C < infinity then FEI holds with constant C, because
  I(f) = (I(f_0)+I(f_1))/2 + Inf_i   and   H(f) = (H(f_0)+H(f_1))/2 + Delta_i H.
Necessarily sup rho_0 >= C_FEI >= beta(1/2) = 6.4547837.

Convention: p = Pr[f = 1]; V = 4p(1-p); h = binary entropy in bits; H = entropy of
the spectral sample S with Pr[S] = fhat(S)^2.
"""
import math
from math import log2

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*log2(x) - (1-x)*log2(1-x)

def phi(w):
    if w <= 0.0:
        return 0.0
    return w*log2(1.0/w)

# ---- tree: ('lit', i, neg) | ('and', a, b) | ('or', a, b) | ('const', 0/1)
def lit(i, neg=False): return ('lit', i, neg)
def AND(a, b): return ('and', a, b)
def OR(a, b):  return ('or', a, b)
CONST0 = ('const', 0)
CONST1 = ('const', 1)

def leaves(t):
    k = t[0]
    if k == 'lit': return [t[1]]
    if k == 'const': return []
    return leaves(t[1]) + leaves(t[2])

def ht_and(p, q):
    """Ht_AND(p,q): the entropy the AND gate itself injects."""
    Vp = 4*p*(1-p); Vq = 4*q*(1-q)
    It_a = q*Vp; It_b = p*Vq
    w_empty = (1 - 2*p*q)**2
    w_ab = w_empty + It_a + It_b - 1
    return phi(w_empty) + phi(It_a - w_ab) + phi(It_b - w_ab) + phi(w_ab), It_a, It_b

def analyse(t):
    """returns (p, I, H) exactly, by the composition recursion."""
    k = t[0]
    if k == 'const':
        return (float(t[1]), 0.0, 0.0)
    if k == 'lit':
        return (0.5, 1.0, 0.0)
    a, b = t[1], t[2]
    pa, Ia, Ha = analyse(a)
    pb, Ib, Hb = analyse(b)
    if pa in (0.0, 1.0) or pb in (0.0, 1.0):
        return analyse(simplify(t))
    if k == 'and':
        p, q = pa, pb
        Ht, It_a, It_b = ht_and(p, q)
        I = q*Ia + p*Ib
        H = q*(Ha - h2(4*p*(1-p))) + p*(Hb - h2(4*q*(1-q))) + Ht
        return (p*q, I, H)
    # OR(a,b) = NOT AND(NOT a, NOT b); H and I are invariant under negation
    p, q = 1-pa, 1-pb
    Ht, It_a, It_b = ht_and(p, q)
    I = q*Ia + p*Ib
    H = q*(Ha - h2(4*p*(1-p))) + p*(Hb - h2(4*q*(1-q))) + Ht
    return (1 - p*q, I, H)

def simplify(t):
    k = t[0]
    if k in ('lit', 'const'): return t
    a = simplify(t[1]); b = simplify(t[2])
    if k == 'and':
        if a == CONST0 or b == CONST0: return CONST0
        if a == CONST1: return b
        if b == CONST1: return a
        return AND(a, b)
    if a == CONST1 or b == CONST1: return CONST1
    if a == CONST0: return b
    if b == CONST0: return a
    return OR(a, b)

def restrict(t, i, val):
    k = t[0]
    if k == 'const': return t
    if k == 'lit':
        if t[1] != i: return t
        v = val ^ (1 if t[2] else 0)
        return CONST1 if v else CONST0
    return simplify((k, restrict(t[1], i, val), restrict(t[2], i, val)))

def rho0(t, verbose=False):
    """min over relevant coordinates of Delta_i H / Inf_i, plus the per-coordinate table."""
    p, I, H = analyse(t)
    rows = []
    for i in sorted(set(leaves(t))):
        t0 = restrict(t, i, 0); t1 = restrict(t, i, 1)
        p0, I0, H0 = analyse(t0)
        p1, I1, H1 = analyse(t1)
        inf_i = abs(p1 - p0)          # read-once: f_0 <= f_1 or >=, so Pr[f0!=f1]=|p1-p0|
        if inf_i <= 1e-15: continue
        dH = H - (H0 + H1)/2.0
        rows.append((i, inf_i, dH, dH/inf_i))
    if not rows: return None, rows, (p, I, H)
    return min(r[3] for r in rows), rows, (p, I, H)
