"""Exact symbolic exterior-algebra audit using only the standard library."""
import json
from fractions import Fraction
from pathlib import Path

class Poly:
    """Rational-coefficient polynomial in c and z."""
    def __init__(self, value=0):
        if isinstance(value, Poly):
            self.d = dict(value.d)
        elif isinstance(value, dict):
            self.d = {k: Fraction(v) for k, v in value.items() if v}
        else:
            self.d = {(0, 0): Fraction(value)} if value else {}
    def __bool__(self):
        return bool(self.d)
    def __add__(self, other):
        other = Poly(other)
        d = dict(self.d)
        for k, v in other.d.items():
            d[k] = d.get(k, 0)+v
        return Poly(d)
    __radd__ = __add__
    def __neg__(self):
        return Poly({k: -v for k, v in self.d.items()})
    def __sub__(self, other):
        return self+-Poly(other)
    def __rsub__(self, other):
        return Poly(other)+-self
    def __mul__(self, other):
        other = Poly(other)
        d = {}
        for (i, j), v in self.d.items():
            for (k, l), w in other.d.items():
                key = (i+k, j+l)
                d[key] = d.get(key, 0)+v*w
        return Poly(d)
    __rmul__ = __mul__
    def dc(self):
        return Poly({(i-1,j): i*v for (i,j),v in self.d.items() if i})
    def serial(self):
        return {f'c^{i} z^{j}': str(v) for (i,j),v in sorted(self.d.items())}

c, z = Poly({(1,0): 1}), Poly({(0,1): 1})

def clean(p):
    return {m: Poly(v) for m, v in p.items() if v}

def add(*ps):
    out = {}
    for p in ps:
        for m, v in p.items():
            out[m] = out.get(m, Poly())+v
    return clean(out)

def scale(p, s):
    return clean({m: v*s for m, v in p.items()})

def mul(p, q):
    out = {}
    for m, a in p.items():
        for n, b in q.items():
            if m & n:
                continue
            inversions = sum((n & ((1 << j)-1)).bit_count()
                             for j in range(8) if m & (1 << j))
            k = m | n
            out[k] = out.get(k, Poly())+a*b*((-1)**inversions)
    return clean(out)

def gen(i):
    return {1 << i: Poly(1)}

# Generator order: bar(xi_a), xi_a, bar(xi_b), xi_b,
#                  bar(psi_s), psi_s, bar(psi_r), psi_r.
ba, a, bb, b, bs, s, br, r = [gen(i) for i in range(8)]
bm, m = scale(add(bs, br), Fraction(1,2)), scale(add(s, r), Fraction(1,2))
qa, qb = mul(add(ba, bm), add(a, m)), mul(add(bb, bm), add(b, m))
qs, qr = mul(bs, s), mul(br, r)
V = add(qa, qb, scale(mul(qa, qb), -c),
        scale(mul(add(qa, qb), add(qs, qr)), -1))
assert not mul(mul(V, V), V)
expV = add({0: Poly(1)}, scale(V, z), scale(mul(V, V), z*z*Fraction(1,2)))

# All conditional residual moments have denominator den=4(c+1).
# The dictionary gives their NUMERATORS, including moment 1=den/den.
den = 4*(c+1)
wick_num = {0: den, 0b0011: c+2, 0b1100: c+2,
            0b1001: c, 0b0110: -c, 0b1111: Poly(1)}

def expect_num(p):
    out = {}
    for mask, val in p.items():
        residual, boundary = mask & 15, mask & ~15
        if residual in wick_num:
            out[boundary] = out.get(boundary, Poly())+val*wick_num[residual]
    return clean(out)

N = expect_num(expV)  # N=den*F
Q, R = mul(add(bs, scale(br, -1)), add(s, scale(r, -1))), mul(qs, qr)
W = c*(4+z)+(2+z)*(2+z)
n1 = -z*(c+2+z)
n2 = -2*z*(2*c+2+z)
predicted_N = add({0: W}, scale(Q, n1), scale(R, n2))
assert not add(N, scale(predicted_N, -1))

# Since Q^2=QR=R^2=0, nonconstant log F=(N-W)/W.
# Its c derivative has numerator N'_non W-N_non W', denominator W^2.
nonconstant_N = add(N, {0: -N[0]})
score_num = clean({mask: val.dc()*W-val*W.dc()
                   for mask, val in nonconstant_N.items()})
prefactor_num = 2*z*(2+z)
predicted_score_num = scale(add(Q, scale(R, -z)), prefactor_num)
assert not add(score_num, scale(predicted_score_num, -1))
assert not (score_num[0b11110000]-(-2*z*z*(z+2)))

# Verify explicitly the common-mode identity R=q_u Q.
qu = mul(scale(add(bs, br), Fraction(1,2)),
         scale(add(s, r), Fraction(1,2)))
assert not add(R, scale(mul(qu, Q), -1))

result = {
    'exact_exterior_factor_matches': True,
    'exact_marked_score_matches': True,
    'quartic_common_mode_identity_matches': True,
    'factor_common_denominator': den.serial(),
    'score_denominator': (W*W).serial(),
    'quartic_score_numerator': score_num[0b11110000].serial(),
    'quartic_score_at_c_1': '-2*z^2*(z+2)/(z^2+5*z+8)^2',
    'quartic_score_series_at_c_1': '-z^2/16 + 3*z^3/64 + O(z^4)',
}
target = Path(__file__).with_name('response_space_lemma_counterexample_audit_results.json')
target.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
