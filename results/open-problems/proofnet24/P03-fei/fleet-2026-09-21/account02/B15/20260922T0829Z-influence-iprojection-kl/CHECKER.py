from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
LN2 = D(2).ln()


def log2(x):
    return x.ln() / LN2


def h2(x):
    if x == 0 or x == 1:
        return D(0)
    return -x * log2(x) - (1 - x) * log2(1 - x)


def root_c(rs):
    # For sum(rs)>1 the concave fixed-point equation
    #   1-prod_i(1-c r_i)=c
    # has one positive root. Bisection is only a numerical sanity check.
    def f(c):
        prod = D(1)
        for r in rs:
            prod *= 1 - c * r
        return D(1) - prod - c

    lo = D('1e-50')
    hi = D(1)
    assert f(lo) > 0 and f(hi) <= 0
    for _ in range(400):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def maxent_nonempty(rs):
    mu = sum(rs, D(0))
    if mu == 1:
        H = -sum((r * log2(r) if r else D(0)) for r in rs)
        return D(0), H
    c = root_c(rs)
    H = (sum((h2(c * r) for r in rs), D(0)) - h2(c)) / c
    return c, H


def qprob(mask, t, c):
    pr = D(1)
    for i, ti in enumerate(t):
        pr *= ti if ((mask >> i) & 1) else (1 - ti)
    return pr / c


# account04/B15's source-checked four-bit composition-prime witness.
# Its nonzero uniform Walsh coefficients are seven coefficients of magnitude
# 4/16 and one coefficient of magnitude 12/16, so the squared spectral law is
# seven atoms of mass 1/16 and one atom of mass 9/16.
masses = {
    1: D(1) / 16,
    2: D(1) / 16,
    4: D(1) / 16,
    7: D(1) / 16,
    8: D(9) / 16,
    11: D(1) / 16,
    13: D(1) / 16,
    14: D(1) / 16,
}

marg = [D(0)] * 4
for mask, p in masses.items():
    for i in range(4):
        if (mask >> i) & 1:
            marg[i] += p

assert marg == [D(1) / 4, D(1) / 4, D(1) / 4, D(3) / 4]

c_vec, H_vec = maxent_nonempty(marg)
mu = sum(marg, D(0))
r_iso = [mu / 4] * 4
c_iso, H_iso = maxent_nonempty(r_iso)
H_actual = D(7) / 4 + D(9) / 16 * log2(D(16) / 9)
K_occ = H_vec - H_actual
K_aniso = H_iso - H_vec

t_vec = [c_vec * r for r in marg]
t_iso = [c_iso * r for r in r_iso]

D_p_q = D(0)
for mask, p in masses.items():
    q = qprob(mask, t_vec, c_vec)
    D_p_q += p * log2(p / q)

D_q_qiso = D(0)
for mask in range(1, 16):
    qv = qprob(mask, t_vec, c_vec)
    qi = qprob(mask, t_iso, c_iso)
    D_q_qiso += qv * log2(qv / qi)

assert abs(K_occ - D_p_q) < D('1e-60')
assert abs(K_aniso - D_q_qiso) < D('1e-60')
assert K_occ > D('0.8')
assert K_aniso > D('0.46')

print('PASS')
print('marginals', *(str(x) for x in marg))
print('c_vector', c_vec)
print('Hmax_vector', H_vec)
print('c_isotropic', c_iso)
print('Hmax_isotropic', H_iso)
print('H_actual', H_actual)
print('K_occ', K_occ)
print('K_anisotropy', K_aniso)
print('K_scalar_total', H_iso - H_actual)
print('Pythagorean_residual_vector', (H_vec - H_actual) - D_p_q)
print('anisotropy_residual', (H_iso - H_vec) - D_q_qiso)
