from fractions import Fraction
from itertools import product

D = 11275278979
J = Fraction(3224554983, D)
states = list(product(range(3), repeat=3))
idx = {s: i for i, s in enumerate(states)}

# Exact average-reward potential h, represented over the common denominator D.
h_num = [
    0,10726825499,19889096814,
    8324677595,18150881670,24853648313,
    12884432758,21684654417,26797062604,
    3224554983,13677153742,22057147965,
    10348158626,19781791629,25791947128,
    13475763285,22087183792,26940182191,
    3899048660,14253504651,22435810396,
    10640078985,19996414062,25881382633,
    13547304096,22127427871,26953596884,
]
h = {s: Fraction(h_num[idx[s]], D) for s in states}

# Exact stationary distribution for the saturated open 3-site block.
p_num = [
    13414693,26829386,31296732,
    49191426,93890196,77297926,
    164039998,120390552,98142768,
    53684082,134222860,111503226,
    371729442,383419440,294428304,
    537141192,389706020,274226740,
    1005115476,897747312,633411344,
    893637560,1043816236,626394684,
    1738215144,663932760,548453480,
]
p = {s: Fraction(p_num[idx[s]], D) for s in states}

def transitions(s, u=Fraction(1), v=Fraction(1, 2)):
    """Three consecutive rate-1/2 sites; u is left injection, v right exit."""
    a, b, c = s
    out = []
    if a < 2 and u:
        out.append(((a + 1, b, c), u, "inj"))
    if a > 0 and b < 2:
        out.append(((a - 1, b + 1, c), Fraction(1, 2), "int1"))
    if b > 0 and c < 2:
        out.append(((a, b - 1, c + 1), Fraction(1, 2), "int2"))
    if c > 0 and v:
        out.append(((a, b, c - 1), v, "exit"))
    return out

print("HARD7-03 exact three-slow-site controlled-current certificate")
print(f"D={D}")
print(f"J={J}")
print(f"J_float={float(J):.15f}")

# Primal: exact stationary law under saturated controls u=1, v=1/2.
assert sum(p.values()) == 1
balance = {s: Fraction(0) for s in states}
for s in states:
    total = Fraction(0)
    for t, rate, _kind in transitions(s):
        balance[t] += p[s] * rate
        total += rate
    balance[s] -= p[s] * total
assert all(x == 0 for x in balance.values())
current = sum(p[s] * Fraction(1, 2) for s in states if s[2] > 0)
assert current == J
print("stationary_sum=1")
print("stationary_balance=EXACT_ZERO_ALL_27")
print(f"stationary_exit_current={current}")

# Dual: Bellman equality for saturated controls.
for s in states:
    value = Fraction(1, 2) if s[2] > 0 else Fraction(0)
    for t, rate, _kind in transitions(s):
        value += rate * (h[t] - h[s])
    assert value == J
print("bellman_saturated=EXACT_EQUALITY_ALL_27")

# For arbitrary admissible u in [0,1] and v in [0,1/2], the Bellman
# expression is affine in u,v. Positive coefficients mean its maximum
# occurs at the saturated endpoint, hence is <= J pointwise.
inj_coeff = []
exit_coeff = []
for s in states:
    a, b, c = s
    if a < 2:
        t = (a + 1, b, c)
        coeff = h[t] - h[s]
        assert coeff > 0
        inj_coeff.append((s, coeff))
    if c > 0:
        t = (a, b, c - 1)
        coeff = Fraction(1) + h[t] - h[s]
        assert coeff > 0
        exit_coeff.append((s, coeff))

s_inj, min_inj = min(inj_coeff, key=lambda z: z[1])
s_exit, min_exit = min(exit_coeff, key=lambda z: z[1])
print(f"min_injection_coefficient={min_inj} at {s_inj}")
print(f"min_exit_reward_coefficient={min_exit} at {s_exit}")
print("arbitrary_control_bellman_upper_bound=VERIFIED_BY_AFFINITY_AND_POSITIVE_COEFFICIENTS")

# Finite-time additive constant: h is nonnegative, so E N_t <= J t + max h.
assert min(h.values()) == 0
H = max(h.values())
s_H = max(states, key=lambda s: h[s])
print("h_min=0")
print(f"h_max={H} at {s_H}")
print(f"finite_time_bound=E[N_t] <= ({J}) t + ({H})")

# Strict improvement over the previous exact 2-site envelope.
C2 = Fraction(71, 219)
assert J < C2
print(f"C2={C2}")
print(f"C2_minus_C3={C2-J}")

# B1 defect-gas recoding: xi=eta-1. Verify the four and only four
# source-model moves at a bond.
moves = []
for a in range(3):
    for b in range(3):
        if a > 0 and b < 2:
            xa, xb = a - 1, b - 1
            ya, yb = (a - 1) - 1, (b + 1) - 1
            moves.append(((xa, xb), (ya, yb)))
expected = [
    ((0, 0), (-1, 1)),
    ((1, 0), (0, 1)),
    ((0, -1), (-1, 0)),
    ((1, -1), (0, 0)),
]
assert set(moves) == set(expected)
for before, after in moves:
    assert sum(before) == sum(after)
print("defect_move_set=EXACT_FOUR")
for before, after in expected:
    print(f"  {before} -> {after}")
print("defect_charge=sum(xi)=particle_number-minus-site_count is conserved")

print("ALL_EXACT_CHECKS_PASS")
