# Independent exact enclosure of the B09 tax-free counterexample quantity.
# g = (-1)^(XY), X ~ Bern(1/8), Y ~ Bern(1/4) independent, A = {X}.
# Spectral masses in the biased product basis (empty, X, Y, XY) = (225, 7, 3, 21)/256,
# M_A = H(masses) - h2(3/32), J_A = h2(3/32) - (1/8) h2(3/4)   (definitions as in the
# B09 / A081 records).  Reduced by hand to
#   J_A - M_A = 7/4 + (450/256) log2 3 + (450/256) log2 5 + (28/256) log2 7 - (464/256) log2 29.
# This script recomputes the masses from the definitions, builds the linear form
# mechanically (no hand reduction used), checks it equals the hand form, and encloses it.
import sys, os, json
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from certlog import enclose_form, factor

p, qq = Fr(1, 8), Fr(1, 4)
# biased Fourier expansion of g(x,y) = 1 - 2xy over phi_p(x) = (x - p)/sigma_p
sp2, sq2 = p * (1 - p), qq * (1 - qq)
# g = 1 - 2xy, x = p + sigma_p phi, y = q + sigma_q psi
#   = 1 - 2pq - 2 q sigma_p phi - 2 p sigma_q psi - 2 sigma_p sigma_q phi psi
m_empty = (1 - 2 * p * qq) ** 2
m_X = 4 * qq * qq * sp2
m_Y = 4 * p * p * sq2
m_XY = 4 * sp2 * sq2
masses = [m_empty, m_X, m_Y, m_XY]
assert sum(masses) == 1, sum(masses)
assert masses == [Fr(225, 256), Fr(7, 256), Fr(3, 256), Fr(21, 256)]

def entropy_form(probs):
    """sum -p log2 p as (const, {prime: coeff}) with exact rational coefficients."""
    const = Fr(0); co = {}
    for pr in probs:
        if pr == 0:
            continue
        # -pr log2 pr = pr log2 den - pr log2 num
        for m, sgn in [(pr.denominator, 1), (pr.numerator, -1)]:
            for pp, v in factor(m).items():
                co[pp] = co.get(pp, Fr(0)) + sgn * pr * v
    return const, co

def h2(x):
    return entropy_form([x, 1 - x])

def combine(*terms):
    const = Fr(0); co = {}
    for c, (k, d) in terms:
        const += c * k
        for pp, v in d.items():
            co[pp] = co.get(pp, Fr(0)) + c * v
    return const, {pp: v for pp, v in co.items() if v != 0}

M = combine((1, entropy_form(masses)), (-1, h2(Fr(3, 32))))
J = combine((1, h2(Fr(3, 32))), (-Fr(1, 8), h2(Fr(3, 4))))
JM = combine((1, J), (-1, M))
const, co = JM
# move log2(2) into the constant
const += co.pop(2, Fr(0))
hand = {3: Fr(450, 256), 5: Fr(450, 256), 7: Fr(28, 256), 29: Fr(-464, 256)}
assert const == Fr(7, 4) and co == hand, (const, co)
lo, hi = enclose_form(co, const)

def dec(x, digits=30, up=False):
    """Exact decimal truncation of a positive Fraction (rounded down, or up)."""
    s = 10 ** digits; v = x.numerator * s // x.denominator
    if up and Fr(v, s) < x:
        v += 1
    t = str(v).rjust(digits + 1, '0')
    return t[:-digits] + '.' + t[-digits:]

res = {'masses': [str(m) for m in masses], 'J_minus_M_form': {'const': str(const), **{f'log2 {k}': str(v) for k, v in co.items()}},
       'enclosure_lo_exact_30_digits_rounded_down': dec(lo), 'enclosure_hi_exact_30_digits_rounded_up': dec(hi, up=True),
       'width': float(hi - lo), 'exceeds_1195/10000': bool(lo > Fr(1195, 10000)),
       'A081_interval_[0.119545016024424957,0.119545016024424958]_contains_ours': bool(
           Fr('0.119545016024424957') <= lo and hi <= Fr('0.119545016024424958'))}
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'out')
with open(os.path.join(OUT, 'b09_interval.json'), 'w', encoding='utf-8') as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
