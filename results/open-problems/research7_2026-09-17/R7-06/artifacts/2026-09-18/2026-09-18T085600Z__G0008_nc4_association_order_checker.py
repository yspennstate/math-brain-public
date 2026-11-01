from fractions import Fraction


def canon(blocks):
    return tuple(sorted(tuple(sorted(b)) for b in blocks))


def all_partitions(n):
    parts = [()]
    for x in range(n):
        new = []
        for p in parts:
            new.append(canon(list(p) + [(x,)]))
            for i in range(len(p)):
                blocks = [list(b) for b in p]
                blocks[i].append(x)
                new.append(canon(blocks))
        parts = list(dict.fromkeys(new))
    return parts


def refines(p, q):
    return all(any(set(b).issubset(set(c)) for c in q) for b in p)


def orbit_type(p):
    sizes = sorted((len(b) for b in p), reverse=True)
    if sizes == [1, 1, 1, 1]:
        return "sigma"
    if sizes == [4]:
        return "epsilon"
    if sizes == [3, 1]:
        return "delta"
    if sizes == [2, 2]:
        return "gamma"
    if sizes == [2, 1, 1]:
        pair = next(b for b in p if len(b) == 2)
        a, b = pair
        dist = min((a - b) % 4, (b - a) % 4)
        return "alpha" if dist == 1 else "beta"
    raise RuntimeError(p)


crossing = canon([(0, 2), (1, 3)])
states = [p for p in all_partitions(4) if p != crossing]
assert len(states) == 14

le = [[refines(states[i], states[j]) for j in range(14)] for i in range(14)]
upsets = []
for mask in range(1 << 14):
    ok = True
    for i in range(14):
        if (mask >> i) & 1:
            for j in range(14):
                if le[i][j] and not ((mask >> j) & 1):
                    ok = False
                    break
            if not ok:
                break
    if ok:
        upsets.append(mask)
assert len(upsets) == 234

theta_p = {
    "sigma": Fraction(1, 4),
    "alpha": Fraction(0),
    "beta": Fraction(19, 108),
    "gamma": Fraction(0),
    "delta": Fraction(1, 27),
    "epsilon": Fraction(1, 4),
}
theta_q = {
    "sigma": Fraction(1, 4),
    "alpha": Fraction(0),
    "beta": Fraction(0),
    "gamma": Fraction(0),
    "delta": Fraction(1, 64),
    "epsilon": Fraction(11, 16),
}
probs_p = [theta_p[orbit_type(s)] for s in states]
probs_q = [theta_q[orbit_type(s)] for s in states]
assert sum(probs_p) == 1
assert sum(probs_q) == 1


def prob(mask, probs):
    return sum((probs[i] for i in range(14) if (mask >> i) & 1), Fraction(0))


def association_certificate(probs):
    vals = {m: prob(m, probs) for m in upsets}
    zero = 0
    positive = []
    for ia, A in enumerate(upsets):
        for B in upsets[ia:]:
            margin = vals[A & B] - vals[A] * vals[B]
            if margin < 0:
                raise AssertionError(("association failure", margin, A, B))
            if margin == 0:
                zero += 1
            else:
                positive.append(margin)
    return zero, min(positive)


zp, mp = association_certificate(probs_p)
zq, mq = association_certificate(probs_q)

dom_zero = 0
dom_positive = []
for U in upsets:
    margin = prob(U, probs_q) - prob(U, probs_p)
    if margin < 0:
        raise AssertionError(("stochastic dominance failure", margin, U))
    if margin == 0:
        dom_zero += 1
    else:
        dom_positive.append(margin)


def L(th, r):
    return (
        th["sigma"]
        + 2 * (1 + r) * th["alpha"]
        + (1 + r) * th["beta"]
        + 2 * r * th["gamma"]
        + (1 + 3 * r * r) * th["delta"]
        + r**3 * th["epsilon"]
    )


def F(th, p):
    q = 1 - p
    return (
        p * th["sigma"]
        + 2 * p * (3 - 2 * p) * th["alpha"]
        + (2 * p - 1) * th["beta"]
        + 2 * p * (1 - p) * (2 - p) * th["gamma"]
        + (2 * p**3 - 7 * p**2 + 8 * p - 2) * th["delta"]
        - (1 - p) ** 3 * th["epsilon"]
    )


def S_T(th):
    S = th["alpha"] + th["gamma"] + 2 * th["delta"] + th["epsilon"]
    T = th["beta"] + 2 * th["delta"] + th["epsilon"]
    return S, T


p = Fraction(1, 3)
q = Fraction(2, 3)
assert L(theta_p, q) == Fraction(19, 27)
assert L(theta_q, p) == Fraction(8, 27)
assert L(theta_p, q) + L(theta_q, p) == 1
assert 1 - L(theta_p, q) == Fraction(8, 27) < p
assert 1 - L(theta_q, p) == Fraction(19, 27) > q
assert theta_p["delta"] - q**3 * theta_p["epsilon"] / 2 == 0
assert theta_q["delta"] - p**3 * theta_q["epsilon"] / 2 == Fraction(5, 1728)
assert F(theta_p, p) == Fraction(-37, 729)
assert F(theta_q, q) == Fraction(133, 864)

for th in (theta_p, theta_q):
    S, T = S_T(th)
    margins = [
        th["delta"] + th["epsilon"] - S * S,
        th["gamma"] + th["epsilon"] - S * S,
        th["delta"] + th["epsilon"] - S * T,
        th["epsilon"] - T * T,
        S * S - th["gamma"],
    ]
    assert all(m >= 0 for m in margins)

print("NC4_STATES", len(states))
print("UPSETS", len(upsets))
print("ASSOCIATION_PAIR_CHECKS_PER_MEASURE", len(upsets) * (len(upsets) + 1) // 2)
print("P_ASSOCIATION_PASS", "zero=", zp, "min_positive=", mp)
print("Q_ASSOCIATION_PASS", "zero=", zq, "min_positive=", mq)
print("Q_STOCHASTICALLY_DOMINATES_P_PASS", "zero=", dom_zero, "min_positive=", min(dom_positive))
print("L_P_AT_2_3", L(theta_p, q))
print("L_Q_AT_1_3", L(theta_q, p))
print("DET_P", 1 - L(theta_p, q))
print("DET_Q", 1 - L(theta_q, p))
print("LEAF_P_MARGIN", theta_p["delta"] - q**3 * theta_p["epsilon"] / 2)
print("LEAF_Q_MARGIN", theta_q["delta"] - p**3 * theta_q["epsilon"] / 2)
print("F_P", F(theta_p, p))
print("F_Q", F(theta_q, q))
print("ALL_EXACT_CHECKS_PASS")
