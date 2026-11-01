"""Exact-rational consistency checks for PROB20-14 Palm switching.

This is a finite-support certificate only; it is not evidence for the universal theorem.
It verifies, for one critical offspring law, the identities used in the
2026-09-15T17-27-24Z report:

  E_Q N_d = n pi_d R_{n,d},
  E_Q[N_d H_{n,d}(N_0)] / pi_d = E_Q O_{n,d},
  the N_d-Palm law of N_0 equals the direct law from n-1 iid variables
      conditioned on S_{n-1}=n-1-d,
  R_{n,d} * E^*_{n,d}[ n H_{n,d}(N_0)] = E_Q O_{n,d}.

All arithmetic is fractions.Fraction exact arithmetic.
"""

from fractions import Fraction
from math import factorial

PI = {
    0: Fraction(11, 20),
    1: Fraction(1, 5),
    2: Fraction(3, 20),
    5: Fraction(1, 10),
}

assert sum(PI.values(), Fraction(0)) == 1
assert sum(x * p for x, p in PI.items()) == 1


def conv_dist(m):
    dist = {0: Fraction(1)}
    for _ in range(m):
        nxt = {}
        for s, p in dist.items():
            for x, px in PI.items():
                nxt[s + x] = nxt.get(s + x, Fraction(0)) + p * px
        dist = nxt
    return dist


def p_sum(m, target):
    return conv_dist(m).get(target, Fraction(0))


def falling(z, k):
    ans = 1
    for j in range(k):
        ans *= z - j
    return ans


def enumerate_counts(n, target):
    """Return count vectors c with sum c_x=n and sum x c_x=target,
    together with their exact multinomial product probabilities.
    """
    values = sorted(PI)
    out = []

    def rec(i, rem_n, rem_sum, counts):
        if i == len(values) - 1:
            x = values[i]
            if rem_n >= 0 and rem_sum == x * rem_n:
                c = counts.copy()
                c[x] = rem_n
                mult = factorial(n)
                for cc in c.values():
                    mult //= factorial(cc)
                prob = Fraction(mult, 1)
                for y, cc in c.items():
                    prob *= PI[y] ** cc
                out.append((c, prob))
            return

        x = values[i]
        max_count = rem_n if x == 0 else min(rem_n, rem_sum // x)
        for count in range(max_count + 1):
            c = counts.copy()
            c[x] = count
            rec(i + 1, rem_n - count, rem_sum - x * count, c)

    rec(0, n, target, {})
    return out


n = 18
d = 5

a_n = p_sum(n, n - 1)
b_nd = p_sum(n - 1, n - 1 - d)
R = b_nd / a_n
E_Nd = Fraction(n) * PI[d] * R

# H_{n,d}(z) = sum_s P(S_s=d) (z)_{s-1}/[pi_0^{s-1}(n)_s].
u = [None] + [p_sum(s, d) for s in range(1, n + 1)]


def H(z):
    ans = Fraction(0)
    for s in range(1, n + 1):
        if z < s - 1:
            continue
        ans += (
            u[s]
            * Fraction(falling(z, s - 1), 1)
            / (PI[0] ** (s - 1) * falling(n, s))
        )
    return ans


# Exact conditioned count-vector law Q_n.
states = enumerate_counts(n, n - 1)
assert sum(prob for _, prob in states) == a_n

E_NdH = Fraction(0)
for counts, uncond_prob in states:
    q_prob = uncond_prob / a_n
    E_NdH += q_prob * counts.get(d, 0) * H(counts.get(0, 0))

# Occupation side of the summed switching identity.
occupation = Fraction(0)
for s in range(1, n + 1):
    occupation += u[s] * p_sum(n - s, n - 1 - d) / a_n

assert E_Nd == sum(
    (prob / a_n) * counts.get(d, 0) for counts, prob in states
)
assert E_NdH / PI[d] == occupation

# N_d-Palm law of N_0 under Q_n.
palm = {}
for counts, uncond_prob in states:
    z = counts.get(0, 0)
    mass = (uncond_prob / a_n) * counts.get(d, 0) / E_Nd
    palm[z] = palm.get(z, Fraction(0)) + mass

# Direct law of N_0 among n-1 iid variables conditioned on S_{n-1}=n-1-d.
states_residual = enumerate_counts(n - 1, n - 1 - d)
assert sum(prob for _, prob in states_residual) == b_nd

direct = {}
for counts, uncond_prob in states_residual:
    z = counts.get(0, 0)
    direct[z] = direct.get(z, Fraction(0)) + uncond_prob / b_nd

all_z = set(palm) | set(direct)
assert all(palm.get(z, 0) == direct.get(z, 0) for z in all_z)

palm_H = sum(prob * H(z) for z, prob in palm.items())
self_normalized = R * n * palm_H
assert self_normalized == occupation == E_NdH / PI[d]

print("a_n =", a_n, float(a_n))
print("b_nd =", b_nd, float(b_nd))
print("R =", R, float(R))
print("E N_d =", E_Nd, float(E_Nd))
print("occupation =", occupation, float(occupation))
print("E[N_d H]/pi_d =", E_NdH / PI[d], float(E_NdH / PI[d]))
print("Palm law equals direct residual conditional law: True")
print("Palm nH =", n * palm_H, float(n * palm_H))
print("R * Palm nH =", self_normalized, float(self_normalized))
print("Palm self-normalization identity exact: True")
