from fractions import Fraction as F
from math import factorial
import itertools
import sympy as sp

print("HARD7-03 exact 3-step order-cone Chernoff certificate")

t = sp.symbols("t")
AIDX = (-1, 0, 1)

def cone_integral(beta, order):
    """
    Integral of exp(sum_i beta_i A_i) against the iid Exp(1)^3 density
    over 0 <= A_order[0] <= A_order[1] <= A_order[2].
    """
    b = [sp.simplify(beta.get(v, 0)) for v in order]
    return sp.factor(
        1 /
        ((3 - (b[0]+b[1]+b[2]))
         * (2 - (b[1]+b[2]))
         * (1 - b[2]))
    )

def integrated_conditional_endpoint_mgf(d):
    total = 0
    for order in itertools.permutations(AIDX):
        rank = {v:i for i,v in enumerate(order)}

        # At time 2, after maximizing over the first step, the additive
        # first-layer shift at site x is the largest reachable A_j.
        shift = {}
        for x in range(-2, 3):
            preds = [j for j in AIDX if abs(x-j) <= 1]
            shift[x] = max(preds, key=lambda j: rank[j])

        # Time-2 predecessors of the fixed time-3 endpoint d.
        xs = [x for x in range(-2, 3) if abs(d-x) <= 1]
        cs = [shift[x] for x in xs]
        cstar = max(cs, key=lambda j: rank[j])

        # Conditional formula for Y=max_i(c_i+B_i), B_i iid Exp(1):
        # E e^{tY}|c = e^{t c*}
        # + t sum_{S != empty} (-1)^(|S|+1)
        #   exp(sum_{i in S} c_i-(|S|-t)c*)/(|S|-t).
        beta0 = {cstar:t}
        total += cone_integral(beta0, order)

        for r in range(1, len(cs)+1):
            for inds in itertools.combinations(range(len(cs)), r):
                beta = {}
                for i in inds:
                    beta[cs[i]] = beta.get(cs[i], 0) + 1
                beta[cstar] = beta.get(cstar, 0) - (r-t)
                coeff = t * ((-1)**(r+1)) / (r-t)
                total += coeff * cone_integral(beta, order)

    # Independent final endpoint Exp(1) weight.
    return sp.factor(total/(1-t))

M = {d: sp.factor(integrated_conditional_endpoint_mgf(d)) for d in range(4)}

expected = {
    0: 4*(18-11*t)/((3-t)**2*(2-t)**3*(1-t)**3),
    1: (648-889*t+394*t**2-57*t**3)/((3-t)**4*(2-t)**3*(1-t)**3),
    2: (8-5*t)/((2-t)**3*(1-t)**3),
    3: 1/(1-t)**3,
}

for d in range(4):
    assert sp.simplify(M[d] - expected[d]) == 0
    assert sp.simplify(M[d].subs(t, 0) - 1) == 0
    print(f"M3_{d}(t) = {sp.factor(M[d])}")

A3 = sp.factor(M[0] + 2*(M[1]+M[2]+M[3]))
expected_A3 = (
    2*(2268-4408*t+3748*t**2-1918*t**3+652*t**4-143*t**5+18*t**6-t**7)
    / ((3-t)**4*(2-t)**3*(1-t)**3)
)
assert sp.simplify(A3-expected_A3) == 0
assert sp.simplify(A3.subs(t,0)-7) == 0
print(f"A3(t) = {sp.factor(A3)}")

theta = F(301,500)
a = F(2989,1000)

def eval_A3(th):
    return (
        2*(F(2268)-4408*th+3748*th**2-1918*th**3+652*th**4-143*th**5+18*th**6-th**7)
        / ((3-th)**4*(2-th)**3*(1-th)**3)
    )

A_theta = eval_A3(theta)
x = 3*theta*a
S18 = sum(x**k / F(factorial(k),1) for k in range(19))
taylor_gap = S18-A_theta
assert taylor_gap > 0

# Since S18(x) < exp(x), this proves exp(3 theta a) > A3(theta).
L_old = F(5000,61903)
L_new = F(1,1)/(4*a)
metric_gain = L_new-L_old
assert metric_gain > 0

# Previous exact two-step upper bound and new three-step upper bound.
G2 = F(61903,20000)
G3 = a
assert G3 < G2

print(f"theta = {theta}")
print(f"a = {a}")
print(f"A3(theta) = {A_theta}")
print(f"A3(theta)_decimal = {float(A_theta):.15f}")
print(f"x=3*theta*a = {x}")
print(f"S18_minus_A3 = {taylor_gap}")
print(f"S18_minus_A3_decimal = {float(taylor_gap):.15f}")
print(f"G2_upper = {G2}")
print(f"G3_upper = {G3}")
print(f"G_bound_gain = {G2-G3}")
print(f"L_old = {L_old}")
print(f"L_new = {L_new}")
print(f"L_new_decimal = {float(L_new):.15f}")
print(f"L_gain = {metric_gain}")
print(f"L_gain_decimal = {float(metric_gain):.15f}")
print("ALL_EXACT_CHECKS_PASS = True")
